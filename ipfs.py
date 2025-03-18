import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
  json_data = json.dumps(data)
  url = "https://ipfs.infura.io:5001/api/v0/add"
    
  files = {
      'file': ('data.json', json_data)
  }
    
  response = requests.post(url, files=files)
  response.raise_for_status()
    
  cid = response.json()["Hash"]
	return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	
  url = f"https://gateway.pinata.cloud/ipfs/{bafkreiclibrsw75ygmqsvebfbmo6mub6xph4vfqudaqhwborhlihmyzjqu}"
  response = requests.get(url)
  response.raise_for_status()
  data = response.json()

	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data
