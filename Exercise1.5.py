import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re

# 1. Ladda textfilen
file_path = 'Exercise_5_Advanced_Text_Analysis.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# 2. Count unique words
words = re.findall(r'\b\w+\b', text.lower())
word_count = Counter(words)

# Display word frequencies
print(f"Unique Words Count: {len(word_count)}")
print("Top 10 Words:", word_count.most_common(10))

# 3. Visualize the top 10 most common words
top_10_words = word_count.most_common(10)
words, counts = zip(*top_10_words)

plt.figure(figsize=(10, 6))
plt.bar(words, counts, color='skyblue')
plt.title('Top 10 Most Common Words')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.show()

# 4. Analyze the longest sentence
sentences = re.split(r'[.!?]', text)
sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
longest_sentence = max(sentences, key=lambda s: len(re.findall(r'\b\w+\b', s)))
longest_sentence_word_count = len(re.findall(r'\b\w+\b', longest_sentence))

print(f"Longest Sentence ({longest_sentence_word_count} words):")
print(longest_sentence)

# 5. Visualize the relationship between sentence index and word count
sentence_word_counts = [len(re.findall(r'\b\w+\b', sentence)) for sentence in sentences]
plt.figure(figsize=(10, 6))
plt.bar(range(1, len(sentences) + 1), sentence_word_counts, color='lightgreen')
plt.title('Words per Sentence')
plt.xlabel('Sentence Index')
plt.ylabel('Word Count')
plt.xticks(range(1, len(sentences) + 1))
plt.show()
