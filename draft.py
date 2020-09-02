import requests
import json

url = 'https://matlab.mathworks.com'

def create_header(header):
	header['Accept'] = 'application/json'
	header['Accept-Encoding'] = 'gzip, deflate'
	header['Accept-Language'] = 'en-US,en;q=0.9,he;q=0.8'
	header['Connection'] = 'keep-alive'
	header['Content-Type'] = 'application/json'

	# header = open('requests.header')
	# return header

header = {}
create_header(header)

def create_body(body):
	body["mwtype"] = "authnz/PasswordLogin"
	body["subjectId"] = "gstubbs"
	body["password"] = "matlab"


body = {}
create_body(body)


def authentication():
	pass

def acquire():
	pass

def createMapping():
	pass

def setMappingCookie():
	pass

def setClientType():
	pass

def getRandomId():
	pass

def handshake():
	pass

def subscribe():
	pass

def connect():
	pass

def sendEval():
	pass

def checkCompletionStatus():
	pass

def destroyMapping():
	pass

def releaseMATLAB():
	pass


x = requests.post(url+"/service/core/authnz", json=body, headers=header)

print(x.text)
