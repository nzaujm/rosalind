import os        # filename manipulations
import shutil    # moving files from one directory to another

DOWNLOAD_DIR = os.path.expanduser("~/Downloads")
ROSALIND_DIR, _ = os.path.split(os.path.realpath(__file__))
INPUTS_DIR = os.path.join(ROSALIND_DIR, "inputs")
if not os.path.isdir(INPUTS_DIR):
	os.mkdir(INPUTS_DIR)
	print "Created Input Folder: %s" % INPUTS_DIR

def make_path(directory, alias):
	return os.path.join(directory, "rosalind_%s.txt" % alias)

def move_input(alias):
	# move the textfile from ~/Downloads to the inputs/ folder
	src = make_path(DOWNLOAD_DIR, alias)
	dst = make_path(INPUTS_DIR, alias)
	shutil.move(src, dst)

def get_input(alias):
	# read the input from the inputs/ folder into a string
	with open(make_path(INPUTS_DIR, alias), 'r') as f:
		fstring = f.read()
	return fstring

def get_string(alias):
	#call move_input and get input
	move_input(alias)
	return get_input(alias)

