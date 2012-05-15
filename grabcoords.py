import csv
import sys


baseURL = 'http://maps.googleapis.com/maps/api/geocode/xml?sensor=false&address='
toGeocode = '7817+Baltimore National Pike+Frederick'
ConnectionString = baseURL + toGeocode
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
