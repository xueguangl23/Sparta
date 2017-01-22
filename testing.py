from urllib2 import Request, urlopen, URLError
import urllib
import json

BackEndURL = 'http://ec2-35-162-32-145.us-west-2.compute.amazonaws.com:5000'

def getLatLug(address):

	KEY = 'AIzaSyC6J06KCLzmvuoab3ve5asK0ygAOvF2wVc'
	address = address.replace(' ','+')
	link = 'https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'.format(address,KEY)
	request = Request(link)

	try:
		response = urlopen(request)
		content = json.loads(response.read())
		lat = content['results'][0]['geometry']['location']['lat']
		lng = content['results'][0]['geometry']['location']['lng']
		return (lat,lng)
	except URLError, e:
	    print('No GeoCode. Got an error code:', e)

def getBalance():
    url = 'http://ec2-35-162-32-145.us-west-2.compute.amazonaws.com:5000/balance'
    post_fields = {'userId':123}
    request = Request(url+'?'+urllib.urlencode(post_fields))
    try:
        response = urlopen(request)
        content = json.loads(response.read())

        return content['balance']
    except URLError, e:
        print('No Balance. Got an error code:', e)

def getNearestBank(location):
    lat,lng = location
    url = BackEndURL+'/nearestLocation'
    post_fields = {"latitude": lat, "longitude": lng}
    link = url +'?' + urllib.urlencode(post_fields)
    try:
        request = Request(link)
        #request.get_method = lambda: "POST"
        response = urlopen(request)
        content = json.loads(response.read())
        return content['nearestLocations']

    except URLError, e:
        print('Unable to get nearest bank. Got an error code:', e)
	

def getHour(location,day):
    lat,lng = location
    url = BackEndURL + '/openHours'
    post_fields = {"latitude": lat, "longitude": lng, "day": day}
    link = url +'?' + urllib.urlencode(post_fields)
    try:
        request = Request(link)
        response = urlopen(request)
        content = json.loads(response.read())
        return content['openHours']
    except URLError, e:
        print('Unable to get Hours, Got an error code: ', e)


def transfer(name,amount):
    url = BackEndURL + '/transferMoney'
    post_fields = {'name':name,'amount':amount}
    link = url +'?' + urllib.urlencode(post_fields)
    #try:
    print link
    request = Request(link)
    response = urlopen(request)
    content = json.loads(response.read())
    print(content)
 #   except URLError, e:
  #      print('Unable to transfer, Got an error code: ', e)


#print 'get balance',getBalance()

#bostonLocation = getLatLug('detroit')
#print getNearestBank(bostonLocation)

print transfer('amul',3.2)




