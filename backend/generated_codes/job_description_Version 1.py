import sys
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

apikey = sys.argv[1]

def generate_openai_output(prompt, input_dict, input_tags, apikey):
	prompt_tempt = PromptTemplate.from_template(prompt)
	filtered_dict = {key: input_dict[key] for key in input_tags}
	final_prompt = prompt_tempt.format(**filtered_dict)
	llm = OpenAI(openai_api_key=apikey)
	output = llm.predict(final_prompt)
	return output

JD= "Our client is an elite institution located in the heart of Hong Kong, renowned for its unparalleled commitment to excellence and innovation.\n\nThey are seeking a talented and motivated Data Scientist to join our dynamic team! As a Data Scientist, you will play a critical role in analyzing complex data sets and providing valuable insights to help drive our business forward. You will work closely with cross-functional teams to identify and solve real-world problems, leveraging your expertise in statistical modeling, data mining, and machine learning.\n\nResponsibilities:\nAnalyze and interpret complex data sets, identifying patterns and trends to inform business decisions\nDesign, build, and deploy predictive models using machine learning algorithms\nDevelop and maintain data pipelines, ensuring accuracy and efficiency of data ingestion and processing\nCollaborate with cross-functional teams to identify opportunities for process improvement and optimization\nCommunicate findings and recommendations to stakeholders in a clear and concise manner\n\nRequirements:\nBachelor's or advanced degree in a quantitative field (e.g. Statistics, Mathematics, Computer Science)\n3+ years of experience in data science, with expertise in statistical modeling, data mining, and machine learning\nProficiency in programming languages such as Python, R, and SQL\nExperience with data visualization tools such as Tableau or PowerBI\nExperience with Oracale Cloud is a BIG plus\nStrong problem-solving skills and ability to work independently and in a team environment\nExcellent communication skills, with the ability to communicate complex findings to both technical and non-technical stakeholders\n\nThey offer a competitive salary, comprehensive benefits package, and a supportive work environment that values collaboration, creativity, and innovation. If you are passionate about using data to drive business decisions and want to be part of a dynamic and growing team, we encourage you to apply for this exciting opportunity!\n"

input_dict = {}
prompt = "Extract top 10 skills from Job description and return the result in a csv format.\nThe result should only contain csv format"
input_dict["JD"] = JD
input_tags = ["JD"]
output1= generate_openai_output(prompt, input_dict, input_tags, apikey)

print(output1)
