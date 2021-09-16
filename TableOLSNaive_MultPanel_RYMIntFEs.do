
global clear all
clear all
set more off

if "`c(username)'" == "Benjamin" {
global hdir "D:\Dropbox\Pirates\PaperwithBen\Work"
}
*

if "`c(username)'" == "benbl" {
global hdir "C:\Users\benbl\Dropbox\Pirates\PaperWithBen\Work"
}
*

use $hdir\Analysis\Input\AnalysisFileOcean.dta, clear

/*
global RegionYes "estadd local GroupFE "X""
global RegionNo "estadd local GroupFE " ""
*/

global YearYes "estadd local Year "X""
global YearNo "estadd local Year " ""

global MonthYes "estadd local Month "X""
global MonthNo "estadd local Month " ""

global RYMIntYes "estadd local RegYrMth "X""
global RYMIntNo "estadd local RegYrMth " ""



/*
global YearMonthYes "estadd local YearMonth "X""
global YearMonthNo "estadd local YearMonth " ""
*/

global OceanYes "estadd local OceanFE "X""
global OceanNo "estadd local OceanFE " ""

/*
global PoissonYes "estadd local Poisson "X""
global PoissonNo "estadd local Poisson " ""

global ModelP "estadd local Model "Poisson""
global ModelOLS "estadd local Model "OLS""

global ClusterYes "estadd local Cluster "X""
global ClusterNo "estadd local Cluster """
*/

set matsize 11000
eststo clear

/*
label variable attacks_rp "Pirate Attacks"


gen attacks2 = attacks
label variable attacks2 "$\hat{PirAtks}$"
*/
gen quarter = 0
replace quarter = 1 if month == 1 | month == 2 | month == 3
replace quarter = 2 if month == 4 | month == 5 | month == 6
replace quarter = 3 if month == 7 | month == 8 | month == 9
replace quarter = 4 if month == 10 | month == 11 | month == 12

**using even ones when wind speed is missing

/*
eststo : reg events attacks ///
	 ///
	, robust
$OceanNo
$YearNo
$MonthNo
$YearMonthNo
$ModelOLS
*/

eststo : reg events attacks_rp ///
	i.oceanpolygon_id, ///
	robust
$OceanYes
$YearNo
$MonthNo
$RYMIntNo
$ModelOLS
	
eststo : reg events attacks_rp ///
	i.oceanpolygon_id i.year i.month, ///
	robust
$OceanYes
$YearYes
$MonthYes
$RYMIntNo
$ModelOLS


eststo : reg events attacks_rp ///
	i.oceanpolygon_id#year#month, ///
	robust
$OceanNo
$YearNo
$MonthNo
$RYMIntYes
$ModelOLS

/*
reg events attacks_rp ///
	i.oceanpolygon_id#year#month, ///
	robust

eststo : reg events attacks ///
	i.oceanpolygon_id i.year#month, ///
	robust
$OceanYes
$YearNo
$MonthNo
$YearMonthYes
$ModelOLS
*/

local tablename = "OLSNaivePanels_RYMIntFEs"
local panelname = "OLSAllObs"

esttab * using $hdir\Build\Input\TableFrags\Table`tablename'\Table`tablename'HeadFootFind.tex, replace ///
	drop(*) noobs collabels(none) nodepvars label ///
	mlabels(none) eqlabels(none) ///
	booktabs cells(b(fmt(%9.2f) star) se(fmt(%9.2f) par)) ///
	starlevels(* 0.10 ** 0.05 *** 0.01) star(b) ///
	scalars("N Observations" "OceanFE Region FEs" ///
	"Year Year FEs" "Month Month FEs" "RegYrMth RegionXYearXMonth FEs") ///
	title("OLS Estimates of the Effect of Pirate Attacks on Land Conflict\label{TableOLSPoissonEstimates}")

esttab * using $hdir\Build\Input\TableFrags\Table`tablename'\Table`tablename'`panelname'.tex, replace ///
	keep(attacks_rp) noobs collabels(none) nodepvars label ///
	mlabels(none) eqlabels(none) nonumbers ///
	booktabs cells(b(fmt(%9.2f) star) se(fmt(%9.2f) par)) ///
	starlevels(* 0.10 ** 0.05 *** 0.01) star(b) ///
	scalars("N Observations" "OceanFE Region FEs" ///
	"Year Year FEs" "Month Month FEs" "RegYrMth RegionXYearXMonth FEs") ///
	title("OLS Estimates of the Effect of Pirate Attacks on Land Conflict\label{TableOLSPoissonEstimates}") ///
	fragment

	
************************************************************************

eststo clear

eststo : reg events attacks_rp ///
	i.oceanpolygon_id ///
	if altwdspd_ptlvlcollapse ~= . ///
	, robust
