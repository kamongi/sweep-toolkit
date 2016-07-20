# Assuming you want to keep a clean-slate, as always back them up first ;)

echo "Note that this script only clean up auto-downloaded/generated data & files..."
echo

# Just the Data-Feeds
rm -r Data-Feeds/

# Just the generated Understand metrics data & dataaset
rm -r Understand-Data/

# Just the IT Products & CVE-ID mappings
rm coreFiles/ITProduct-CVEID.txt

# Reset the lastRun.txt
> coreFiles/lastRun.txt

# Be gone ...
rm runmefirst.sh

echo "Back to the beginnings..."
echo
echo "Run <quick-start.sh> or follow the <instructions.txt> to perform your IT Products Metrics generation and analysis."