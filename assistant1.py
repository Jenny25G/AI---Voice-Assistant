import pyttsx3
import wikipedia

milverton = pyttsx3.init()

In = input("Search Wikipedia/Google: ")
Input = input("In how many lines you want the answer? : ")


result = wikipedia.summary(In, sentences = Input)
milverton.say('According to Wikipedia ')
print(result)

milverton.say(result)
milverton.say('Thank you')
milverton.runAndWait()