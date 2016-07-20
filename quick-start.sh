# This assume that you have the README requirements set.
# For more see. <instructions.txt>

# The goal of this simple script, is to give you a flavor on how sweep-toolkit works 
# Using some samples data. Make necessary changes before running it.

# For an elaborated example, see "Cases-Study".

echo ":: Step 1: Download the latest NVD data feeds..."
echo
python3 plugins/SupportingScripts/vulnsDataFeeds.py

echo ":: Step 2: Generate the IT Products -> CVE-IDs mappings ..."
echo "This may take awhile ..., ensure that your box has enough memory at > 2GB."
echo
cd plugins/SupportingScripts/
javac ITProductCVEID.java
java -Xmx2048m ITProductCVEID
cd ../..

# Update -> lastRun.txt
echo "Dataset Generation:" > coreFiles/lastRun.txt
date >> coreFiles/lastRun.txt

echo ":: Step 3: Download and install <Understand> tool"
echo

# Time to breath for a bit. 
sleep 5

# For more information, see "instructions.txt". You can uncomment the following as well.

# Download a copy of Scitools Understand 

# This will be different, if you have a different version but it's okay.

# Check its integrity to see if it's equal to md5: 7004a67dbb95c07c22d65da85d7310db
#md5sum Understand-4.0.813-Linux-64bit.tgz

# Install Understand
#tar -xvzf Understand-4.0.813-Linux-64bit.tgz
#cd scitools/bin/linux64
#echo
#echo "Trigger the Understand free trial activation & DO close the GUI App manually..."
#echo "...Then, go back to the command line started session to resume & observe the sweep-toolkit execution."
#./understand
#cd ../../..
#echo "Back to the normal execution..."

# Time to breath for a bit. 
sleep 5

echo "Environment configurations for the Understand Tool"
# Replace "/path/scitools" with the full path of the Understand installation directory (/path/scitools)
# as described in: "Step 3" of the "instructions.txt" guide.
# i.e. /home/username/Downloads/scitools

python3 plugins/MetricsGeneration/setupEnv.py /path/scitools

source runmefirst.sh
echo "Verify that the PATH settings are properly set ..."
echo $PATH

sleep 5

echo "Timer begins:" >> coreFiles/lastRun.txt
date >> coreFiles/lastRun.txt

echo ":: Step 4: Auto assisted software metrics generations for one or more IT Product(s) given its source codes"
python3 manager.py examples/OpenSSL-Samples/OpenSSL-Preview 1 

echo ":: Step 5: Auto analysis of the generated metrics for the IT-Product dataset auto construction," 
python3 manager.py Understand-Data/Metrics 0

echo "Timer ends:" >> coreFiles/lastRun.txt
date >> coreFiles/lastRun.txt

echo "Run <clean.sh> to clean up all auto downloaded or generated data."