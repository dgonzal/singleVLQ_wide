# singleVLQ_wide

The file 'copy_cards.py' copy the four cards of the template 'channel'_M800GeV_W10p in the other mass and width hiphoteses
To run you do: 

python copy_cards.py 'channel' 

Where for example  'channel' = bWbj_YL
  ==> note that the intermediary particle and chirality are already chosen with this name

** You SHOULD have the template cards 'channel'_M800GeV_W10p 

On those please quadruple check:

 - The couplings that are on/of in the customize card. 
   This is a version of the param_card.dat, buth only with the relevant parameters to be changed
   All the other parameters are taken as the default of the model 

 - The sintax in the the proc card

=========================================================================================================

rules about the cards: 

 - In the proc_cards the name of the output folder should match the beggining of the name of the file
 
 - The " QCD=1 QED=1 VLQ<=2 " means that I only want processes that have exactly 2 VLQ couplings inside
   + one QCD coupling to make the additional jet

 - The " / x y bp" means that I do NOT want the VLQ in the middle to be one of these

