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
	for i in range(len(rawData)):
		row = rawData[i]
		for j in range(len(row)):
			currentItem = row[j]
			rawData[i][j] = currentItem.replace('"', '')
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
		print row

'''
'''
attrToNumberMap = {
	'school': {'GP': 0, 'MS': 1},
	'sex': {'M': 0, 'F': 1},
	'address': {'U': 0, 'R': 1},
	'famsize': {'LE3': 0, 'GT3': 1},
	'Pstatus': {'T': 0, 'A': 1}	
}