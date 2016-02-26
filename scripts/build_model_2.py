
from modeller import *
from modeller.automodel import *

log.verbose()
env = environ()
# directories for input atom files
env.io.atom_files_directory = ['../Structure-Prediction-Assignment/data/model_emboss/']

env = environ()
a = automodel(env,
              alnfile  = '3gk5_emboss.pir',
              knowns   = '3gk5',
              sequence = 'd2_emboss',
              assess_methods=(assess.DOPE, assess.GA341),
              inifile = 'D2/res/d2_emboss.B99990001.pdb')
a.starting_model = 1
a.ending_model = 5

a.md_level = None

a.make()