# ClassProject-Bioinformatics-ColorScript
Given a protein and a connection map, the script will color amino acids that are indicated as matching by the contact map

To use, First open Chimera.

Open the protein that you would like to see the contacts.
Download the contact map and delete everything in the file except the contacts.
Replace all spaces with commas in the contact map file.

To run in Chimera:
there are 4 parameters, the location of the script, the location of the contact map, whether the script should recolor 
residues (0 for no 1 for yes), the lowest confidence interval the script should use.

EX: run C:\Users\dhaslam\Desktop\contactColorer.py "C:/Users/dhaslam/Downloads/274635.all_in_one/274635.all_in_one/274635.contactmap.txt" 0 .8
