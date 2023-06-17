import pymongo
import asyncio

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["prompt_builder"]
mycollection = mydb["prompt_archs"]
mycollection.create_index(
	[
		("flow_name", 1),
		("version", -1)
	],
	unique = True
)

def save_or_update(json_data):
	data = mycollection.find_one({'flow_name': json_data["flow_name"], 'version': json_data["version"]})
	if data is None:
		mycollection.insert_one(json_data)
	else:
		mycollection.replace_one({'flow_name': json_data["flow_name"], 'version': json_data["version"]}, json_data, True)
