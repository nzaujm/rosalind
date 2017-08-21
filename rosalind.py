import os        # filename manipulations
import shutil    # moving files from one directory to another

DOWNLOAD_DIR = os.path.expanduser("~/Downloads")
INPUTS_DIR = os.path.expanduser("~/Desktop/Python/rosalind/inputs")

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

