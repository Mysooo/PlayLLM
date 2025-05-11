# Playwright Automation Script Generator Documentation
## Project Overview
This project provides a Streamlit application that generates Playwright automation scripts using the Gemini 2.0 Flash model. It takes a list of actions and locators as input and outputs JavaScript code for a Playwright page class and flow function.
**Key Features:**
*   Generates Playwright code from a list of actions.
*   Uses Google's Gemini 2.0 Flash model for code generation.
*   Provides a user-friendly Streamlit interface.
*   Supports uploading actions from a text file.
**Requirements:**
*   Python 3.6+
*   Streamlit
*   google-generativeai
*   python-dotenv
*   A Google Cloud project with the Gemini API enabled and an API key.
## Getting Started
### Installation
1.  **Clone the repository (if applicable):**  This step is not applicable as the codebase is provided as a single file.
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    
3.  **Set up environment variables:**
    *   Create a `.env` file in the project directory.
    *   Add your Google API key to the `.env` file:
                GOOGLE_API_KEY=YOUR_API_KEY
        ```
        
        Replace `YOUR_API_KEY` with your actual Google API key.
### Running the Application
1.  **Run the Streamlit application:**
    ```bash
    streamlit run playLLM.py
    ```
    
    This will start the Streamlit server and open the application in your web browser.
## Code Structure
The project consists of the following files:
*   `playLLM.py`: The main Streamlit application file.
*   `requirements.txt`: Lists the project dependencies.
*   `.gitignore`: Specifies intentionally untracked files that Git should ignore.
*   `.devcontainer/devcontainer.json`: Configuration file for VS Code Dev Containers.
### Key Components
*   **`playLLM.py`:**
    *   Imports necessary libraries (Streamlit, google-generativeai, dotenv, os, json, re, ast).
    *   Loads environment variables and configures the Gemini model.
    *   Sets up the Streamlit UI with input fields for page name, flow name, and actions file upload.
    *   Reads the actions file, extracts the actions list, and generates a prompt for the Gemini model.
    *   Calls the Gemini model to generate Playwright code.
    *   Displays the generated code in a code block with a copy button.
    *   Handles errors and provides informative messages to the user.
## FAQ
**Q: I'm getting an error that the Google API key is missing.**
A: Make sure you have created a `.env` file in the project directory and added your Google API key to it as `GOOGLE_API_KEY=YOUR_API_KEY`. Also, ensure that you have loaded the environment variables using `load_dotenv()`.
**Q: The generated code is not valid JavaScript.**
A: The quality of the generated code depends on the clarity and completeness of the actions list provided in the input file.  Ensure that the actions and locators are well-defined.  The model may also require some manual adjustments to the generated code.
**Q: The application is not running.**
A: Make sure you have installed all the required dependencies using `pip install -r requirements.txt`. Also, check the Streamlit console for any error messages.
**Q: How do I format the actions.txt file?**
A: The `actions.txt` file should contain a Python list of dictionaries, where each dictionary represents an action and its associated locators. The application extracts the list using regular expressions and `ast.literal_eval`. Example:
```text
[
    {"action": "click", "locator": "#login-button"},
    {"action": "type", "locator": "#username", "value": "testuser"},
    {"action": "type", "locator": "#password", "value": "password123"},
    {"action": "click", "locator": "#submit-button"}
]
```
**Q: The application is not displaying correctly.**
A: Ensure that your browser supports modern JavaScript features. Try clearing your browser cache or using a different browser.
