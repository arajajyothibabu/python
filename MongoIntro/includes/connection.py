import pymongo
from pymongo import MongoClient

connection = MongoClient("localhost", 27017)

dbName = connection.test

collectionName = "tests"

#print(dbName.tests.insert({"jb":"Araja Jyothi Babu"}))
print(dbName.tests.find_one())