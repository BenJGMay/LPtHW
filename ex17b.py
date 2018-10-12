# We import the arguments module from sys
from sys import argv
# We import the exists function from os.path (wherever that is)
from os.path import exists
# We set script, from_file and to_file as the arguments passed in
script, from_file, to_file = argv

# we boil two lines into one - we open from_file and read it as our indata
# then we set outfile to open a new file and write indata to it
indata = open(from_file).read() ; out_file = open(to_file, 'w').write(indata)
