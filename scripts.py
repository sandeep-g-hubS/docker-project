import re
from collections import Counter
import socket
import os

# Create output directory if it doesn't exist
output_dir = '/home/data/output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to count words and get frequencies
def count_words(text):
    words = text.split()  # Extract words, ignoring punctuation, case insensitive
    return len(words), Counter(words)



# Handle contractions by splitting them into individual words
def handle_contractions(text):
    contractions = {
        "I'm": "I am", "can't": "can not", "don't": "do not", "didn't": "did not", "won't": "will not",
        "I'll": "I will", "you'll": "you will", "we're": "we are", "they're": "they are",
        "I've": "I have", "you've": "you have", "isn't": "is not", "aren't": "are not",
        "it's": "it is", "couldn't": "could not", "wouldn't": "would not"
    }
    # Replace contractions in the text using regex for word boundaries
    for contraction, full_form in contractions.items():
        text = re.sub(r'\b' + re.escape(contraction) + r'\b', full_form, text)
    return text

# Read and process IF.txt
with open('/home/data/IF.txt', 'r') as if_file:
    if_text = if_file.read()
    if_text = handle_contractions(if_text)
    total_words_if, word_count_if = count_words(if_text)
    

# Read and process AlwaysRememberUsThisWay.txt
with open('/home/data/AlwaysRememberUsThisWay.txt', 'r') as arutw_file:
    arutw_text = arutw_file.read()
    arutw_text = handle_contractions(arutw_text)
    total_words_arutw, word_count_arutw = count_words(arutw_text)


# Get top 3 frequent words in both texts
top_3_if = word_count_if.most_common(3)
top_3_arutw = word_count_arutw.most_common(3)

# Get the IP address of the machine running the container
ip_address = socket.gethostbyname(socket.gethostname())

# Write results to result.txt
with open(f'{output_dir}/result.txt', 'w') as result_file:
    result_file.write(f"Total words in IF.txt: {total_words}\n")
    result_file.write(f"Total words in AlwaysRememberUsThisWay.txt: {total_words_arutw}\n")
    result_file.write(f"Grand total: {total_words_if + total_words_arutw}\n")
    result_file.write(f"Top 3 words in IF.txt: {top_3_if}\n")
    result_file.write(f"Top 3 words in AlwaysRememberUsThisWay.txt: {top_3_arutw}\n")
    result_file.write(f"Container IP address: {ip_address}\n")

# Print the result to the console
with open(f'{output_dir}/result.txt', 'r') as result_file:
    print(result_file.read())
