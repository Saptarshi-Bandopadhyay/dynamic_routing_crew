# Math_job_crew

This is a project consisting of three crews which perform the following operation - 
1. Prompt Analysing - This analyses the prompt and routes it to the specific crew
2. Math Operations - This performs mathematical operation based on a given prompt
3. Job Description Generation - This provides a job description based on a given prompt which describes the company, their needs, benefits that they will provide etc.

The prompts are sent through a post request to a REST API made using Flask.

## Usage

1. Clone the repo

2. Install dependencies
 ```
 pip install -r requirements
 ```
3. Install ollama and pull llama3
```
curl -fsSL https://ollama.com/install.sh | sh
```
```
ollama serve
```
```
ollama pull llama3
```
4. Set the env variables for SerperDevTool and OpenAI
```
env SERPER_API_KEY="your_api_key"
```
```
env OPENAI_API_KEY="your_api_key"
```
5. Run
```
python app.py
```
6. Test the API
```
curl -X POST http://127.0.0.1:5000/route_prompt -H "Content-Type: application/json" -d '{"prompt": "3+4"}'
```

## Output

For different prompts, different outputs can be observed - 
1. For a mathematical prompt the resultant output is sent back.
2. For a job description prompt the resultant job description is stored in the 'job_posting.md' file.
3. For a prompt that is neither of the above, an error message is sent back.