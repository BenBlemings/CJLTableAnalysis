
global clear all
clear all

if "`c(username)'" == "Benjamin" {
global hdir "D:\Dropbox\Pirates\PaperwithBen\Work"
global bdir "D:\Dropbox\Pirates\PaperwithBen\Work\Build"
}
*

if "`c(username)'" == "benbl" {
global hdir "C:\Users\benbl\Dropbox\Pirates\PaperWithBen\Work"
}
*

use $hdir\Analysis\Input\AnalysisFileOcean.dta, clear


global RegionYes "estadd local GroupFE "X""
global RegionNo "estadd local GroupFE "-""

global YearYes "estadd local Year "X""
global YearNo "estadd local Year "-""

global MonthYes "estadd local Month "X""
global MonthNo "estadd local Month "-""

global YearMonthYes "estadd local YearMonth "X""
global YearMonthNo "estadd local YearMonth "-""

global RegionYearYes "estadd local RegionYear "Yes""
global RegionYearNo "estadd local RegionYear "No""

global OceanYes "estadd local OceanFE "X""
global OceanNo "estadd local OceanFE "-""

global PoissonYes "estadd local Poisson "X""
global PoissonNo "estadd local Poisson "-""

global ClusterYes "estadd local Cluster "X""
global ClusterNo "estadd local Cluster "-""

global RYMIntYes "estadd local RegYrMth "Yes""
global RYMIntNo "estadd local RegYrMth "No""


global landcovars "precip_mean tmax_mean"


set matsize 11000
eststo clear

winsor altwdspd_ptlvlcollapse_reproj, p(.05) gen(wdspd_ptlvl_winsor_05_rp)
label variable wdspd_ptlvl_winsor_05_rp "Median Wind Speed (Winsor 5\%)"
label variable altwdspd_ptlvlcollapse_reproj "Median Wind Speed"
label variable attacks_rp "Pirate Attacks"

lab var precip_mean "Precip. Mean"
lab var tmax_mean "Temp. Max. Mean"



eststo: reg events altwdspd_ptlvlcollapse_reproj ///
	///
	, robust
	
eststo: reg attacks_rp altwdspd_ptlvlcollapse_reproj ///
	 ///
	, robust
	
eststo: ivreg2 events (attacks_rp = altwdspd_ptlvlcollapse_reproj) ///
	 ///
	, robust
$RYMIntNo

estadd scalar InstrumentFStat = e(widstat)

boottest attacks_rp, weight(webb) ar statistic(c) nograph

weakiv

local arcfset = e(ar_cset)
disp "`arcfset'"
estadd local arcfset "`arcfset'": est3

local arp = e(ar_p)
disp "`arp'"
estadd scalar arp = `arp': est3


local tablename = "MainRYMIntFEsWithLandCovars"	
local fragname = "SingleIndVar"


esttab * using $hdir\Build\Input\TableFrags\Table`tablename'\Table`tablename'`fragname'.tex, replace ///
	keep(altwdspd_ptlvlcollapse_reproj attacks_rp ) ///
	noobs collabels(none) label depvars nonumbers ///
	mlabels(none) eqlabels(none) ///
	booktabs cells(b(fmt(%9.2f) star) se(fmt(%9.2f) par)) ///
	starlevels(* 0.10 ** 0.05 *** 0.01) star(b) ///
	scalars("N Observations" "InstrumentFStat Kleibergen-Paap F" ///
	"arcfset A-R 95\% Confidence Set" "arp A-R P-Value" ///
	"RegYrMth RegionXYearXMonth FEs") ///
	title("2SLS Estimates, Wd2 \label{TableMain2SLSReStudPanelwd2}") ///
	fragment

	
esttab * using $hdir\Build\Input\TableFrags\Table`tablename'\Table`tablename'HeaderFooterFind.tex, replace ///
	drop(*) noobs collabels(none) label depvars ///
	mlabels("Reduced Form" "First Stage" "Second Stage") eqlabels(none) ///
	booktabs cells(b(fmt(%9.2f) star) se(fmt(%9.2f) par)) ///
	starlevels(* 0.10 ** 0.05 *** 0.01) star(b) ///
	title("2SLS Estimates of Piracy on Land Conflict  \label{TableMain2SLSReStudPanelwd2}")

