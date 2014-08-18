MGHPCC
======

Storage of MassDOT data feeds
-----------------------------

This repository houses the scripts used to collect and archive data
exposed by MassDOT (http://www.massdot.state.ma.us/DevelopersData.aspx)
on servers at the MGHPCC.

Current Feeds
-------------

**In Progress on MGHPCC**

All of the data feeds being collected and their url locations are listed
in **feeds.ini**.

Currently, all General Transit Feed Specification (**GTFS**) require their schema 
to be loaded manually.  The only feed this currently applies to is 
**vehicleLocations**, via the **MBTA_GTFS.zip** file.

Accessing Data on MGHPCC
------------------------

The data feeds are collected on **opendata.mghpcc.org** and 
can be accessed via ssh.
	- **user**: massdot
	- **hostname**: opendata.mghpcc.org
	- **ssh key**: id_rsa_massdot
		- file and passphrase located on MOC private repo

**example**: ``ssh -i ~/.ssh/id_rsa_massdot massdot@opendata.mghpcc.org``

There is a clone of this repository located on opendata.mghpcc.org 
collecting data, and the data is stored in **~/MGHPCC/massDOT/data**.


