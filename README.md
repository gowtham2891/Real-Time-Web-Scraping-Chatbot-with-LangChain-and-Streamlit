# Real-Time Web Scraping Chatbot with LangChain and Streamlit

## Project Overview

This project showcases a sophisticated chatbot capable of performing real-time web scraping and answering user queries based on the scraped data. The implementation leverages OpenAI's GPT-4o model, integrated with LangChain for workflow management and Streamlit for an interactive user interface. Users can input URLs to scrape, and the chatbot processes the data to respond accurately to user questions.

## Features

- **Real-Time Web Scraping:** Users can input URLs, and the chatbot scrapes the web pages in real-time to extract relevant data.
- **Query Response:** The chatbot utilizes the scraped data to answer user queries accurately and contextually.
- **LangChain Integration:** Manages the structured workflow for data processing and response generation.
- **Streamlit Interface:** Provides a user-friendly web interface for inputting URLs and querying the chatbot.

## Key Achievements

- Developed a robust system for real-time web scraping and querying.
- Utilized LangChain to coordinate the interaction between web scraping, data processing, and the OpenAI GPT-4o model.
- Created an intuitive user interface with Streamlit, allowing users to easily input URLs and receive responses to their queries.

## Project Workflow

1. **User Input:**
   - Users input a URL into the Streamlit interface.

2. **Real-Time Web Scraping:**
   - The system scrapes the provided URL to extract relevant data using `WebBaseLoader`.

3. **LangChain Core Integration:**
   - The scraped data is processed using LangChain, setting up a prompt template and connecting it with the OpenAI GPT-4o model.

4. **User Query:**
   - Users can ask questions about the scraped data, and the chatbot generates accurate responses using the processed data.

## Usage

1. **Install Dependencies:**
   - Ensure all necessary dependencies are installed. Use a `requirements.txt` file to manage dependencies and install them using:
     ```sh
     pip install -r requirements.txt
     ```

2. **Set Up Environment Variables:**
   - Create a `.env` file with the necessary environment variables, such as your OpenAI API key:
     ```sh
     OPENAI_API_KEY=your_api_key_here
     ```

3. **Run the Streamlit App:**
   - Execute the Streamlit application to start interacting with the chatbot:
     ```sh
     streamlit run app.py
     ```

4. **Interact with the Chatbot:**
   - Open the Streamlit app in your browser, input a URL to scrape, and ask questions about the scraped data.

## Technologies Used

- **LangChain:** For defining the prompt template and managing workflow.
- **OpenAI GPT-4o:** The language model used for generating responses.
- **Streamlit:** For creating an interactive web interface.
- **FAISS:** For efficient similarity search and retrieval of high-dimensional data.
- **dotenv:** For managing environment variables securely.

## Contact

For any questions or suggestions, please contact [gowthamdupati28@gmail.com](gowthamdupati28@gmail.com).
