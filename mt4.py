"""
This script creates a file and writes a list of three-letter words that start with the letter 'B'.
"""

b_words = [
    "bat", "bit", "bot", "but", "bun", "bid", "bad", "bag", "bog", "bug",
    "bus", "bar", "bay", "ben", "bet", "bib", "bod", "bow", "bum", "bye"
]

file_name = "b_words.txt"

with open(file_name, "w") as file:
    for word in b_words:
        file.write(word + "\n")

print(f"File '{file_name}' created with {len(b_words)} words.")
