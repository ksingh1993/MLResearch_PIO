import dataParsing
import json
import urllib.request, urllib.parse

'''
Reads from the file 'filename', sends first half of data to pio data preparator to train engine.

Input: 
filename - a .csv file in the same directory 

Output:
<no return value>
'''
def sendTrainingData(filename):
	allData = dataParsing.cleanParseData(filename)
	trainingData = allData[0:len(allData)/2]
	#to extract later for testing the algo
	totalPOSTs = ""
	currentId = 0
	for row in trainingData:
		eId = "u"+ str(currentId)
		data = {
			"event" : "$set",
			"entityType" : "user",
			"entityId" : eId,
			"properties" : {
				"attr0" : float(row[0]),
				"attr1" : float(row[1]),
				"attr2" : float(row[2]),
				"plan" : float(row[4])
			}
		}
		url = 'http://127.0.0.1:7070/events.json?accessKey=UrWAZaTlA1Nflr-wAzo8sUC-Fgg2AscnYhBtmb5eyVTBNsKEq3R_j2rwPiEf0Dbh'
		encodedData = json.dumps(data).encode('utf-8')
		header = {"Content-Type" : "application/json"}
		req = urllib.request.Request(url, encodedData, header)
		f = urllib.request.urlopen(req)
		print(f.read())
		currentId += 1
		#totalPOSTs += currentPOST + "\n\n"
	print(currentId)



def testAccuracy():
	testingData = parseMyCsv()[1]
	hit = 0
	miss = 0
	for row in testingData:
		if(row[4] != ""):
			expectedOutput = float(row[4])
			data = {
				"attr0" : float(row[0]),
				"attr1" : float(row[1]),
				"attr2" : float(row[2])
			}
			url = 'http://127.0.0.1:8000/queries.json'
			encodedData = json.dumps(data).encode('utf-8')
			header = {"Content-Type" : "application/json"}
			req = urllib.request.Request(url, encodedData, header)
			f = urllib.request.urlopen(req)
			fetchedData = f.read()
			jsResult = json.loads(fetchedData.decode('utf-8'))
			actualResult = jsResult['label']
			print(actualResult)
			if float(actualResult) == expectedOutput:
				hit += 1
			else:
				miss += 1
			print("expected: " + str(expectedOutput) + " actualOutput: " + str(actualResult))
	print("hit: " + str(hit))
	print("miss: " + str(miss))