def createUNDlink():
		"""
		Assuming that you have "Understand tool" already installed. 
		Create a symbolic link of the Understand cmd line tool to the "plugins/MetricsGeneration" directory.
		And prepare the script to be used for the execution environment setup.
		"""
		
		import sys
		import shlex
		from subprocess import call

		# Prompt the user for the Understand installation directory path. 
		# i.e.: "path/scitools/" (Keep the "/" at the end of your input)
		
		# Uncomment these, if you want to receive the path details via prompt.
		#print ("\nEnter a resolvable path to the Understand installation directory path. i.e.: \"/path/scitools\"\n\n")
		#undDir = input()

		# Receive the path via command cmd-line
		# i.e., python3 setupEnv.py /home/username/Downloads/scitools
		undDir = sys.argv[1]

		# Export the paths (Write them to runmefirst.sh & source it later on)
		pathOne = "export PATH=$PATH:" + undDir + "/bin/linux64"
		pathTwo = "export STIHOME=" + undDir

		createRun = "touch runmefirst.sh"
		call(shlex.split(createRun))

		outObj = open("runmefirst.sh", "w")

		outObj.write(pathOne + "\n")
		outObj.write(pathTwo)

		outObj.close()

		chmodit = "chmod u+x runmefirst.sh"
		call(shlex.split(chmodit))

if __name__ == "__main__":
	createUNDlink()
	print ("\nThe scripts for setting up the environment have been prepared -- see runmefirst.sh, source it.\n")