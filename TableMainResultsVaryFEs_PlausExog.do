
global clear all
clear all


if "`c(username)'" == "Benjamin" {
global hdir "D:\Dropbox\Pirates\PaperwithBen\Work"
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

global RegionYearYes "estadd local RegionYear "X""
global RegionYearNo "estadd local RegionYear "-""

global OceanYes "estadd local OceanFE "X""
global OceanNo "estadd local OceanFE "-""

global PoissonYes "estadd local Poisson "X""
global PoissonNo "estadd local Poisson "-""

global ClusterYes "estadd local Cluster "X""
global ClusterNo "estadd local Cluster "-""


*set matsize 11000
eststo clear

winsor altwdspd_ptlvlcollapse_reproj, p(.05) gen(wdspd_ptlvl_winsor_05_rp)
label variable wdspd_ptlvl_winsor_05_rp "Median Wind Speed (Winsor 5\%)"
label variable altwdspd_ptlvlcollapse_reproj "Median Wind Speed"
label variable attacks_rp "Pirate Attacks"

/*

plausexog uci events (attacks_rp = altwdspd_ptlvlcollapse_reproj) ///
	, gmin(-10000) gmax(10000) grid(2)

plausexog uci events i.oceanpolygon_id#year#month ///
	(attacks_rp = altwdspd_ptlvlcollapse_reproj) ///
	, robust ///
	gmin(-1) gmax(1) grid(2)
	
	
plausexog ltz events ///
	(attacks_rp = altwdspd_ptlvlcollapse_reproj) ///
	tmax_mean ///
	, vce(robust) ///
	mu(0) omega(1) ///
	graph(attacks_rp) graphmu(-1(1)1) graphomega(-1(1)1)

	
plausexog ltz events ///
	(attacks_rp = altwdspd_ptlvlcollapse_reproj) ///
	tmax_mean ///
	i.oceanpolygon_id i.year i.month ///
	, vce(robust) ///
	mu(0) omega(1) ///
	graph(attacks_rp) graphmu(-1(1)1) graphomega(-1(1)1)
*/


*Using beyond plausibly exogenous cookbook
*https://watermark.silverchair.com/ectj0316.pdf?token=AQECAHi208BE49Ooan9kkhW_Ercy7Dm3ZL_9Cf3qfKAc485ysgAAAp0wggKZBgkqhkiG9w0BBwagggKKMIIChgIBADCCAn8GCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQM9zrXwwt75AgJE03RAgEQgIICUDbkRDDgggwRsSywwIMZhjv5Yd_BtSUBJGsAVdSKlx1YQWlrLEIjYRlk0JvhWZV_U5AobgTjtQutlbV2rddiXiaZlcYooxWmaewzeSA_2PbOybEo72x-GxHy2mw-_qMU9N3to0626qUd1ly-l7ZhtkTmPLvMr5OHB-KFdJrnFREhfP43cqqk0zAtiJatb-eKkE2VLSer3ygl3HK5Ml0h2KM16rP3xKeO5WTla6EkMVi0j8IFgMn8Ktw7eisuAwdPzFOUGxB8HkKeh9J_fS1Ij2RAElyI1Tz4-UxgYoWOddXiHvtbA7X1auG-roEiTkNMfvYT6HXtmrjWTc_Jyu5ViWVbg6XxwubkU40omn11Zls0pHfwTkvK-QU26n-QXTyfsQOHOcvUVhuIRJE_oBhnls-TRzn6Bv_TxfU_Tumm3IOJjnSzGX1AKuYpKpqSNP9ncz5v1KbZUyDmFeT3MsG_7ygeIiReDdy9ipZDu8J1ProHWZqsHUUv8JfMHno5FaeC2DyeIZ9hw8YIHT5Bc4dne8c9RsTb9PJLOv3xubl4jt8Xp66EgSJpyTqsRZazjK56tG4XuY0z_bsnEbRbaufuhRQuOdjVa9GPDJ89YNZ26MxyvO0a_5LPuJqU_yQ-d98i6mKfhtp8ZKzXazvlaM4p-4-E9epvldNHbXrGimbrypYs1_PmZRFTNOWJf0mgKXlmBKgXAqIBzLlFCZ6HN_qc8SbmN-CiLbMShK00xW_IN5eD0w6OGGEaLWv7Q7G6H0dt7d8qQQkcZaVyiZNv5I33Auo
*https://academic.oup.com/ectj/article/21/3/316/5145983
/*

plausexog ltz events ///
	(attacks_rp = altwdspd_ptlvlcollapse_reproj) ///
	i.oceanpolygon_id#year#month ///
	, graph(attacks_rp) graphmu(-0.06(0.03)0.06) graphomega(-0.1(0.05)0.1) ///
	mu(-0.06) omega(.01)
	
	
plausexog ltz events ///
	(attacks_rp = altwdspd_ptlvlcollapse_reproj) ///
	i.oceanpolygon_id#year#month ///
	, mu(-0.06) omega(0)

/*
forvalues mu = -.1(.05).2 {
	
	disp "`mu'"
	
	plausexog ltz events ///
		(attacks_rp = altwdspd_ptlvlcollapse_reproj) ///
		i.oceanpolygon_id#year#month ///
		, mu(`mu') omega(0)

	sleep 3000
}
*/


forvalues mu = .15(.01).2 {
	
	disp "`mu'"
	
	plausexog ltz events ///
		(attacks_rp = altwdspd_ptlvlcollapse_reproj) ///
		i.oceanpolygon_id#year#month ///
		, mu(`mu') omega(0)

	sleep 3000
}

/*
forvalues mu = .159(.0002).161 {
	
	disp "`mu'"
	
	plausexog ltz events ///
		(attacks_rp = altwdspd_ptlvlcollapse_reproj) ///
		i.oceanpolygon_id#year#month ///
		, mu(`mu') omega(0)

	sleep 2000
}
*/


forvalues mu = .1606(.00002).1608 {
	
	disp "`mu'"
	
	plausexog ltz events ///
		(attacks_rp = altwdspd_ptlvlcollapse_reproj) ///
		i.oceanpolygon_id#year#month ///
		, mu(`mu') omega(0)

	sleep 2000
}


/*
forvalues mu = -.1(.02).1 {
	
	disp "`mu'"
	
	plausexog uci events ///
		(attacks_rp = altwdspd_ptlvlcollapse_reproj) ///
		i.oceanpolygon_id#year#month ///
		, mu(`mu') gmin(0) gmax(0)
		
	sleep 3000
}
*/
*/

*******************************************************************************

matrix peNoUncertain = J(1,3,.)
matrix colnames peNoUncertain = Beta ll95 ul95


plausexog uci events i.oceanpolygon_id#year#month ///
	(attacks_rp = altwdspd_ptlvlcollapse_reproj) ///
	, robust ///
	gmin(-.06) gmax(-.06) grid(2)

/*
disp "e(lb_endogname)"
disp "`e(lb_endogname)'"
*/

disp "e(lb_attacks_rp)"
disp "`e(lb_attacks_rp)'"

matrix peNoUncertain[1,1] = e(b)[1,1]
matrix list peNoUncertain
	
matrix peNoUncertain[1,2] = `e(lb_attacks_rp)'
matrix peNoUncertain[1,3] = `e(ub_attacks_rp)'

matrix list peNoUncertain
	
frmttable , ///
	statmat(peNoUncertain) ///
	ctitle("", "Pt. Estimate", "Confidence Interval, 95\%" \ ///
	"","Beta","Lower Bound","Upper Bound") ///
	multicol(1,3,2) ///
	rtitle("Pirate Attacks")
	
frmttable , ///
	statmat(peNoUncertain) ///
	ctitle("", "Pt. Estimate", "Confidence Interval, 95\%" \ ///
	"","Beta","Lower Bound","Upper Bound") ///
	multicol(1,3,2) ///
	rtitle("Pirate Attacks") ///
	hlines(110)
	


frmttable , ///
	statmat(peNoUncertain) ///
	ctitle("", "Pt. Estimate", "Confidence Interval, 95\%" \ ///
	"","Beta","Lower Bound","Upper Bound") ///
	multicol(1,3,2) ///
	rtitle("Pirate Attacks") ///
	addrows("Method", "", "", "UCI" \ ///
	"Gamma Upper Bound", "", "", "-0.06" \ ///
	"Gamma Lower Bound", "", "", "-0.06")

	
	
local tablename = "Plausexog"	
local fragname = "NoUncertainty"	



frmttable using $hdir\Build\Input\TableFrags\Table`tablename'\Table`tablename'`fragname'.tex, ///
	statmat(peNoUncertain) ///
	replace tex fragment ///
	ctitle("", "Pt. Estimate", "Confidence Interval, 95\%" \ ///
	"","Beta","Lower Bound","Upper Bound") ///
	multicol(1,3,2) ///
	rtitle("Pirate Attacks") ///
	addrows("Method", "", "", "UCI" \ ///
	"$\gamma$ Upper Bound", "", "", "-0.06" \ ///
	"$\gamma$ Lower Bound", "", "", "-0.06") ///
	hlines(10;10;10;11)
	
	

	


*******************************************************************************

matrix peUncertainPrior = J(1,3,.)
matrix colnames peUncertainPrior = Beta ll95 ul95

local gmean = -0.06

local s1 = 0.018
local s2 = 0.17

local rootsum = ((`s1')^2+(`s2')^2)^(1/2)
disp `rootsum'

local gerror = (0.125*`rootsum')^2
disp `gerror'

*egen rymintfes = group(oceanpolygon_id year month)

/*
plausexog ltz events i.oceanpolygon_id#year#month ///
	(attacks_rp = altwdspd_ptlvlcollapse_reproj) ///
	, robust ///
	mu(-.06) omega(`gerror') ///
	graph(attacks_rp) graphmu(-1(1)1) graphomega(-1(1)1)
*/

plausexog ltz events ///
	(attacks_rp = altwdspd_ptlvlcollapse_reproj) ///
	i.oceanpolygon_id#year#month ///
	, vce(robust) ///
	mu(-.06) omega(`gerror')
	
*graph(attacks_rp) graphmu(-1(1)1) graphomega(-1(1)1)

matrix peUncertainPrior[1,1] = e(b)[1,1]
matrix list peUncertainPrior
	
matrix peUncertainPrior[1,2] = `e(lb_attacks_rp)'
matrix peUncertainPrior[1,3] = `e(ub_attacks_rp)'

matrix list peUncertainPrior


frmttable , ///
	statmat(peUncertainPrior) ///
	ctitle("", "Pt. Estimate", "Confidence Interval, 95\%" \ ///
	"","Beta","Lower Bound","Upper Bound") ///
	multicol(1,3,2) ///
	rtitle("Pirate Attacks")

local tablename = "Plausexog"	
local fragname = "UncertainPriors"	

frmttable using $hdir\Build\Input\TableFrags\Table`tablename'\Table`tablename'`fragname'.tex ///
	, statmat(peUncertainPrior) ///
	replace tex fragment ///
	ctitle("", "Pt. Estimate", "Confidence Interval, 95\%" \ ///
	"","Beta","Lower Bound","Upper Bound") ///
	multicol(1,3,2) ///
	rtitle("Pirate Attacks") ///
	addrows("Method", "", "", "LTZ" \ ///
	"$\gamma$ Distribution", "", "", "Normal" \ ///
	"$\gamma$ $\mu$", "", "", "-0.06" \ ///
	"$\gamma$ $\Omega$", "", "", "0.0004") ///
	hlines(10;10;10;11)
	

/*	
plausexog ltz events ///
	(attacks_rp = altwdspd_ptlvlcollapse_reproj) ///
	i.oceanpolygon_id#year#month ///
	, vce(robust) ///
	mu(-.06) omega(`gerror') ///
	graph(attacks_rp) graphmu(-1(1)1) graphomega(-1(1)1)

	

disp `gmean'+10*`gerror'
local 10devup = `gmean'+10*`gerror'
disp `gmean'-10*`gerror' 
local 10devdown = `gmean'-10*`gerror'
	

	
plausexog ltz events ///
	(attacks_rp = altwdspd_ptlvlcollapse_reproj) ///
	i.oceanpolygon_id#year#month ///
	, vce(robust) ///
	mu(-.06) omega(`gerror') ///
	graph(attacks_rp) graphmu(`gmean'(1)`gmean') graphomega(`10devdown'(.0005)`10devup')

		

/*
***********************

****Finding pirate attacks by year and month

preserve

import excel "$hdir\Build\Input\Piracy\ListOfIncidents (1).xls", sheet("FullList") firstrow clear

local maxlon = 66
local minlon = 40

local maxlat = 18
local minlat = -4

tolower

*local deg = char(176)

foreach var of varlist lat lon {

split `var', p(" ")

gen `var'deg = real(regexs(1)) if regexm(`var'1,"([0-9]+)")
gen `var'min = real(regexs(1)) if regexm(`var'2,"([0-9]+)")

}
*


replace latitudedeg = latitudedeg * -1 if latitude3 == "S"
replace longitudedeg = longitudedeg * -1 if longitude3 == "W"


replace latitudedeg = latitudedeg + (latitudemin/60) if latitude3 == "N"
replace latitudedeg = latitudedeg - (latitudemin/60) if latitude3 == "S"

replace longitudedeg = longitudedeg + (longitudemin/60) if longitude3 == "E"
replace longitudedeg = longitudedeg - (longitudemin/60) if longitude3 == "W"


keep if longitudedeg < `maxlon'
keep if longitudedeg > `minlon'

keep if latitudedeg < `maxlat'
keep if latitudedeg > `minlat'


rename date date2
gen date = date(date2,"YMD")
drop date2
gen date_rawnum = date

format date %td

gen year = year(date)
gen month = month(date)



keep if year >=2008
keep if year < 2017


tab year month


restore