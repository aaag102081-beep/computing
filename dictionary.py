import json

file = open("data.json","r")
jsonData = json.load(file)
word = input("enter a word you want to know the meaning of:")

if word in jsonData:
    print("found")
else:
    print("word not found")
final_word = word.lower()

for i in range(len([jsonData[final_word]])):
    print(jsonData[final_word][i])

