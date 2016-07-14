from pathlib import Path
import sys, shlex
from subprocess import call

"""
These below function assists to automate the boring stuffs.
"""

def tarGzAutoExtract(topDir):
	"""
	For the given topdir, look into it and auto extract all tar ball files discovered
	"""
	dest = "/path/" # Edit it
	p = Path(topDir)
	count = 0

	for item in p.iterdir():
		if item.is_file():
			sItem = (str(item).split("/")[-1:])[0]
			sItem = (sItem.split(".tar.gz"))[0]
			varDest = dest + sItem
			cmdOne = "mkdir " + varDest

			call(shlex.split(cmdOne))
			cmdLines = "tar -zxvf " + str(item) + " -C " + varDest + " --strip-components=1"
			count += 1 

			call(shlex.split(cmdLines))

	print ("\nCount: ", count) # Maybe useful.

if __name__ == '__main__':
	# Supply the topdir that contains bunch of *.tar.gz files to auto extract them

	entryPoint = sys.argv[1]
	tarGzAutoExtract(entryPoint)