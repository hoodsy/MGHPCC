import urllib2
import xml.etree.cElementTree as ET
import os

request = urllib2.Request('http://www.massdot.state.ma.us/feeds/traveltimes/RTTM_feed.aspx')
data = urllib2.urlopen(request).read()

root = ET.fromstring(data)
lastUpdated = root[0].find('LastUpdated').text
currentDay = lastUpdated[:-13]
path = '/Users/loganbernard/Dropbox/MOC/massDOT/data/' + currentDay

# test if there is a dir for the current day
if currentDay in os.listdir(os.getcwd()+'/data'):
	os.chdir(path)
	open(lastUpdated+".xml", 'w').write(data)

# if not, create that directory (with name as month-day-year), and write inside it
else:
	os.mkdir(path)
	os.chdir(path)
	open(lastUpdated+".xml", 'w').write(data)
