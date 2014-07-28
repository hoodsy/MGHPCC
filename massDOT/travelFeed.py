import urllib2
import xml.etree.cElementTree as ET
import os

"""
Pulls the xml file for Travel Times from massDOT's website
and writes it to a file, titled by it's timestamp.

Creates a new directory, titled by date, to store each day's data.

** currently pulling Last-Modified for timestamp from XML data - not response header 
"""

request = urllib2.Request('http://www.massdot.state.ma.us/feeds/traveltimes/RTTM_feed.aspx')
data = urllib2.urlopen(request).read()

root = ET.fromstring(data)
lastUpdated = root[0].find('LastUpdated').text
currentDay = lastUpdated[:-13]
path = os.getcwd() +  '/data/'


if currentDay in os.listdir(path):
	os.chdir(path + currentDay)
	open(lastUpdated+".xml", 'w').write(data)
else:
	os.mkdir(path + currentDay)
	os.chdir(path + currentDay)
	open(lastUpdated+".xml", 'w').write(data)
