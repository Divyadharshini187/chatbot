from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Updated responses with more enthusiasm, variety, and emojis
responses = {
    "recommend": [
        "Oh wow, I recommend 'To Kill a Mockingbird' by Harper Lee – it's a timeless classic that'll blow your mind! 📖",
        "You gotta check out '1984' by George Orwell – super relevant and thrilling! 😲",
        "Fantasy lovers, dive into 'The Name of the Wind' by Patrick Rothfuss – epic and totally addictive! ✨",
        "For a hilarious sci-fi ride, try 'The Hitchhiker's Guide to the Galaxy' by Douglas Adams – you'll laugh out loud! 😂"
    ],
    "genre": {
        "sci-fi": [
            "Sci-fi rocks! Blast off with 'Dune' by Frank Herbert – it's out-of-this-world! 🚀",
            "Thrilled you like sci-fi! 'The Martian' by Andy Weir is gripping and fun – you'll love it! 🌌"
        ],
        "fantasy": [
            "Fantasy is magical! 'The Lord of the Rings' by J.R.R. Tolkien is legendary – get ready for adventure! 🧙‍♂️",
            "Awesome choice! 'Mistborn' by Brandon Sanderson has twists that'll keep you hooked! 🔥"
        ],
        "mystery": [
            "Mystery fans unite! 'The Girl with the Dragon Tattoo' by Stieg Larsson is intense and thrilling! 🕵️‍♀️",
            "'Gone Girl' by Gillian Flynn is a wild ride – you won't put it down! 😱"
        ],
        "romance": [
            "Romance is heartwarming! 'Pride and Prejudice' by Jane Austen is charming and classic! 💕",
            "Love stories? 'The Notebook' by Nicholas Sparks will sweep you off your feet! 🌹"
        ],
        "horror": [
            "Horror chills! 'The Shining' by Stephen King is spine-tingling – perfect for scares! 👻",
            "'Bird Box' by Josh Malerman is creepy and exciting – brace yourself! 😈"
        ],
        "default_genre": [
            "That's an awesome genre! Tell me more – I'm super excited to suggest something! 🎉",
            "Genres like that are the best! What's your fave sub-type? Let's find your next read! 📚"
        ]
    },
    "author": {
        "rowling": ["J.K. Rowling is a wizard! Her Harry Potter series is pure magic – which one's your fave? 🪄"],
        "king": ["Stephen King is the horror master! 'It' is epic and terrifying – you'll be hooked! 👹"],
        "christie": ["Agatha Christie is brilliant! 'And Then There Were None' is suspenseful genius! 🔍"],
        "default_author": ["That author is fascinating! What do you love about their work? I'm buzzing to hear! 🤩"]
    },
    "favorite": [
        "My 'favorite' changes, but 'The Hitchhiker's Guide' always makes me smile! 😄",
        "If I had to pick, 'Dune' is epic sci-fi – it's a total thrill! 🌟",
        "Classics like '1984' are unbeatable – thought-provoking and awesome! 💡"
    ],
    "like": [
        "You like that? Wow, great taste! Based on it, I suggest [something amazing]. Tell me more! 👍",
        "Awesome! If you enjoy [topic], you'll adore [related book] – it's fantastic! 🎊"
    ],
    "greet": [
        "Hey there, book lover! Ready to chat about awesome reads? What's your favorite genre? 📖😊",
        "Hi! I'm pumped to talk books – what's on your mind? Let's get excited! 🚀"
    ],
    "bye": [
        "Bye for now! Happy reading – come back anytime for more book fun! 📚👋",
        "See ya! Don't forget to grab a great book – you're gonna love it! 😄"
    ],
    "default": [
        "Books are amazing! What genre or author are you into? I'm thrilled to help! 🎉",
        "Tell me more about what you like – I'm super excited to suggest something! 🤗",
        "I'm all about books! Try mentioning a genre or asking for recs – let's make it fun! 📖✨"
    ]
}

def get_response(user_input):
    user_input = user_input.lower().strip()
    words = user_input.split()
    
    # Check for greetings
    if any(word in words for word in ["hello", "hi", "hey", "greetings"]):
        return random.choice(responses["greet"])
    
    # Check for goodbyes
    if any(word in words for word in ["bye", "goodbye", "quit", "exit"]):
        return random.choice(responses["bye"])
    
    # Check for recommendations
    if any(word in words for word in ["recommend", "suggest", "what", "should", "read"]):
        return random.choice(responses["recommend"])
    
    # Check for genres
    for genre, replies in responses["genre"].items():
        if genre in user_input:
            return random.choice(replies)
    if any(word in words for word in ["genre", "type", "book"]):
        return random.choice(responses["genre"]["default_genre"])
    
    # Check for authors
    for author, replies in responses["author"].items():
        if author in user_input:
            return random.choice(replies)
    if "author" in user_input:
        return random.choice(responses["author"]["default_author"])
    
    # Check for favorites
    if any(word in words for word in ["favorite", "fave", "best"]):
        return random.choice(responses["favorite"])
    
    # Check for likes
    if any(word in words for word in ["like", "love", "enjoy", "prefer"]):
        if "sci-fi" in user_input:
            return "You like sci-fi? Wow, try 'Dune' – it's a masterpiece that'll excite you! 🚀"
        elif "fantasy" in user_input:
            return "Fantasy fan? 'The Name of the Wind' is epic and thrilling! ✨"
        else:
            return random.choice(responses["like"])
    
    return random.choice(responses["default"])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    bot_response = get_response(user_message)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)

