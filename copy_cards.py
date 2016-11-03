#!/usr/bin/env python
# RUN: python copy_cards.py --channel bWbj_T
import os, sys, time,math
import subprocess
from random import randint
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

fprocess = open('../../submit_'+str(channel)+'.sh', 'w')
fprocess.write('#!/bin/bash \n')

fsetup = open('../../setup_'+str(channel)+'.sh', 'w')
fsetup.write('#!/bin/bash \n')
fsetup.write('mkdir '+channel+'\n')


frun = open('../../run_'+str(channel)+'.sh', 'w')
frun.write('#!/bin/bash \n')

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
    filedecaybase =  folderbase+folderbaseMW+slash+folderbaseMW+decay
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
    ####################################################################################
    # make scripts to run
    ###################################################################################
    fprocess.write('./gridpack_generation.sh '+channel+toMass+str(mass[m])+toWidth+str(width[w])+"p cards/singleVLQ_wide/"+\
                    channel+slash+channel+toMass+str(mass[m])+toWidth+str(width[w])+'p 1nh & \n')
    dirrun=channel+slash+channel+toMass+str(mass[m])+toWidth+str(width[w])+'p'
    fsetup.write('mkdir '+dirrun+" \n"+\
                 'mv '+channel+toMass+str(mass[m])+toWidth+str(width[w])+'p_tarball.tar.xz ' +dirrun+" \n"+\
                 'cd '+dirrun+"\n"+\
                 'tar xvfJ '+channel+toMass+str(mass[m])+toWidth+str(width[w])+'p_tarball.tar.xz &\n'+\
                 'cd - \n')

    frun.write('cp cards/singleVLQ_wide/runcmsgrid_PDF4LHC.sh '+dirrun+'\n'+\
               'cd '+dirrun+"\n"+\
               './runcmsgrid.sh 30000 '+str(randint(0,10000)) +' 10 > output_'+channel+toMass+str(mass[m])+toWidth+str(width[w])+'p &\n'+\
               'cd - \n')
    
fprocess.close()

