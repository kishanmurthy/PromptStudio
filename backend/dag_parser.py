import json

def read_sample_json():
	f = open('sample.json')
	data = json.load(f)
	return data

class Nodes:
	def __init__(self, json_data):
		print(json_data)
		self.node_id = json_data["id"]
		self.node_type = json_data["type"]
		self.node_label = json_data["label"]
		self.node_incomings = []
		self.node_outgoings = []

		if self.node_type == "prompt":
			self.node_prompt = json_data["prompt"]
			self.node_output_format = json_data["output_format"]

		if self.node_type != "output":
			self.node_output_tag = json_data["output_tag"]

def topological_sort(node_dict):
	tp_sort = []
	zero_indegrees_stack = []
	current_indegrees = {}
	for node in node_dict:
		indegrees = len(node_dict[node].node_incomings)
		current_indegrees[node] = indegrees
		if indegrees == 0:
			zero_indegrees_stack.append(node)

	while len(zero_indegrees_stack) != 0:
		vertex = zero_indegrees_stack.pop()
		tp_sort.append(vertex)
		vertex_node = node_dict[vertex]
		vertex_outgoing_nodes = vertex_node.node_outgoings
		for outgoing_node in vertex_outgoing_nodes:
			current_indegrees[outgoing_node] = current_indegrees[outgoing_node] - 1
			if current_indegrees[outgoing_node] == 0:
				zero_indegrees_stack.append(outgoing_node)
	return tp_sort

def process_prompt_nodes(node_dict):
	tp_sort = topological_sort(node_dict)
	return tp_sort
	
def create_dag_object(dag_arch):
	node_dict = {}
	json_data = dag_arch
	for obj in json_data["dag_data"]:
		# its edge to process 
		if "edge" in str(obj["id"]):
			source = node_dict[obj["source"]]
			target = node_dict[obj["target"]]

			source.node_outgoings.append(obj["target"])
			target.node_incomings.append(obj["source"])

		else:
			node = Nodes(obj)
			node_key = ""
			if node.node_type == "start" or node.node_type == "end":
				node_key = node.node_type
			else:
				node_key = node.node_id
			node_dict[str(node_key)] = node

	tp_sort = process_prompt_nodes(node_dict)
	return node_dict, tp_sort

