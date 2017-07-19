import sys
import boto


connection = boto.connect_s3()


def check_bucket( name ):
	# Comprobar si existe un bucket.
	#bucket_content = connection.lookup('alvaro-test')
	bucket_content = connection.lookup(name)	
	if bucket_content is None:
	    print "BUCKET DOESNT EXIST"
	    return False
	else:
	    print "BUCKET EXIST"
	    return True

def check_file( bucket_name, file_name ):
	# Comprobar si existe un bucket.
	if (not check_bucket(bucket_name)):
		return False

	#Comprobar si existe un fichero
	bucket = connection.get_bucket(bucket_name)
	

	fichero_recuperado = bucket.get_key(file_name)
	if fichero_recuperado is None:
	    print"FILE DOESNT EXIST"
	    return False
	else:
	    print "FILE EXIST"
	    return True

