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
	trainingData = allData[0:(len(allData))/2]
	#to extract later for testing the algo
	currentId = 0
	for row in trainingData:
		eId = "u"+ str(currentId)
		totalGrade= row[30] + row[31] + row[32]
		tier = 0
		if totalGrade >= 30:
			tier = 1
		data = {
			"event" : "$set",
			"entityType" : "user",
			"entityId" : eId,
			"properties" : {
				"attr0" : row[0],
				"attr1" : row[1],
				"attr2" : row[2],
				"attr3" : row[3],
				"attr4" : row[4],
				"attr5" : row[5],
				"attr6" : row[6],
				"attr7" : row[7],
				"attr8" : row[8],
				"attr9" : row[9],
				"attr10" : row[10],
				"attr11" : row[11],
				"attr12" : row[12],
				"attr13" : row[13],
				"attr14" : row[14],
				"attr15" : row[15],
				"attr16" : row[16],
				"attr17" : row[17],
				"attr18" : row[18],
				"attr19" : row[19],
				"attr20" : row[20],
				"attr21" : row[21],
				"attr22" : row[22],
				"attr23" : row[23],
				"attr24" : row[24],
				"attr25" : row[25],
				"attr26" : row[26],
				"attr27" : row[27],
				"attr28" : row[28],
				"attr29" : row[29],
				"plan" : tier
			}
		}
		url = 'http://127.0.0.1:7070/events.json?accessKey=UrWAZaTlA1Nflr-wAzo8sUC-Fgg2AscnYhBtmb5eyVTBNsKEq3R_j2rwPiEf0Dbh'
		encodedData = json.dumps(data).encode('utf-8')
		header = {"Content-Type" : "application/json"}
		req = urllib.request.Request(url, encodedData, header)
		f = urllib.request.urlopen(req)
		print(f.read())
		currentId += 1
	print(currentId)


'''
Tests the accuracy of the Prediction engine.

Input: 
filename - a .csv file in the same directory 

Output:
<no return value>
'''
def testAccuracy(filename):
	allData = dataParsing.cleanParseData(filename)
	testingData = allData[(len(allData))/2:len(allData)]
	hit = 0
	miss = 0
	for row in testingData:
		totalGrade= row[30] + row[31] + row[32]
		tier = 0
		if totalGrade >= 30:
			tier = 1
		expectedOutput = float(tier)
		data = {
			"attr0" : row[0],
			"attr1" : row[1],
			"attr2" : row[2],
			"attr3" : row[3],
			"attr4" : row[4],
			"attr5" : row[5],
			"attr6" : row[6],
			"attr7" : row[7],
			"attr8" : row[8],
			"attr9" : row[9],
			"attr10" : row[10],
			"attr11" : row[11],
			"attr12" : row[12],
			"attr13" : row[13],
			"attr14" : row[14],
			"attr15" : row[15],
			"attr16" : row[16],
			"attr17" : row[17],
			"attr18" : row[18],
			"attr19" : row[19],
			"attr20" : row[20],
			"attr21" : row[21],
			"attr22" : row[22],
			"attr23" : row[23],
			"attr24" : row[24],
			"attr25" : row[25],
			"attr26" : row[26],
			"attr27" : row[27],
			"attr28" : row[28],
			"attr29" : row[29]
		}
		url = 'http://127.0.0.1:8000/queries.json'
		encodedData = json.dumps(data).encode('utf-8')
		header = {"Content-Type" : "application/json"}
		req = urllib.request.Request(url, encodedData, header)
		f = urllib.request.urlopen(req)
		fetchedData = f.read()
		jsResult = json.loads(fetchedData.decode('utf-8'))
		actualResult = jsResult['label']
		#print(actualResult)
		if float(actualResult) == expectedOutput:
			hit += 1
		else:
			miss += 1
	print("hit: " + str(hit))
	print("miss: " + str(miss))