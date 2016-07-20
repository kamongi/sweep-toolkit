# The assumption is that you have met the requirements set out in the README file.
# This script needs to be run from the sweep-toolkit root directory

# House keeping
echo "OpenSSL Study Case -- Record" > Cases-Study/OpenSSL/housekeeping.rst
echo " " >> Cases-Study/OpenSSL/housekeeping.rst
echo "Date:" >> Cases-Study/OpenSSL/housekeeping.rst
date >> Cases-Study/OpenSSL/housekeeping.rst
echo " " >> Cases-Study/OpenSSL/housekeeping.rst

# Set up a local directory with all OpenSSL old releases to study
python3 Cases-Study/OpenSSL/downloader.py

sleep 5

echo "Environment configurations for the Understand Tool"
# Replace "/path/scitools" with the full path of the Understand installation directory (/path/scitools)
# as described in: "Step 3" of the "instructions.txt" guide.
# i.e. /home/username/Downloads/scitools

python3 plugins/MetricsGeneration/setupEnv.py /path/scitools
source runmefirst.sh
echo
echo "Verify that the PATH settings are properly set ..."
echo $PATH

sleep 5

echo "Auto assisted software metrics generations for OpenSSL old releases's source codes"
python3 manager.py Cases-Study/OpenSSL/Releases/ 1 

echo "Auto analysis of the generated metrics for the OpenSSL dataset auto construction"
python3 manager.py Understand-Data/Metrics 0

# Word of wisdom: This is a PoC. Subsquent updates will be made as the need arise.