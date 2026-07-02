def chatbot():

    print("🤖 Simple Chatbot")
    print("Type 'bye' to exit.\n")

    while True:

        user = input("You: ").lower()

        if user == "hello" or user == "hi":
            print("Bot: Hi! Nice to meet you.")

        elif user == "how are you":
            print("Bot: I'm fine, thanks! How are you?")

        elif user == "what is your name":
            print("Bot: I'm a simple Python chatbot.")

        elif user == "who made you":
            print("Bot: I was created using Python.")

        elif user == "thank you":
            print("Bot: You're welcome!")

        elif user == "bye":
            print("Bot: Goodbye! Have a nice day.")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

# Run chatbot
chatbot()