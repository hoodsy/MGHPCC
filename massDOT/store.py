"""
Stores MassDOT data feeds specified in 'feeds.ini'
into a directory 'data' in the current working directory.

Logging information specifying server response and file writing times
is written to 'feedData.log' inside of the 'data' directory.
"""

import urllib2, os, time, logging, ConfigParser


import ssl
from functools import wraps
def sslwrap(func):
	"""
	Work around for MassDOT server not accepting newer versions 
	of TLS - specifies v1. Necessary for massPort data feeds.
	"""

	@wraps(func)
	def bar(*args, **kw):
			kw['ssl_version'] = ssl.PROTOCOL_TLSv1
			return func(*args, **kw)
	return bar

ssl.wrap_socket = sslwrap(ssl.wrap_socket)


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

	currentDay = time.strftime("%b-%d-%Y")
	lastUpdated = (currentDay + time.strftime("_%H:%M:%S_%Z"))
	path = os.getcwd()+'/data/'+feedname+'/'+currentDay
	if not os.path.exists(path):
  		os.makedirs(path)
	open(path+'/'+lastUpdated+".xml",'w').write(data)

	writeTime = (time.time()-start-resTime) 

	logging.info('Data Feed: '+feedname+' Date/Time: '+lastUpdated)
	logging.info('Response Time: '+`resTime`+' Write Time: '+`writeTime`)
	logging.info('=========')

os.mkdir(os.getcwd()+'/data')
logging.basicConfig(filename=os.getcwd()+'/data/feedData.log',level=logging.INFO)
config = ConfigParser.ConfigParser()
config.read('feeds.ini')
for feed in config.sections():
	writeFeed(config.get(feed, 'url'), feed)
