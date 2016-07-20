"""
Fetch and download all openssl releases
"""

import sys, shlex, os, re
from subprocess import call

def releasesListExtractor(filename):
	"""
	Given a text file with the unformatted list of OpenSSL old releases, 
	extract the list of releases names to automated their download and extraction.
	"""
	tmpList = []

	# Each entry is for each openssl release (KBytes, Date, File) details.
	tmpFile = open(filename, "r")

	for item in tmpFile:
		item	= item.split(" ")
		var		= item[3]
		tmpList.append(var.replace("\t", ""))

	tmpFile.close()

	return tmpList


def downloadReleases(releases_list, topdir, tag_version):
	"""
	Download all old openssl releases.
	"""
	for item in releases_list:
		#i.e., https://www.openssl.org/source/old/0.9.x/openssl-fips-ecp-2.0.9.tar.gz
		#i.e., https://www.openssl.org/source/old/1.0.0/openssl-1.0.0k.tar.gz
		#i.e., https://www.openssl.org/source/old/1.0.1/openssl-1.0.1s.tar.gz
		#i.e., https://www.openssl.org/source/old/1.0.2/openssl-1.0.2g.tar.gz
		#i.e., https://www.openssl.org/source/old/1.1.0/openssl-1.1.0-pre3.tar.gz
		#i.e., https://www.openssl.org/source/old/fips/openssl-fips-2.0.11.tar.gz

		atYourCommands = "wget " + "https://www.openssl.org/source/old/" + tag_version + "/" + item
		atYourCommands += " --output-document=" + topdir + item
		print (atYourCommands)
		call(shlex.split(atYourCommands))

		postCommand = "tar -xzf " + topdir + item + " -C " + topdir
		print (postCommand)
		call(shlex.split(postCommand))

		cleanOld = "rm " + topdir + item
		print (cleanOld)
		call(shlex.split(cleanOld))

if __name__ == '__main__':
	# Set up a local directory to store all openssl releases.

	tag_version_list	= ["0.9.x", "1.0.0", "1.0.1", "1.0.2", "1.1.0", "fips"]
	entryPoint			= "Cases-Study/OpenSSL/Releases/"

	if not os.path.isdir(entryPoint):
		os.makedirs(entryPoint)

	for oldTag in tag_version_list:
		oldReleaseFile = "Cases-Study/OpenSSL/OpenSSL-Old-Releases-" + oldTag

		# List of OpenSSL releases to download
		releases = releasesListExtractor(oldReleaseFile)
		#print ("Releases: \n\n", releases, "\n\nReleases#: ", len(releases))

		# Download the above OpenSSL releases 
		downloadReleases(releases, entryPoint, oldTag)

	print ("\nAt ease!\n\t Verify to see if all OpenSSL old releases have been " \
			"dowloaded successfully under this directory: \n\t\tCases-Study/OpenSSL/Releases/\n")