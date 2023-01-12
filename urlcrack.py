import hashlib
import requests

for i in range(0,100):
	str2hash = str(i)
	result = hashlib.md5(str2hash.encode())
	# print(result.hexdigest())
	url = "http://10.10.161.19/" + str(result.hexdigest())
	response = requests.get(url)
	print("request sent to ", url, end="")
	if response.status_code == 404:
		print(" with no success")
	else:
		print(" we maybe find something ...")
		print("code", response.status_code)
		print("at : ", i, "/", result.hexdigest())
