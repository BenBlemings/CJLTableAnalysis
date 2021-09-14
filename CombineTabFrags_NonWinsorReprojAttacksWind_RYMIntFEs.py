_# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 22:13:23 2019

@author: Benjamin
"""


import os
import shutil
import numpy as np
import re

hdir = "D:/Dropbox/Pirates/PaperwithBen/Work"

fragdir = hdir + '/Build/Input/TableFrags'


try:
    os.mkdir(fragdir)
except OSError:
    print("Did not create %s failed, already created" % fragdir)
else:
    print("Successfully created the directotry %s " % fragdir)
    


######Desc Stats Table Together with aggregate events/sub-events_wd2
tablename = "CombinedDescStats_wd3"

tablepath = fragdir + "/Table" + tablename

try:
    os.makedirs(tablepath)
except OSError:
    print("Did not create %s failed, already created" % tablepath)
else:
    print("Successfully created the directotry %s " % tablepath)

##Switch to this method of folder for paper, folder for slides
outplaces = ("P", "S")
                    
for outplace in outplaces :
    
    soutplace = str(outplace)
    
    tablename = "CombinedDescStats_wd3_" + soutplace
    
    tablepath = fragdir + "/Table" + tablename
    
    try:
        os.makedirs(tablepath)
    except OSError:
        print("Did not create %s failed, already created" % tablepath)
    else:
        print("Successfully created the directotry %s " % tablepath)
    
    
#Re-establishing table paths after new folder creation
tablename = "CombinedDescStats_wd3"

tablepath = fragdir + "/Table" + tablename

try:
    os.makedirs(tablepath)
except OSError:
    print("Did not create %s failed, already created" % tablepath)
else:
    print("Successfully created the directotry %s " % tablepath)

headerpath = tablepath + "/Table" + tablename + "Header.tex" 
footerpath = tablepath + "/Table" + tablename + "Footer.tex"

PanelABSep1 = tablepath + "/PanelsABSep.txt"
PanelBCSep2 = tablepath + "/PanelsBCSep.txt"
TopPanelASep0 = tablepath + "/TopPanelASep.txt"


midpath1 = tablepath + "/Table" + tablename + "Frag.tex"
midpath2 = tablepath + "/Table" + tablename + "FragAboveMedWdSpd.tex"
midpath3 = tablepath + "/Table" + tablename + "FragBelowMedWdSpd.tex"


outpath = hdir + "/Analysis/Output/" + tablename + '.tex'
    
filenames = [headerpath, TopPanelASep0, midpath1, PanelABSep1, midpath2, PanelBCSep2, midpath3, footerpath]
with open(outpath , 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                    outfile.write(line)
                    
                    
tablename = "CombinedDescStats_wd3_S"

tablepath = fragdir + "/Table" + tablename

headerpath = tablepath + "/Table" + tablename + "Header.tex" 
footerpath = tablepath + "/Table" + tablename + "Footer.tex"

PanelABSep1 = tablepath + "/PanelsABSep.txt"
PanelBCSep2 = tablepath + "/PanelsBCSep.txt"
TopPanelASep0 = tablepath + "/TopPanelASep.txt"


midpath1 = tablepath + "/Table" + tablename + "Aggregate_S.tex"
midpath2 = tablepath + "/Table" + tablename + "WdAboveMed_S.tex"
midpath3 = tablepath + "/Table" + tablename + "WdBelowMed_S.tex"


outpath = hdir + "/Analysis/Output/" + tablename + '.tex'
    
filenames = [headerpath, TopPanelASep0, midpath1, PanelABSep1, midpath2, PanelBCSep2, midpath3, footerpath]
with open(outpath , 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                    outfile.write(line)


######Main 2SLS Table_ wd2_winsor05
tablename = "OLSNaivePanels_RYMIntFEs"

tablepath = fragdir + "/Table" + tablename

try:
    os.makedirs(tablepath)
except OSError:
    print("Did not create %s failed, already created" % tablepath)
else:
    print("Successfully created the directotry %s " % tablepath)


###Copied and pasted header/footers from non-winsor table


headerpath = tablepath + "/Table" + tablename + "Header.tex" 
footerpath = tablepath + "/Table" + tablename + "Footer.tex"

TopPanelASep0 = tablepath + "/TopPanelASep.txt"
PanelABSep1 = tablepath + "/PanelABSep.txt"
PanelBCSep2 = tablepath + "/PanelBCSep.txt"


midpath1 = tablepath + "/Table" + tablename + "OLSAllObs.tex"
midpath2 = tablepath + "/Table" + tablename + "OLSNoObsWMissWindSpeed.tex"
midpath3 = tablepath + "/Table" + tablename + "PoissonAllObs.tex"


outpath = hdir + "/Analysis/Output/" + tablename + '.tex'
    
filenames = [headerpath, TopPanelASep0, midpath1, PanelABSep1, midpath2, PanelBCSep2, midpath3, footerpath]
with open(outpath , 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                    outfile.write(line)




######Main 2SLS Table_ wd2_winsor05
tablename = "MainResultsVaryFEs_RYMIntFEs"

tablepath = fragdir + "/Table" + tablename

try:
    os.makedirs(tablepath)
except OSError:
    print("Did not create %s failed, already created" % tablepath)
else:
    print("Successfully created the directotry %s " % tablepath)


###Copied and pasted header/footers from non-winsor table


headerpath2 = tablepath + "/Table" + tablename + "Header.tex" 
footerpath = tablepath + "/Table" + tablename + "Footer.tex"

PanelABSep1 = tablepath + "/PanelABSep.txt"
PanelBCSep2 = tablepath + "/PanelBCSep.txt"
PanelCDSep3 = tablepath + "/PanelCDSep.txt"
PanelDESep4 = tablepath + "/PanelDESep.txt"
TopPanelASep0 = tablepath + "/TopPanelASep.txt"


midpath1 = tablepath + "/Table" + tablename + "SingleIndVar.tex"
midpath2 = tablepath + "/Table" + tablename + "2WayFE.tex"
midpath3 = tablepath + "/Table" + tablename + "RegionSpecificYear.tex"
midpath4 = tablepath + "/Table" + tablename + "RegionYearMonthIntFEs.tex"
midpath5 = tablepath + "/Table" + tablename + "LinearTimeTrend.tex"


outpath = hdir + "/Analysis/Output/Table" + tablename + '.tex'
   
filenames = [headerpath2, TopPanelASep0, midpath1, PanelABSep1, midpath2, PanelBCSep2, midpath3, PanelCDSep3, midpath4, PanelDESep4, midpath5, footerpath]
with open(outpath , 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                    outfile.write(line)



######Main 2SLS Table_ wd2_winsor05
tablename = "MainResultsWithAgCycleVars"

tablepath = fragdir + "/Table" + tablename

try:
    os.makedirs(tablepath)
except OSError:
    print("Did not create %s failed, already created" % tablepath)
else:
    print("Successfully created the directotry %s " % tablepath)


###Copied and pasted header/footers from non-winsor table


headerpath2 = tablepath + "/Table" + tablename + "Header.tex" 
footerpath = tablepath + "/Table" + tablename + "Footer.tex"


PanABSep = tablepath + "/PanelABSep.txt"
PanBCSep = tablepath + "/PanelBCSep.txt"
PanCDSep = tablepath + "/PanelCDSep.txt"
PanDESep = tablepath + "/PanelDESep.txt"
TopPanASep = tablepath + "/TopPanelASep.txt"


midpath1 = tablepath + "/Table" + tablename + "PrecipMean.tex"
midpath2 = tablepath + "/Table" + tablename + "TempMaxMean.tex"
midpath3 = tablepath + "/Table" + tablename + "Both.tex"
midpath4 = tablepath + "/Table" + tablename + "BothNoFEs.tex"
midpath5 = tablepath + "/Table" + tablename + "LinearTimeTrend.tex"


outpath = hdir + "/Analysis/Output/Table" + tablename + '.tex'
   
filenames = [headerpath2, TopPanASep, midpath1, PanABSep, midpath2, PanBCSep, midpath3, PanCDSep, midpath4, footerpath]
with open(outpath , 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                    outfile.write(line)






######Main 2SLS Table_ wd2_winsor05
tablename = "MainResultsWithJustSomalia"

tablepath = fragdir + "/Table" + tablename

try:
    os.makedirs(tablepath)
except OSError:
    print("Did not create %s failed, already created" % tablepath)
else:
    print("Successfully created the directotry %s " % tablepath)


###Copied and pasted header/footers from non-winsor table


headerpath2 = tablepath + "/Table" + tablename + "Header.tex" 
footerpath = tablepath + "/Table" + tablename + "Footer.tex"


PanABSep = tablepath + "/PanelABSep.txt"
PanBCSep = tablepath + "/PanelBCSep.txt"
PanCDSep = tablepath + "/PanelCDSep.txt"
PanDESep = tablepath + "/PanelDESep.txt"
TopPanASep = tablepath + "/TopPanelASep.txt"


midpath1 = tablepath + "/Table" + tablename + "SingleIndVar.tex"
midpath2 = tablepath + "/Table" + tablename + "YearFEs.tex"
midpath3 = tablepath + "/Table" + tablename + "YearFEsQuarterFEs.tex"
midpath4 = tablepath + "/Table" + tablename + "YearQuarterFEs.tex"
midpath5 = tablepath + "/Table" + tablename + "YearFEsMonthFEs.tex"

   
outpath = hdir + "/Analysis/Output/Table" + tablename + '.tex'
   
filenames = [headerpath2, TopPanASep, midpath1, PanABSep, midpath2, PanBCSep, midpath3, PanCDSep, midpath4, PanDESep, midpath5, footerpath]
with open(outpath , 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                    outfile.write(line)







######Main 2SLS Table_ wd2_winsor05
tablename = "MainResultsWithAlternativeMappings"

tablepath = fragdir + "/Table" + tablename

try:
    os.makedirs(tablepath)
except OSError:
    print("Did not create %s failed, already created" % tablepath)
else:
    print("Successfully created the directotry %s " % tablepath)


###Copied and pasted header/footers from non-winsor table


headerpath2 = tablepath + "/Table" + tablename + "Header.tex" 
footerpath = tablepath + "/Table" + tablename + "Footer.tex"


PanABSep = tablepath + "/PanelABSep.txt"
PanBCSep = tablepath + "/PanelBCSep.txt"
PanCDSep = tablepath + "/PanelCDSep.txt"
PanDESep = tablepath + "/PanelDESep.txt"
TopPanASep = tablepath + "/TopPanelASep.txt"


midpath1 = tablepath + "/Table" + tablename + "AltMapping1.tex"
midpath2 = tablepath + "/Table" + tablename + "AltMapping2.tex"
midpath3 = tablepath + "/Table" + tablename + "AltMapping3.tex"

   
outpath = hdir + "/Analysis/Output/Table" + tablename + '.tex'
   
filenames = [headerpath2, TopPanASep, midpath1, PanABSep, midpath2, PanBCSep, midpath3, footerpath]
with open(outpath , 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                    outfile.write(line)



######Main 2SLS Table_ wd2_winsor05
tablename = "MainResultsVaryFEs_FullSpatialDisaggregate"

tablepath = fragdir + "/Table" + tablename

try:
    os.makedirs(tablepath)
except OSError:
    print("Did not create %s failed, already created" % tablepath)
else:
    print("Successfully created the directotry %s " % tablepath)


###Copied and pasted header/footers from non-winsor table


headerpath2 = tablepath + "/Table" + tablename + "Header.tex" 
footerpath = tablepath + "/Table" + tablename + "Footer.tex"


PanABSep = tablepath + "/PanelABSep.txt"
PanBCSep = tablepath + "/PanelBCSep.txt"
PanCDSep = tablepath + "/PanelCDSep.txt"
PanDESep = tablepath + "/PanelDESep.txt"
TopPanASep = tablepath + "/TopPanelASep.txt"


midpath1 = tablepath + "/Table" + tablename + "SingleIndVar.tex"
midpath2 = tablepath + "/Table" + tablename + "RegionYearMonthFEs.tex"
midpath3 = tablepath + "/Table" + tablename + "RegionYearMonthInteractedFEs.tex"

   
outpath = hdir + "/Analysis/Output/Table" + tablename + '.tex'
   
filenames = [headerpath2, TopPanASep, midpath1, PanABSep, midpath2, PanBCSep, midpath3, footerpath]
with open(outpath , 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                    outfile.write(line)



######Main 2SLS Table_ wd2_winsor05
tablename = "MainRYMIntFEsWithLandCovars"

tablepath = fragdir + "/Table" + tablename

try:
    os.makedirs(tablepath)
except OSError:
    print("Did not create %s failed, already created" % tablepath)
else:
    print("Successfully created the directotry %s " % tablepath)


###Copied and pasted header/footers from non-winsor table


headerpath2 = tablepath + "/Table" + tablename + "Header.tex" 
footerpath = tablepath + "/Table" + tablename + "Footer.tex"


PanABSep = tablepath + "/PanelABSep.txt"
PanBCSep = tablepath + "/PanelBCSep.txt"
PanCDSep = tablepath + "/PanelCDSep.txt"
PanDESep = tablepath + "/PanelDESep.txt"
TopPanASep = tablepath + "/TopPanelASep.txt"


midpath1 = tablepath + "/Table" + tablename + "SingleIndVar.tex"
#midpath2 = tablepath + "/Table" + tablename + "UninteractedRegionYearMonth.tex"
#midpath3 = tablepath + "/Table" + tablename + "RegionYearInteractedMonth.tex"
midpath4 = tablepath + "/Table" + tablename + "RegionYearMonthInteracted.tex"
#midpath5 = tablepath + "/Table" + tablename + "RegionYearMonthInteractedCovarsWildCluster.tex"
midpath5 = tablepath + "/Table" + tablename + "RegionYearMonthInteractedCovarsAndChlorWildCluster.tex"
midpath6 = tablepath + "/Table" + tablename + "MonthlyWithAgPriceCovars.tex"

   
outpath = hdir + "/Analysis/Output/Table" + tablename + '.tex'
   
# =============================================================================
# filenames = [headerpath2, TopPanASep, midpath1, PanABSep, midpath2, PanBCSep, midpath3, PanCDSep, midpath4, PanDESep, midpath5, footerpath]
# with open(outpath , 'w') as outfile:
#     for fname in filenames:
#         with open(fname) as infile:
#             for line in infile:
#                     outfile.write(line)
# =============================================================================
                    
                    
filenames = [headerpath2, TopPanASep, midpath1, PanABSep, midpath4, PanBCSep, midpath5, PanCDSep, midpath6, footerpath]
with open(outpath , 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                    outfile.write(line)


######Main 2SLS Table_ wd2_winsor05
tablename = "MonthlyWithNoCovars"

tablepath = fragdir + "/Table" + tablename

try:
    os.makedirs(tablepath)
except OSError:
    print("Did not create %s failed, already created" % tablepath)
else:
    print("Successfully created the directotry %s " % tablepath)


###Copied and pasted header/footers from non-winsor table


headerpath = tablepath + "/Table" + tablename + "Header.tex" 
footerpath = tablepath + "/Table" + tablename + "Footer.tex"


TopPanASep = tablepath + "/TopPanelASep.txt"


midpath1 = tablepath + "/Table" + tablename + "MonthlyWithNoCovars.tex"

   
outpath = hdir + "/Analysis/Output/Table" + tablename + '.tex'

                    
                    
filenames = [headerpath, TopPanASep, midpath1, footerpath]
with open(outpath , 'w') as outfile:3
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                    outfile.write(line)






######Main 2SLS Table_ wd2_winsor05
tablename = "MainResultsVaryFEs"

tablepath = fragdir + "/Table" + tablename

try:
    os.makedirs(tablepath)
except OSError:
    print("Did not create %s failed, already created" % tablepath)
else:
    print("Successfully created the directotry %s " % tablepath)


###Copied and pasted header/footers from non-winsor table


headerpath2 = tablepath + "/Table" + tablename + "Header.tex" 
footerpath = tablepath + "/Table" + tablename + "Footer.tex"

PanelABSep1 = tablepath + "/PanelABSep.txt"

PanelBCSep2 = tablepath + "/PanelBCSep.txt"

PanelCDSep3 = tablepath + "/PanelCDSep.txt"

PanelDESep4 = tablepath + "/PanelDESep.txt"

TopPanelASep0 = tablepath + "/TopPanelASep.txt"


midpath1 = tablepath + "/Table" + tablename + "SingleIndVar.tex"

midpath2 = tablepath + "/Table" + tablename + "2WayFE.tex"

midpath3 = tablepath + "/Table" + tablename + "Wind6Dummy.tex"

midpath4 = tablepath + "/Table" + tablename + "RegionSpecificYear.tex"

midpath5 = tablepath + "/Table" + tablename + "Wind6DummyRegYrInteract.tex"


outpath = hdir + "/Analysis/Output/Table" + tablename + '.tex'
   
filenames = [headerpath2, TopPanelASep0, midpath1, PanelABSep1, midpath2, PanelBCSep2, midpath3, PanelCDSep3, midpath4, PanelDESep4, midpath5, footerpath]
with open(outpath , 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                    outfile.write(line)




######Main 2SLS Table_ wd2_winsor05
tablename = "DefendingExclusion_RYMIntFEs"

tablepath = fragdir + "/Table" + tablename

try:
    os.makedirs(tablepath)
except OSError:
    print("Did not create %s failed, already created" % tablepath)
else:
    print("Successfully created the directotry %s " % tablepath)


###Copied and pasted header/footers from non-winsor table


headerpath = tablepath + "/Table" + tablename + "Header.tex"     
footerpath = tablepath + "/Table" + tablename + "Footer.tex"

PanelABSep1 = tablepath + "/PanelABSep.txt"
PanelBCSep2 = tablepath + "/PanelBCSep.txt"
PanelCDSep3 = tablepath + "/PanelCDSep.txt"
PanelDESep4 = tablepath + "/PanelDESep.txt"
TopPanelASep0 = tablepath + "/TopPanelASep.txt"

#midpath1 = tablepath + "/Table" + tablename + "ChlorophyllLinear.tex"
midpath1 = tablepath + "/Table" + tablename + "NoPiratelessInts.tex"
midpath2 = tablepath + "/Table" + tablename + "SubEventDrop.tex"
midpath3 = tablepath + "/Table" + tablename + "BazookaGunsGrens.tex"
midpath4 = tablepath + "/Table" + tablename + "PeacefulProtests.tex"



# =============================================================================
# outpath = hdir + "/Analysis/Output/Table" + tablename + '.tex'
#    
# filenames = [headerpath, TopPanelASep0, midpath1, PanelABSep1, midpath2, PanelBCSep2, midpath3, PanelCDSep3, midpath4, footerpath]
# with open(outpath , 'w') as outfile:
#     for fname in filenames:
#         with open(fname) as infile:
#             for line in infile:
#                     outfile.write(line)
#                     
# =============================================================================
                    
outpath = hdir + "/Analysis/Output/Table" + tablename + '.tex'
   
filenames = [headerpath, TopPanelASep0, midpath1, PanelABSep1, midpath2, PanelBCSep2, midpath3, PanelCDSep3, midpath4, footerpath]
with open(outpath , 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                    outfile.write(line)


######2SLSRobustness2_wd2
tablename = "OldRobustToAppendix_RYMIntFEs"

tablepath = fragdir + "/Table" + tablename

try:
    os.makedirs(tablepath)
except OSError:
    print("Did not create %s failed, already created" % tablepath)
else:
    print("Successfully created the directotry %s " % tablepath)


#Copied and Pasted the Header/Footers and Panels

headerpath = tablepath + "/Table" + tablename + "Header.tex" 
    
footerpath = tablepath + "/Table" + tablename + "Footer.tex"

PanelABSep1 = tablepath + "/PanelABSep.txt"

PanelBCSep2 = tablepath + "/PanelBCSep.txt"

PanelCDSep3 = tablepath + "/PanelCDSep.txt"

PanelDESep4 = tablepath + "/PanelDESep.txt"

TopPanelASep0 = tablepath + "/TopPanelASep.txt"


#midpath1 = tablepath + "/Table" + tablename + "NonWindsor.tex"

midpath1 = tablepath + "/Table" + tablename + "RemoveACLEDMarineEvents.tex"

midpath2 = tablepath + "/Table" + tablename + "RegionReassign.tex"


outpath = hdir + "/Analysis/Output/Table" + tablename + '.tex'


filenames = [headerpath, TopPanelASep0, midpath1, PanelABSep1, midpath2, footerpath]
with open(outpath , 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                    outfile.write(line)


######2SLSRobustness2_wd2
tablename = "Robustness_NonWinsor_RYFEs"

tablepath = fragdir + "/Table" + tablename

try:
    os.makedirs(tablepath)
except OSError:
    print("Did not create %s failed, already created" % tablepath)
else:
    print("Successfully created the directotry %s " % tablepath)


#Copied and Pasted the Header/Footers and Panels

headerpath = tablepath + "/Table" + tablename + "Header.tex" 
    
footerpath = tablepath + "/Table" + tablename + "Footer.tex"

PanelABSep1 = tablepath + "/PanelABSep.txt"

PanelBCSep2 = tablepath + "/PanelBCSep.txt"

PanelCDSep3 = tablepath + "/PanelCDSep.txt"

PanelDESep4 = tablepath + "/PanelDESep.txt"

TopPanelASep0 = tablepath + "/TopPanelASep.txt"


#midpath1 = tablepath + "/Table" + tablename + "NonWindsor.tex"

midpath1 = tablepath + "/Table" + tablename + "RemoveACLEDMarineEvents.tex"

midpath2 = tablepath + "/Table" + tablename + "RegionReassign.tex"

midpath4 = tablepath + "/Table" + tablename + "ChlorophyllLinear.tex"

#midpath5 = tablepath + "/Table" + tablename + "Chlorophyll_dummy.tex"

midpath3 = tablepath + "/Table" + tablename + "LinearTimeTrend.tex"


outpath = hdir + "/Analysis/Output/Table" + tablename + '.tex'


filenames = [headerpath, TopPanelASep0, midpath1, PanelABSep1, midpath2, PanelBCSep2, midpath3, PanelCDSep3, midpath4, footerpath]
with open(outpath , 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                    outfile.write(line)



######2SLSSpecChecks
tablename = "DiffSpecs_RYMIntFEs"

tablepath = fragdir + "/Table" + tablename

try:
    os.makedirs(tablepath)
except OSError:
    print("Did not create %s failed, already created" % tablepath)
else:
    print("Successfully created the directotry %s " % tablepath)
    

#Copied and Pasted from non-winsor
headerpath = tablepath + "/Table" + tablename + "Header.tex" 
footerpath = tablepath + "/Table" + tablename + "Footer.tex"

PanelABSep1 = tablepath + "/PanelABSep.txt"
PanelBCSep2 = tablepath + "/PanelBCSep.txt"
PanelCDSep3 = tablepath + "/PanelCDSep.txt"
PanelDESep4 = tablepath + "/PanelDESep.txt"
TopPanelASep0 = tablepath + "/TopPanelASep.txt"


midpath1 = tablepath + "/Table" + tablename + "WeekFE.tex"
#midpath2 = tablepath + "/Table" + tablename + "TemporalIntSaturate.tex"
#midpath2 = tablepath + "/Table" + tablename + "Wind6Dummy.tex"
#midpath3 = tablepath + "/Table" + tablename + "WindLess5Dummy.tex"
midpath2 = tablepath + "/Table" + tablename + "WindMeanCollapse.tex"
midpath3 = tablepath + "/Table" + tablename + "LogConflict.tex"
midpath4 = tablepath + "/Table" + tablename + "ASinHConflict.tex"
#midpath52 = tablepath + "/Table" + tablename + "ASinHConflict.tex"
#midpath6 = tablepath + "/Table" + tablename + "WindSpeedSquared.tex"
#midpath7 = tablepath + "/Table" + tablename + "WindDummies.tex"

                    
outpath = hdir + "/Analysis/Output/Table" + tablename + '.tex'
    
    
filenames = [headerpath,  TopPanelASep0, midpath1, PanelABSep1, midpath2, PanelBCSep2, midpath3, PanelCDSep3, midpath4, footerpath]
with open(outpath , 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                    outfile.write(line)
                    



######2SLSSpecChecks
tablename = "SaturateTemporalInt"
#FROM DIFF SPECS DO FILE END

tablepath = fragdir + "/Table" + tablename

try:
    os.makedirs(tablepath)
except OSError:
    print("Did not create %s failed, already created" % tablepath)
else:
    print("Successfully created the directotry %s " % tablepath)
    

#Copied and Pasted from non-winsor
headerpath = tablepath + "/Table" + tablename + "Header.tex" 
footerpath = tablepath + "/Table" + tablename + "Footer.tex"

PanelABSep1 = tablepath + "/PanelABSep.txt"
PanelBCSep2 = tablepath + "/PanelBCSep.txt"
PanelCDSep3 = tablepath + "/PanelCDSep.txt"
PanelDESep4 = tablepath + "/PanelDESep.txt"
TopPanelASep0 = tablepath + "/TopPanelASep.txt"


midpath1 = tablepath + "/Table" + tablename + "MainSample.tex"
midpath2 = tablepath + "/Table" + tablename + "ExtremeDisaggSample.tex"

                    
outpath = hdir + "/Analysis/Output/Table" + tablename + '.tex'
    
    
filenames = [headerpath,  TopPanelASep0, midpath1, PanelABSep1, midpath2, footerpath]
with open(outpath , 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                    outfile.write(line)
                    


                    




######2SLSSpecChecks
tablename = "DiffSpecs_NoWinsor_RYFEs"

tablepath = fragdir + "/Table" + tablename

try:
    os.makedirs(tablepath)
except OSError:
    print("Did not create %s failed, already created" % tablepath)
else:
    print("Successfully created the directotry %s " % tablepath)
    

#Copied and Pasted from non-winsor
headerpath = tablepath + "/Table" + tablename + "Header.tex" 
    
footerpath = tablepath + "/Table" + tablename + "Footer.tex"

PanelABSep1 = tablepath + "/PanelABSep.txt"

PanelBCSep2 = tablepath + "/PanelBCSep.txt"

PanelCDSep3 = tablepath + "/PanelCDSep.txt"

PanelDESep4 = tablepath + "/PanelDESep.txt"

TopPanelASep0 = tablepath + "/TopPanelASep.txt"

WdSquareHd = tablepath + "/MidPanelWdSquare.txt"

WdDummyHd = tablepath + "/TopPanelWdDummy.txt"


midpath1 = tablepath + "/Table" + tablename + "WeekFE_WindLess5Dummy.tex"

midpath2 = tablepath + "/Table" + tablename + "WeekFE.tex"

midpath3 = tablepath + "/Table" + tablename + "WeekFE_Wind6Dummy.tex"

midpath4 = tablepath + "/Table" + tablename + "LogConflict.tex"

midpath5 = tablepath + "/Table" + tablename + "ASinHConflict.tex"

#midpath52 = tablepath + "/Table" + tablename + "ASinHConflict.tex"

#midpath6 = tablepath + "/Table" + tablename + "WindSpeedSquared.tex"

#midpath7 = tablepath + "/Table" + tablename + "WindDummies.tex"



                    
outpath = hdir + "/Analysis/Output/Table" + tablename + '.tex'
    
    
filenames = [headerpath,  TopPanelASep0, midpath1, PanelABSep1, midpath2, PanelBCSep2, midpath3, PanelCDSep3, midpath4, PanelDESep4, midpath5, footerpath]
with open(outpath , 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                    outfile.write(line)
                    


                    
                    
        


                    

######2SLSPirateActivityCapital
tablename = "PirateActivitiesCapital_NonWinsor_RYFEs"

tablepath = fragdir + "/Table" + tablename

try:
    os.makedirs(tablepath)
except OSError:
    print("Did not create %s failed, already created" % tablepath)
else:
    print("Successfully created the directotry %s " % tablepath)
                    
    
  
## Copied Over
headerpath = tablepath + "/Table" + tablename + "Header.tex" 
    
footerpath = tablepath + "/Table" + tablename + "Footer.tex"

PanelABSep1 = tablepath + "/PanelABSep.txt"

PanelBCSep2 = tablepath + "/PanelBCSep.txt"

PanelCDSep3 = tablepath + "/PanelCDSep.txt"

PanelDESep4 = tablepath + "/PanelDESep.txt"

TopPanelASep0 = tablepath + "/TopPanelASep.txt"

#WdSquareHd = tablepath + "/MidPanelWdSquare.txt"

    
#midpath1 = tablepath + "/Table" + tablename + "EventDrop.tex"

midpath1 = tablepath + "/Table" + tablename + "SubEventDrop.tex"

midpath2 = tablepath + "/Table" + tablename + "BazookaGunsGrens.tex"

#midpath4 = tablepath + "/Table" + tablename + "BazookaGunsGrensMthYrInteract.tex"

#midpath5 = tablepath + "/Table" + tablename + "BazookaGunsGrensRYFEs.tex"

midpath3 = tablepath + "/Table" + tablename + "ViolAgCivilians.tex"


#midpath6 = tablepath + "/Table" + tablename + "GunsWinsor05.tex"

#midpath7 = tablepath + "/Table" + tablename + "GunsWindSq.tex"


outpath = hdir + "/Analysis/Output/Table" + tablename + '.tex'
    
filenames = [headerpath, TopPanelASep0, midpath1, PanelABSep1, midpath2, PanelBCSep2, midpath3, footerpath]
with open(outpath , 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                    outfile.write(line)
                    
                    
        



        
######2SLSWhoFights2
tablename = "Who_NonWinsor_RYFEs"

tablepath = fragdir + "/Table" + tablename

try:
    os.makedirs(tablepath)
except OSError:
    print("Did not create %s failed, already created" % tablepath)
else:
    print("Successfully created the directotry %s " % tablepath)
       
    
### Copied Over

headerpath = tablepath + "/Table" + tablename + "Header.tex" 
    
footerpath = tablepath + "/Table" + tablename + "Footer.tex"

PanelABSep1 = tablepath + "/PanelABSep.txt"

PanelBCSep2 = tablepath + "/PanelBCSep.txt"

PanelCDSep3 = tablepath + "/PanelCDSep.txt"

PanelDESep4 = tablepath + "/PanelDESep.txt"

TopPanelASep0 = tablepath + "/TopPanelASep.txt"
    



midpath1 = tablepath + "/Table" + tablename + "NoPiratelessInts.tex"

midpath2 = tablepath + "/Table" + tablename + "1ComMilitia.tex"

midpath3 = tablepath + "/Table" + tablename + "1ComMilitiaWd6.tex"

midpath4 = tablepath + "/Table" + tablename + "2ComMilitiaWd6.tex"


#midpath5 = tablepath + "/Table" + tablename + "1ComMiltGMMWd6.tex"


outpath = hdir + "/Analysis/Output/Table" + tablename + '.tex'
    
filenames = [headerpath, TopPanelASep0, midpath1, PanelABSep1, midpath2, PanelBCSep2, midpath3, PanelCDSep3, midpath4, footerpath]
with open(outpath , 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                    outfile.write(line)



        




######2SLSAuthorityEvents
tablename = "FatalitiesCivilianClanViolence_RYMIntFEs"

tablepath = fragdir + "/Table" + tablename

try:
    os.makedirs(tablepath)
except OSError:
    print("Did not create %s failed, already created" % tablepath)
else:
    print("Successfully created the directotry %s " % tablepath)
    


# Directly copied and pasted
#headerpath = tablepath + "/Table" + tablename + "Header.tex" 

headerpath = tablepath + "/Table" + tablename + "Header.tex"
footerpath = tablepath + "/Table" + tablename + "Footer.tex"

PanelABSep1 = tablepath + "/PanelABSep.txt"
PanelBCSep2 = tablepath + "/PanelBCSep.txt"
PanelCDSep3 = tablepath + "/PanelCDSep.txt"
PanelDESep4 = tablepath + "/PanelDESep.txt"
TopPanelASep0 = tablepath + "/TopPanelASep.txt"

midpath1 = tablepath + "/Table" + tablename + "AllInstitutionRelated.tex"
midpath2 = tablepath + "/Table" + tablename + "Fatalities.tex"
midpath3 = tablepath + "/Table" + tablename + "ViolAgCivilians.tex"
midpath4 = tablepath + "/Table" + tablename + "ViolAgCivilians_Fatalities.tex"




#midpath4 = tablepath + "/Table" + tablename + "1ComMilitiaWd6.tex"

#midpath5 = tablepath + "/Table" + tablename + "2ComMilitiaWd6.tex"


#midpath = tablepath + "/Table" + tablename + "2ComMilitias.tex"


outpath = hdir + "/Analysis/Output/Table" + tablename + '.tex'
    
filenames = [headerpath, TopPanelASep0, midpath1, PanelABSep1, midpath2, PanelBCSep2, midpath3, PanelCDSep3, midpath4, footerpath]
with open(outpath , 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                    outfile.write(line)
                    
                    
                    

######2SLSAuthorityEvents
tablename = "InstitutionFocused_RYMIntFEs"

tablepath = fragdir + "/Table" + tablename

try:
    os.makedirs(tablepath)
except OSError:
    print("Did not create %s failed, already created" % tablepath)
else:
    print("Successfully created the directotry %s " % tablepath)
    


# Directly copied and pasted
#headerpath = tablepath + "/Table" + tablename + "Header.tex" 

headerpath = tablepath + "/Table" + tablename + "Header.tex"

    
footerpath = tablepath + "/Table" + tablename + "Footer.tex"

PanelABSep1 = tablepath + "/PanelABSep.txt"

PanelBCSep2 = tablepath + "/PanelBCSep.txt"

PanelCDSep3 = tablepath + "/PanelCDSep.txt"

PanelDESep4 = tablepath + "/PanelDESep.txt"

TopPanelASep0 = tablepath + "/TopPanelASep.txt"

midpath1 = tablepath + "/Table" + tablename + "1ComMilitia.tex"

midpath2 = tablepath + "/Table" + tablename + "1ComMilitiaWd6.tex"

midpath3 = tablepath + "/Table" + tablename + "2ComMilitia.tex"

midpath4 = tablepath + "/Table" + tablename + "2ComMilitiaWd6.tex"

midpath5 = tablepath + "/Table" + tablename + "AllInstitutionRelated.tex"


#midpath5 = tablepath + "/Table" + tablename + "ViolAgCivilians_Fatalities.tex"




outpath = hdir + "/Analysis/Output/Table" + tablename + '.tex'
    
filenames = [headerpath, TopPanelASep0, midpath1, PanelABSep1, midpath2, PanelBCSep2, midpath3, PanelCDSep3, midpath4, footerpath]
with open(outpath , 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                    outfile.write(line)






######Main 2SLS Table_ wd2_winsor05
tablename = "RedForm_MultPanel_Tanzania"

tablepath = fragdir + "/Table" + tablename

try:
    os.makedirs(tablepath)
except OSError:
    print("Did not create %s failed, already created" % tablepath)
else:
    print("Successfully created the directotry %s " % tablepath)


###Copied and pasted header/footers from non-winsor table


headerpath = tablepath + "/Table" + tablename + "Header.tex" 
    
footerpath = tablepath + "/Table" + tablename + "Footer.tex"

TopPanelASep0 = tablepath + "/TopPanelASep.txt"

PanelABSep1 = tablepath + "/PanelABSep.txt"

PanelBCSep2 = tablepath + "/PanelBCSep.txt"


midpath1 = tablepath + "/Table" + tablename + "OLS_3CountryBorderExtend.tex"

midpath2 = tablepath + "/Table" + tablename + "Poisson_3CountryBorderExtend.tex"

midpath3 = tablepath + "/Table" + tablename + "OLS_CoastalOnly.tex"


outpath = hdir + "/Analysis/Output/Table" + tablename + '.tex'
    
filenames = [headerpath, TopPanelASep0, midpath1, PanelABSep1, midpath2, PanelBCSep2, midpath3, footerpath]
with open(outpath , 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                    outfile.write(line)
                    
                    
                    
######Main 2SLS Table_ wd2_winsor05
tablename = "3PlaceboCountries_ReducedForm"

tablepath = fragdir + "/Table" + tablename

try:
    os.makedirs(tablepath)
except OSError:
    print("Did not create %s failed, already created" % tablepath)
else:
    print("Successfully created the directotry %s " % tablepath)


###Copied and pasted header/footers from non-winsor table


headerpath = tablepath + "/Table" + tablename + "Header.tex" 
footerpath = tablepath + "/Table" + tablename + "Footer.tex"

TopPanelASep0 = tablepath + "/TopPanelASep.txt"
PanABSep = tablepath + "/PanelABSep.txt"
PanBCSep = tablepath + "/PanelBCSep.txt"
PanCDSep = tablepath + "/PanelCDSep.txt"

midpath1 = tablepath + "/Table" + tablename + "Tanzania.tex"
midpath2 = tablepath + "/Table" + tablename + "Libya.tex"
midpath3 = tablepath + "/Table" + tablename + "SAfrica.tex"
midpath4 = tablepath + "/Table" + tablename + "All3Countries.tex"


outpath = hdir + "/Analysis/Output/Table" + tablename + '.tex'
    
filenames = [headerpath, TopPanelASep0, midpath1, PanABSep, midpath2, PanBCSep, midpath3, PanCDSep, midpath4, footerpath]
with open(outpath , 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                    outfile.write(line)



######
tablename = "Plausexog"

tablepath = fragdir + "/Table" + tablename

try:
    os.makedirs(tablepath)
except OSError:
    print("Did not create %s failed, already created" % tablepath)
else:
    print("Successfully created the directotry %s " % tablepath)

#Need to strip out begin center, end center and begin tabular lines

filenames = ("NoUncertainty","UncertainPriors")

for file in filenames:
    sfile = str(file)
    print(sfile)
    
    filein = tablepath + "/Table" + tablename + sfile + ".tex"
    print(filein)    
    
    reading_file = open(filein, "r")
    
    new_file_content = ""
    
    for line in reading_file:
        stripped_line = line.strip()
        new_line = stripped_line.replace("begin", "")
      
        new_file_content += new_line +"\n"
        #reading_file.close()    

    fileout = tablepath + "/Table" + tablename + sfile + "Modded.tex"
    print(fileout)
    
    writing_file = open(fileout, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
    ########
    
    reading_file = open(fileout, "r")
    
    new_file_content = ""
    
    for line in reading_file:
        stripped_line = line.strip()
        new_line = stripped_line.replace("end", "")
      
        new_file_content += new_line +"\n"
        #reading_file.close()    

    fileout = tablepath + "/Table" + tablename + sfile + "Modded.tex"
    print(fileout)
    
    writing_file = open(fileout, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
    ########

    reading_file = open(fileout, "r")
    
    new_file_content = ""
    
    for line in reading_file:
        stripped_line = line.strip()
        new_line = stripped_line.replace("\{center}", "")
      
        new_file_content += new_line +"\n"
        #reading_file.close()    

    fileout = tablepath + "/Table" + tablename + sfile + "Modded.tex"
    print(fileout)
    
    writing_file = open(fileout, "w")
    writing_file.write(new_file_content)
    writing_file.close()


    ########

    reading_file = open(fileout, "r")
    
    new_file_content = ""
    
    for line in reading_file:
        stripped_line = line.strip()
        new_line = stripped_line.replace("\{tabular}", "")
      
        new_file_content += new_line +"\n"
        #reading_file.close()    

    fileout = tablepath + "/Table" + tablename + sfile + "Modded.tex"
    print(fileout)
    
    writing_file = open(fileout, "w")
    writing_file.write(new_file_content)
    writing_file.close()


    ########

    reading_file = open(fileout, "r")
    
    new_file_content = ""
    
    for line in reading_file:
        stripped_line = line.strip()
        new_line = stripped_line.replace("{lccc}", "")
      
        new_file_content += new_line +"\n"
        #reading_file.close()    

    fileout = tablepath + "/Table" + tablename + sfile + "Modded.tex"
    print(fileout)
    
    writing_file = open(fileout, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    

    ########

    reading_file = open(fileout, "r")
    
    new_file_content = ""
    
    for line in reading_file:
        stripped_line = line.strip()
        new_line = stripped_line.replace("{\smallskip}", "")
      
        new_file_content += new_line +"\n"
        #reading_file.close()    

    fileout = tablepath + "/Table" + tablename + sfile + "Modded.tex"
    print(fileout)
    
    writing_file = open(fileout, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
    

    ########

    reading_file = open(fileout, "r")
    
    new_file_content = ""
    
    for line in reading_file:
        stripped_line = line.strip()
        new_line = stripped_line.replace("\\noalign\\\\", "")
      
        new_file_content += new_line +"\n"
        #reading_file.close()    

    fileout = tablepath + "/Table" + tablename + sfile + "Modded.tex"
    print(fileout)
    
    writing_file = open(fileout, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
    

    ########

    reading_file = open(fileout, "r")
    
    new_file_content = ""
    
    for line in reading_file:
        stripped_line = line.strip()
        new_line = stripped_line.replace("\\noalign", "")
      
        new_file_content += new_line +"\n"
        #reading_file.close()    

    fileout = tablepath + "/Table" + tablename + sfile + "Modded.tex"
    print(fileout)
    
    writing_file = open(fileout, "w")
    writing_file.write(new_file_content)
    writing_file.close()


# =============================================================================
#     #input file
#     fin = open(filein, "rt")
#     #output file to write the result to
#     fout = open(fileout, "wt")
#     
#     for line in fin:
# 	#read replace the string and write to output file
#     	fout.write(line.replace('\begin{center}',''))
#     
#     
#     fin.close()
#     fout.close()
# 
# 
#     with open (filein, 'r+' ) as f:
#         text = f.read()
#         text2 = re.sub("\"," ", text)
#         
#         
#     print(text)
#     print(text2)
 
#     with open(filein) as f:
#         text=f.read()
#         
#     newText = text.re.sub('\begin{tabular}{lccc}',' ')
#     
#     print(text)
#     print(newText)
#     
#     fileout = tablepath + "/Table" + tablename + sfile + "Modded.tex"
#     
#     with open(fileout, "w") as f:
#         f.write(newText)
#
#
#     f = open(filein,'r')
#     filedata = f.read()
#     f.close()
#     
#     
#     newdata = filedata.replace('\begin{center}','',1)
#     
#     
#     fileout = tablepath + "/Table" + tablename + sfile + "Modded.tex"
#     f = open(fileout,'w')
#     f.write(newdata)
#     f.close()
# =============================================================================


###Copied and pasted header/footers from non-winsor table
headerpath = tablepath + "/Table" + tablename + "Header.tex" 
footerpath = tablepath + "/Table" + tablename + "Footer.tex"

TopPanelASep0 = tablepath + "/TopPanelASep.txt"
PanABSep = tablepath + "/PanelABSep.txt"
PanBCSep = tablepath + "/PanelBCSep.txt"
PanCDSep = tablepath + "/PanelCDSep.txt"

midpath1 = tablepath + "/Table" + tablename + "NoUncertaintyModded.tex"
midpath2 = tablepath + "/Table" + tablename + "UncertainPriorsModded.tex"
#midpath3 = tablepath + "/Table" + tablename + "SAfrica.tex"
#midpath4 = tablepath + "/Table" + tablename + "All3Countries.tex"


outpath = hdir + "/Analysis/Output/Table" + tablename + '.tex'
    
filenames = [headerpath, TopPanelASep0, midpath1, PanABSep, midpath2, footerpath]
with open(outpath , 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                    outfile.write(line)



# =============================================================================
# outpath = hdir + "/Analysis/Output/Table" + tablename + '2.tex'
#     
# filenames = [headerpath, TopPanelASep0, midpath1, PanABSep, midpath2, footerpath]
# with open(outpath , 'w') as outfile:
#     for fname in filenames:
#         with open(fname) as infile:
#             for line in infile:
#                     outfile.write(line)
# =============================================================================




######
tablename = "PlausexogParametersForZero"

tablepath = fragdir + "/Table" + tablename

try:
    os.makedirs(tablepath)
except OSError:
    print("Did not create %s failed, already created" % tablepath)
else:
    print("Successfully created the directotry %s " % tablepath)

#Need to strip out begin center, end center and begin tabular lines

filenames = ("MuVary","OmegaVary")

for file in filenames:
    sfile = str(file)
    print(sfile)
    
    filein = tablepath + "/Table" + tablename + sfile + ".tex"
    print(filein)    
    
    reading_file = open(filein, "r")
    
    new_file_content = ""
    
    for line in reading_file:
        stripped_line = line.strip()
        new_line = stripped_line.replace("begin", "")
      
        new_file_content += new_line +"\n"
        #reading_file.close()    

    fileout = tablepath + "/Table" + tablename + sfile + "Modded.tex"
    print(fileout)
    
    writing_file = open(fileout, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
    ########
    
    reading_file = open(fileout, "r")
    
    new_file_content = ""
    
    for line in reading_file:
        stripped_line = line.strip()
        new_line = stripped_line.replace("end", "")
      
        new_file_content += new_line +"\n"
        #reading_file.close()    

    fileout = tablepath + "/Table" + tablename + sfile + "Modded.tex"
    print(fileout)
    
    writing_file = open(fileout, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
    ########

    reading_file = open(fileout, "r")
    
    new_file_content = ""
    
    for line in reading_file:
        stripped_line = line.strip()
        new_line = stripped_line.replace("\{center}", "")
      
        new_file_content += new_line +"\n"
        #reading_file.close()    

    fileout = tablepath + "/Table" + tablename + sfile + "Modded.tex"
    print(fileout)
    
    writing_file = open(fileout, "w")
    writing_file.write(new_file_content)
    writing_file.close()


    ########

    reading_file = open(fileout, "r")
    
    new_file_content = ""
    
    for line in reading_file:
        stripped_line = line.strip()
        new_line = stripped_line.replace("\{tabular}", "")
      
        new_file_content += new_line +"\n"
        #reading_file.close()    

    fileout = tablepath + "/Table" + tablename + sfile + "Modded.tex"
    print(fileout)
    
    writing_file = open(fileout, "w")
    writing_file.write(new_file_content)
    writing_file.close()


    ########

    reading_file = open(fileout, "r")
    
    new_file_content = ""
    
    for line in reading_file:
        stripped_line = line.strip()
        new_line = stripped_line.replace("{lccc}", "")
      
        new_file_content += new_line +"\n"
        #reading_file.close()    

    fileout = tablepath + "/Table" + tablename + sfile + "Modded.tex"
    print(fileout)
    
    writing_file = open(fileout, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    

    ########

    reading_file = open(fileout, "r")
    
    new_file_content = ""
    
    for line in reading_file:
        stripped_line = line.strip()
        new_line = stripped_line.replace("{\smallskip}", "")
      
        new_file_content += new_line +"\n"
        #reading_file.close()    

    fileout = tablepath + "/Table" + tablename + sfile + "Modded.tex"
    print(fileout)
    
    writing_file = open(fileout, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
    

    ########

    reading_file = open(fileout, "r")
    
    new_file_content = ""
    
    for line in reading_file:
        stripped_line = line.strip()
        new_line = stripped_line.replace("\\noalign\\\\", "")
      
        new_file_content += new_line +"\n"
        #reading_file.close()    

    fileout = tablepath + "/Table" + tablename + sfile + "Modded.tex"
    print(fileout)
    
    writing_file = open(fileout, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
    

    ########

    reading_file = open(fileout, "r")
    
    new_file_content = ""
    
    for line in reading_file:
        stripped_line = line.strip()
        new_line = stripped_line.replace("\\noalign", "")
      
        new_file_content += new_line +"\n"
        #reading_file.close()    

    fileout = tablepath + "/Table" + tablename + sfile + "Modded.tex"
    print(fileout)
    
    writing_file = open(fileout, "w")
    writing_file.write(new_file_content)
    writing_file.close()


# =============================================================================
#     #input file
#     fin = open(filein, "rt")
#     #output file to write the result to
#     fout = open(fileout, "wt")
#     
#     for line in fin:
# 	#read replace the string and write to output file
#     	fout.write(line.replace('\begin{center}',''))
#     
#     
#     fin.close()
#     fout.close()
# 
# 
#     with open (filein, 'r+' ) as f:
#         text = f.read()
#         text2 = re.sub("\"," ", text)
#         
#         
#     print(text)
#     print(text2)
 
#     with open(filein) as f:
#         text=f.read()
#         
#     newText = text.re.sub('\begin{tabular}{lccc}',' ')
#     
#     print(text)
#     print(newText)
#     
#     fileout = tablepath + "/Table" + tablename + sfile + "Modded.tex"
#     
#     with open(fileout, "w") as f:
#         f.write(newText)
#
#
#     f = open(filein,'r')
#     filedata = f.read()
#     f.close()
#     
#     
#     newdata = filedata.replace('\begin{center}','',1)
#     
#     
#     fileout = tablepath + "/Table" + tablename + sfile + "Modded.tex"
#     f = open(fileout,'w')
#     f.write(newdata)
#     f.close()
# =============================================================================


###Copied and pasted header/footers from non-winsor table
headerpath = tablepath + "/Table" + tablename + "Header.tex" 
footerpath = tablepath + "/Table" + tablename + "Footer.tex"

TopPanelASep0 = tablepath + "/TopPanelASep.txt"
PanABSep = tablepath + "/PanelABSep.txt"
PanBCSep = tablepath + "/PanelBCSep.txt"
PanCDSep = tablepath + "/PanelCDSep.txt"

midpath1 = tablepath + "/Table" + tablename + "MuVaryModded.tex"
midpath2 = tablepath + "/Table" + tablename + "OmegaVaryModded.tex"
#midpath3 = tablepath + "/Table" + tablename + "SAfrica.tex"
#midpath4 = tablepath + "/Table" + tablename + "All3Countries.tex"


outpath = hdir + "/Analysis/Output/Table" + tablename + '.tex'
    
filenames = [headerpath, TopPanelASep0, midpath1, PanABSep, midpath2, footerpath]
with open(outpath , 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                    outfile.write(line)



# =============================================================================
# outpath = hdir + "/Analysis/Output/Table" + tablename + '2.tex'
#     
# filenames = [headerpath, TopPanelASep0, midpath1, PanABSep, midpath2, footerpath]
# with open(outpath , 'w') as outfile:
#     for fname in filenames:
#         with open(fname) as infile:
#             for line in infile:
#                     outfile.write(line)
# =============================================================================









######Main 2SLS Table_ wd2_winsor05
tablename = "CovariateBalance"

tablepath = fragdir + "/Table" + tablename

try:
    os.makedirs(tablepath)
except OSError:
    print("Did not create %s failed, already created" % tablepath)
else:
    print("Successfully created the directotry %s " % tablepath)


###Copied and pasted header/footers from non-winsor table


headerpath = tablepath + "/Table" + tablename + "Header.tex" 
footerpath = tablepath + "/Table" + tablename + "Footer.tex"

TopPanelASep0 = tablepath + "/TopPanelASep.txt"
PanelABSep1 = tablepath + "/PanelABSep.txt"
PanelBCSep2 = tablepath + "/PanelBCSep.txt"


midpath1 = tablepath + "/Table" + tablename + "Chlorophyll.tex"
midpath2 = tablepath + "/Table" + tablename + "Temperature.tex"
midpath3 = tablepath + "/Table" + tablename + "Precipitation.tex"


outpath = hdir + "/Analysis/Output/Table" + tablename + '.tex'
    
filenames = [headerpath, TopPanelASep0, midpath1, PanelABSep1, midpath2, PanelBCSep2, midpath3, footerpath]
with open(outpath , 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                    outfile.write(line)





































######2SLSAuthorityEvents
tablename = "FatalitiesEconomyEvents_NonWinsor_RYFEs"

tablepath = fragdir + "/Table" + tablename

try:
    os.makedirs(tablepath)
except OSError:
    print("Did not create %s failed, already created" % tablepath)
else:
    print("Successfully created the directotry %s " % tablepath)
    


# Directly copied and pasted
#headerpath = tablepath + "/Table" + tablename + "Header.tex" 

headerpath = tablepath + "/Table" + tablename + "Header.tex"

    
footerpath = tablepath + "/Table" + tablename + "Footer.tex"

PanelABSep1 = tablepath + "/PanelABSep.txt"

PanelBCSep2 = tablepath + "/PanelBCSep.txt"

PanelCDSep3 = tablepath + "/PanelCDSep.txt"

PanelDESep4 = tablepath + "/PanelDESep.txt"

TopPanelASep0 = tablepath + "/TopPanelASep.txt"

midpath1 = tablepath + "/Table" + tablename + "Fatalities.tex"

midpath2 = tablepath + "/Table" + tablename + "FatalitiesWd6.tex"

midpath3 = tablepath + "/Table" + tablename + "BadInstSubEventWdMean.tex"

midpath4 = tablepath + "/Table" + tablename + "BadInstSubEventWd6.tex"



#midpath = tablepath + "/Table" + tablename + "2ComMilitias.tex"


outpath = hdir + "/Analysis/Output/Table" + tablename + '.tex'
    
filenames = [headerpath, TopPanelASep0, midpath1, PanelABSep1, midpath2, footerpath]
with open(outpath , 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                    outfile.write(line)
    
                    
                    
                    

######2SLSAuthorityEvents
tablename = "2SLSInstitutionsSubEvents_SingleWdDummy"

tablepath = fragdir + "/Table" + tablename

try:
    os.makedirs(tablepath)
except OSError:
    print("Did not create %s failed, already created" % tablepath)
else:
    print("Successfully created the directotry %s " % tablepath)
    

headerpath = tablepath + "/Table" + tablename + "Header.tex"

    
footerpath = tablepath + "/Table" + tablename + "Footer.tex"

PanelABSep1 = tablepath + "/PanelABSep.txt"

PanelBCSep2 = tablepath + "/PanelBCSep.txt"

PanelCDSep3 = tablepath + "/PanelCDSep.txt"

PanelDESep4 = tablepath + "/PanelDESep.txt"

TopPanelASep0 = tablepath + "/TopPanelASep.txt"
    

midpath1 = tablepath + "/Table" + tablename + "AboveMean.tex"

midpath2 = tablepath + "/Table" + tablename + "AboveMedian.tex"

midpath3 = tablepath + "/Table" + tablename + "Above6.tex"


outpath = hdir + "/Analysis/Output/Table" + tablename + '.tex'
    
filenames = [headerpath, TopPanelASep0, midpath2, PanelABSep1, midpath1, PanelBCSep2, midpath3, footerpath]
with open(outpath , 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                    outfile.write(line)
                    
                    
                    


######2SLSRobustness
tablename = "WindByMonth"

tablepath = fragdir + "/Table" + tablename

try:
    os.makedirs(tablepath)
except OSError:
    print("Did not create %s failed, already created" % tablepath)
else:
    print("Successfully created the directotry %s " % tablepath)
    

#headerpath = tablepath + "/Table" + tablename + "Header.tex" 

headerpath = tablepath + "/Table" + tablename + "Header.tex" 

    
footerpath = tablepath + "/Table" + tablename + "Footer.tex"

PanelABSep1 = tablepath + "/PanelsABSep.txt"

PanelBCSep2 = tablepath + "/PanelsBCSep.txt"

PanelCDSep3 = tablepath + "/PanelsCDSep.txt"

PanelDESep = tablepath + "/PanelsDESep.txt"

PanelEFSep = tablepath + "/PanelsEFSep.txt"

PanelFGSep = tablepath + "/PanelsFGSep.txt"

PanelGHSep = tablepath + "/PanelsGHSep.txt"

PanelHISep = tablepath + "/PanelsHISep.txt"

PanelIJSep = tablepath + "/PanelsIJSep.txt"

PanelJKSep = tablepath + "/PanelsJKSep.txt"

PanelKLSep = tablepath + "/PanelsKLSep.txt"

TopPanelASep0 = tablepath + "/TopPanelASep.txt"



midpath1 = tablepath + "/Table" + tablename + "Month1.tex"

midpath2 = tablepath + "/Table" + tablename + "Month2.tex"

midpath3 = tablepath + "/Table" + tablename + "Month3.tex"

midpath4 = tablepath + "/Table" + tablename + "Month4.tex"

midpath5 = tablepath + "/Table" + tablename + "Month5.tex"

midpath6 = tablepath + "/Table" + tablename + "Month6.tex"

midpath7 = tablepath + "/Table" + tablename + "Month7.tex"

midpath8 = tablepath + "/Table" + tablename + "Month8.tex"

midpath9 = tablepath + "/Table" + tablename + "Month9.tex"

midpath10 = tablepath + "/Table" + tablename + "Month10.tex"

midpath11 = tablepath + "/Table" + tablename + "Month11.tex"

midpath12 = tablepath + "/Table" + tablename + "Month12.tex"





outpath = hdir + "/Analysis/Output/Table" + tablename + '.tex'
    
filenames = [headerpath, TopPanelASep0, midpath1, PanelABSep1, midpath2, PanelBCSep2, midpath3, PanelCDSep3, midpath4, PanelDESep,midpath5 ,PanelEFSep,midpath6 ,PanelFGSep,midpath7 , PanelGHSep,midpath8 ,PanelHISep, midpath9,PanelIJSep, midpath10 , PanelJKSep,midpath11 , PanelKLSep,midpath12,  footerpath]
with open(outpath , 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                    outfile.write(line)





######2SLSRobustness
tablename = "WindByMonth_wd3"

tablepath = fragdir + "/Table" + tablename

try:
    os.makedirs(tablepath)
except OSError:
    print("Did not create %s failed, already created" % tablepath)
else:
    print("Successfully created the directotry %s " % tablepath)
    

#headerpath = tablepath + "/Table" + tablename + "Header.tex" 

headerpath = tablepath + "/Table" + tablename + "Header.tex" 

    
footerpath = tablepath + "/Table" + tablename + "Footer.tex"

PanelABSep1 = tablepath + "/PanelsABSep.txt"

PanelBCSep2 = tablepath + "/PanelsBCSep.txt"

PanelCDSep3 = tablepath + "/PanelsCDSep.txt"

PanelDESep = tablepath + "/PanelsDESep.txt"

PanelEFSep = tablepath + "/PanelsEFSep.txt"

PanelFGSep = tablepath + "/PanelsFGSep.txt"

PanelGHSep = tablepath + "/PanelsGHSep.txt"

PanelHISep = tablepath + "/PanelsHISep.txt"

PanelIJSep = tablepath + "/PanelsIJSep.txt"

PanelJKSep = tablepath + "/PanelsJKSep.txt"

PanelKLSep = tablepath + "/PanelsKLSep.txt"

TopPanelASep0 = tablepath + "/TopPanelASep.txt"



midpath1 = tablepath + "/Table" + tablename + "Month1.tex"

midpath2 = tablepath + "/Table" + tablename + "Month2.tex"

midpath3 = tablepath + "/Table" + tablename + "Month3.tex"

midpath4 = tablepath + "/Table" + tablename + "Month4.tex"

midpath5 = tablepath + "/Table" + tablename + "Month5.tex"

midpath6 = tablepath + "/Table" + tablename + "Month6.tex"

midpath7 = tablepath + "/Table" + tablename + "Month7.tex"

midpath8 = tablepath + "/Table" + tablename + "Month8.tex"

midpath9 = tablepath + "/Table" + tablename + "Month9.tex"

midpath10 = tablepath + "/Table" + tablename + "Month10.tex"

midpath11 = tablepath + "/Table" + tablename + "Month11.tex"

midpath12 = tablepath + "/Table" + tablename + "Month12.tex"





outpath = hdir + "/Analysis/Output/Table" + tablename + '.tex'
    
filenames = [headerpath, TopPanelASep0, midpath1, PanelABSep1, midpath2, PanelBCSep2, midpath3, PanelCDSep3, midpath4, PanelDESep,midpath5 ,PanelEFSep,midpath6 ,PanelFGSep,midpath7 , PanelGHSep,midpath8 ,PanelHISep, midpath9,PanelIJSep, midpath10 , PanelJKSep,midpath11 , PanelKLSep,midpath12,  footerpath]
with open(outpath , 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                    outfile.write(line)
                    
                    
                    
######Main 2SLS Table
tablename = "OLSNaivePanels"

tablepath = fragdir + "/Table" + tablename

try:
    os.makedirs(tablepath)
except OSError:
    print("Did not create %s failed, already created" % tablepath)
else:
    print("Successfully created the directotry %s " % tablepath)
    

headerpath = tablepath + "/Table" + tablename + "Header.tex" 
    
footerpath = tablepath + "/Table" + tablename + "Footer.tex"

PanelABSep1 = tablepath + "/PanelABSep.txt"

PanelBCSep2 = tablepath + "/PanelBCSep.txt"

TopPanelASep0 = tablepath + "/TopPanelASep.txt"


midpath1 = tablepath + "/Table" + tablename + "OLSAllObs.tex"

midpath2 = tablepath + "/Table" + tablename + "OLSNoObsWMissWindSpeed.tex"

midpath3 = tablepath + "/Table" + tablename + "PoissonAllObs.tex"


outpath = hdir + "/Analysis/Output/Table" + tablename + '.tex'
    
filenames = [headerpath, TopPanelASep0, midpath1, PanelABSep1, midpath2, PanelBCSep2, midpath3, footerpath]
with open(outpath , 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                    outfile.write(line)

                    
