import sys, shlex, os
from subprocess import call

"""
These scripts serves to auto download the NVD data feeds. 
"""

def autoDownload(topdir):
	"""
	Given a directory location, download all current NVD, data feeds.
	"""
	#2002 -> Curreny year
	from datetime import date

	currentYear = (date.today().year + 1)

	for year in range(2002, currentYear):
		#i.e., http://static.nvd.nist.gov/feeds/xml/cve/nvdcve-2.0-2002.xml.gz
		atYourCommands = "wget " + "http://static.nvd.nist.gov/feeds/xml/cve/nvdcve-2.0-" + str(year) + ".xml.gz"
		atYourCommands += " --output-document=" + topdir + "nvdcve-2.0-" + str(year) + ".xml.gz"
		print (atYourCommands)
		call(shlex.split(atYourCommands))

		postCommand = "gunzip " + topdir + "nvdcve-2.0-" + str(year) + ".xml.gz"
		print (postCommand)
		call(shlex.split(postCommand))

if __name__ == '__main__':
	
	#Default path to store NVD data feeds

	#Uncomment this if you are running this program from /SupportingScripts directory
	#entryPoint = "../../Data-Feeds/NVD/"

	#Uncommented to be run in the directory root by default
	entryPoint = "Data-Feeds/NVD/"
	if not os.path.isdir(entryPoint):
	   os.makedirs(entryPoint)

	#Uncomment this next line to specify where to store them otherwise.
	#entryPoint = sys.argv[1]

	autoDownload(entryPoint)

	print ("\nAt Ease...")
