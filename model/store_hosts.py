# store_hosts.py

from myzodb import MyZODB, transaction
db = MyZODB('./Data.fs')
dbroot = db.dbroot

from mymodel import Host
host1 = Host('www.example.com', '192.168.7.2', ['eth0', 'eth1'])
dbroot['www.example.com'] = host1
host2 = Host('dns.example.com', '192.168.7.4', ['eth0', 'gige0'])
dbroot['dns.example.com'] = host2

transaction.commit()
db.close()
