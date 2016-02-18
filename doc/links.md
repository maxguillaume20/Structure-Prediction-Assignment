## HMMer
http://www.ebi.ac.uk/Tools/hmmer

## Sequence Alignment
http://www.ebi.ac.uk/Tools/emboss/align/

## PIR Format Documentation
http://www.salilab.org/modeller/manual/node494.html

## Modeller tutorial ("4. Model building" and "5. Model evaluation”)
http://www.salilab.org/modeller/tutorial/basic.html

## Alignment problems in Modeller

Firstly check you .log file. Usually there is information here to explain what went wrong.

If  modeller thinks sequences do not align, and you do not understand why, you can check which sequence MODELLER reads from your PDB file:
http://salilab.org/modeller/ FAQ.html#17

## LGA for GDT calculations
http://proteinmodel.org/AS2TS/LGA/lga.html

Make sure to read http://proteinmodel.org/AS2TS/LGA/lga_format.html
You should think about including the following options (please read the description):
-3
-aa1, -aa2 
-ch1, -ch2

Be very careful, this program assumes the alignment is known (it only makes a superposition). This means there may be NO differences in sequence between your two sets of amino acids you specify for each of the files you want to compare!



