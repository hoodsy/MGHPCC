"""
Stores MassDOT data feeds specified in 'feeds.ini'
into a directory 'data' in the current working directory.

Runs until user interrupt.

Logging information specifying server response and file writing times
is written to 'feedData.log' inside of the 'data' directory.
"""

import urllib2, os, time, logging, datetime, ConfigParser

def writeFeed(url, feedname):
	"""
	Pulls a specified data feed, 'url', from MassDOT's website
	and writes the contents to a new file, named by timestamp*.

	Creates a directory 'feedname' to house the feed's data. Inside 'feedname', a new
	directory is created each day and named by date to store updates to the feed.

	* the timestap used to name each file is recorded after
	the response is received; the update being written may
	not be consistent with the filename 
	"""

	start = time.time()

	request = urllib2.Request(url)
	data = urllib2.urlopen(request).read()
	
	resTime = (time.time()-start)

	date = datetime.datetime.utcnow()
	currentDay = ("%s-%s-%s" % (date.year, date.month, date.day))
	lastUpdated = (currentDay + " %s:%s:%s UTC" % (date.hour, date.minute, date.second))

	path = os.getcwd()
	if 'data' not in os.listdir(path):
		os.mkdir(path+'/data/')
	if feedname not in os.listdir(path+'/data/'):
		os.mkdir(path+'/data/'+feedname)
	if currentDay not in os.listdir(path+'/data/'+feedname):
		os.mkdir(path+'/data/'+feedname+'/'+currentDay)

	os.chdir(path+'/data/'+feedname+'/'+currentDay)
	open(lastUpdated+".xml",'w').write(data)
	os.chdir(path)

	writeTime = (time.time()-start-resTime) 

	logging.basicConfig(filename=path+'/data/feedData.log',level=logging.INFO)
	logging.info('Data Feed: '+feedname+' Date/Time: '+lastUpdated)
	logging.info('Response Time: '+`resTime`+' Write Time: '+`writeTime`)
	logging.info('=========')


config = ConfigParser.ConfigParser()
config.read('feeds.ini')
while True:
	for feed in config.sections():
		writeFeed(config.get(feed, 'url'), config.get(feed, 'name'))
		time.sleep(1)
