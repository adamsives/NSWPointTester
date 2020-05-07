from itertools import chain, combinations
import re
import requests
import json


#Create a list of ordered subsets of address elements
def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1,len(s)+1))


#create and address api parameter
def createAddressParameters(streetNum,streetName,streetOrRoad,suburb,postcode):
    addressSubsets = list(powerset([streetNum,streetName,streetOrRoad,suburb,postcode]))
    addressParams = []
    for subset in addressSubsets:# a list of tuples
        addressString = []
        for addressElement in subset:
            addressString.append(addressElement)
        addressStr = re.sub("[\['\],]", '', str(addressString))
        addressParams.append(addressStr)
    return addressParams

#create endpoint(s)
def makeCalls(baseUrl, apiFrags,addresses):
    for fragment in apiFrags:
        for addressStr in addresses:
            print("</p><h2>" + baseURL + fragment + "?address=" + addressStr + "</h2><p>")#-------------debug
            response = requests.get(
                baseURL + fragment,
                params={'address': addressStr},
                headers={'x-api-key': 'IG4fkvA3yH8edKHi8CYDC6WnmJaRd9G3XuNQenHb'}
            )
            print(str(response.text))
            json_data = response.text
            json_object = json.loads(json_data)
            json_formatted_str = json.dumps(json_object, indent=2)
            print(json_formatted_str)

    return "Done"


#create list of endpoints
baseURL =  "https://point.digital.nsw.gov.au/v2/api/"
apiFragment = ['predictive1','predictive2','addressValidation1','addressValidation2','propertyLotDp','adminBoundaries','Mailpoint2']


#create list of variations on address (permutated subset)
addressSubsets = createAddressParameters("499","Marrickville","Road","Dulwich Hill","2203")


#make http requests
x = makeCalls(baseURL,apiFragment,addressSubsets)