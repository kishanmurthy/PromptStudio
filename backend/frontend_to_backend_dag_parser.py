def to_backend_json(frontend_dag):
	backend_dag = {}
	backend_dag["flow_name"] = "job_description"
	backend_dag["version"] = frontend_dag["DAGS"]["name"]


	input_text = {}
	input_panels = frontend_dag["DAGS"]["inputPanels"]
	input_tag_values = frontend_dag["input_text"]

	count = 0
	for input_panel in input_panels:
		input_text[input_panel["input_tag"]] = input_tag_values[count]
		count = count + 1

	backend_dag["input"] = input_text

	elements = frontend_dag["DAGS"]["elements"]
	prompt_panels = frontend_dag["DAGS"]["promptPanels"]
	input_panels = frontend_dag["DAGS"]["inputPanels"]

	element_mappings = {}
	prompt_panel_mappings = {}
	input_panel_mappings = {}

	for element in elements:
		element_mappings[element["id"]] = element

	for prompt_panel in prompt_panels:
		prompt_panel_mappings[prompt_panel["node_id"]] = prompt_panel

	for input_panel in input_panels:
		input_panel_mappings[input_panel["node_id"]] = input_panel

	dag_data= []

	for element_id in element_mappings:
		element_data = element_mappings[element_id]
		if element_data["type"] == "input":
			dag_node_element = {}
			dag_node_element["id"] = element_data["id"]
			dag_node_element["type"] = "input"
			dag_node_element["label"] = element_data["label"]
			dag_node_element["output_tag"] = input_panel_mappings[element_data["id"]]["input_tag"]
			dag_data.append(dag_node_element)
		elif element_data["type"] == "default":
			dag_node_element = {}
			dag_node_element["id"] = element_data["id"]
			dag_node_element["type"] = "prompt"
			dag_node_element["label"] = element_data["label"]
			print(prompt_panel_mappings[element_data["id"]])
			dag_node_element["prompt"] = prompt_panel_mappings[element_data["id"]]["prompt_value"]
			dag_node_element["output_tag"] = prompt_panel_mappings[element_data["id"]]["output_tag"]
			dag_node_element["output_format"] = prompt_panel_mappings[element_data["id"]]["output_format"]
			dag_data.append(dag_node_element)
		elif element_data["type"] == "output":
			dag_node_element = {}
			dag_node_element["id"] = element_data["id"]
			dag_node_element["type"] = "output"
			dag_node_element["label"] = element_data["label"]
			dag_data.append(dag_node_element)
		else:
			dag_node_element = {}
			dag_node_element["id"] = "edge" + element_data["source"] + "-" + element_data["target"]
			dag_node_element["source"] = element_data["source"]
			dag_node_element["target"] = element_data["target"]
			dag_data.append(dag_node_element)

	backend_dag["dag_data"] = dag_data

	return backend_dag
