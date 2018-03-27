import re
from pymongo import MongoClient

count = 0

text = open("./cnn.txt", 'r')
content = text.read()
text.close()

client = MongoClient()
db = client.pplt
collection = db.adlist

for index in collection.find():
    tempRe = index['list']
    #print(tempRe)
    res = re.search(tempRe, content)
    if res is None:
        continue
    count = count + 1

print ("Number of ADs: ")
print (count)
