#added to Git on 5/15/2012

import csv
import sys
import urllib2


reader = csv.reader(open("C:\MES_Facilities2.csv", "rb"))
reader.next()
for row in reader:
    rowString = ', ' .join(row[2:3]) .split(' ', 1)
    
    bldgNumber = ', ' .join(rowString[0:1]) .split(' ', 1)
    newbldgNumber = ', ' .join(bldgNumber)
    rdName = ', ' .join(rowString[1:2])
    cityName =  ', ' .join(row[3:4])
    toGeocode = newbldgNumber + "+"  + rdName + "+" + cityName
    #print toGeocode
    baseURL = 'http://maps.googleapis.com/maps/api/geocode/xml?sensor=false&address='
    ConnectionString = baseURL + toGeocode
    print ConnectionString
