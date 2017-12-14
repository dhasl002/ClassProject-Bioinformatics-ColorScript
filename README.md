# ClassProject-Bioinformatics-ColorScript

It is difficult to determine how a 2D amino acid sequence threads through the 3D cryo-EM image without a template. Many different applications have been created to improve this process. Recently a software tool known as [RaptorX](http://raptorx.uchicago.edu/) has been created to understand local contacts on an amino acid sequence. In order to explore how this information can be utilized, I wanted to color code amion acids in the 3D image. This program uses the contact predictions and displays the results in on a 3D image of the protein. 

##To use

First open Chimera

Open the protein that you would like to see the contacts.
Download the contact map and delete everything in the file except the contacts.
Replace all spaces with commas in the contact map file.

###To run in Chimera

there are 4 parameters, the location of the script, the location of the contact map, whether the script should recolor 
residues (0 for no 1 for yes), the lowest confidence interval the script should use.

EX: run C:\Users\dhaslam\Desktop\contactColorer.py "C:/Users/dhaslam/Downloads/274635.all_in_one/274635.all_in_one/274635.contactmap.txt" 0 .8
