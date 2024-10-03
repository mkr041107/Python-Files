import csv
from geopy.geocoders import Nominatim
zip = []
name = []
address = []
city = []
csvfile = 'C:\\Users\\334706\\Downloads\\addresses.csv'
with open(csvfile, 'r') as f:
        state = []
        # create a list of rows in the CSV file
        rows = f.readlines()

        # strip white-space and newlines
        rows = list(map(lambda x:x.strip(), rows))
        for row in rows:
            
            # further split each row into columns assuming delimiter is comma 
            row = row.split(',')

            # append to data-frame our new row-object with columns
          
            
            geolocator = Nominatim(user_agent="geolocator")
            #location = geolocator.geocode("175 5th Avenue NYC")
            location = geolocator.geocode(row[1] + " " +row[2])
            print(location.address)
            print((location.latitude, location.longitude))
            print(location.raw)
            print (location)
           # first line is AdressCity
            

