import urllib2
import xml.etree.cElementTree as ET
import os

"""
Pulls the xml file for Travel Times from massDOT's website
and writes it to a new file, titled by timestamp.

Creates a new directory, titled by date, to store each day's data.

All new directories and files are stored in a directory 'data'
inside the current working directory.

** currently pulling Last-Modified for timestamp from XML data - not response header 
"""

request = urllib2.Request('http://www.massdot.state.ma.us/feeds/traveltimes/RTTM_feed.aspx')
data = urllib2.urlopen(request).read()
root = ET.fromstring(data)
lastUpdated = root[0].find('LastUpdated').text
currentDay = lastUpdated[:-13]

path = os.getcwd()
if 'data' not in os.listdir(path):
	os.mkdir(path + '/data/')
if currentDay not in os.listdir(path + '/data/'):
	os.mkdir(path + '/data/' + currentDay)

os.chdir(path + '/data/' + currentDay)
open(lastUpdated + ".xml", 'w').write(data)
