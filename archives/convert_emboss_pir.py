#!/usr/bin/python

import argparse
import os
import sys

"""Convert EMBOSS to PIR alignment"""
__author__ = "Ashvin and Olivier"

def parse_emboss(filename):
    """
    Description
    Parses an EMBOSS alignment file and returns a dictionnary

    Arguments
    filename: str. path of EMBOSS

    Value
    emboss:
    """
    f = open(filename, "r")
    for line in f:
        line = line.strip("\r\n") # remove breakline at end of line

        if line.startswith("#"): # skip comments
            skip

        if line.startswith

        seq = line[20:100] # get sequence
    f.close()
    return 0

def convert_to_pir(emboss):
    """
    Description
    Converts a parsed EMBOSS file (use parse_emboss) into a PIR formatted string

    Arguments
    emboss: dict. parse_emboss output

    Value:
    pir: str: PIR formatted string to be written a file
    """
    return "0"

def parse_arguments():

    """Parse arguments"""

    def _is_valid_file_(filename):
        """ Checks if argument if an existing file, else returns an error"""
        if not os.path.isfile(filename):
            raise argparse.ArgumentTypeError("%s is not a valid file", filename)
        return filename

    parser = argparse.ArgumentParser(description="Convert EMBOSS to PIR alignment")
    parser.add_argument("emboss_file", type=_is_valid_file_, help="EMBOSS filename (input)")
    parser.add_argument("pir_file", help="PIR filename (output)")
    args = parser.parse_args()
    return args

def main():
    args = parse_arguments()
    emboss = parse_emboss(args.emboss_file)
    pir = convert_to_pir(emboss, )
    pir_f = open(args.pir_file, "w")
    pir_f.write(pir)
    pir_f.close()

if __name__ == "__main__":
    main()
