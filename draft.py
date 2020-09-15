import requests
import json
import random
import sys
# import time
# open is built-in
# print is built-in


# def send_request(body_file_path, api):
# 	body = json.load(open(baseDir_requests + body_file_path))
# 	response = session.post(hostname+api, json=body, headers=header)
# 	return response

# To-do: add timeout parameter in all request
# To-do: check response status code
# To-do: check response content
# To-do: check fault message pattern in reponse
# To-do: extract response from sendEval
# To-do: need session?
# To-do: what happened if not enough MATLAB?

def read_script():
	line = []
	for l in script:
		if l == "\n":
			continue
		line.append(l)
	return "\n".join(line)


def authentication():
	body = json.load(open(baseDir_requests + "/authentication.json")) # opens a json file to a json object, load json object to dictionary
	try:
		response = session.post(hostname + "/service/core/authnz", json=body, headers=header, timeout=1) # pass in url, header, and json body to the post request
	except requests.exceptions.RequestException as e:
		return False, e
	# print(response.text)
	# print(response.status_code)
	data = response.json()
	if data["authenticated"] == "false":
		return False, "Invalid Credential"
	return True, None

# def listResources():
# 	body = json.load(open(baseDir_requests + "/listVersion.json")) # opens a json file to a json object, load json object to dictionary
# 	response = session.post(hostname + "/service/core/resource/lifecycle", json=body, headers=header) # pass in url, header, and json body to the post request
# 	print(response.text)
# 	print(response.status_code)

def listVersion():
	body = json.load(open(baseDir_requests + "/listVersion.json")) # opens a json file to a json object, load json object to dictionary
	response = session.post(hostname + "/service/core/resource/lifecycle", json=body, headers=header) # pass in url, header, and json body to the post request
	print(response.text)
	print(response.status_code)

def acquire():
	body = json.load(open(baseDir_requests + "/acquire.json"))
	try:
		response = session.post(hostname + "/service/core/resource/lifecycle", json=body, headers=header)
	except requests.exceptions.RequestException as e:
		return False, e, None
	# print(response.text)
	# print(response.status_code)
	data = response.json()
	return True, None, data["resource"]["resourceToken"] #??

def createMapping():
	body = json.load(open(baseDir_requests + "/gateway.json"))
	body["resourceToken"] = resourceToken # change resourceToken attribute in the request body to the resourceToken variable
	try:
		response = session.post(hostname + "/service/core/gateway", json=body, headers=header)
	except requests.exceptions.RequestException as e:
		return False, e, None
	# print(response.text)
	# print(response.status_code)
	data = response.json()
	return True, None, data["mapping"]["mappingToken"]

def setMappingCookie():
	param = {"mappingToken": mappingToken}
	try:
		response = session.post(hostname + "/_setmappingcookie", headers=header, params=param)
	except requests.exceptions.RequestException as e:
		return False, e
	return True, None

def setClientType():
	body = json.load(open(baseDir_requests + "/clientType.json"))
	try:
		response = session.post(hostname + "/messageservice/json/secure", json=body, headers=header)
	except requests.exceptions.RequestException as e:
		return False, e
	# print(response.text)
	return True, None

def handshake():
	body = json.load(open(baseDir_requests + "/longPollHandshake.json"))
	body[0]["id"] = randomId
	try:
		response = session.post(hostname + "/messageservice/async", json=body, headers=header)
	except requests.exceptions.RequestException as e:
		return False, e, None
	# print(response.text)
	data = response.json()
	return True, None, data[0]["clientId"] #??

def subscribe():
	body = json.load(open(baseDir_requests + "/subscribe.json"))
	body[0]["id"] = randomId
	body[0]["clientId"] = clientId
	try:
		response = session.post(hostname + "/messageservice/async", json=body, headers=header)
	except requests.exceptions.RequestException as e:
		return False, e
	# print(response.text)
	return True, None

def connect():
	body = json.load(open(baseDir_requests + "/longPollConnect.json"))
	body[0]["id"] = randomId
	body[0]["clientId"] = clientId
	try:
		response = session.post(hostname + "/messageservice/async", json=body, headers=header)
	except requests.exceptions.RequestException as e:
		return False, e
	# print(response.text)
	return True, None

