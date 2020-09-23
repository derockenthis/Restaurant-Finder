'https://api.yelp.com/v3/businesses/search'
import random
import json
import requests
#define a business ID



#FULL CODE----------------------------
business_id = '_4MHBRFCep_1OamUnU4k1Q'

#define api key, Define the endpoint, and define the header
API_KEY = 'YXnypAjbAusiaPaSHTrgFw_qLa9rNNXWZy1-37FuLP9jun0Ev52j5ruXGncmGdyD351WPb9lvXPWRuluVl6hUwgE-flYATqkMNtggXruoNxSuKSmacc45XWebqgbX3Yx'
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization':'bearer %s' % API_KEY}

#Define the parameters

PARAMETERS = {'term':'restaurants',
              'limit':50,
              'radius':10000,
              'location':'Modesto California'}

#Make a request to the yelp API

response = requests.get(url = ENDPOINT,params=PARAMETERS,headers=HEADERS)

#convert the JSON string to a Dictionary
business_data = response.json()
num = random.randint(0, len(business_data['businesses']))
#print(business_data['businesses'][0]['name'])

def locateuser(location):
    business_id = '_4MHBRFCep_1OamUnU4k1Q'

    #define api key, Define the endpoint, and define the header
    API_KEY = 'YXnypAjbAusiaPaSHTrgFw_qLa9rNNXWZy1-37FuLP9jun0Ev52j5ruXGncmGdyD351WPb9lvXPWRuluVl6hUwgE-flYATqkMNtggXruoNxSuKSmacc45XWebqgbX3Yx'
    ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
    HEADERS = {'Authorization':'bearer %s' % API_KEY}

    #Define the parameters

    PARAMETERS = {'term':'restaurants',
                  'limit':50,
                  'radius':10000,
                  'location':location}

    #Make a request to the yelp API

    response = requests.get(url = ENDPOINT,params=PARAMETERS,headers=HEADERS)

    #convert the JSON string to a Dictionary
    business_data1 = response.json()
    return business_data1['businesses']

def listofr(location):
    newlist = []
    business_id = '_4MHBRFCep_1OamUnU4k1Q'

    #define api key, Define the endpoint, and define the header
    API_KEY = 'YXnypAjbAusiaPaSHTrgFw_qLa9rNNXWZy1-37FuLP9jun0Ev52j5ruXGncmGdyD351WPb9lvXPWRuluVl6hUwgE-flYATqkMNtggXruoNxSuKSmacc45XWebqgbX3Yx'
    ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
    HEADERS = {'Authorization':'bearer %s' % API_KEY}

    #Define the parameters

    PARAMETERS = {'term':'restaurants',
                  'limit':50,
                  'radius':10000,
                  'location':location}

    #Make a request to the yelp API

    response = requests.get(url = ENDPOINT,params=PARAMETERS,headers=HEADERS)

    #convert the JSON string to a Dictionary
    business_data1 = response.json()
    for biz in business_data1['businesses']:
        newlist.append(biz['name'])
    return newlist
print(listofr('modesto'))
