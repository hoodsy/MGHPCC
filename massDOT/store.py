import urllib2
import xml.etree.cElementTree as ET
import os, time

"""
Pulls the xml file from massDOT's website for the specified data feed, 'url',
and writes it to a new file, named by timestamp.

Creates a directory 'feedname' to house the feed's data. Inside feedname, a new directory
is created each day and named by date to store each new file.

All new directories and files are stored in a directory 'data'
inside the current working directory.

** currently pulling timestamp from XML data - not response header 
"""
def feed(url, feedname):

	request = urllib2.Request(url)
	data = urllib2.urlopen(request).read()
	root = ET.fromstring(data)
	lastUpdated = root[0].find('LastUpdated').text
	currentDay = lastUpdated[:-13]

	path = os.getcwd()
	if 'data' not in os.listdir(path):
		os.mkdir(path + '/data/')
	if feedname not in os.listdir(path + '/data/'):
		os.mkdir(path + '/data/' + feedname)
	if currentDay not in os.listdir(path + '/data/' + feedname):
		os.mkdir(path + '/data/' + feedname + '/' + currentDay)

	os.chdir(path + '/data/' + feedname + '/' + currentDay)
	open(lastUpdated + ".xml", 'w').write(data)