$OceanYes
$YearNo
$MonthNo
$RYMIntNo
$ModelOLS


eststo : reg events attacks_rp ///
	i.oceanpolygon_id i.year i.month ///
	if altwdspd_ptlvlcollapse ~= . ///
	, robust
$OceanYes
$YearYes
$MonthYes
$RYMIntNo
$ModelOLS


eststo : reg events attacks_rp ///
	i.oceanpolygon_id#year#month ///
	if altwdspd_ptlvlcollapse ~= . ///
	, robust
$OceanNo
$YearNo
$MonthNo
$RYMIntYes
$ModelOLS


local tablename = "OLSNaivePanels_RYMIntFEs"
local panelname = "OLSNoObsWMissWindSpeed"

esttab * using $hdir\Build\Input\TableFrags\Table`tablename'\Table`tablename'`panelname'.tex, replace ///
	keep(attacks_rp) noobs collabels(none) nodepvars label ///
	mlabels(none) eqlabels(none) nonumbers  ///
	booktabs cells(b(fmt(%9.2f) star) se(fmt(%9.2f) par)) ///
	starlevels(* 0.10 ** 0.05 *** 0.01) star(b) ///
	scalars("N Observations" "OceanFE Region FEs" ///
	"Year Year FEs" "Month Month FEs" "RegYrMth RegionXYearXMonth FEs") ///
	title("OLS Estimates of the Effect of Pirate Attacks on Land Conflict\label{TableOLSPoissonEstimates}") ///
	fragment


***************************************************************************

eststo clear

eststo : poisson events attacks_rp ///
	i.oceanpolygon_id, ///
	robust
$OceanYes
$YearNo
$MonthNo
$RYMIntNo
$ModelP


eststo : poisson events attacks_rp ///
	i.oceanpolygon_id i.year i.month, ///
	robust	
$OceanYes
$YearYes
$MonthYes
$RYMIntNo
$ModelP


eststo : poisson events attacks_rp ///
	i.oceanpolygon_id#year#month, ///
	robust	
$OceanNo
$YearNo
$MonthNo
$RYMIntYes
$ModelP

/*
poisson events attacks_rp ///
	i.oceanpolygon_id#year#month, ///
	robust	
*/

local tablename = "OLSNaivePanels_RYMIntFEs"
local panelname = "PoissonAllObs"

esttab * using $hdir\Build\Input\TableFrags\Table`tablename'\Table`tablename'`panelname'.tex, replace ///
	keep(attacks_rp) noobs collabels(none) nodepvars label ///
	mlabels(none) eqlabels(none) nonumbers ///
	booktabs cells(b(fmt(%9.2f) star) se(fmt(%9.2f) par)) ///
	starlevels(* 0.10 ** 0.05 *** 0.01) star(b) ///
	scalars("N Observations" "OceanFE Region FEs" ///
	"Year Year FEs" "Month Month FEs" "RegYrMth RegionXYearXMonth FEs") ///
	title("OLS Estimates of the Effect of Pirate Attacks on Land Conflict\label{TableOLSPoissonEstimates}") ///
	fragment



/*

\begin{table}[htbp]\centering
\small
\def\sym#1{\ifmmode^{#1}\else\(^{#1}\)\fi}
\caption{OLS Estimates of the Effect of Pirate Attacks on Land Conflict\label{TableOLSPoissonEstimates}}
\begin{threeparttable}

**************************

\begin{tablenotes} [flushleft]
Note: * p$<$0.1, ** p$<$0.05, *** p$<$0.01. Heteroskedasticity robust standard errors in parentheses. The table shows OLS estimates of the number of attacks on the number of conflict events. Column 2-8 control for region fixed effects. Column 3 controls region fixed effects, year, and month fixed effects. Column 4, 6, and 8 control for interacted year-month fixed effects. Columns 5 and 6 drop observations where wind speed is missing. Columns 7 and 8 use a Poisson model, because conflict events are a count variable.  \end{tablenotes}
\end{threeparttable}
\end{tablenotes}
*/

/*
*****Slides

eststo : reg events attacks ///
	i.oceanpolygon_id i.year i.month ///
	if altwdspd_ptlvlcollapse ~= . ///
	, robust
$OceanYes
$YearYes
$MonthYes
$YearMonthNo
$ModelOLS


eststo : poisson events attacks ///
	i.oceanpolygon_id i.year i.month ///
	, robust
$OceanYes
$YearYes
$MonthYes
$YearMonthNo
$ModelP


esttab est2 est3 est5 est9 est7 est10 using $hdir\Analysis\Output\TableOLSPoissonOceanLevelSlides.tex, replace ///
	keep(attacks) noobs collabels(none) nodepvars label ///
	mlabels(none) eqlabels(none) ///
	booktabs cells(b(fmt(%9.2f) star) se(fmt(%9.2f) par)) ///
	starlevels(* 0.10 ** 0.05 *** 0.01) star(b) ///
	scalars("N Obs." "OceanFE Ocean FE" ///
	"Year Year" "Month Month" ///
	"Model Model Type") ///
	mgroup("OLS" "No Missing Wind" "Poisson", pattern(1 0 1 0 1 0) span ///
		erepeat(\cmidrule(lr){@span}) ///
		prefix(\multicolumn{@span}{c}{) suffix (}))


********************************************************************************

		
	
/*	
i.oceanpolygon_id quarter i.year, ///
robust partial(i.oceanpolygon_id#quarter i.year)
*/


