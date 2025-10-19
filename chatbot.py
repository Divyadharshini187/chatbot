import random
import sys

# Expanded dictionary of responses with more keywords and context
responses = {
    "recommend": [
        "I recommend 'To Kill a Mockingbird' by Harper Lee – a timeless classic about justice and empathy.",
        "How about '1984' by George Orwell? It's a dystopian thriller that feels eerily relevant today.",
        "If you like fantasy, try 'The Name of the Wind' by Patrick Rothfuss – epic and beautifully written.",
        "For a quick read, 'The Hitchhiker's Guide to the Galaxy' by Douglas Adams is hilarious sci-fi."
    ],
    "genre": {
        "sci-fi": [
            "Sci-fi is awesome! Try 'Dune' by Frank Herbert or 'Neuromancer' by William Gibson.",
            "You might enjoy 'The Martian' by Andy Weir – it's thrilling and realistic."
        ],
        "fantasy": [
            "Fantasy fans love 'The Lord of the Rings' by J.R.R. Tolkien. Have you read it?",
            "Check out 'Mistborn' by Brandon Sanderson for a unique magic system."
        ],
        "mystery": [
            "Mystery keeps you guessing! 'The Girl with the Dragon Tattoo' by Stieg Larsson is intense.",
            "'Gone Girl' by Gillian Flynn is a modern psychological thriller."
        ],
        "romance": [
            "Romance novels are heartwarming. 'Pride and Prejudice' by Jane Austen is a classic.",
            "Try 'The Notebook' by Nicholas Sparks for an emotional story."
        ],
        "horror": [
            "Horror can be chilling. 'The Shining' by Stephen King is a must-read.",
            "'Bird Box' by Josh Malerman is a recent page-turner."
        ],
        "default_genre": [
            "That's a great genre! Tell me more about what you like in it, and I'll suggest something.",
            "Genres like that have so many options. What's your favorite sub-type?"
        ]
    },
    "author": {
        "rowling": ["J.K. Rowling's Harry Potter series is magical. Which book is your favorite?"],
        "king": ["Stephen King is the master of horror. 'It' is a long but epic read."],
        "christie": ["Agatha Christie wrote brilliant mysteries. 'And Then There Were None' is suspenseful."],
        "default_author": ["That's a fascinating author! What do you like about their work?"]
    },
    "favorite": [
        "My 'favorite' is subjective, but I'd say 'The Hitchhiker's Guide to the Galaxy' for its humor.",
        "If I had to pick, 'Dune' by Frank Herbert is epic sci-fi.",
        "Classics like '1984' are always a favorite for thought-provoking reads."
    ],
    "like": [
        "You like that? Based on what you've said, I suggest [insert suggestion]. Tell me more!",
        "Great taste! If you enjoy [topic], you might like [related book]."
    ],
    "greet": [
        "Hello! Ready to talk books? What's your favorite genre?",
        "Hi there! Let's chat about books. What are you reading now?"
    ],
    "bye": [
        "Goodbye! Happy reading – come back anytime.",
        "See you later! Don't forget to pick up a good book."
    ],
    "default": [
        "Books are wonderful! What genre or author are you interested in?",
        "Tell me more about what you like in books – I can suggest something.",
        "I'm here to chat about books. What's on your mind? Try asking for recommendations or mentioning a genre."
    ]
}

def get_response(user_input, debug=False):
    user_input = user_input.lower().strip()
    words = user_input.split()  # Split into words for better matching
    
    if debug:
        print(f"Debug: Detected words: {words}")
    
    # Check for greetings
    if any(word in words for word in ["hello", "hi", "hey", "greetings"]):
        if debug: print("Debug: Matched greeting")
        return random.choice(responses["greet"])
    
    # Check for goodbyes
    if any(word in words for word in ["bye", "goodbye", "quit", "exit"]):
        if debug: print("Debug: Matched goodbye")
        return random.choice(responses["bye"])
    
    # Check for recommendations
    if any(word in words for word in ["recommend", "suggest", "what", "should", "read"]):
        if debug: print("Debug: Matched recommend")
        return random.choice(responses["recommend"])
    
    # Check for genres (more specific matching)
    for genre, replies in responses["genre"].items():
        if genre in user_input:  # Check full input for phrases like "sci-fi"
            if debug: print(f"Debug: Matched genre '{genre}'")
            return random.choice(replies)
    # Fallback for genre mentions
    if any(word in words for word in ["genre", "type", "book"]):
        if debug: print("Debug: Matched general genre")
        return random.choice(responses["genre"]["default_genre"])
    
    # Check for authors (specific names)
    for author, replies in responses["author"].items():
        if author in user_input:
            if debug: print(f"Debug: Matched author '{author}'")
            return random.choice(replies)
    if "author" in user_input:
        if debug: print("Debug: Matched general author")
        return random.choice(responses["author"]["default_author"])
    
    # Check for favorites
    if any(word in words for word in ["favorite", "fave", "best"]):
        if debug: print("Debug: Matched favorite")
        return random.choice(responses["favorite"])
    
    # Check for likes/preferences
    if any(word in words for word in ["like", "love", "enjoy", "prefer"]):
        # Basic attempt at context: if they mention a genre/author, tie it in
        if "sci-fi" in user_input:
            if debug: print("Debug: Matched like with sci-fi")
            return "You like sci-fi? Try 'Dune' – it's a masterpiece!"
        elif "fantasy" in user_input:
            if debug: print("Debug: Matched like with fantasy")
            return "Fantasy fan? 'The Name of the Wind' is epic."
        else:
            if debug: print("Debug: Matched general like")
            return random.choice(responses["like"])
    
    # Default fallback
    if debug: print("Debug: No match, using default")
    return random.choice(responses["default"])

def main():
    debug = "--debug" in sys.argv
    print("Book Chatbot: Hi! Let's talk about books. Type 'quit' to exit." + (" (Debug mode on)" if debug else ""))
    while True:
        user_input = input("You: ")
        if user_input.lower().strip() in ["quit", "exit", "bye"]:
            print("Book Chatbot: Goodbye! Happy reading.")
            break
        response = get_response(user_input, debug)
        print(f"Book Chatbot: {response}")

if __name__ == "__main__":
    main()
