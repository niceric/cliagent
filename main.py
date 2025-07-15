import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
user_input = sys.argv


def main():
    print("Hello from cliagent!")
    if len(user_input) == 1:
        sys.exit()
        
    

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_input[1])])
    ]
    response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=messages
    )
    print(response.text)
    if len(user_input) > 2:
        if user_input[2] == "--verbose":
            print(f"User prompt: {user_input[1]}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}\nResponse tokens: {response.usage_metadata.candidates_token_count}")
        else:
            return 
if __name__ == "__main__":
    main()
