#!/usr/bin/env python
# RUN: python python copy_cards.py --channel bWbj_YL
import os, sys, time,math
import subprocess
from optparse import OptionParser
parser = OptionParser()

parser.add_option("--channel", type="str", dest="chan", help="channel: it should contain particle and chirality")
(options, args) = parser.parse_args()
channel = options.chan
#channel="bWbj_YL"

mass=(800 , 1000 , 1400)
width=(10 , 20 , 30) 

base="_M800GeV_W10p"
slash="/"
toMass="_M"
toWidth="GeV_W"
pp="p"

cust="_customizecards.dat"
proc="_proc_card.dat"
EM="_extramodels.dat"     
run="_run_card.dat"
run="_run_card.dat"
decay="_madspin_card.dat"

for m in range(0,len(mass)):
  for w in range(0,len(width)):
    print str(mass[m])+"  "+str(width[w])+"  "+str(float(mass[m]*width[w]/100))
    #
    folderbase= channel+slash
    folderbaseMW=channel+base
    print folderbaseMW
    filecustbase =  folderbase+folderbaseMW+slash+folderbaseMW+cust
    fileprocbase =  folderbase+folderbaseMW+slash+folderbaseMW+proc
    fileEMbase =  folderbase+folderbaseMW+slash+folderbaseMW+EM
    filerunbase =  folderbase+folderbaseMW+slash+folderbaseMW+run
    filerdecaybase =  folderbase+folderbaseMW+slash+folderbaseMW+decay
    #
    folder= channel+slash
    folderMW=channel+toMass+str(mass[m])+toWidth+str(width[w])+"p"
    procMW=folderMW+proc
    filecust =  folder+folderMW+slash+folderMW+cust
    fileproc =  folder+folderMW+slash+folderMW+proc
    fileEM =  folder+folderMW+slash+folderMW+EM
    filerun =  folder+folderMW+slash+folderMW+run
    filedecay =  folder+folderMW+slash+folderMW+decay
    #
    process = subprocess.Popen(["mkdir "+folder+folderMW],shell=True,stdout=subprocess.PIPE)
    out = process.stdout.read()
    process = subprocess.Popen(["cp "+fileprocbase+" "+fileproc+"; "+\
                                "cp "+filecustbase+" "+filecust+"; "+\
                                "cp "+fileEMbase+" "+fileEM+"; "+\
                                "cp "+filedecaybase+" "+filedecay+"; "+\
                                "cp "+filerunbase+" "+filerun+"; "\
                               ],shell=True,stdout=subprocess.PIPE)
    out = process.stdout.read()
    # 
    print fileproc
    with open(fileproc, 'r+') as f:
       content = f.read()
       f.seek(0)
       f.truncate()
       f.write(content.replace(folderbaseMW, folderMW))
    print filecust
    
    with open(filecust, 'r+') as fp:
       content = fp.read()
       fp.seek(0)
       fp.truncate()
       fp.write(content.replace('800.0', str(mass[m])+".0"))
    fp.close()
    with open(filecust, 'r+') as fp:
       content = fp.read()
       fp.seek(0)
       fp.truncate()
       fp.write(content.replace('80.0', str(float(mass[m]*width[w]/100))))


