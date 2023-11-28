import openai

# Read the API key from the "key.txt" file
with open("key.txt", "r") as file:
    api_key = file.read().strip()

# Set up the OpenAI API client
openai.api_key = api_key

# Define a function to generate a response from the chatbot
def generate_response(prompt):

    completion = openai.ChatCompletion.create( # Change the function Completion to ChatCompletion
    model = 'gpt-3.5-turbo',
    messages = [ # Change the prompt parameter to the messages parameter
    {'role': 'user', 'content': prompt}
    ],
    temperature = 0  
    )
    return completion.choices[0].message.content.strip()

# Example usage
user_input = input("User: ")
while user_input.lower() != "exit":
    prompt = f"User: {user_input}\nChatbot:"
    response = generate_response(prompt)
    print(response)
    user_input = input("User: ")

