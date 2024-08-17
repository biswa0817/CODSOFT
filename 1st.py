def chatbot_response(user_input):
    user_input = user_input.lower()

    if 'hello' in user_input or 'hi' in user_input:
        return "Hello! How can I help you today?"
    elif 'what is your name' in user_input or 'who are you' in user_input:
        return "I am a simple chatbot created to assist you."
    elif 'how are you' in user_input:
        return "I'm just a chatbot, but I'm here to help you!"
    elif 'bye' in user_input:
        return "Goodbye! Have a great day!"
    elif 'help' in user_input:
        return "Sure! What do you need help with?"
    else:
        return "I'm not sure how to respond to that. Can you ask something else?"

def main():
    print("Chatbot: Hi! I'm a simple chatbot. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if _name_ == "_main_":
  _main_()