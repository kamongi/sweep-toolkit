# Sweep-Toolkit: 

	:: This toolkit facilitates the automation process of software metrics generation for any given IT Product's releases source codes using UNDERSTAND tool [1]. 
	
	:: In addition, it leverages National Vulnerability Database (NVD) data-feeds [2] to automatically extract all disclosed vulnerability details for each analyzed IT Product release.

	:: Then, it produces a dataset in a .csv format with lot of interesting features and computed statistics.

	:: For a look into the collected features see "Guides/dataset-features.txt"

## Requirements

	- openjdk-8-jdk
	- python3
	- scitools Understand (Static Code Analysis Tool)

## Usage

	:: Clone a copy, and see the "instructions.txt" document on how to use this toolkit. 

## Applications

	:1:
		Patrick Kamongi, Krishna Kavi, and Mahadevan Gomathisankaran. "Predicting Unknown Vulnerabilities using Software Metrics and Maturity Models". In: The Eleventh International Conference on Software Engineering Advances (ICSEA 2016), Rome, Italy, August 21-25, 2016.

## Contributing

	1. Fork it!
	2. Create your feature branch: `git checkout -b my-new-feature`
	3. Commit your changes: `git commit -am 'Add some feature'`
	4. Push to the branch: `git push origin my-new-feature`
	5. Submit a pull request :D

## History

	:: 07/13/2016 Pre-alpha-1

## References

	[1]. UNDERSTAND, https://scitools.com/
	[2]. NVD data feeds, https://nvd.nist.gov/

## License

	:: See "LICENSE" document.
