def chatbot():
    print("================================")
    print("       BASIC CHATBOT")
    print("================================")
    print("Bot: Hi! I am a simple chatbot.")
    print("Bot: You can say hello, ask how I am, or say bye.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Bot: Hi!")

        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user_input == "bye":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")


chatbot()