import openai, os, logging, base64
from openai import OpenAI


def generate_openai_completion(user_prompt, question):
    openai_client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
    )
    
    response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": user_prompt},
            {"role": "user", "content": question},
        ]
    )

    return response.choices[0].message.content

def openai_image_description(image_path, image_data):

    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Describe this image and also mention in which sector the things visible in the image are used: "},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_data}"}}
                ]
            }
        ],
        max_tokens=200,
    )

    caption = response.choices[0].message.content.strip()
    return caption


def openai_api_request(prompt, model="gpt-4o", temperature=0.7, max_tokens=2000, n=1):
    """
    Sends a request to the specified OpenAI model and returns the response.

    Parameters:
        prompt (str): The input prompt for the model.
        model (str): The model to use (default is "gpt-4o").
        temperature (float): Sampling temperature for response variability.
        max_tokens (int): Maximum number of tokens in the response.
        n (int): Number of completions to generate.

    Returns:
        str: The model's response.
    """    
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("OpenAI API key not found. Set the OPENAI_API_KEY environment variable.")

    try:
        client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "Use the available knowledge to generate a coherent and factual text. Ensure that the text does not contain bullet points, does not exhibit hallucinations, and is direct, covering all key aspects."},
                {"role": "user", "content": prompt}
            ],
        )
        if response and response.choices:
            return response.choices[0].message.content.strip()
        else:
            logging.info("No response received from the API.")
            return None
    except Exception as e:
        logging.info(f"An error occurred: {e}")
        return None

def get_openai_response_as_text(company, sector):
    """
    Composes questions based on the provided sector, sends them to GPT-4o, 
    and combines the responses into a single, structured text.
    """
    # Compose questions based on the sector
    if sector.lower() in ['slaughterhouse', 'butchery']:
        questions = [
            "What are the biggest lubrication issues in a pig slaughterhouse?",
            "Which machines are most common in this specific sector, give machine numbers in return?",
            "Which Interflon products can I use to lubricate each of these machines?"
        ]
    else:
        # For other sectors, generate a general question
        questions = [
            f"Provide the most important information about the operations and challenges in the {company} sector."
        ]
    
    # Combine questions into a single prompt
    combined_prompt = f"""[INST] <<SYS>>
                        Use the available knowledge to generate a detailed, coherent, and factual text addressing all the following questions. Ensure that the text is structured in full paragraphs without bullet points, remains accurate, and comprehensively covers the key aspects of the topic.
                        <</SYS>>

                        Questions:
                        {chr(10).join(questions)}

                        Answer:"""

    # Send the prompt and get a single combined response
    return openai_api_request(combined_prompt, model="gpt-4o")