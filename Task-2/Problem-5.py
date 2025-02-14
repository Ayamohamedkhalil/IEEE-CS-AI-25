from collections import Counter
import re

# Read the file
file_path = "Task-2\simple_text.txt"

with open(file_path, "r", encoding="utf-8") as file:
    text = file.read().lower()  


words = re.findall(r"\b\w+'\w+|\w+\b", text)  


word_counts = Counter(words)


for word, count in word_counts.items():
    print(f"{word}: {count}")
