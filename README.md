# Prompt Studio

Inspiration
A lot of existing businesses use LLM to make their systems better. But there does not exist an easy way for version controlling prompt engineering. Prompt Studio helps in bridging the gap and making it easy to do prompt engineering

What it does
Prompt Studio is a versioning tool to aid in prompt engineering. It helps in trying out various flows, specify input and output and type check the output. It lets a user focus on the solution rather than coding. It also allows the user to test multiple flows, download the code for the finalized flow and even publish the api endpoint.

How we built it
Langchain and OpenAI are the main components. The backend is developed using Flask and Python programming language. Frontend is developed using Vue

Challenges we ran into
Challenges we ran into – Handling complex flows. These are directed acyclic graphs with multiple inputs, prompts and then finally leading to one prompt. This required maintaining the state of nodes, prompt details and topological sorting to process the nodes in the required order.

Accomplishments that we're proud of
Developing a unique idea - version controlling for prompt engineering. Having a working model of the problem.

What we learned
Langchain and its capabilities, OpenAI apis. Multiple learning from projects that other teams were working on. Great workshops held by sponsors and founders throughout the workshop has been very insightful.

What's next for Prompt Studio
Data validation, Performance metrics, Test suites

