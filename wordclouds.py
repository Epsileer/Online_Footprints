# Generates a Wordcloud
# Author: Pranshu Gupta

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Read the whole text.
text = open('output/words.txt').read()

# Generate a word cloud image
wordcloud = WordCloud(width=1200, height=1000).generate(text)
wordcloud.to_file("images/wordcloud.png")
