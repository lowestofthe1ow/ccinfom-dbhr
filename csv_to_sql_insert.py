import sys
import csv

writeTo = open("dbhr_insert.sql", "a")
readFrom = open(sys.argv[1], 'r')
csvFile = csv.reader(readFrom)
header = next(csvFile)
headers = map((lambda x: '`'+x+'`'), header)
insert = 'INSERT INTO ' + sys.argv[2] + ' (' + ", ".join(headers) + ") VALUES "
for row in csvFile:
    values = map((lambda x: (x if x == "NULL" else "'"+x+"'")), row)
    writeTo.write(insert +"("+ ", ".join(values) +");\n" )
writeTo.write("\n")
readFrom.close()