*disp "Panel A"
*sleep 3000
	
*******************************************************************************
eststo clear

global fes "i.oceanpolygon_id i.month i.year"

eststo: reg events altwdspd_ptlvlcollapse_reproj ///
	 ///
	$fes ///
	, robust
	
eststo: reg attacks_rp altwdspd_ptlvlcollapse_reproj ///
	 ///
	$fes ///
	, robust 
	
eststo: ivreg2 events (attacks_rp = altwdspd_ptlvlcollapse_reproj) ///
	 ///
	$fes ///
	, robust partial($fes)


estadd scalar InstrumentFStat = e(widstat)

*boottest attacks_rp, weight(webb) ar statistic(c) nograph

weakiv

local arcfset = e(ar_cset)
disp "`arcfset'"
estadd local arcfset "`arcfset'": est3

local arp = e(ar_p)
disp "`arp'"
estadd scalar arp = `arp': est3


local tablename = "MainRYMIntFEsWithLandCovars"	
local fragname = "UninteractedRegionYearMonth"


esttab * using $hdir\Build\Input\TableFrags\Table`tablename'\Table`tablename'`fragname'.tex, replace ///
	keep(altwdspd_ptlvlcollapse_reproj attacks_rp) ///
	noobs collabels(none) label depvars nonumbers ///
	mlabels(none) eqlabels(none) ///
	booktabs cells(b(fmt(%9.2f) star) se(fmt(%9.2f) par)) ///
	starlevels(* 0.10 ** 0.05 *** 0.01) star(b) ///
	scalars("InstrumentFStat Kleibergen-Paap F" ///
	"arcfset A-R 95\% Confidence Set" "arp A-R P-Value" ///
	"RegYrMth RegionXYearXMonth FEs") ///
	title("2SLS Estimates, Wd2 \label{TableMain2SLSReStudPanelwd2}") ///
	fragment

*disp "Panel B"
*sleep 3000
	
*******************************************************************************
eststo clear

global fes "i.oceanpolygon_id#year i.month"

eststo: reg events altwdspd_ptlvlcollapse_reproj ///
	///
	$fes ///
	, robust 
	
eststo: reg attacks_rp altwdspd_ptlvlcollapse_reproj ///
	///
	$fes ///
	, robust 
	 
eststo: ivreg2 events (attacks_rp = altwdspd_ptlvlcollapse_reproj) ///
	 ///
	$fes ///
	, robust partial($fes)

estadd scalar InstrumentFStat = e(widstat)

boottest attacks_rp, weight(webb) ar statistic(c) nograph

weakiv

local arcfset = e(ar_cset)
disp "`arcfset'"
estadd local arcfset "`arcfset'": est3

local arp = e(ar_p)
disp "`arp'"
estadd scalar arp = `arp': est3


local tablename = "MainRYMIntFEsWithLandCovars"	
local fragname = "RegionYearInteractedMonth"


esttab * using $hdir\Build\Input\TableFrags\Table`tablename'\Table`tablename'`fragname'.tex, replace ///
	keep(altwdspd_ptlvlcollapse_reproj attacks_rp) ///
	noobs collabels(none) label depvars nonumbers ///
	mlabels(none) eqlabels(none) ///
	booktabs cells(b(fmt(%9.2f) star) se(fmt(%9.2f) par)) ///
	starlevels(* 0.10 ** 0.05 *** 0.01) star(b) ///
	scalars("N Observations" "InstrumentFStat Kleibergen-Paap F" ///
	"arcfset A-R 95\% Confidence Set" "arp A-R P-Value") ///
	title("2SLS Estimates, Wd2 \label{TableMain2SLSReStudPanelwd2}") ///
	fragment

*disp "Panel C"
*sleep 3000	

*******************************************************************************	
eststo clear

global fes "i.oceanpolygon_id#year#month"

eststo: reg events altwdspd_ptlvlcollapse_reproj ///
	 ///
	$fes ///
	, robust 
	
eststo: reg attacks_rp altwdspd_ptlvlcollapse_reproj ///
	 ///
	$fes ///
	, robust
	
eststo: ivreg2 events (attacks_rp = altwdspd_ptlvlcollapse_reproj) ///
	 ///
	$fes ///
	, robust partial($fes)
$RYMIntYes

estadd scalar InstrumentFStat = e(widstat)

/*
boottest attacks_rp ///
	, weight(webb) ar statistic(c) nograph ///
	gridmin(-50) gridmax(50)
*/

weakiv

local arcfset = e(ar_cset)
disp "`arcfset'"
estadd local arcfset "`arcfset'": est3

