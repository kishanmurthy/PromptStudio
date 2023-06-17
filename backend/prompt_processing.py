from open_api_calls import generate_openai_output

def prompt_process(node_input, node_dict, tp_sort):
    input_dicts = {}
    for input in node_input:
        input_dicts[input] = node_input[input]
    
    for node_id in tp_sort:
        node = node_dict[node_id]
        if node.node_type == "prompt":
            input_tags = []
            for node_incoming in node.node_incomings:
                input_tags.append(node_dict[node_incoming].node_output_tag)
            node_prompt = node.node_prompt

            for input_tag in input_tags:
                node_prompt = node_prompt.replace(input_tag, input_dicts[input_tag])
            
            node_output_tag = node.node_output_tag
            node_output_format = node.node_output_format
            prompt_output = generate_openai_output(node_prompt, node_output_format)
            input_dicts[node_output_tag] = prompt_output


    all_output_dict = {}
    for node_id in tp_sort:
        node = node_dict[node_id]
        if node.node_type == "output":
            for node_incoming in node.node_incomings:
                all_output_dict[node_dict[node_incoming].node_output_tag] = input_dicts[node_dict[node_incoming].node_output_tag]

    return all_output_dict

        