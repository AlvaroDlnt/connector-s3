This program provide functions to check if a file or a bucket exists in a S3 file system.

Now, we are going to explain how to run the script:
	The result script was made using Python 2.7.12

	Install pip 8.1.1:
	sudo apt-get install python-pip

	Install virtual environment:
	pip install virtualenv

	# Create folder for the project
	mkdir connector-s3

	# Create virtual environment inside the folder project.
	virtualenv connector-s3

	# Activate shell script for virt.env
	# Initial path = connector-s3
	source ./bin/activate

	(# Deactive virtual env)
	(deactivate)

	# Install boto-2.48.0 
	pip install boto

	# Execute script. Success example
	python test_check_file_console.py 'alvaro-test' 'foobar'

	#Output:
	# Bucket exist
	# File exist

	# Execute script with command line. Failure example
	python test_check_file_console.py 'alvaro-test' 'asdf'

	#Output:
	# Bucket exist
	# File doesnt exist


	# "Automated test" (see the file)
	python test_check_file.py



