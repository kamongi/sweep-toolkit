from pathlib import Path

class GenMets(object):
	"""
	This class service our metrics toolkit for the tasks of preparing batch jobs and tasking them, 
		for metrics generations. 
	"""

	def __init__(self):
		"""
		Set important default parameters to use throughout this project. 
		"""

		self.udbProjectsDir = self.makesomedirs("Understand-Data/udbProjectsDir/")
		self.metricsDir     = self.makesomedirs("Understand-Data/Metrics/")
		self.commandsDir    = self.makesomedirs("Understand-Data/Commandos/")
		self.rVersions      = []
		self.rReleases      = []

	def makesomedirs(self, entryPoint):
		"""
		Make some directories for me. 
		"""

		import os, sys

		if not os.path.isdir(entryPoint):
		   os.makedirs(entryPoint)
		   print (entryPoint, "..Directory is created.\n")

		   return entryPoint
		else:
			print ("Warning: the directory is already created, make sure it is empty or properly backed for accurate metrics generation process.\n")


	def identifyDirs(self, topDir):
		"""
		This method, analyze the top dir for inner diretories of any provided IT Product release versions, 
			and update the global rVersions list for discovered IT Products release versions. 
		"""

		p = Path(topDir)

		for item in p.iterdir():
			if item.is_dir():
				self.rVersions.append(str(item)) #Intetional use of str() for later processings...

	def identifyReleases(self):
		"""
		From each, identified IT product release directory, manipulate its dir path name, 
			to extract the release name + version. 
		"""

		tmpVersions = self.rVersions
		for item in tmpVersions:
			sItem = str(item).split("/")[-1:]
			self.rReleases.append(sItem[0])

	def undBatchMode(self, CommandsFileName):
		"""
			Given a list of text files names of relevant commands, construct a batch mode command line to execute each text file. 
		"""

		import shlex
		from subprocess import call
		from time import sleep

		# Create und symbolic link and export the relevant path. 
		# self.createUNDlink()
		# Run the setupEnv.py & runmefirst.sh

		print ("\n\nAssuming that you have Understand tool installed within your environment. \n\tIf you do not know what is UNDERSTAND TOOL, learn more at: (https://scitools.com/).\n\n")

		#input("\n\nNot Ready, break CTRL + C, otherwise ENTER to continue...\n\n") # At this stage, verify the path & links before proceeding.
		print("\n\nNot Ready, break CTRL + C, otherwise ENTER to continue...\n\n")
		sleep(5)
		
		#recommend to execute this program in the local directory where the "./und" script reside, otherwise, you will have to point its path.

		# Here, we access und command line tool via a created symbolic link or sourced paths to this package
		cmdLines = "und " + CommandsFileName 
	
		call(shlex.split(cmdLines))

	def genBatchFile(self, CommandsToRun, prodName):
		"""
			Given an input of Understand commands, write them into a text file to be used later for the generation of the metrics csv file.
		"""

		tmpFile = self.commandsDir + prodName + ".txt"
	
		outFile = open(tmpFile, "w")
		outFile.write(CommandsToRun)
		outFile.close()

		# To execute the generated Commands text file
		self.undBatchMode(tmpFile)

	def generateCommandFile(self):
		"""
			Given each IT Product name, build up a batch file of Understand commands, to be used later for generating, its metrics csv file.
			-- Read more at "https://scitools.com/support/commandline/", "https://scitools.com/feature/supported-languages/"
		"""

		itProductsReleases  = self.rReleases
		itProductsPaths     = self.rVersions

		#This can be parallelized, but for now, it is going to be executed in serial
		for iCount in range(len(itProductsReleases)):

			#Create and open a new "multi-languages i.e. C++, Java, etc." project
			createLanguages = "create -languages Ada Assembly C++ FORTRAN Java JOVIAL VHDL Pascal Cobol Web Python C# " + self.udbProjectsDir + "project-" + itProductsReleases[iCount] + ".udb\n"
	
			#Add the specified directory of source to the project and Analyze the project
			sourceProject = "add " + itProductsPaths[iCount] + "\n" + "analyze\n"
		
			#Specify to generate all metrics
			genMetrics = "settings -metrics all\n"	

			#Set the path for the metrics csv file
			setMetricsPath = "settings -metricsOutputFile " + self.metricsDir + "metrics-" + itProductsReleases[iCount] + ".csv\n"	
		
			#Generate the metrics csv file and exit interactive mode
			lastStep = "metrics\n" + "quit\n" 

			#Temporal Commands Data
			tmpData = createLanguages + sourceProject + genMetrics + setMetricsPath + lastStep
			
			#Construct the Understand commands to be used for project metrics csv file generation 
			print ("\nTasking --", itProductsReleases[iCount], " #For Metrics Generation\n")
			self.genBatchFile(tmpData, itProductsReleases[iCount])
			print ("\nTask is completed for --", itProductsReleases[iCount], " #Metrics Generation\n")

	def dirMatching(self, inputDir):
		"""
		Cordinate the process of generating metrics from source codes, 
		"""

		self.identifyDirs(inputDir)

		self.identifyReleases()

		# Prepare -- Understand -- commands for each IT Product release versions to be written into various batch files. 
		self.generateCommandFile()
		
		print ("\n\nExhale...\n\tSee the generated metrics under this directory: ", self.metricsDir, "\n")