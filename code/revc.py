import rosalind
import os

def test(alias):
	## check to see if alias file is in downloads
	s = rosalind.get_string(alias)
	
	### New Code ###
	key = {'A':'T', 'C':'G', 'T':'A', 'G':'C'}
	new = []
	for item in s:
		new.append(key.get(item,item)) # Try to get from dict, otherwise keep value
	output = "".join(new[::-1])
	print output

	################
	## Save to outputs
	rosalind.create_output(alias,output)