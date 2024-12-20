import nltk
from nltk.chat.util import Chat, reflections

# Define conversation pairs (patterns and responses)
pairs = [
    (r"hi|hello|hey", ["Hello! How can I assist you today?"]),
    (r"what is your name?", ["I am a chatbot created using NLTK!"]),
    (r"how are you?", ["I'm just a bot, but I'm doing great! How about you?"]),
    (r"quit", ["Goodbye! It was nice chatting with you."]),
    (r"(.*) your favorite (.*)?", ["I don't have preferences, but I love helping people!"]),
    (r"can you help me with (.*)?", ["Of course! I'm here to assist with anything you need."]),
    (r"(.*)", ["I'm sorry, I didn't quite understand that. Can you ask something else?"])
]

# Create the chatbot with the defined pairs and reflections
chatbot = Chat(pairs, reflections)

# Function to start the chat with the user
def chat():
    print("Hello! Type 'quit' to exit.")
    while True:
        # User input
        user_input = input("You: ")
        
        # Check for quit command to end the chat
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        
        # Get response from chatbot
        response = chatbot.respond(user_input)
        
        # Print chatbot response
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chat()
