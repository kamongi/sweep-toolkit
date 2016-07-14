"""
Cordinate all necessary tasks towards metrics generation and analysis for any IT Product source code.
"""

from plugins.MetricsGeneration.genMetsCenter import GenMets
from plugins.MetricsGeneration.metsAnalyzer import OpsOnMets

import sys

if __name__ == '__main__':
	# This is the path of the top directory of a given IT Product that contains 
	# all necessary IT Product release versions directories or generated metrics for metrics generation or analysis

	if len(sys.argv) == 3:
		# Add some exception checking and handling
		entryPoint = sys.argv[1]
		checkCode  = sys.argv[2]	

		if checkCode == "1":
			instaGen = GenMets()
			instaGen.dirMatching(entryPoint)

		elif checkCode == "0":
			opsInstance = OpsOnMets()
			opsInstance.dirMatching(entryPoint)

		else:
			print ("\n::To generate metrics.\n\tUsage: python3 manager.py /path/itProductsSourceCodesTopDir 1")
			print ("\n\tFor example : python3 manager.py examples/OpenSSL-Samples/OpenSSL-Preview/ 1\n\n")
			print ("\n::To analyze generated metrics.\n\tUsage: python3 manager.py /path/itProductsGeneratedMetricsDir 0\n")
			print ("\n\tFor example : python3 manager.py examples/OpenSSL-Samples/OpenSSL-Metrics/ 0\n\n")
			print ("\nStuck..., see: README, instructions.txt and other Guides docs.\n")
	else:
		print ("\n::To generate metrics.\n\tUsage: python3 manager.py /path/itProductsSourceCodesTopDir 1")
		print ("\n\tFor example : python3 manager.py examples/OpenSSL-Samples/OpenSSL-Preview/ 1\n\n")
		print ("\n::To analyze generated metrics.\n\tUsage: python3 manager.py /path/itProductsGeneratedMetricsDir 0\n")
		print ("\n\tFor example : python3 manager.py examples/OpenSSL-Samples/OpenSSL-Metrics/ 0\n\n")
		print ("\nStuck..., see: README, instructions.txt and other Guides docs.\n")