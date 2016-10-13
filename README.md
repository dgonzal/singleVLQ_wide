# singleVLQ_wide

Fork and clone https://github.com/cms-sw/genproductions

Load this scripts inside the following folder

cd  $LOCAL/genproductions/bin/MadGraph5_aMCatNLO/cards
git clone https://github.com/acarvalh/singleVLQ_wide

========================================================================================================

The file 'copy_cards.py' copy the four cards of the template 'channel'_M800GeV_W10p in the other mass and width hiphoteses encoded

To run you do: 

python copy_cards.py 'channel' 

Where for example  'channel' = bWbj_Y ==> note that the intermediary particle is already chosen with this name

** You SHOULD have the template cards 'channel'_M800GeV_W10p 
The chirality is chosen in the customize_cards (the name convention should be clear)

Before use please quadruple check:

 - The couplings that are on/of in the customize card. 
   This is a version of the param_card.dat, buth only with the relevant parameters to be changed
   All the other parameters are taken as the default of the model 

 - The sintax in the the proc card

=========================================================================================================

Three scripts will be created in $LOCAL/genproductions/bin/MadGraph5_aMCatNLO/

./submit_bWbj_T.sh ==> submits the Gridpacks
./setup_bWbj_T.sh ==> setupt folders to run the events

(do cmsenv)

./run_bWbj_T.sh ==> run the events (the nevents is encoded) 
