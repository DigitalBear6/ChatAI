import openai

def ai_get(prompt = "Hello, how are you today?"):
    # Set up the OpenAI API client
    openai.api_key = "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"

    # Set up the model and prompt
    model_engine = "text-davinci-003"

    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    response = completion.choices[0].text
    return response
    

if __name__ == "__main__":
    prompt = input("What's your question?")
    print(ai_get(prompt))