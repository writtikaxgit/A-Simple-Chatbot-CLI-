import time

def chatbot():
    print("Chatbot: Hello! I'm ChatSimple. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()

        # Exit condition
        if user_input in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a great day! 👋")
            break

        # Greetings
        elif user_input in ["hi", "hello", "hey"]:
            print("Chatbot: Hello there! How can I help you today?")

        # Asking about the bot
        elif "your name" in user_input:
            print("Chatbot: I'm ChatSimple, your friendly assistant.")

        # Asking about the time
        elif "time" in user_input:
            current_time = time.strftime("%I:%M %p")
            print(f"Chatbot: The current time is {current_time}.")

        # Help or FAQ
        elif "help" in user_input or "can you do" in user_input:
            print("Chatbot: I can chat with you, tell the time, and answer simple questions!")

        # Default/fallback response
        else:
            print("Chatbot: I'm not sure how to respond to that. Try asking something else.")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
