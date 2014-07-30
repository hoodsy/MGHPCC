import urllib2, os, time, logging, datetime

"""
Pulls the xml file from massDOT's website for the specified data feed, 'url',
and writes it to a new file, named by timestamp*.

Creates a directory 'feedname' to house the feed's data. Inside feedname, a new directory
is created each day and named by date to store versions of the feed.

All new directories and files are stored in a directory 'data'
inside the current working directory.

* the timestap used to name each file is recorded after
the response is received; the update being written may
not be consistent with the filename 
"""
def feed(url, feedname):

	start = time.time()

	request = urllib2.Request(url)
	data = urllib2.urlopen(request).read()
	
	resTime = (time.time() - start)

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

	writeTime = (time.time()-start-resTime) 

	logging.basicConfig(filename=path+'/data/'+feedname+'/'+feedname+'.log',level=logging.INFO)
	logging.info('Date/Time: '+lastUpdated)
	logging.info('Response Time: '+`resTime`+' Write Time: '+`writeTime`)
	logging.info('=========')
