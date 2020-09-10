import requests
import json
import random


# def send_request(body_file_path, api):
# 	body = json.load(open(baseDir_requests + body_file_path))
# 	response = session.post(url+api, json=body, headers=header)
# 	return response


def authentication():
	body = json.load(open(baseDir_requests + "/authentication.json"))
	response = requests.post(url+"/hello", json=body, headers=header)
	# response = send_request('/authentication.json', "/hello")
	print(response.text)

def acquire():
	body = json.load(open(baseDir_requests + "/acquire.json"))
	response = requests.post(url+"/hello", json=body, headers=header)
	# response = send_request('/acquire.json', "/hello"
	session_attributes["resourceToken"] = "1"
	print(response.text)
	return response["resourceToken"]

def createMapping():
	body = json.load(open(baseDir_requests + "/gateway.json"))
	body["resourceToken"] = session_attributes["resourceToken"]
	response = requests.post(url+"/hello", json=body, headers=header)
	# response = send_request('/gateway.json', "/hello")
	print(response.text)
	return response["mappingToken"]

def setMappingCookie():
	cookies = dict(cookies_are='working')
	response = requests.post(url+"/hello", headers=header)
	print(response.text)

def setClientType():
	body = json.load(open(baseDir_requests + "/clientType.json"))
	response = requests.post(url+"/hello", json=body, headers=header)
	print(response.text)
	return response["clientId"]

def getRandomId():
	return random.randrange(1000)

def handshake():
	body = json.load(open(baseDir_requests + "/longPollHandshake.json"))
	body["id"] = randomId
	response = requests.post(url+"/hello", json=body, headers=header)
	print(response.text)

def subscribe():
	body = json.load(open(baseDir_requests + "/subscribe.json"))
	body["id"] = randomId
	body["clientId"] = clientId
	response = requests.post(url+"/hello", json=body, headers=header)
	print(response.text)

def connect():
	body = json.load(open(baseDir_requests + "/longPollConnect.json"))
	body["id"] = randomId
	body["clientId"] = clientId
	response = requests.post(url+"/hello", json=body, headers=header)
	print(response.text)

def sendEval():
	body = json.load(open(baseDir_requests + "/asyncEval.json"))
	body["id"] = randomId
	body["clientId"] = clientId
	response = requests.post(url+"/hello", json=body, headers=header)
	print(response.text)

def checkCompletionStatus():
	body = json.load(open(baseDir_requests + "/longPollConnect.json"))
	body["id"] = randomId
	body["clientId"] = clientId
	response = requests.post(url+"/hello", json=body, headers=header)
	print(response.text)

def destroyMapping():
	body = json.load(open(baseDir_requests + "/destroy_gateway_mapping.json"))
	body["mappingToken"] = mappingToken
	response = requests.post(url+"/hello", json=body, headers=header)
	print(response.text)

def releaseMATLAB():
	body = json.load(open(baseDir_requests + "/releaseMATLAB.json"))
	body["resourceToken"] = resourceToken
	response = requests.post(url+"/hello", json=body, headers=header)
	print(response.text)


url = 'http://localhost:5000'
baseDir_requests = './resources/requests'

session = requests.Session()
header = json.load(open(baseDir_requests + '/header.json'))
# session_attributes = {}

if __name__ == "__main__":
	authentication()
	resourceToken = acquire()
	mappingToken = createMapping()
	setMappingCookie()
	clientId = setClientType()
	randomId = str(getRandomId())
	handshake()
	subscribe()
	connect()
	sendEval()
	checkCompletionStatus()
	destroyMapping()
	releaseMATLAB()