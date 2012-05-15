#added to Git repository XMLParser on 5/15/2012
#Based on a script found at http://www.travisglines.com/web-coding/python-xml-parser-tutorial

#all these imports are standard on most modern python implementations
#import library to do http requests:
import urllib2
import sys
import unicodedata
import csv

#import easy to use xml parser called minidom:
from xml.dom.minidom import parseString

#opens up our csv
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

 
#Sets the URL to our address (building number, road name, road type, and city
#at the end of the base Google Maps Geocoder)
#baseUrl = 'http://maps.googleapis.com/maps/api/geocode/xml?sensor=false&address='
#toGeocode = '259+najoles+rd+millersville'
#ConnectionString = baseUrl + toGeocode
#
    #download the file:
    file = urllib2.urlopen(ConnectionString)

    #convert to string:
    data = file.read()

    #close file because we dont need it anymore:
    file.close()

    #parse the xml you downloaded
    dom = parseString(data)

    #create empty list
    doc = []
    #loop through the first 8 xml tags and display
    f = 0
    for f in range(8):
        xmlTag = dom.getElementsByTagName('short_name') [i].toxml()

        #strip off the tag (<tag>data</tag>  --->   data):
        xmlData=xmlTag.replace('<short_name>','').replace('</short_name>','')

        #encode each xmlTag element as ASCII to avoid unicode character
        Data=xmlData.encode('ascii')

        #append Data element to our list 'row'
        doc.append(Data)

        #rinse, repeat    
        f+= 1

    #now we get the lat/lon (but we don't
    #need to loop through like we did above)
    a = 0
    xmlLatTag = dom.getElementsByTagName('lat') [a].toxml()
    xmlLat=xmlLatTag.replace('<lat>','').replace('</lat>','')
    xmlLonTag = dom.getElementsByTagName('lng') [a].toxml()
    xmlLon=xmlLonTag.replace('<lng>','').replace('</lng>','')
    Lat=xmlLat.encode('ascii')
    Lon=xmlLon.encode('ascii')
    doc.append(Lat)
    doc.append(Lon)
    print doc

    #convert our row back to csv


    #convert csv to shapefile
