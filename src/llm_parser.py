import anthropic
import json
import os
from dotenv import load_dotenv

load_dotenv()

def parse_cad_command(user_input):
    """
    Takes a plain English CAD command from the user,
    sends it to Claude, and returns structured data.
    """
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    system_prompt = """
    You are a CAD assistant that converts plain English descriptions into structured data.
    
    When the user describes a shape, respond with ONLY a valid JSON object.
    No explanation, no extra text, just the JSON.
    
    For a cylinder use this format:
    {
        "shape": "cylinder",
        "diameter": 0.05,
        "height": 0.1
    }
    
    For a box use this format:
    {
        "shape": "box",
        "width": 0.1,
        "depth": 0.1,
        "height": 0.05
    }
    
    Always convert millimeters to meters.
    Always use lowercase for shape names.
    """

    response = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=256,
        system=system_prompt,
        messages=[
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    raw_text = response.content[0].text
    raw_text = raw_text.strip().removeprefix("```json").removesuffix("```").strip()

    try:
        cad_data = json.loads(raw_text)
        print(f"Parsed command: {cad_data}")
        return cad_data
    except json.JSONDecodeError:
        print(f"Claude returned unexpected format: {raw_text}")
        return None


if __name__ == "__main__":
    test = parse_cad_command("make a cylinder 50mm wide and 100mm tall")
    print(test)