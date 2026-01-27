# ezFCF_overlap_new_order
In ezFCF 1.3 (2026, Jan), after generating *.txt file, the overlap matrix for vibration mode between two states may flipped. Using this code to get the "new_order". Haven't been widely tested, but at least work on the manual one (phenolate photoelectron spec.)


run python new_order.py *.txt, then u get new order, follow Dr. Krylov's manual (http://q-chem.com/Teaching%20Materials/QChemCompLabs/ezFCF_lab-Gozem.pdf) and paste/modify whatever u have to do.


For dicussion/code modification, d05223110@ntu.edu.tw

2026, Jan. 28, I noticed repeat numbering emerged sometimes. Updated code show repeated/missing numbers as well.
Maunally chk the repeating ones, lock into the repeated number of a specific column, and see if the missing number on the column always sharing comparable overlap.
If yes, change the repeated number to the missing number.

Sometimes more than one repeating/missing are presented. Chk the overlaps, should roughly work. I use excel to chk the *.txt btw., easier to locate the root.
