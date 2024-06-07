
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def mental_health_assistant(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Example usage
if __name__ == "__main__":
    user_input = "I am feeling very stressed and anxious."
    print(mental_health_assistant(user_input))