local arp = e(ar_p)
disp "`arp'"
estadd scalar arp = `arp': est3



*estadd scalar InstrumentFStat = e(widstat)

/*
boottest attacks_rp ///
	, weight(webb) ar statistic(c) nograph ///
	gridmin(-50) gridmax(50)
*/

local tablename = "MainRYMIntFEsWithLandCovars"	
local fragname = "RegionYearMonthInteracted"


esttab * using $hdir\Build\Input\TableFrags\Table`tablename'\Table`tablename'`fragname'.tex, replace ///
	keep(altwdspd_ptlvlcollapse_reproj attacks_rp) ///
	noobs collabels(none) label depvars nonumbers ///
	mlabels(none) eqlabels(none) ///
	booktabs cells(b(fmt(%9.2f) star) se(fmt(%9.2f) par)) ///
	starlevels(* 0.10 ** 0.05 *** 0.01) star(b) ///
	scalars("N Observations" "InstrumentFStat Kleibergen-Paap F" ///
	"arcfset A-R 95\% Confidence Set" "arp A-R P-Value" ///
	"RegYrMth RegionXYearXMonth FEs") ///
	title("2SLS Estimates, Wd2 \label{TableMain2SLSReStudPanelwd2}") ///
	fragment


*disp "Panel D"
*sleep 3000
	
******************************************************************************
eststo clear

global fes "i.oceanpolygon_id#year#month"
global landcovars "precip_mean tmax_mean"

*****Create the matrix of bootstrapped

**regs
reg events altwdspd_ptlvlcollapse_reproj ///
	$landcovars ///
	$fes ///
	, cluster(oceanpolygon_id) 

boottest altwdspd_ptlvlcollapse_reproj, weight(webb) seed(1234) nograph

disp "`r(p)'"
local bootpround1 = round(`r(p)', 0.001)
disp "`bootpround1'"

disp "`r(CI)'"

matrix list r(CI)

**
reg attacks_rp altwdspd_ptlvlcollapse_reproj ///
	$landcovars ///
	$fes ///
	, cluster(oceanpolygon_id) 

boottest altwdspd_ptlvlcollapse_reproj, weight(webb) seed(1234) nograph

disp "`r(p)'"
local bootpround2 = round(`r(p)', 0.001)
disp "`bootpround2'"

**
ivreg2 events (attacks_rp = altwdspd_ptlvlcollapse_reproj) ///
	$landcovars ///
	$fes ///
	, cluster(oceanpolygon_id) partial($fes $landcovars)

boottest attacks_rp ///
	, weight (webb) ar statistic(c) seed(1234) nograph ///
	gridmin(-50) gridmax(50)

disp "`r(p)'"
local bootpround3 = round(`r(p)', 0.001)
disp "`bootpround3'"

**matrix of pvs
matrix bootps = (`bootpround1',`bootpround2',`bootpround3')

matrix colnames bootps = altwdspd_ptlvlcollapse_reproj poop poop
matrix list bootps

*********************************

eststo: reg events altwdspd_ptlvlcollapse_reproj ///
	$landcovars ///
	$fes ///
	, robust
	
estadd matrix bootps
	
**

matrix colnames bootps = poop altwdspd_ptlvlcollapse_reproj poop
matrix list bootps


eststo: reg attacks_rp altwdspd_ptlvlcollapse_reproj ///
	$landcovars ///
	$fes ///
	, robust

estadd matrix bootps

**

matrix colnames bootps = poop poop attacks_rp
matrix list bootps	

eststo: ivreg2 events (attacks_rp = altwdspd_ptlvlcollapse_reproj) ///
	$landcovars ///
	$fes ///
	, robust partial($fes)
$RYMIntYes

estadd scalar InstrumentFStat = e(widstat)


estadd matrix bootps


weakiv

local arcfset = e(ar_cset)
disp "`arcfset'"
estadd local arcfset "`arcfset'": est3

local arp = e(ar_p)
disp "`arp'"
estadd scalar arp = `arp': est3



/*
ivreg2 events (attacks_rp = altwdspd_ptlvlcollapse_reproj) ///
	precip_mean tmax_mean ///
	$fes ///
	, cluster(oceanpolygon_id) partial($fes)

*estadd scalar InstrumentFStat = e(widstat)

boottest attacks_rp ///
	, weight(webb) ar statistic(c) nograph ///
	gridmin(-50) gridmax(50)
*/

local tablename = "MainRYMIntFEsWithLandCovars"	
local fragname = "RegionYearMonthInteractedCovarsWildCluster"


esttab * using $hdir\Build\Input\TableFrags\Table`tablename'\Table`tablename'`fragname'.tex, replace ///
	keep($landcovars altwdspd_ptlvlcollapse_reproj attacks_rp) ///
	noobs collabels(none) label depvars nonumbers ///
	mlabels(none) eqlabels(none) ///
	booktabs ///
	cells("b(fmt(%9.2f) star)" "se(fmt(%9.2f) par)" "bootps(fmt(2) par([ ]))") ///
	starlevels(* 0.10 ** 0.05 *** 0.01) star(b) ///
	scalars("N Observations" "InstrumentFStat Kleibergen-Paap F" ///
	"arcfset A-R 95\% Confidence Set" "arp A-R P-Value" ///
	"RegYrMth RegionXYearXMonth FEs") ///
	title("2SLS Estimates, Wd2 \label{TableMain2SLSReStudPanelwd2}") ///
	fragment

*disp "Panel E"
*sleep 3000

******************************************************************************
eststo clear

global fes "i.oceanpolygon_id#year#month"
global landcovars "precip_mean tmax_mean"

lab var chlor_a "Chlorophyll Concentration"

*****Create the matrix of bootstrapped

**regs
reg events altwdspd_ptlvlcollapse_reproj ///
	$landcovars chlor_a ///
	$fes ///
	, cluster(oceanpolygon_id) 

boottest altwdspd_ptlvlcollapse_reproj, weight(webb) seed(1234) nograph

disp "`r(p)'"
local bootpround1 = round(`r(p)', 0.001)
disp "`bootpround1'"

disp "`r(CI)'"

matrix list r(CI)

**
reg attacks_rp altwdspd_ptlvlcollapse_reproj ///
	$landcovars chlor_a ///
	$fes ///
	, cluster(oceanpolygon_id) 

boottest altwdspd_ptlvlcollapse_reproj, weight(webb) seed(1234) nograph

disp "`r(p)'"
local bootpround2 = round(`r(p)', 0.001)
disp "`bootpround2'"

**
ivreg2 events (attacks_rp = altwdspd_ptlvlcollapse_reproj) ///
	$landcovars  chlor_a ///
	$fes ///
	, cluster(oceanpolygon_id) partial($fes $landcovars)

boottest attacks_rp ///
	, weight (webb) ar statistic(c) seed(1234) nograph ///
	gridmin(-50) gridmax(50)

disp "`r(p)'"
local bootpround3 = round(`r(p)', 0.001)
disp "`bootpround3'"

**matrix of pvs
matrix bootps = (`bootpround1',`bootpround2',`bootpround3')

matrix colnames bootps = altwdspd_ptlvlcollapse_reproj poop poop
matrix list bootps


********************************

eststo: reg events altwdspd_ptlvlcollapse_reproj ///
	$landcovars chlor_a ///
	$fes ///
	, robust
	
estadd matrix bootps
	
**

matrix colnames bootps = poop altwdspd_ptlvlcollapse_reproj poop
matrix list bootps


eststo: reg attacks_rp altwdspd_ptlvlcollapse_reproj ///
	$landcovars chlor_a ///
	$fes ///
	, robust

estadd matrix bootps

**

matrix colnames bootps = poop poop attacks_rp
matrix list bootps	

eststo: ivreg2 events (attacks_rp = altwdspd_ptlvlcollapse_reproj) ///
	$landcovars chlor_a ///
	$fes ///
	, robust partial($fes)
$RYMIntYes

estadd scalar InstrumentFStat = e(widstat)


estadd matrix bootps


weakiv

local arcfset = e(ar_cset)
disp "`arcfset'"
estadd local arcfset "`arcfset'": est3

local arp = e(ar_p)
disp "`arp'"
estadd scalar arp = `arp': est3


/*
ivreg2 events (attacks_rp = altwdspd_ptlvlcollapse_reproj) ///
	precip_mean tmax_mean ///
	$fes ///
	, cluster(oceanpolygon_id) partial($fes)

*estadd scalar InstrumentFStat = e(widstat)

boottest attacks_rp ///
	, weight(webb) ar statistic(c) nograph ///
	gridmin(-50) gridmax(50)
*/

local tablename = "MainRYMIntFEsWithLandCovars"	
local fragname = "RegionYearMonthInteractedCovarsAndChlorWildCluster"


esttab * using $hdir\Build\Input\TableFrags\Table`tablename'\Table`tablename'`fragname'.tex, replace ///
	keep($landcovars chlor_a altwdspd_ptlvlcollapse_reproj attacks_rp) ///
	noobs collabels(none) label depvars nonumbers ///
	mlabels(none) eqlabels(none) ///
	booktabs ///
	cells("b(fmt(%9.2f) star)" "se(fmt(%9.2f) par)" "bootps(fmt(2) par([ ]))") ///
	starlevels(* 0.10 ** 0.05 *** 0.01) star(b) ///
	scalars("N Observations" "InstrumentFStat Kleibergen-Paap F" ///
	"arcfset A-R 95\% Confidence Set" "arp A-R P-Value" ///
	"RegYrMth RegionXYearXMonth FEs") ///
	title("2SLS Estimates, Wd2 \label{TableMain2SLSReStudPanelwd2}") ///
	fragment

******************************************************************************
eststo clear

use $bdir\Output\AnalysisFile_AgOceanWindByYearMonthRegion.dta, clear

preserve

use $hdir\Analysis\Input\AnalysisFileOcean.dta, clear

collapse (sum) attacks_rp events ///
	, by(oceanpolygon_id year month)
	
save $hdir\Analysis\Temp\AttacksEventsByYearMonthRegion.dta, replace

restore

dmerge year month oceanpolygon_id using $hdir\Analysis\Temp\AttacksEventsByYearMonthRegion.dta

tab _merge
keep if _merge == 3
drop _merge

order oceanpolygon_id year month alt* attacks events

lab var altwdspd "Median Wind Speed"
lab var attacks_rp "Pirate Attacks"

ivreg2 events (attacks_rp = altwdspd) ///
	, robust

ivreg2 events (attacks_rp = altwdspd) ///
	i.oceanpolygon_id#year ///
	, robust small
	


/*
global foods = "price_median_CattleLocal price_median_LocalSesOil" ///
		"price_median_Sugar"
		
disp "$foods"
*/

inspect price_median*

preserve

drop *_ln

/*
ivreg2 events (attacks_rp = altwdspd) ///
	price_* ///
	i.oceanpolygon_id#year ///
	, robust

*With few/none missing
*At least 290
ivreg2 events (attacks_rp = altwdspd) ///
	price_median_CattleLocal price_median_DailyLaborRate ///
	price_median_LocalSesOil1L price_median_Sugar price_median_WheatFlour1kg ///
	price_median_CamelLocal price_median_Charcoal price_median_Cowpeas ///
	price_median_Diesel price_median_Firewood price_median_FreshCamelMilk ///
	price_median_GoatExport price_median_GoatLocal price_median_GrindingCost ///
	price_median_ImportedRedRice price_median_Kerosene price_median_Petrol ///
	price_median_RedSorghum1kg price_median_Salt price_median_SheepExport ///
	price_median_Soap price_median_TeaLeaves price_median_VegOil ///
	price_median_WaterDrum price_median_WheatGrain price_median_WhiteMaize1kg ///
	i.oceanpolygon_id#year /// 
	, robust
*/

eststo: reg events altwdspd ///
	price_median_CattleLocal price_median_DailyLaborRate ///
	price_median_LocalSesOil1L price_median_Sugar price_median_WheatFlour1kg ///
	price_median_CamelLocal price_median_Charcoal price_median_Cowpeas ///
	price_median_Diesel price_median_Firewood price_median_FreshCamelMilk ///
	price_median_GoatExport price_median_GoatLocal price_median_GrindingCost ///
	price_median_ImportedRedRice price_median_Kerosene price_median_Petrol ///
	price_median_RedSorghum1kg price_median_Salt price_median_SheepExport ///
	price_median_Soap price_median_TeaLeaves price_median_VegOil ///
	price_median_WaterDrum price_median_WheatGrain price_median_WhiteMaize1kg ///
	i.oceanpolygon_id#year /// 
	, robust

eststo: reg attacks_rp altwdspd ///
	price_median_CattleLocal price_median_DailyLaborRate ///
	price_median_LocalSesOil1L price_median_Sugar price_median_WheatFlour1kg ///
	price_median_CamelLocal price_median_Charcoal price_median_Cowpeas ///
	price_median_Diesel price_median_Firewood price_median_FreshCamelMilk ///
	price_median_GoatExport price_median_GoatLocal price_median_GrindingCost ///
	price_median_ImportedRedRice price_median_Kerosene price_median_Petrol ///
	price_median_RedSorghum1kg price_median_Salt price_median_SheepExport ///
	price_median_Soap price_median_TeaLeaves price_median_VegOil ///
	price_median_WaterDrum price_median_WheatGrain price_median_WhiteMaize1kg ///
	i.oceanpolygon_id#year /// 
	, robust

eststo: ivreg2 events (attacks_rp = altwdspd) ///
	price_median_CattleLocal price_median_DailyLaborRate ///
	price_median_LocalSesOil1L price_median_Sugar price_median_WheatFlour1kg ///
	price_median_CamelLocal price_median_Charcoal price_median_Cowpeas ///
	price_median_Diesel price_median_Firewood price_median_FreshCamelMilk ///
	price_median_GoatExport price_median_GoatLocal price_median_GrindingCost ///
	price_median_ImportedRedRice price_median_Kerosene price_median_Petrol ///
	price_median_RedSorghum1kg price_median_Salt price_median_SheepExport ///
	price_median_Soap price_median_TeaLeaves price_median_VegOil ///
	price_median_WaterDrum price_median_WheatGrain price_median_WhiteMaize1kg ///
	i.oceanpolygon_id#year /// 
	, robust
$RYMIntNo
$RegionYearYes

estadd scalar InstrumentFStat = e(widstat)


weakiv

local arcfset = e(ar_cset)
disp "`arcfset'"
estadd local arcfset "`arcfset'": est3

local arp = e(ar_p)
disp "`arp'"
estadd scalar arp = `arp': est3


local tablename = "MainRYMIntFEsWithLandCovars"	
local fragname = "MonthlyWithAgPriceCovars"


esttab * using $hdir\Build\Input\TableFrags\Table`tablename'\Table`tablename'`fragname'.tex, replace ///
	keep(altwdspd attacks_rp) ///
	noobs collabels(none) label depvars nonumbers ///
	mlabels(none) eqlabels(none) ///
	booktabs ///
	cells("b(fmt(%9.2f) star)" "se(fmt(%9.2f) par)") ///
	starlevels(* 0.10 ** 0.05 *** 0.01) star(b) ///
	scalars("N Observations" "InstrumentFStat Kleibergen-Paap F" ///
	"arcfset A-R 95\% Confidence Set" "arp A-R P-Value" ///
	"RegYrMth RegionXYearXMonth FEs" "RegionYear RegionXYear FEs") ///
	title("2SLS Estimates, Wd2 \label{TableMain2SLSReStudPanelwd2}") ///
	fragment


restore
	
*****************************************************************************	
eststo clear


*preserve

*Non-ag
drop *Hollow* *Hol* *Daily* *Cement* *Charcoal* *CookingPot* *Diesel* 
drop *Firewood* *Grinding* *Iron* *JerryCan* *Kerosene* *Petrol* *Plastic*
drop *Roofing* *Soap* *Timber* *Blanket*

*using median
drop *mean*

keep oceanpolygon_id-events *_ln

*no export
drop *CattleExport* *GoatExport* *SheepExport*

*not in figure- not sure why
drop price_median_WheatFlour1kg_ln


reg events altwdspd ///
	price_*, robust
	
reg attacks_rp altwdspd ///
	price_*, robust

ivreg2 events (attacks_rp = altwdspd) ///
	price_*, robust
	
	
reg events altwdspd ///
	price_* ///
	i.oceanpolygon_id#year i.month ///
	, robust
	
reg attacks_rp altwdspd ///
	price_*, robust

ivreg2 events (attacks_rp = altwdspd) ///
	price_* ///
	i.oceanpolygon_id#year i.month ///
	, robust

*restore


*****************************************************************************	
eststo clear

eststo: reg events altwdspd ///
	i.oceanpolygon_id#year /// 
	, robust
	

eststo: reg attacks_rp altwdspd ///
	i.oceanpolygon_id#year /// 
	, robust

	
eststo: ivreg2 events (attacks_rp = altwdspd) ///
	i.oceanpolygon_id#year /// 
	, robust
$RYMIntNo
$RegionYearYes

estadd scalar InstrumentFStat = e(widstat)

weakiv

local arcfset = e(ar_cset)
disp "`arcfset'"
estadd local arcfset "`arcfset'": est3

local arp = e(ar_p)
disp "`arp'"
estadd scalar arp = `arp': est3


local tablename = "MonthlyWithNoCovars"	
local fragname = "MonthlyWithNoCovars"


esttab * using $hdir\Build\Input\TableFrags\Table`tablename'\Table`tablename'`fragname'.tex, replace ///
	keep(altwdspd attacks_rp) ///
	noobs collabels(none) label depvars nonumbers ///
	mlabels(none) eqlabels(none) ///
	booktabs ///
	cells("b(fmt(%9.2f) star)" "se(fmt(%9.2f) par)") ///
	starlevels(* 0.10 ** 0.05 *** 0.01) star(b) ///
	scalars("N Observations" "InstrumentFStat Kleibergen-Paap F" ///
	"arcfset A-R 95\% Confidence Set" "arp A-R P-Value" ///
	"RegYrMth RegionXYearXMonth FEs" "RegionYear RegionXYear FEs") ///
	title("2SLS Estimates, Wd2 \label{TableMain2SLSReStudPanelwd2}") ///
	fragment

/*
******************************************************************************
eststo clear

global fes "i.oceanpolygon_id#year#month i.week"


********

eststo: reg events altwdspd_ptlvlcollapse_reproj ///
	$landcovars ///
	$fes ///
	, robust 
	
eststo: reg attacks_rp altwdspd_ptlvlcollapse_reproj ///
	$landcovars ///
	$fes ///
	, robust
	
eststo: ivreg2 events (attacks_rp = altwdspd_ptlvlcollapse_reproj) ///
	$landcovars ///
	$fes ///
	, robust partial($fes)

estadd scalar InstrumentFStat = e(widstat)

boottest attacks_rp ///
	, weight(webb) ar statistic(c) nograph ///
	gridmin(-50) gridmax(50)

weakiv

local arcfset = e(ar_cset)
disp "`arcfset'"
estadd local arcfset "`arcfset'": est3

local arp = e(ar_p)
disp "`arp'"
estadd scalar arp = `arp': est3


ivreg2 events (attacks_rp = altwdspd_ptlvlcollapse_reproj) ///
	$landcovars ///
	$fes ///
	, cluster(oceanpolygon_id) partial($fes)

*estadd scalar InstrumentFStat = e(widstat)

boottest attacks_rp ///
	, weight(webb) ar statistic(c) nograph ///
	gridmin(-50) gridmax(50)

/*
local tablename = "MainRYMIntFEsWithLandCovars"	
local fragname = "RegionYearMonthInteracted"


esttab * using $hdir\Build\Input\TableFrags\Table`tablename'\Table`tablename'`fragname'.tex, replace ///
	keep(precip_mean tmax_mean altwdspd_ptlvlcollapse_reproj attacks_rp) ///
	noobs collabels(none) label depvars nonumbers ///
	mlabels(none) eqlabels(none) ///
	booktabs cells(b(fmt(%9.2f) star) se(fmt(%9.2f) par)) ///
	starlevels(* 0.10 ** 0.05 *** 0.01) star(b) ///
	scalars("InstrumentFStat Kleibergen-Paap F" ///
	"arcfset A-R 95\% Conf. Set" "arp A-R P-Value") ///
	title("2SLS Estimates, Wd2 \label{TableMain2SLSReStudPanelwd2}") ///
	fragment