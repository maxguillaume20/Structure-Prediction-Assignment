"""Pastes PDB sequence to console"""

import argparse
import os

def parse_arguments():

    """Parse arguments"""

    def _is_valid_file_(filename):
        """ Checks if argument if an existing file, else returns an error"""
        if not os.path.isfile(filename):
            raise argparse.ArgumentTypeError("%s is not a valid file" % filename)
        return filename

    parser = argparse.ArgumentParser(description="Convert EMBOSS to PIR alignment")
    parser.add_argument("pdb_file", type=_is_valid_file_,
                        help="PDB filename (input file)")
    args = parser.parse_args()
    return args

def retrieve_sequence(pdb_file):

    """
    Reads PDB file and saves sequence in ATOM and HETATM to string
    """

    f = open(pdb_file, "r")
    seq = ""
    last_residue_nbr = None
    for line in f:
        if line.startswith("ATOM") or line.startswith("HETATM"):
            residue_nbr = line[22:26]
            if residue_nbr != last_residue_nbr:
                seq += line[17:20] + " "
                last_residue_nbr = residue_nbr
        if "END" in line:
            break
    f.close()
    return seq

def main():
    args = parse_arguments()
    seq = retrieve_sequence(args.pdb_file)
    print seq


if __name__ == "__main__":
    main()
