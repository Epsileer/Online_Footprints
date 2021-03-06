from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Read the whole text.
# please remove words like - official, private, deleted video, song etc from the file here

text = open('output/youtubetitles.txt').read()

# Generate a word cloud image
wordcloud = WordCloud(width=1200, height=1000).generate(text)
wordcloud.to_file("images/youtubewordcloud.png")