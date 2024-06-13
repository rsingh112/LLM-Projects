
# Text To SQL Based on Google Gemini LLM Project

This is an end to end LLM project based on Google Gemini. We have used a free dataset free from Tableau and build a Q&A system where you can ask questions in natural language realted to nature of data and the model internally convert the natural language to sql query and fetch result from backend database. We have used streamlit for user interface for students where you can ask questions and get answers. 


## Project Highlights

- Use a dummy data from Tableau dummmy dataset, which is Sample Super Store. 
- We will build an LLM based question and answer system related to same dataset.
- Google Gemini will convert the natural language code to sql and fetch the result

## You will learn following,
  - Google Gemini: LLM based Q&A
  - Streamlit: UI


## Sample Questions
  - What is my total profit?
  - How many orders I have sold for East?
  - Tell me top 5 product which contributes to my maximum profit and show the product name only?
  - Who is the top 2 customer based on revenue?

## Project Structure

- main.py: The main Streamlit application script.
- SuperStoreModelLLM.py: This has all the langchain code
- requirements.txt: A list of required Python packages for the project.
- .env: Configuration file for storing your Google API key.