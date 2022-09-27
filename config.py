import os
import getpass 
import logging

# misc
recommended_version = 1.1
production = True

# user details
# checks environment variables LOGNAME, USER, and USERNAME" and returns the value of the 
# first one set to non-empty string. 
current_user  = getpass.getuser()

# Sets home directory ... but ideally this isn't hardcoded 
centinel_home = "/opt/centinel-server/"

# directory structure
results_dir     = os.path.join(centinel_home, 'results')
experiments_dir = os.path.join(centinel_home, 'experiments')
inputs_dir = os.path.join(centinel_home, 'inputs')
static_files_allowed = ['economistDemocracyIndex.pdf', 'consent.js']

# details for how to access the database
def load_uri_from_file(filename):
    with open(filename, 'r') as filep:
        uri = filep.read()
    return uri

# Setup the database to connect to 
# password file for PostgreSQL --> refers to "centinel password file" 
database_uri_file = os.path.join(centinel_home, "cent.pgpass")

if not production:
    DATABASE_URI = "postgresql://postgres:postgres@localhost/centinel"
else:
    DATABASE_URI = load_uri_from_file(database_uri_file)

# GeoIP and AS databases from http://dev.maxmind.com/geoip/legacy/geolite/
# use https://dev.maxmind.com/geoip/geoipupdate/#For_Free_GeoLite2_and_GeoLite_Legacy_Databases
# to update databases
geoip_db = '/usr/local/share/GeoIP/GeoLite2-Country.mmdb'
asn_db = '/usr/local/share/GeoIP/GeoLiteASNum.dat'

# consent form
prefetch_freedomhouse = False

# web server
ssl_cert  = "server.iclab.org.crt"
ssl_key   = "server.iclab.org.key"
ssl_chain = "server.iclab.org_bundle.crt"

LOG_FILE  = os.path.join(centinel_home, "centinel-server.log")
LOG_LEVEL = logging.DEBUG
