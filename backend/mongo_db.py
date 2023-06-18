import pymongo
import asyncio
from bson.json_util import dumps

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["prompt_builder"]
front_end_collection = mydb["prompt_archs_frontend"]
mycollection = mydb["prompt_archs"]
published_collection = mydb["published_flow_versions"]


mycollection.create_index(
	[
		("flow_name", 1),
		("version", -1)
	],
	unique = True
)

front_end_collection.create_index(
	[
		("name", 1)
	],
	unique = True
)

published_collection.create_index(
	[
		("flow_name", 1),
		("version", -1)
	],
	unique = True
)

def save_or_update_frontend(json_data):
	data = front_end_collection.find_one({'name': json_data["name"]})
	if data is None:
		front_end_collection.insert_one(json_data)
	else:
		front_end_collection.replace_one({'name': json_data["name"]}, json_data, True)

def load_frontend():
	versions = front_end_collection.find()
	list_cur = list(versions)
	for curr in list_cur:
		del curr["_id"]
	json_data = dumps(list_cur)
	print(type(json_data))

	return json_data

def save_or_update(json_data):
	data = mycollection.find_one({'flow_name': json_data["flow_name"], 'version': json_data["version"]})
	if data is None:
		mycollection.insert_one(json_data)
	else:
		mycollection.replace_one({'flow_name': json_data["flow_name"], 'version': json_data["version"]}, json_data, True)


def save_publish_version(json_data):
	data_to_insert = {}
	data_to_insert["flow_name"] = json_data["flow_name"]
	data_to_insert["version"] = json_data["version"]
	
	data = published_collection.find_one({'flow_name': json_data["flow_name"], 'version': json_data["version"]})
	if data is None:
		published_collection.insert_one(data_to_insert)
	else:
		myquery = {'flow_name': json_data["flow_name"], 'version': json_data["version"]}
		published_collection.delete_one(myquery)
		published_collection.insert_one(data_to_insert)

def find_published_dag_arch(flow_name):
	data = published_collection.find_one({'flow_name': flow_name})
	print(data)
	dag_arch = mycollection.find_one({'flow_name': data["flow_name"], 'version': data["version"]})
	return dag_arch