/*

eststo : ivreg2 events (attacks2 = altwdspd) ///
	i.oceanpolygon_id#month i.year, ///
	robust partial(i.oceanpolygon_id#month)
$OceanYes
$YearYes
$MonthYes
$YearMonthNo
$PoissonNo




eststo : ivreg2 events (attacks2 = altwdspd) ///
	i.oceanpolygon_id#year, ///
	robust partial(i.oceanpolygon_id#year)


	


eststo : ivreg2 events (attacks2 = altwdspd) ///
	i.oceanpolygon_id#year i.month, ///
	robust partial(i.oceanpolygon_id#year i.month)
$OceanYes
$YearYes
$MonthYes
$YearMonthNo
$PoissonNo





eststo : ivreg2 events (attacks2 = altwdspd) ///
	i.oceanpolygon_id#year i.month, ///
	robust partial(i.oceanpolygon_id#year i.month)
$OceanYes
$YearYes
$MonthYes
$YearMonthNo
$PoissonNo




eststo : ivreg2 events (attacks2 = altwdspd) ///
	i.oceanpolygon_id i.year#i.month, ///
	robust partial(i.oceanpolygon_id i.year#i.month)
$OceanYes
$YearNo
$MonthNo
$YearMonthYes
$PoissonNo


eststo : ivpoisson gmm events (attacks2 = altwdspd) ///
	i.oceanpolygon_id, ///
	vce(robust) multiplicative
$OceanYes
$YearNo
$MonthNo
$YearMonthNo
$PoissonYes

eststo : ivpoisson gmm events (attacks2 = altwdspd) ///
	i.oceanpolygon_id i.year i.month, ///
	vce(robust) multiplicative
$OceanYes
$YearYes
$MonthYes
$YearMonthNo
$PoissonYes

/*
eststo : ivpoisson gmm events (attacks = altwdspd) ///
	i.oceanpolygon_id i.year#i.month, ///
	vce(robust) multiplicative
$OceanYes
$YearYes
$MonthYes
$YearMonthNo
$PoissonYes
*/

*poisson events attacks i.oceanpolygon_id i.year i.month, robust

/*
eststo : ivpoisson cfunc events (attacks = altwdspd) ///
	i.oceanpolygon_id i.year i.month, ///
	vce(robust) 
$OceanYes
$YearYes
$MonthYes
$YearMonthNo
$PoissonYes
*/


/*
eststo: poisson events attack ///
	, robust
$OceanNo
$YearNo
$MonthNo


eststo: poisson events attack ///
	i.oceanpolygon_id i.year i.month, robust
$OceanYes
$YearYes
$MonthYes	
*/

esttab * using $hdir\Analysis\Output\NaiiveAndSecondStageTableOcean.tex, replace ///
	keep(attacks attacks2) noobs collabels(none) nodepvars label ///
	mlabels(none) eqlabels(none) ///
	booktabs cells(b(fmt(%9.2f) star) se(fmt(%9.2f) par)) ///
	starlevels(* 0.10 ** 0.05 *** 0.01) star(b) ///
	scalars("OceanFE Region" ///
	"Year Year" "Month Month" "YearMonth YrXMonth" ///
	"Poisson Poisson") ///
	mgroup("Naiive" "Instrumented Pirate Attacks", pattern(1 0 1 0 0 0 0) span ///
		erepeat(\cmidrule(lr){@span}) ///
		prefix(\multicolumn{@span}{c}{) suffix (})) ///
	title("The Effect of Increased Pirate Activity on Somalian Land Conflict \label{TableStage2NaiiveAndInstrument}")

/*
\begin{tablenotes} [flushleft]
\item Notes: N = 1436. * p$<$0.1, ** p$<$0.05, *** p$<$0.01. Standards errors are heteroskedasticity robust. Naiive estimates in columns 1 and 2 show estimates from the second stage without using wind as an instrument for pirate attacks. Poisson models in columns 7 and 8 use a Poisson model for the second stage with multiplicative errors estimated via general method of moments (gmm). All fixed effects are partialed out.
\end{tablenotes}
\end{threeparttable}
