import requests
import csv

region='%5E87494'
page_index = '&index=48'
url = 'https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=REGION'+ \
        region+'&maxBedrooms=1&maxPrice=1300&radius=3.0'+page_index \
        +'&propertyTypes=flat&includeLetAgreed=false&mustHave=&dontShow=&furnishTypes=furnished&keywords='