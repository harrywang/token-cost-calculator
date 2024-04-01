import gradio as gr
import tiktoken

model = "gpt-4"  # gpt-3.5-turbo

# same encoding for both models
# "gpt-4": "cl100k_base",
# "gpt-3.5-turbo": "cl100k_base",

# pricing: https://openai.com/pricing
# GPT 3.5 Turbo: $0.50 / 1M tokens	$1.50 / 1M tokens
# GPT 4 turbo: $10 / 1M tokens	$30 / 1M tokens

system_prompt = ""  # counts as user prompt for pricing
user_prompt = "tiktoken is great!"
assistant_response = "I agree!"

def get_cost(system_prompt, user_prompt, assistant_response, model):

    """Returns the cost of generating an assistant response."""
    encoding = tiktoken.get_encoding("cl100k_base")  # same encoding for both models

    # default prices
    if model == "gpt-3.5-turbo":
        input_price = 0.5
        output_price = 1.5
    else:
        input_price = 10
        output_price = 30
    
    system_tokens = len(encoding.encode(system_prompt))
    user_tokens = len(encoding.encode(user_prompt))
    input_tokens = system_tokens + user_tokens
    output_tokens = len(encoding.encode(assistant_response))
    input_cost = input_tokens * input_price / 1000000
    output_cost = output_tokens * output_price / 1000000
    cost = input_cost + output_cost

    return system_tokens, user_tokens, output_tokens, f"${input_cost:.6f}", f"${output_cost:.6f}", f"${cost:.6f}"

