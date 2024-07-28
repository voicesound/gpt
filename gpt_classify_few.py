#Few-shot classification involves providing the model with a few examples to learn from.
##prompt안에다가 예시를 넣어주는거네 그냥

import openai

# Set up the OpenAI API key
openai.api_key = 'your-api-key'

def classify_symptom_few_shot(text):
    prompt = f"""
    Classify the following symptoms of an autistic child into the categories provided.

    Categories:
    - Social Communication Issues
    - Repetitive Behaviors
    - Sensory Sensitivities
    - Cognitive Challenges

    Examples:
    1. Symptom: "The child has difficulty making eye contact and often avoids social interactions."
       Category: Social Communication Issues
    2. Symptom: "The child frequently flaps their hands and rocks back and forth."
       Category: Repetitive Behaviors
    3. Symptom: "The child is extremely sensitive to loud noises and certain textures."
       Category: Sensory Sensitivities
    4. Symptom: "The child struggles with problem-solving and understanding abstract concepts."
       Category: Cognitive Challenges

    Now classify the following symptom:
    Symptom: "{text}"
    Category:
    """

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=10,
        temperature=0.0,
        top_p=1.0,
        n=1,
        stop=["\n"]
    )

    return response.choices[0].text.strip()

# Example usage
symptom_description = "The child avoids eye contact and prefers to play alone."
category = classify_symptom_few_shot(symptom_description)
print(f"Symptom: {symptom_description}\nCategory: {category}")
