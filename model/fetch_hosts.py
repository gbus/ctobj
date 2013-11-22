# fetch_hosts.py - show hosts in the database

from myzodb import MyZODB
db = MyZODB('./Data.fs')
dbroot = db.dbroot

from mymodel import Host
for key in dbroot.keys():
	obj = dbroot[key]
	if isinstance(obj, Host):
		print "Host:", obj.name
		print "  IP address:", obj.ip, "  Interfaces:", obj.interfaces

db.close()
