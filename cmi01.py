from langdetect import detect
import os
file = open("Hinglish_train_14k_split_conll.txt","r")
lines = file.readlines()
engCount = 0
hinCount = 0
for line in lines:
  if 'Eng' in line:
    engCount+=1
  elif 'Hin'in line:
    hinCount+=1
print("engCount is "+ str(engCount)+", Hindi Count is "+str(hinCount))
  # print(line)
