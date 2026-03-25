import numpy as np

# Example: Bag of Words for text classification
def create_bag_of_words(texts):
    """Convert texts to bag of words vectors"""
    # Get all unique words
    words = set()
    for text in texts:
        for word in text.lower().split():
            words.add(word)
    
    words = sorted(list(words))
    word_to_idx = {word: i for i, word in enumerate(words)}
    
    # Create vectors
    vectors = []
    for text in texts:
        vector = np.zeros(len(words))
        for word in text.lower().split():
            vector[word_to_idx[word]] += 1
        vectors.append(vector)
    
    return np.array(vectors), words

# Example usage
texts = [
    "I love machine learning",
    "I love artificial intelligence",
    "machine learning is fun",
    "artificial intelligence is amazing"
]

vectors, vocabulary = create_bag_of_words(texts)
print("Vocabulary:", vocabulary)
print("\nBag of Words Vectors:")
print(vectors)