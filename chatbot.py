import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

def get_response(user_input):
    # Process the user's input using spaCy
    doc = nlp(user_input)

    # Define some sample responses based on keywords
    responses = {
        "greeting": "Hello! How can I help you?",
        "goodbye": "Goodbye! Have a great day!",
        "thanks": "You're welcome!",
        "default": "I'm sorry, I don't understand that. Can you please rephrase?"
    }

    # Check for keywords in the user's input
    if any(token.text.lower() in ["hello", "hi", "hey"] for token in doc):
        return responses["greeting"]
    elif any(token.text.lower() in ["bye", "goodbye"] for token in doc):
        return responses["goodbye"]
    elif any(token.text.lower() in ["thanks", "thank", "thank you"] for token in doc):
        return responses["thanks"]
    else:
        return responses["default"]

def main():
    print("Simple Chatbot: Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        
        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
