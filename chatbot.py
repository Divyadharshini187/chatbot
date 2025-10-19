from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Updated responses with modern books, enthusiasm, and current trends
responses = {
    "recommend": [
        "Oh wow, dive into 'Shatter Me' by Tahereh Mafi – it's a thrilling YA dystopian romance that'll hook you! 💥📖",
        "You gotta try the 'Twisted' series by Ana Huang – steamy, addictive romance with twists! 🔥😍",
        "For modern fantasy, 'Fourth Wing' by Rebecca Yarros is epic and unputdownable! 🐉✨",
        "Check out 'The Cruel Prince' by Holly Black – dark fae fantasy that's totally binge-worthy! 🌑🧚"
    ],
    "genre": {
        "sci-fi": [
            "Sci-fi is lit! 'The Long Way to a Small, Angry Planet' by Becky Chambers is heartwarming space adventure! 🚀❤️",
            "Thrilled for sci-fi? 'Project Hail Mary' by Andy Weir is hilarious and mind-blowing! 🌌😂"
        ],
        "fantasy": [
            "Fantasy fans, 'A Court of Thorns and Roses' by Sarah J. Maas is magical and steamy! 🧙‍♀️💕",
            "Awesome! 'The Bridge Kingdom' by Danielle L. Jensen has epic battles and romance – you'll love it! ⚔️👑"
        ],
        "mystery": [
            "Mystery vibes! 'The Maidens' by Alex Michaelides is psychological thriller gold! 🕵️‍♀️😱",
            "'Verity' by Colleen Hoover is twisty and intense – perfect for modern suspense! 📖🔍"
        ],
        "romance": [
            "Romance is everything! 'It Ends with Us' by Colleen Hoover is emotional and real – a must-read! 💔❤️",
            "Love stories? 'The Kiss Quotient' by Helen Hoang is sweet, sexy, and hilarious! 😘📚"
        ],
        "horror": [
            "Horror chills! 'Mexican Gothic' by Silvia Moreno-Garcia is creepy and atmospheric! 👻🕸️",
            "'The Only One Left' by Riley Sager is a modern haunted house thriller – spine-tingling! 😈🏚️"
        ],
        "default_genre": [
            "That's a hot genre right now! Tell me more – I'm pumped to suggest fresh reads! 🎉📚",
            "Modern takes on that are amazing! What's your fave sub-type? Let's find your next obsession! 🤩"
        ]
    },
    "author": {
        "mafi": ["Tahereh Mafi is a queen! 'Shatter Me' series is dystopian romance perfection – which book first? 💥"],
        "huang": ["Ana Huang rocks! Her 'Twisted' series is steamy and addictive – binge it now! 🔥😏"],
        "hoover": ["Colleen Hoover is unstoppable! 'It Ends with Us' is raw and powerful – life-changing! 💪❤️"],
        "yarros": ["Rebecca Yarros is fire! 'Fourth Wing' is dragons, romance, and epic vibes! 🐲✨"],
        "default_author": ["That author is trending! What do you love about their work? I'm buzzing to chat! 🤩📖"]
    },
    "favorite": [
        "My 'favorite' shifts, but 'Fourth Wing' by Rebecca Yarros always thrills me! 🐉😄",
        "If I had to pick, 'Shatter Me' is intense YA magic – totally addictive! 💥",
        "Modern gems like 'Twisted Love' are unbeatable – steamy and smart! 🔥💡"
    ],
    "like": [
        "You like that? Wow, spot-on taste! Based on it, try [something fresh]. Tell me more! 👍📚",
        "Awesome! If you enjoy [topic], you'll devour [related modern book] – it's trending for a reason! 🎊"
    ],
    "greet": [
        "Hey, bookworm! Ready for modern reads? What's your vibe – romance, fantasy, or dystopian? 📖😊",
        "Hi! I'm hyped for current books – let's chat 'Shatter Me' or 'Twisted' series! 🚀"
    ],
    "bye": [
        "Catch ya later! Grab a modern bestseller and enjoy – come back for more recs! 📚👋",
        "Bye! Don't forget 'Fourth Wing' – you're gonna love it! 😄🖤"
    ],
    "default": [
        "Books are epic! What modern genre or author are you into? I'm thrilled to suggest hits! 🎉📖",
        "Tell me your tastes – I'm all about current trends like YA romance! Let's get excited! 🤗✨",
        "Modern reads rule! Try mentioning 'Shatter Me' or a genre – I'll hook you up! 📚🔥"
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
            return "You like sci-fi? Wow, try 'Project Hail Mary' – it's hilarious and thrilling! 🚀"
        elif "fantasy" in user_input:
            return "Fantasy fan? 'Fourth Wing' is dragons and drama – epic! 🐉"
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
