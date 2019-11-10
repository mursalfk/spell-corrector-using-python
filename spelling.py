from textblob import TextBlob

file1 = open("1.txt", "r+")
a = file1.read()

print("Original Text : \n" + str(a))

b = TextBlob(a)

print("Corrected Text : \n" + str(b.correct()))

file1.close()

d = open("1.txt", "w")
d.write(str(b.correct()))
d.close()