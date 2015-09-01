### Centinel server

The Server used to control Centinel nodes in the wild.

### Install and usage
#### Preparation (all platforms)
Get the maxind geolocation database by running 

    $ mkdir ~/.centinel
    $ curl http://geolite.maxmind.com/download/geoip/database/GeoLite2-Country.mmdb.gz -o ~/.centinel/maxmind.db

Download and install PostgreSQL [here](http://www.postgresql.org/download/).
Create user root:

    $ sudo -u postgres createuser -s root

Change the password for the user postgres since Centinel-server connects to PSQL Database with this password: 

    $ sudo -u postgres psql
    $ postgres=> alter user postgres password 'postgres';

Install psycopg2:
	pyscopg2 has a dependency on postgresql-server-dev. So install postgresql-server-dev
	$ pip install -U postgresql-server-dev-X.Y
	$ pip install -U psycopg2
	
Install GeoIP :
	First install library libgeoip-dev
	$ apt-get install libgeoip-dev
	$ pip install GeoIP
	

It is recommended that you run Python version > 2.7.9 and Werkzeug version >= 0.10.0 for better TLS support.

#### Debian & OS X

    $ pip install flask flask-httpauth flask-sqlalchemy passlib geoip2 netaddr postgres
    $ python run.py

### Supported platforms
    * Unix
    * Mac OS X

### Running with Apache (WSGI) for production environments
Install mod_wsgi and apache

	$ sudo apt-get install apache2 libapache2-mod-wsgi

Create the directory /opt/centinel-server and clone a copy of the centinel server repo with

	$ sudo mkdir /opt/centinel-server
    $ cd /opt/centinel-server; git clone https://github.com/iclab/centinel-server.git

Add centinel server port to /etc/ports.conf by adding Listen 8082 to /etc/apache2/ports.conf.

Add misc/centinel.conf to /etc/apache2/sites-enabled/

And setup your mod\_wsgi with your virtual env by adding this line to your /etc/apache2/mods_available/wsgi.conf:

        WSGIPythonPath /home/iclab/env/lib/python2.7/site-packages

Edit your WSGI script if necessary at centinel.wsgi



