def chatbot_response(message):
    message = message.lower().strip()

    if message == "hello":
        return "Hi!"

    elif message == "how are you":
        return "I'm fine, thanks!"

    elif message == "thank you":
        return "You're welcome!"

    elif message == "bye":
        return "Goodbye!"

    else:
        return "Sorry, I don't understand."


print("Welcome to Python Chatbot!")
print("Type 'bye' to exit.")

while True:
    user_message = input("You: ")
    response = chatbot_response(user_message)
    print("Bot:", response)

    if user_message.lower().strip() == "bye":
        break
