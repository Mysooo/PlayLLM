import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
import json
import re
import ast

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize Gemini model
model = genai.GenerativeModel('gemini-2.0-flash')

# Streamlit UI setup
st.set_page_config(page_title="Playwright Automation Generator", layout="centered")
st.markdown(
    """
    <style>
    body {
        background-color: #540D6E;
        color: white;
    }
    .stTextArea textarea {
        background-color: #540D6E;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Playwright Automation Script Generator 🎭")

# Inputs for page name and flow name
page_name = st.text_input("Enter Page Name (e.g., LoginPage):")
flow_name = st.text_input("Enter Flow Name (e.g., loginFlow):")
uploaded_file = st.file_uploader("Upload your actions.txt file", type="txt")

if uploaded_file and page_name and flow_name:
    file_content = uploaded_file.read().decode("utf-8")
    
    try:
        # Extract the [ ... ] list
        match = re.search(r'\[.*?\]', file_content, re.DOTALL)
        if not match:
            raise ValueError("Could not find actions list in file.")
        
        actions_list_text = match.group(0)
        actions = ast.literal_eval(actions_list_text)

        actions_input = {
            "actions": actions
        }

        prompt = f"""
        You are a Playwright automation script generator. Based on the following list of actions, generate the corresponding Playwright code.

        Actions and Locators:
        {json.dumps(actions_input, indent=4)}

        Page Class Name: {page_name}
        Flow Function Name: {flow_name}

        Generate the Playwright code in JavaScript with the following format:

        class {page_name} {{
            constructor(page) {{
                this.page = page;
                // Define locators like:
                // this.elementName = page.getByTestId('test-id');
            }}

            async {flow_name}() {{
                // Use the locators defined in constructor
            }}
        }}

        Do not include triple backticks or extra explanation. Only the class code.
        """

        with st.spinner("Generating Playwright code..."):
            response = model.generate_content(prompt)

        generated_code = response.text.strip()

        # Remove triple backticks if present
        if generated_code.startswith("```") and generated_code.endswith("```"):
            generated_code = re.sub(r"^```(?:\w+)?\n|\n```$", "", generated_code).strip()

        # Show code with copy button
        st.code(generated_code, language='javascript')

    except Exception as e:
        st.error(f"Failed to parse file. Error: {e}")
elif uploaded_file:
    st.warning("Please enter both Page Name and Flow Name.")
