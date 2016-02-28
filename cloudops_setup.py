import urllib2
import datetime
import time
import psycopg2
from subprocess import call, Popen
import os

os.system('sudo apt-get update')

os.system('sudo apt-get install apache2')

os.system('sudo apt-get build-dep build-essential')

os.system('sudo apt-get install lamp-server')

os.system('sudo wget -qO- https://apt.boundlessgeo.com/gpg.key | apt-key add -')

os.system('sudo echo "deb https://apt.boundlessgeo.com/suite/latest/ubuntu/ trusty main" > /etc/apt/sources.list.d/opengeo.list')

os.system('sudo apt-get update')

os.system('apt-cache search opengeo')

os.system('sudo apt-get install opengeo')

os.system("sudo sh -c "echo 'ProxyPassReverse /geoexplorer http://localhost:8080/geoexplorer' >> /etc/apache2/sites-available/000-default.conf"")

os.system("sudo sh -c "echo 'ProxyPass /geoeditor http://localhost:8080/geoeditor' >>/etc/apache2/sites-available/000-default.conf"")

os.system("sudo sh -c "echo 'ProxyPassReverse /geoeditor http://localhost:8080/geoeditor' >>/etc/apache2/sites-available/000-default.conf"")

os.system("sudo sh -c "echo 'ProxyPass /geowebcache http://localhost:8080/geowebcache' >> /etc/apache2/sites-available/000-default.conf"")

os.sytem("sudo sh -c "echo 'ProxyPassReverse /geowebcache http://localhost:8080/geowebcache' >> /etc/apache2/sites-available/000-default.conf"")

os.system("sudo sh -c "echo 'ProxyPass /dashboard http://localhost:8080/dashboard' >> /etc/apache2/sites-available/000-default.conf""

os.system("sudo sh -c "echo 'ProxyPassReverse /dashboard http://localhost:8080/dashboard' >> /etc/apache2/sites-available/000-default.conf"")

os.system("sudo sh -c "echo 'ProxyPass /recipes http://localhost:8080/recipes' >>/etc/apache2/sites-available/000-default.conf"")

os.system("sudo sh -c "echo 'ProxyPassReverse /recipes http://localhost:8080/recipes' >>/etc/apache2/sites-available/000-default.conf"")
os.system("sudo sh -c "echo 'ProxyPass /opengeo-docs http://localhost:8080/opengeo-docs' >> /etc/apache2/sites-available/000-default.conf"")

os.system("sudo sh -c "echo 'ProxyPassReverse /opengeo-docs http://localhost:8080/opengeo-docs' >> /etc/apache2/sites-available/000-default.conf"")

os.system("sudo sh -c "echo ' ' >> /etc/apache2/sites-available/000-default.conf"")

os.system("sudo sh -c "echo '</VirtualHost>' >> /etc/apache2/sites-available/000-default.conf"")

os.system("sudo chmod -R 755 /var/www")

os.system("sudo service apache2 restart")

