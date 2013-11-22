#!/usr/bin/python


import ZODB.blob, transaction
from ZODB.interfaces import IBlob
from ZODB import FileStorage, DB
from ZODB.blob import BlobStorage

datafs = 'data.fs'
base_storage = FileStorage.FileStorage(datafs)

blob_dir = 'blobs'
#blob_storage = create_storage(blob_dir=blob_dir)
blob_storage = BlobStorage(blob_dir, base_storage)
database = DB(blob_storage)
connection1 = database.open()
root1 = connection1.root()

myblob = ZODB.blob.Blob()
#IBlob.providedBy(myblob)

f = myblob.open("w")
localfile = open('smallsample-2.6.37.tar.gz', 'rb')


while True:
	data = localfile.read(512)
	if len(data) == 0:
		break
	f.write(data)

root1['myblob'] = myblob

transaction.commit()
 
base_storage.close()
localfile.close()
f.close()

