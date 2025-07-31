import os
import json
import math
import chainlit as cl
import google.generativeai as genai
import dotenv

dotenv.load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_KEY"))

try:
    with open("products.json") as f:
        catalog = json.load(f)
except Exception as e:
    catalog = []
    print(f"Failed to load products.json: {e}")

def format_catalog(items):
    lines = [f"- {p['name']} ({p['type']}): {p['price']}, use: {p['use']}" for p in items]
    return "\n".join(lines)

@cl.on_message
async def handler(msg: cl.Message):
    user_input = msg.content.strip()
    text = user_input.lower()

    if any(word in text for word in ['gallon', 'how many']):
        dims = [int(x) for x in text.split() if x.isdigit()]
        if len(dims) >= 3:
            length, width, height = dims[:3]
            area = 2 * (length + width) * height
            needed = math.ceil(area / 350)
            await cl.Message(content=f"You will need about {needed} gallon(s) of paint to cover a {length}x{width} room with {height} ft walls.").send()
            return

    model = genai.GenerativeModel("gemini-2.0-flash")
    catalog_text = format_catalog(catalog)

    prompt = (
        "You are a helpful hardware store assistant. Use the following product catalog to answer customer queries.\n"
        "If the user asks for painting advice or product recommendations, refer to the catalog when possible.\n\n"
        f"Catalog:\n{catalog_text}\n\n"
        f"User: {user_input}\nAssistant:"
    )

    try:
        response = model.generate_content(prompt)
        await cl.Message(content=response.text.strip()).send()
    except Exception as e:
        await cl.Message(content=f"Sorry, I had trouble processing that: {e}").send()
