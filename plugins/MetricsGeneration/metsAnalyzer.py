from pathlib import Path

class OpsOnMets(object):
	"""
	This class supports the analysis of various computed software metrics using UNDERSTAND tool.

	It contains a suite of automatic scripts to analyze the generated metrics, getting the 
	proper CPE name for each IT Product release and for each CPEName returns relevant 
	number of reported vulnerabilities for the particular CPE. 
	"""

	def __init__(self):
		"""
		Set important default parameters to use throughout this project. 
		"""

		self.datasetsDir           = self.makesomedirs("Understand-Data/Datasets/")
		self.rVersionsMetrics      = []
		self.rReleasesNames        = []
		self.datasetFeatures	   = ""
		self.thisYear			   = self.updateYear()

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
			print ("Warning: the directory is already created, make sure it is empty or properly backed up for accurate metrics generation process.\n")

	def updateYear(self):
		""" Return this year """

		from datetime import date
		tmp = date.today()

		return tmp.year 
	     
	def processOpenSSL(self, itemName):
	    """
	    Given an openSSL metrics file name, pre-process for later use.
	    I.E. "openssl-0.9.1c" -> "openssl:0.9.1c"
	    """

	    tmp2 = itemName.split("-")
	    if len(tmp2) == 2:
	        dataItem = tmp2[0]+ ":" +tmp2[1]
	    else:
	        dataItem = tmp2[0] + "-" + tmp2[1]+ ":" +tmp2[2]

	    return dataItem
	     
	def vulcanizationCVEIDs(self, tmpCPEname):
	    """
	    Given a potential product CPE name as input,
	    return the number of found vulnerabilities
	    """

	    prodVulnPairFile = "coreFiles/ITProduct-CVEID.txt"
	    inFile = open(prodVulnPairFile, "r")
	     
	    tmpCVEIDs = []
	     
	    for item in inFile:
	        cpeName, vulnID = item.split("&")    
	        cpeName = cpeName.replace(" ", "")
	         
	        if cpeName == tmpCPEname:
	            tmpCVEIDs.append(vulnID)
	    
	    inFile.close()

	    #Initialize it with year-1999 to year-2016 (or thisYear value) keys and zero as value to be later updated
	    dictByYearNumCVEIDs = {}

	    for i in range(1999, self.thisYear + 1):
	    	dictByYearNumCVEIDs[i] = 0

	    cveidsold = str(len(tmpCVEIDs))

	    for cve in tmpCVEIDs:
	    	cve = cve.split("-")
	    	for key in iter(dictByYearNumCVEIDs):
	    		if str(cve[1]) == str(key):
	    			dictByYearNumCVEIDs[key] += 1

	    for chef in iter(sorted(dictByYearNumCVEIDs)):
	    	cveidsold += "," + str(dictByYearNumCVEIDs[chef])

	    # Some CVE-IDs instance may be pulled back "aka. REJECTED. i.e. CVE-2015-3199"

	    return cveidsold 
	 
	def vulcanizationProducts(self, productName):
	    """
	    Given a potential product name as input,
	    return its CPE full name
	    """

	    prodVulnPairFile = "coreFiles/ITProduct-CVEID.txt"
	    inFile = open(prodVulnPairFile, "r")
	     
	    for item in inFile:
	         
	        cpeName, vulnID = item.split("&") 
	        tmp = cpeName.split(":")
	        lenVar = len(tmp)
	         
	        #Add a handle
	        partialInfo = ""
	        if lenVar >= 5:
	            partialInfo = tmp[3] + ":" + tmp[4]
	        else:
	            if lenVar == 4:
	                partialInfo = tmp[3]
	            else:
	                if lenVar == 3:
	                    partialInfo = tmp[2]
	         
	        if partialInfo == productName:
	            inFile.close()
	            return cpeName

	    inFile.close()
	    return
	 
	def featuresNames(self, filename):
	    """
	    Given a *.csv file of computed metrics (Using UNDERSTAND TOOL), return the features names. 
	    """

	    iSample        = open(filename, "r")
	     
	    numKinds        = -1 #skip the first line
	    featuresList    = []
	     
	    for item in iSample:
	        featuresList = item.split(",")
	        break
	     
	    tmpList     = []
	     
	    for var in iSample:
	        tmpList.append(var)
	        numKinds += 1
	     
	    numFeatures = len(featuresList)
	     
	    iSample.close()
	     
	    featTmp = featuresList[2:numFeatures] #remove the first two columns
	    featString = "cpeName,#CVEIDs"

	    for i in range(1999, self.thisYear+1):
	    	featString += ",Year-" + str(i) 
	     
	    for i in range(len(featTmp)):
	        featString = featString + "," + featTmp[i] 
	     
	    self.datasetFeatures = featString 
	     
	def sumMetrics(self, filename):
	    """
	    Given a csv file of computed metrics (Using UNDERSTAND TOOL) for a given IT product (source codes), 
	    return a list of each metric feature sum for all kinds analyzed. 
	    """

	    iSample        = open(filename, "r")
	    numKinds        = -1 #skip the first line
	     
	    for item in iSample:
	        item = item.split(",")
	        break
	     
	    tmpList     = []
	    newTmpList  = []
	     
	    for var in iSample:
	        tmpList.append(var)
	        numKinds += 1
	     
	    for var in tmpList:
	        var = var.replace("\n", "")
	        tmp = var.split(',')
	        lenTmp = len(tmp)
	         
	        for i in range(lenTmp):
	            if i > 1:
	                if tmp[i] is "":
	                    tmp[i] = float("0")
	                else:
	                    try:
	                        tmp[i] = float(tmp[i])
	                    except:
	                        tmp[i] = 0.0 #Exception handling
	         
	        newTmpList.append(tmp[2:lenTmp])
	     
	    sumOfAllKinds = [sum(i) for i in zip(*newTmpList)]
	    iSample.close()
	     
	    tmpMetrics = str(sumOfAllKinds[0])
	    for i in range(1, len(sumOfAllKinds)):
	        tmpMetrics = tmpMetrics + "," + str(sumOfAllKinds[i])
	     
	    return tmpMetrics
	     
	def identifyFiles(self, topDir):
		"""
		This method, analyze the top dir for inner diretories of any provided IT Product release versions, 
			and update the global rVersions list for discovered IT Products release versions. 
		"""

		p = Path(topDir)

		for item in p.iterdir():
			if item.is_file():
				self.rVersionsMetrics.append(str(item)) #Intetional use of str() for later processings...

	def identifyReleases(self):
		"""
		From each, identified IT product release directory, manipulate its dir path name, 
			to extract the release name + version. 
		"""

		tmpVersions = self.rVersionsMetrics
		for item in tmpVersions:
			sItem = str(item).split("/")[-1:]
			sItem = str(sItem).split("metrics-")[1]
			sItem = str(sItem).split(".csv")[0]
			self.rReleasesNames.append(sItem)

	def analyzer(self):
		"""
		For each discovered IT Product release metrics file, analyze it and build a dataset:
			Where, each dataset entry will look like (CPE + #CVE-IDs + Metrics Sums) exported into a *.csv file.
		"""

		#Only useful for the feature names extraction
		filename = "coreFiles/metrics-openssl-1.0.1.csv"
		self.featuresNames(filename)
		print ("\nFeatures: ", self.datasetFeatures)

		#Extract the name to use for the dataset name, i.e., /path/openssl.csv
		#genericName = self.rReleasesNames[0]
		#genericName = genericName.split("-")[0]

		genericName = "openssl-test"     # Test
		#genericName = "openssl-dataset" # Production (Auto detect it, TODO)

		outCsvFile  = self.datasetsDir + genericName + ".csv"
		print ("\nProposed metrics dataset name: ", outCsvFile)

		inCSV       = open(outCsvFile, "w")
		inCSV.write(self.datasetFeatures)

		for iThink in range(len(self.rVersionsMetrics)):

		    tmpCPENAME = ""
		    if self.vulcanizationProducts(self.processOpenSSL(self.rReleasesNames[iThink])) == None:
		    	tmpCPENAME = self.processOpenSSL(self.rReleasesNames[iThink]).replace(" ", "")
		    else:
		    	#This is for OpenSSL use case, otherwise, the process* should be updated accordingly.
		    	tmpCPENAME  = self.vulcanizationProducts(self.processOpenSSL(self.rReleasesNames[iThink])).replace(" ", "")

		    numCVEIDsold = self.vulcanizationCVEIDs(tmpCPENAME)

		    metricsData = tmpCPENAME + "," + numCVEIDsold + "," + self.sumMetrics(self.rVersionsMetrics[iThink]) + "\n"
		    print ("\n", metricsData)

		    inCSV.write(metricsData)
		    
		inCSV.close()
		print ("\nMetrics analysis is done.\n")

	def dirMatching(self, inputDir):
		"""
		Cordinate the process of generating metrics from source codes, 
		"""

		self.identifyFiles(inputDir)
		
		self.identifyReleases()
		print ("\nMetrics to analyze are of these IT Product releases: ", self.rReleasesNames, "\n")

		# Analyze each discovered IT Product release generated metrics, then produce a dataset (CPE + #CVE-IDs + Metrics' Sums)
		self.analyzer()
		print ("\n\nExhale...\n\tSee the generated dataset of analyzed metrics under this directory: ", self.datasetsDir,"\n")