import os, sys
from dotenv import load_dotenv
from google import genai 


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
user_input = sys.argv[1]


def main():
    print("Hello from cliagent!")
    response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=user_input
    )
    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}\nResponse tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
