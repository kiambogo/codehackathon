#!/usr/bin/python
import csv
import json

#Script reads the first row of the CSV and uses the values as the JSON ids
f = open( 'MinistryData.csv', 'r' )
firstLine = f.readline().strip()
firstLine = firstLine.split(',')
reader = csv.DictReader( f, fieldnames = ( firstLine ) )
for row in reader:
	print '{"index": {}}'
	print json.dumps(row)
#out = json.dumps( [ row for row in reader ] )
#print out
