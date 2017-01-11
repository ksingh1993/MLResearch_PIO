import csv

'''
Imports raw data from csv file and returns output in form of list of rows (which are also in list form)

Input:
filename - a .csv filename in the same directory

Output:
result - a list of lists, where the inner list elements are the corresponding rows in the csv file
'''
def parseMyCsv(filename):
	#returns a list of list of strings
	result = []
	with open(filename) as csvFile:
		csvReader = csv.reader(csvFile)
		for row in csvReader:
			result += [row]
	return result

'''
Builds on top of parseMyCsv by cleaning out the double quotes present inside some string values when data
is imported from CSV.
'''
def cleanParseData(filename):
	rawData = parseMyCsv(filename)
	for i in range(1, len(rawData)):
		row = rawData[i]
		for j in range(len(row)):
			currentItem = row[j].replace('"', '')
			numericVal = 0
			if currentItem in general.keys():
				numericVal = general[currentItem]
			elif 'job' in rawData[0][j]:
				numericVal = job[currentItem]
			elif 'reason' in rawData[0][j]:
				numericVal = reason[currentItem]
			elif 'guardian' in rawData[0][j]:
				numericVal = guardian[currentItem]
			else:
				numericVal = float(currentItem)
			rawData[i][j] = numericVal
	return rawData

'''
Prints a list of lists in an orderly fashion.
It will print each list in the original list in a new line.

Input:
rowList - a list of lists to be pretty printed

Output:
<no return value> 
'''
def prettyPrint(rowList):
	for row in rowList:
		print(row)

'''
Following are four dictionaries to map attribute values that are strings into corresponding numbers
'''
general = {
	'GP' : 0,
	'MS' : 1,
	'F' : 0,
	'M' : 1,
	'U' : 0,
	'R' : 1,
	'LE3' : 0,
	'GT3' : 1,
	'T' : 0,
	'A' : 1,
	'yes' : 1,
	'no' : 0
}

job = {
	'teacher' : 0,
	'health' : 1,
	'services' : 2,
	'at_home' : 3,
	'other' : 4
}

reason = {
	'home' : 0,
	'reputation' : 1,
	'course' : 2,
	'other' : 3
}

guardian = {
	'mother' : 0,
	'father' : 1,
	'other' : 2,
}
