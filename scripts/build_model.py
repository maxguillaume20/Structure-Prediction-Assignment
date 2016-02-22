import argparse
import os
from modeller import *
from modeller.automodel import *

def parse_arguments():

    """Parse arguments"""

    def _is_valid_file_(x):
        """ Checks if argument if an existing file, else returns an error"""
        if not os.path.isfile(x):
            raise argparse.ArgumentTypeError(x + " is not a valid file")
        return x

    parser = argparse.ArgumentParser(description="Make models with MODELLER")
    parser.add_argument("alignment", help="Alignment file in PIR format")
    parser.add_argument("sequence", help="Sequence to be modelled")
    parser.add_argument("template", help="Name of template (should also have a PDB file in the same directory)")
    parser.add_argument("-n", "--n_models", type=int, default=5, help="Integer specifying the number of models")
    args = parser.parse_args()
    #_is_valid_file_(args.template + ".pdb")
    return args

def main():

    args = parse_arguments()
    env = environ()
    a = automodel(env,
                  alnfile=args.alignment,
                  knowns=args.template,
                  sequence=args.sequence,
                  assess_methods=(assess.DOPE, assess.GA341))
    a.starting_model = 1
    a.ending_model = args.n_models
    a.make()

if __name__ == "__main__":
    main()
