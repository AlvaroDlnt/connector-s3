from check_file import check_file
import sys
import boto


# Retrieve script parameters.
# Example python test_check_file.py 'alvaro-test' 'foobar'
bucket_name = sys.argv[1] 
file_name = sys.argv[2]

check_file( bucket_name, file_name )