"""
OpenAI API model settings and pricing information.
Last updated: April 2025
"""

# Model settings dictionary with pricing information
# Prices in USD per 1M tokens
MODEL_SETTINGS = {
    "gpt-3.5-turbo": {
        "encoding": "cl100k_base",
        "input_price": 0.5,
        "output_price": 1.5,
        "description": "Fast and cost-effective for everyday tasks"
    },
    "gpt-4": {
        "encoding": "cl100k_base",
        "input_price": 30.0,
        "output_price": 60.0,
        "description": "Advanced reasoning capabilities"
    },
    "gpt-4-turbo": {
        "encoding": "cl100k_base",
        "input_price": 30.0,
        "output_price": 60.0,
        "description": "Faster version of GPT-4"
    },
    "gpt-4o": {
        "encoding": "cl100k_base",
        "input_price": 5.0,
        "output_price": 15.0,
        "description": "Optimized for better performance and efficiency"
    },
    "gpt-4o-mini": {
        "encoding": "cl100k_base",
        "input_price": 0.15,
        "output_price": 0.6,
        "description": "Smaller, faster version of GPT-4o"
    },
    "gpt-o1": {
        "encoding": "cl100k_base",
        "input_price": 15.0,
        "output_price": 75.0,
        "description": "Specialized for complex reasoning tasks"
    },
    "gpt-4.5": {
        "encoding": "cl100k_base",
        "input_price": 60.0,
        "output_price": 120.0,
        "description": "Next generation model with enhanced capabilities"
    }
}

# Get list of available models
def get_available_models():
    """Returns a list of available model names."""
    return list(MODEL_SETTINGS.keys())

# Get model pricing info
def get_model_pricing_info():
    """Returns a formatted string with pricing information for all models."""
    info = "Pricing (per 1M tokens):\n"
    for model, settings in MODEL_SETTINGS.items():
        info += f"{model}: input ${settings['input_price']}, output ${settings['output_price']}\n"
    return info

# Get model encoding
def get_model_encoding(model):
    """Returns the encoding for the specified model."""
    if model in MODEL_SETTINGS:
        return MODEL_SETTINGS[model]["encoding"]
    return "cl100k_base"  # default encoding

# Get model input price
def get_input_price(model):
    """Returns the input price for the specified model."""
    if model in MODEL_SETTINGS:
        return MODEL_SETTINGS[model]["input_price"]
    return 30.0  # default to GPT-4 pricing

# Get model output price
def get_output_price(model):
    """Returns the output price for the specified model."""
    if model in MODEL_SETTINGS:
        return MODEL_SETTINGS[model]["output_price"]
    return 60.0  # default to GPT-4 pricing

# Get compact pricing info for UI
def get_compact_pricing_info():
    """Returns a compact pricing info string for the UI."""
    info = "Pricing (per 1M tokens): "
    models = ["gpt-3.5-turbo", "gpt-4o-mini", "gpt-4o", "gpt-4", "gpt-o1", "gpt-4.5"]
    model_info = []
    
    for model in models:
        if model in MODEL_SETTINGS:
            settings = MODEL_SETTINGS[model]
            model_info.append(f"{model}: ${settings['input_price']}/{settings['output_price']}")
    
    return info + " | ".join(model_info)
