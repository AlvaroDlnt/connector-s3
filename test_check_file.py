from check_file import check_bucket
from check_file import check_file

import sys
import boto



# An existing bucket
check_bucket("alvaro-test")

# An NOT existing bucket
check_bucket("qwer")

# An NOT existing bucket AND  existing file
check_file("qwer","foobar")

# An  existing bucket AND  NOT existing file
check_file("alvaro-test","asdf")

# An existing bucket AND existing file
check_file("alvaro-test","foobar")