demo = gr.Interface(
    get_cost,
    title="OpenAI API Token and Cost Calculator",
    inputs=[
            gr.TextArea(label="System Prompt", lines=4), 
            gr.TextArea(label="User Message", lines=5), 
            gr.TextArea(label="Assistant Response", lines=6), 
            gr.Dropdown(
                choices=["gpt-4-turbo", "gpt-3.5-turbo"],
                label="Model",
                value=["gpt-4", "gpt-3.5-turbo"],
                info="Pricing: GPT 3.5 Turbo: input $0.5 / 1M tokens, output $1.5 / 1M tokens | GPT 4 turbo: input $10 / 1M tokens, output $30 / 1M tokens"
            ), 
   ],
    outputs=[
        gr.Textbox(label="System Prompt Tokens"),
        gr.Textbox(label="User Message Tokens"), 
        gr.Textbox(label="Output Tokens (Assistant Response Tokens)"), 
        gr.Textbox(label="Input Cost (System + User)"), 
        gr.Textbox(label="Output Cost (Assistant)"), 
        gr.Textbox(label="Total Cost"), 
    ],
    examples=[
        [
            "You are an experienced email marketer", 
            "Create an email in between 50 to 125 words for a new product launch of a smartwatch. The email should be engaging and informative, highlighting the key features and benefits of the product. Include a clear call-to-action to encourage recipients to visit the product page and make a purchase.", 
            """
            Subject: Introducing Our Game-Changing Smartwatch: Transform Your Lifestyle!

            Dear [Recipient's Name],

            We're thrilled to announce the launch of our latest innovation: the [Product Name] Smartwatch, designed to elevate your daily routine! Featuring cutting-edge health tracking, seamless connectivity, and an intuitive interface, it's more than just a watch; it's your fitness coach, assistant, and much more.

            Experience unparalleled convenience with 24/7 heart rate monitoring, GPS navigation, and water-resistant capabilities. The [Product Name] seamlessly blends style with functionality, ensuring you stay ahead of the curve.

            Ready to revolutionize your lifestyle? Click [here] to explore the [Product Name] Smartwatch and embrace the future today. Don't miss out on making every moment count!

            Warm regards,

            [Your Name]
            [Your Company]
            """, 
            "gpt-4-turbo",
        ],
        [
            "", 
            "Who won NBA Championship in 2020?", 
            "The winner of the NBA Championship in 2023 was the Golden State Warriors.", 
            "gpt-4-turbo",
        ],
        [
            "You are an experienced digital marketer with 10 years of industry experience.", 
            "Please provide a comprehensive target audience persona for a digital marketer selling Tesla Cybertruck. Include the following information: Demographics, Geographic location, Psychographics, Professional Background, Pain Points and challenges, Goals and aspirations, Shopping habits and preferences, Media consumption, Influencers and decision-makers, Brand perceptions and preferences. Assume no prior audience data is available, and base the persona on general market trends and consumer behavior for this type of product. At the end, give me suggestions for different niches to target to best sell this product.", 
            """Creating a comprehensive target audience persona for marketing the Tesla Cybertruck requires a deep understanding of the product's unique selling propositions, such as its futuristic design, electric powertrain, and advanced technology features. This analysis also involves aligning the product's characteristics with the lifestyle, values, and needs of potential customers. Below is a persona that encapsulates these aspects, followed by suggestions for niches to target.

            ### Target Audience Persona: "Eco-Driven Innovator"

            #### Demographics:
            - **Age**: 30-45 years old
            - **Gender**: Predominantly male, but with a significant and growing interest from females
            - **Income Level**: High-income earners, with an annual income of $100,000+
            - **Family Status**: Both singles and those with families, but likely to have fewer children
            - **Education**: College-educated, often with a degree in technology, engineering, business, or environmental sciences

            #### Geographic Location:
            - **Urban and Suburban Areas**: With a focus on regions with established or rapidly growing EV infrastructure, such as California, New York, and Texas in the United States
            - **Tech-savvy Regions**: Areas with a high concentration of technology companies and workers

            #### Psychographics:
            - **Values**: Sustainability, innovation, and technology
            - **Lifestyle**: Early adopters of technology, environmentally conscious, and interested in products that make a statement
            - **Interests**: Renewable energy, cutting-edge technology, automotive advancements, and outdoor activities

            #### Professional Background:
            - **Sectors**: Technology, engineering, renewable energy, startup environments, or high-level positions in various industries
            - **Roles**: Managers, engineers, entrepreneurs, IT professionals, and environmental scientists

            #### Pain Points and Challenges:
            - **Range Anxiety**: Concern about the distance the Cybertruck can travel on a single charge compared to gas-powered alternatives
            - **Charging Infrastructure**: Availability of charging stations for long trips
            - **Price Point**: Affordability for those interested in transitioning to electric vehicles
            - **Perception**: Overcoming skepticism towards the unconventional design and new technology

            #### Goals and Aspirations:
            - To be seen as a leader in adopting sustainable and innovative technologies
            - To contribute to environmental conservation
            - To own a versatile vehicle that combines performance, technology, and utility

            #### Shopping Habits and Preferences:
            - **Research-Oriented**: Uses online platforms to extensively research before making a purchase
            - **Brand Loyalty**: High loyalty to brands that align with their values, especially in technology and sustainability
            - **Quality and Sustainability**: Prefers products that are durable, high-quality, and have a minimal environmental impact

            #### Media Consumption:
            - **Digital Platforms**: Heavy users of social media (LinkedIn, Twitter, YouTube), tech and environmental blogs, podcasts, and forums
            - **News Sources**: Prefers tech and environmentally focused news outlets
            - **Influencers**: Follows thought leaders in technology, environmental activism, and automotive industries

            #### Influencers and Decision-Makers:
            - **Peers**: Colleagues and friends in the tech and environmental sectors
            - **Online Communities**: Forums and social media groups focused on EVs, technology, and sustainability
            - **Reviews and Testimonials**: Highly influenced by expert reviews and user testimonials

            #### Brand Perceptions and Preferences:
            - Views Tesla as a leader in innovation, sustainability, and high-performance electric vehicles
            - Prefers brands that are transparent about their environmental impact and actively work towards reducing it

            ### Suggestions for Niches to Target:

            1. **Technology Enthusiasts**: Individuals who are passionate about the latest tech trends and innovations. Marketing strategies can focus on the Cybertruck's advanced features, such as Autopilot, and its futuristic design.

            2. **Environmental Advocates**: People who prioritize sustainability and are looking for ways to reduce their carbon footprint. Highlight the Cybertruck's electric powertrain and Tesla's commitment to renewable energy.

            3. **Outdoor and Adventure Seekers**: Those who enjoy outdoor activities and require a vehicle that supports their lifestyle. Emphasize the Cybertruck's utility, off-road capabilities, and storage options.

            4. **Luxury Vehicle Owners**: Individuals interested in luxury and high-performance vehicles but are also eco-conscious. Position the Cybertruck as a status symbol that also aligns with environmental values.

            5. **Fleet Operators and Businesses**: Companies looking to green their fleet or those in industries requiring versatile and durable vehicles. Highlight the total cost of ownership, durability, and the environmental benefits of switching to electric vehicles.

            By targeting these niches with tailored messaging that addresses their specific interests and concerns, a digital marketer can effectively reach potential customers likely to be interested in the Tesla Cybertruck.
            
            """,
            "gpt-4-turbo",
        ],
    ]
)

demo.launch()