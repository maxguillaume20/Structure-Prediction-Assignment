#!/usr/bin/python

import argparse
import os
import sys

"""Convert EMBOSS to PIR alignment
Example usage: python ./scripts/convert_emboss_pir.py data/templates_models/D1/2kpw.emboss data/templates_models/D1/2kpw.pir D1_2kpw 2kpw 2 A 1 122
"""

def parse_emboss(emboss_file, template_position):
    """
    Description
    Parses an EMBOSS alignment file and returns a dictionnary

    Arguments
    filename: str. path of EMBOSS

    Value
    emboss:
    """
    # Dictionnary containing parsed emboss file
    # Keys: sequence and structure (sequence is sequence to be modelled, structure is template)
    # Value: sequence alignment
    emboss = {"sequence": "", "structure": ""}

    # Number of sequence in file (takes on value 0 or 1, init -1)
    number = -1

    f = open(emboss_file, "r")

    for line in f:
        line = line.strip("\r\n") # remove breakline at end of line

        if line.startswith("#") or line.startswith(" ") or line == "":
            continue

        number = (number + 1) % 2 # update sequence position
        sequence = line[21:71] # get sequence
        sequence = ''.join([i for i in sequence if not i.isdigit()]) # remove numeric
        sequence = sequence.strip() # remove whichspaces

        if (number + 1) == template_position:
            emboss["structure"] += sequence
        else:
            emboss["sequence"] += sequence

    emboss["structure"] += "*"
    emboss["sequence"] += "*"

    f.close()
    return emboss

def convert_to_pir(emboss, sequence_name, template_name,
                   template_chain, template_first, template_last):
    """
    Description
    Converts a parsed EMBOSS file (use parse_emboss) into a PIR formatted string

    Arguments
    emboss: dict. parse_emboss output

    Value:
    pir: str: PIR formatted string to be written a file
    """

    pir = ">P1;%s\n" %sequence_name
    pir += "sequence:%s: . : . : . : : : : :\n" %sequence_name
    pir += emboss["sequence"] + "\n\n"
    pir += ">P1;%s\n" %template_name
    pir += "structure:%s.pdb: %s  : %s : %s  :%s  : : : :\n" %(template_name, template_first, template_chain, template_last, template_chain)
    pir += emboss["structure"]
    return pir

def parse_arguments():

    """Parse arguments"""

    def _is_valid_file_(filename):
        """ Checks if argument if an existing file, else returns an error"""
        if not os.path.isfile(filename):
            raise argparse.ArgumentTypeError("%s is not a valid file" % filename)
        return filename

    parser = argparse.ArgumentParser(description="Convert EMBOSS to PIR alignment")
    parser.add_argument("emboss_file", type=_is_valid_file_,
                        help="EMBOSS filename (input file)")
    parser.add_argument("pir_file",
                        help="PIR filename (output file)")
    parser.add_argument("sequence_name",
                        help="Name of sequence to be modelled")
    parser.add_argument("template_name",
                        help="Name of template used to model sequence")
    parser.add_argument("template_position", type=int, choices=[1,2],
                        help="Which sequence in EMBOSS file corresponds to the template")
    parser.add_argument("template_chain",
                        help="Template chain in PDB file")
    parser.add_argument("template_first", type=int,
                        help="Template first residue in PDB file")
    parser.add_argument("template_last", type=int,
                        help="Template last residue in PDB file")
    args = parser.parse_args()
    return args

def main():

    # Parse arguments
    args = parse_arguments()

    # Parse EMBOSS File
    emboss = parse_emboss(args.emboss_file, args.template_position)

    # Convert EMBOSS to PIR
    pir = convert_to_pir(emboss, args.sequence_name, args.template_name,
                         args.template_chain, args.template_first, args.template_last)

    # Write PIR file
    pir_f = open(args.pir_file, "w")
    pir_f.write(pir)
    pir_f.close()

if __name__ == "__main__":
    main()
