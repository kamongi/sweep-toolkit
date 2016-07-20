# Getting Started

## What's OpenSSL?
	
	:: See. "https://www.openssl.org/"

## Assumptions
	
	:: We assume that you have read our paper on:
		"Predicting Unknown Vulnerabilities using Software Metrics and Maturity Models"
	:: You have read our "Readme" and tried our our sample examples using the "instructions.txt" guide.

## Metrics generation and analysis

	::Download all publicy available OpenSSL releases
	
	:: The most recent previous releases can be found at "ftp://ftp.openssl.org/source/" 
	:: and all releases can be found at "https://www.openssl.org/source/old".

	:: For simplicity, run:

		$ cd ../.. # To the root of the sweep-toolkit directory
		$ ./setup-openssl-case.sh
		
		# This script will:

			:: Fetch all openssl releases and download them locally

			:: Generate Understand metrics for each OpenSSL release

			:: Generate a dataset by analyzing the above metrics, in addition
				with the vulnerability disclosure trend for each OpenSSL release.

			:: Note that this script, can be updated and apply to any other software product.


## Application

	:: This OpenSSL case study (note that there could be some minor differences due to the time of study, since the vulnerabilities and releases could have changed) is futured in this paper:

		Patrick Kamongi, Krishna Kavi, and Mahadevan Gomathisankaran. "Predicting Unknown Vulnerabilities using Software Metrics and Maturity Models". In: The Eleventh International Conference on Software Engineering Advances (ICSEA 2016), Rome, Italy, August 21-25, 2016.