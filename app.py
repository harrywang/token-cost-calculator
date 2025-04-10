import gradio as gr
import tiktoken
from model_settings import (
    MODEL_SETTINGS, 
    get_available_models, 
    get_model_encoding, 
    get_input_price, 
    get_output_price, 
    get_compact_pricing_info
)

model = "gpt-4"  # default model

system_prompt = ""  # counts as user prompt for pricing
user_prompt = "tiktoken is great!"
assistant_response = "I agree!"

def get_cost(system_prompt, user_prompt, assistant_response, model):
    """Returns the cost of generating an assistant response."""
    encoding = tiktoken.get_encoding(get_model_encoding(model))
    
    # Get prices from model settings
    input_price = get_input_price(model)
    output_price = get_output_price(model)
    
    system_tokens = len(encoding.encode(system_prompt))
    user_tokens = len(encoding.encode(user_prompt))
    input_tokens = system_tokens + user_tokens
    output_tokens = len(encoding.encode(assistant_response))
    input_cost = input_tokens * input_price / 1000000
    output_cost = output_tokens * output_price / 1000000
    cost = input_cost + output_cost

    return system_tokens, user_tokens, output_tokens, f"${input_cost:.6f}", f"${output_cost:.6f}", f"${cost:.6f}"

# Define examples separately for clarity
example1 = [
    "You are an experienced email marketer", 
    "Create an email in between 50 to 125 words for a new product launch of a smartwatch.", 
    "Subject: Introducing Our Game-Changing Smartwatch!\n\nDear [Name],\n\nWe're thrilled to announce our latest innovation: the SmartLife Watch, designed to elevate your daily routine! With health tracking, connectivity, and an intuitive interface, it's more than a watch.\n\nExperience 24/7 heart monitoring, GPS, and water-resistance. SmartLife blends style with functionality.\n\nReady to transform your lifestyle? Click here to explore the SmartLife Watch today!\n\nRegards,\n[Your Name]", 
    "gpt-4"
]

example2 = [
    "", 
    "Who won NBA Championship in 2020?", 
    "The Los Angeles Lakers won the NBA Championship in 2020, defeating the Miami Heat in the Finals.", 
    "gpt-3.5-turbo"
]

example3 = [
    "You are a helpful AI assistant", 
    "Explain quantum computing in simple terms", 
    "Quantum computing is like having a super-powered calculator that can try many answers at once instead of one at a time. Normal computers use bits (0s and 1s), but quantum computers use 'qubits' that can be 0, 1, or both simultaneously - a bit like being in multiple places at once.", 
    "gpt-4o"
]

example4 = [
    "You are a coding assistant", 
    "Write a simple Python function to calculate the Fibonacci sequence", 
    "def fibonacci(n):\n    \"\"\"Generate Fibonacci sequence up to n terms.\"\"\"\n    fib_sequence = [0, 1]\n    \n    if n <= 0:\n        return []\n    elif n == 1:\n        return [0]\n    elif n == 2:\n        return fib_sequence\n    \n    for i in range(2, n):\n        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])\n    \n    return fib_sequence\n\nprint(fibonacci(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]", 
    "gpt-4o-mini"
]

example5 = [
    "You are a marketing expert", 
    "Create a brief target audience persona for Tesla Cybertruck", 
    "Target Audience: 'Tech-Forward Adventurer'\n\nDemographics: 30-45 years old, predominantly male, high income ($100k+), college educated\n\nPsychographics: Early tech adopters, environmentally conscious, values innovation and sustainability\n\nInterests: Cutting-edge technology, outdoor activities, renewable energy\n\nPain Points: Range anxiety, charging infrastructure, price point\n\nMedia: Heavy social media users, follows tech influencers, consumes tech and environmental news", 
    "gpt-o1"
]

# Create the Gradio interface
demo = gr.Interface(
    get_cost,
    title="OpenAI API Token and Cost Calculator",
    inputs=[
        gr.TextArea(label="System Prompt", lines=4), 
        gr.TextArea(label="User Message", lines=5), 
        gr.TextArea(label="Assistant Response", lines=6), 
        gr.Dropdown(
            choices=get_available_models(),
            label="Model",
            value="gpt-4",
            info=get_compact_pricing_info()
        )
    ],
    outputs=[
        gr.Textbox(label="System Prompt Tokens"),
        gr.Textbox(label="User Message Tokens"), 
        gr.Textbox(label="Output Tokens (Assistant Response Tokens)"), 
        gr.Textbox(label="Input Cost (System + User)"), 
        gr.Textbox(label="Output Cost (Assistant)"), 
        gr.Textbox(label="Total Cost") 
    ],
    examples=[example1, example2, example3, example4, example5]
)

# Launch the app
demo.launch()
