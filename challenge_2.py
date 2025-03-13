
def get_bot_response(user_message):
    responses = {
        "hello": "Hi there! How can I help you?",
        "tell me about": "What specific place or topic would you like to know?",
        "bye": "Goodbye! Have a great day!"
    }
    
    return responses.get(user_message, "I'm sorry, I don't understand that.")

def main():
    print("Welcome to the chatbot! You can ask me simple questions or type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()  
        
        if user_input == "bye":
            print("Chatbot: Goodbye! Have a nice day!")
            break
        
        response = get_bot_response(user_input)
        print(f"Chatbot: {response}")


if __name__ == "__main__":
    main()