def eval():
	body = json.load(open(baseDir_requests + "/eval.json"))
	body["messages"]["Eval"][0]["mcode"] = read_script()
	try:
		response = session.post(hostname + "/messageservice/json/secure", json=body, headers=header)
	except requests.exceptions.RequestException as e:
		return False, e, None
	# print(response.text)
	data = response.json()
	# print(data["messages"]["EvalResponse"][0]["responseStr"])
	return True, None, data["messages"]["EvalResponse"][0]["responseStr"]

def sendEval():
	body = json.load(open(baseDir_requests + "/asyncEval.json"))
	body[0]["id"] = randomId
	body[0]["clientId"] = clientId
	try:
		response = session.post(hostname + "/messageservice/async", json=body, headers=header)
	except requests.exceptions.RequestException as e:
		return False, e
	print(response.text)
	return True, None

def checkCompletionStatus():
	body = json.load(open(baseDir_requests + "/longPollConnect.json"))
	body[0]["id"] = randomId
	body[0]["clientId"] = clientId
	try:
		response = session.post(hostname + "/messageservice/async", json=body, headers=header)
	except requests.exceptions.RequestException as e:
		return False, e
	# print(response.text)
	return True, None

def destroyMapping():
	body = json.load(open(baseDir_requests + "/destroy_gateway_mapping.json"))
	body["mappingToken"] = mappingToken
	try:
		response = session.post(hostname + "/service/core/gateway", json=body, headers=header)
	except requests.exceptions.RequestException as e:
		return False, e
	# print(response.text)
	return True, None

def releaseMATLAB():
	body = json.load(open(baseDir_requests + "/releaseMATLAB.json"))
	body["resourceToken"] = resourceToken
	try:
		response = session.post(hostname + "/service/core/resource/lifecycle", json=body, headers=header)
	except requests.exceptions.RequestException as e:
		return False, e
	# print(response.text)
	return True, None

def getRandomId():
	return random.randrange(1000)



if __name__ == "__main__":

	# hostname = 'http://localhost:5000'
	# hostname = "https://wrprod01-prod-useast1.mathworks.com"
	hostname = "https://scalability-mos.mwcloudtest.com"
	# hostname = "https://hpoolrelease-qual.mwcloudtest.com"
	baseDir_requests = './resources/requests'

	session = requests.Session()
	header = json.load(open(baseDir_requests + '/header.json'))

	script = open("matlab_script.txt", "r")


	success, e = authentication()
	if not success:
		print(e)
		sys.exit()
	print("Login successfully")
	# listVersion()
	# acquire()

	success, e, resourceToken = acquire()
	if not success:
		print(e)
		sys.exit()

	success, e, mappingToken = createMapping()
	if not success:
		print(e)
		releaseMATLAB()
		sys.exit()

	success, e = setMappingCookie()
	if not success:
		print(e)
		destroyMapping()
		releaseMATLAB()
		sys.exit()
	print("MATLAB gotten")

	success, e = setClientType()
	if not success:
		print(e)
		destroyMapping()
		releaseMATLAB()
		sys.exit()

	randomId = str(getRandomId())
	
	# handshake()
	success, e, clientId = handshake()
	if not success:
		print(e)
		destroyMapping()
		releaseMATLAB()
		sys.exit()

	success, e = subscribe()
	if not success:
		print(e)
		destroyMapping()
		releaseMATLAB()
		sys.exit()

	success, e = connect()
	if not success:
		print(e)
		destroyMapping()
		releaseMATLAB()
		sys.exit()

	# sendEval()
	success, e, result = eval()
	if not success:
		print(e)
		destroyMapping()
		releaseMATLAB()
		sys.exit()
	print("The result of the script:")
	print(result)
	# time.sleep(1)

	success, e = checkCompletionStatus()
	if not success:
		print(e)
		destroyMapping()
		releaseMATLAB()
		sys.exit()

	# mappingToken = "48HVIvAf1G9aQu93GM85UDgbZ4wQ6XG3"
	success, e = destroyMapping()
	if not success:
		print(e)
		releaseMATLAB()
		sys.exit()
	# resourceToken = "mathworks-matlab-pool.hk513ckjst0vy5q520faj5d4lxrro0kmyu0rv"
	success, e = releaseMATLAB()
	if not success:
		print(e)

	print("Logout")
