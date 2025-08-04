import random

# A fake context-to-next-word predictor (like a mini GPT)
context = "Tell me a joke about clouds"
possible_words = ["They", "It", "Why", "What"]
next_words = {
    "They": ["look", "are", "float", "dance"],
    "It": ["rains", "shines", "storms"],
    "Why": ["did", "was", "is"],
    "What": ["makes", "happens", "floats"]
}

# Step 1: Pick a starter word (simulate prediction)
first_word = random.choice(possible_words)
print(f"{context} {first_word}", end=" ")

# Step 2: Predict next words based on that
second_word = random.choice(next_words[first_word])
print(second_word)
