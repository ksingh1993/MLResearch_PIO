import json
import pprint
import urllib.request, urllib.parse

accessKey = 'DAJiRK28vlxL0Qm78yyuzXgEXbrdcdVsON8gt4Z8hV2uoB77SaIgKiHbs8gO3tkU'

sentiment = 'sentimentanalysis.json'
stopwords = 'stopwords.json'
email = 'emails.json'

def getData(filename):
	data = []
	with open(filename) as f:
		for line in f:
			data.append(json.loads(line))
	return data



# print(data[0]['properties'])

def generatePOST(filename):
	trainingData = getData(filename)
	#to extract later for testing the algo
	currentId = 0
	for row in trainingData:
		entityId = row['entityId']
		entityType = row['entityType']
		eventTime = row['eventTime']
		properties = row['properties']
		event = row['event']
		# if properties['sentiment'] > 2:
		# 	properties['sentiment'] = 1
		# else:
		# 	properties['sentiment'] = 0
		data = {
			"event" : event,
			"entityType" : entityType,
			"entityId" : entityId,
			"properties" : properties,
			"eventTime" : eventTime
		}
		url = 'http://127.0.0.1:7070/events.json?accessKey=DAJiRK28vlxL0Qm78yyuzXgEXbrdcdVsON8gt4Z8hV2uoB77SaIgKiHbs8gO3tkU'
		encodedData = json.dumps(data).encode('utf-8')
		header = {"Content-Type" : "application/json"}
		req = urllib.request.Request(url, encodedData, header)
		f = urllib.request.urlopen(req)
		print(f.read())
		currentId += 1
		#totalPOSTs += currentPOST + "\n\n"
	print(currentId)

generatePOST(email)