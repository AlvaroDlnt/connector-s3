
Using Python 2.7.12

sudo apt-get install python-pip

Using pip 8.1.1

pip install virtualenv

Using

# Create de virtual environment
virtualenv connector-s3

# Activate shell script for virt.env
source bin/activate

# Undo the changes
deactivate

# 
pip install boto
Using boto-2.48.0

./lib/python2.7/site-packages





# Imports y conexión a S3
import boto
from boto.s3.key import Key

connection = boto.connect_s3()


#Crear bucket.

bucket = connection.create_bucket('alvaro-test')

#Crear fichero dentro de un bucket.
file = Key(bucket)
file.key = 'key_for_file'
file.set_contents_from_string('This is the content of a file')


#Listar fichero dentro de un bucket.

bucket_alvaro = connection.get_bucket('alvaro-test')

#Comprobar si existe un fichero
bucket_alvaro = connection.get_bucket('alvaro-test')
fichero_recuperado = bucket_alvaro.get_key('asdf')
if fichero_recuperado is None:
    print "This Key doesn't exist."



#Ver contenido de un fichero dentro de un bucket.
file = Key(bucket_alvaro)
file.key = 'asdf'
file.get_contents_as_string()



# Listar Buckets existentes.

connection = boto.connect_s3()
bucket_alvaro = connection.get_bucket('alvaro-test')


bucket_content = bucket_alvaro.list()


for b in bucket_content:
	print b.name


# Comprobar si existe un bucket.
bucket_content = connection.lookup('alvaro-test')
if bucket_content is None:
    print "This bucket doesn't exist."
