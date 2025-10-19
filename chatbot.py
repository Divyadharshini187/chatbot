import random

# Dictionary of responses based on keywords
responses = {
    "recommend": [
        "I recommend 'To Kill a Mockingbird' by Harper Lee – a timeless classic about justice and empathy.",
        "How about '1984' by George Orwell? It's a dystopian thriller that feels eerily relevant today.",
        "If you like fantasy, try 'The Name of the Wind' by Patrick Rothfuss – epic and beautifully written."
    ],
    "genre": [
        "Sci-fi is great for mind-bending adventures. What's your favorite sci-fi book?",
        "Romance novels often explore deep emotions. Have you read 'Pride and Prejudice'?",
        "Mystery keeps you guessing! 'The Girl with the Dragon Tattoo' is a modern classic."
    ],
    "author": [
        "J.K. Rowling is amazing for her Harry Potter series. Which book of hers have you read?",
        "Stephen King writes thrilling horror. 'The Shining' is a must-read.",
        "Agatha Christie is the queen of mystery. Try 'Murder on the Orient Express'."
    ],
    "favorite": [
        "My 'favorite' is subjective, but I'd say 'The Hitchhiker's Guide to the Galaxy' for its humor.",
        "If I had to pick, 'Dune' by Frank Herbert is epic sci-fi.",
        "Classics like '1984' are always a favorite for thought-provoking reads."
    ],
    "default": [
        "Books are wonderful! What genre or author are you interested in?",
        "Tell me more about what you like in books – I can suggest something.",
        "I'm here to chat about books. What's on your mind?"
    ]
}

def get_response(user_input):
    user_input = user_input.lower()
    if "recommend" in user_input or "suggest" in user_input:
        return random.choice(responses["recommend"])
    elif "genre" in user_input:
        return random.choice(responses["genre"])
    elif "author" in user_input:
        return random.choice(responses["author"])
    elif "favorite" in user_input:
        return random.choice(responses["favorite"])
    else:
        return random.choice(responses["default"])

def main():
    print("Book Chatbot: Hi! Let's talk about books. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Book Chatbot: Goodbye! Happy reading.")
            break
        response = get_response(user_input)
        print(f"Book Chatbot: {response}")

if __name__ == "__main__":
    main()
