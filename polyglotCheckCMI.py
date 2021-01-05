from polyglot.detect import Detector
import os.path
compareFile = open('compareFile.txt','w')
readFile = open("Hinglish_train_14k_split_conll.txt","r",encoding='utf-8')
lines = readFile.readlines()
# considering words of length greater than 2 due to library limitations
actualEng=0
foundEng =0
actualHin =0
foundHin =0
for line in lines:
  if 'Eng' in line:
    for word in line.split():
      # print("word is "+word)
      if word.isalpha()==True and word!='Eng' and word!='https' and len(word)>2:
        try:
          detector = Detector(word)
          if detector.language.name =='English' and float(detector.language.confidence)>80.0:
            compareFile.write("\n"+word + " -- "+ "Eng- "+' -English')
            actualEng+=1
            foundEng+=1
          else:
            compareFile.write("\n"+word + " -- "+ "Eng- "+' -Hindi')
            actualEng+=1
            foundHin+=1
        except:
          compareFile.write("\n"+word + " -- "+ "Eng- "+' -Null')
          actualEng+=1
          # print("in word is "+word)
          # print(detector.language.name)
          # print(detector.language.confidence)
  elif 'Hin' in line:
    for word in line.split():
      # print("word is "+word)
      if word.isalpha()==True and word!='Hin' and word!='https' and len(word)>2:
        try:
          detector = Detector(word)
          if detector.language.name =='English' and float(detector.language.confidence)>80.0:
            compareFile.write("\n"+word + " -- "+ "Hin- "+' -English')
            actualHin+=1
            foundEng+=1
          else:
            compareFile.write("\n"+word + " -- "+ "Hin- "+' -Hindi')
            actualHin+=1
            foundHin+=1
        except:
          compareFile.write("\n"+word + " -- "+ "Hin- "+' -Null')
          actualHin+=1
          # print("in word is "+word)
          # print(detector.language.name)
          # print(detector.language.confidence)

compareFile.write("\nactual English = "+ str(actualEng))
compareFile.write("\nfound English = "+ str(foundEng))
compareFile.write("\nactual Hindi = "+ str(actualHin))
compareFile.write("\nfound Hindi = "+ str(foundHin))
print("\nactual English = "+ str(actualEng))
print("\nfound English = "+ str(foundEng))
print("\nactual Hindi = "+ str(actualHin))
print("\nfound Hindi = "+ str(foundHin))


### Finding CMI from these values

numOfTokens =0
u=0
n=0
cmi=0
maxW=0

for line in lines:
	for word in line.split():
		if word!='' and word!='Hin' and word!='Eng' and word!='meta' and word!='positive' and word!='negative' and word!='neutral' and word!='O' and word.isdigit()==False:
			numOfTokens+=1
			# print(word)
		# print(word)
for line in lines:
	for word in line.split():
		if word!='' and word.isalpha()==False:
			u+=1;
			# print(word)
			
### Finding Actual CMI value 
	
n = numOfTokens
maxW = max(actualEng,actualHin)
cmiActual = 100 * (1-(maxW/(actualEng+actualHin)))
print("Actual cmi value is "+str(cmiActual))

### Finding Found CMI Value
n = numOfTokens
maxW = max(foundEng,foundHin)
cmiFound = 100* (1-(maxW/(foundEng+foundHin)))
print("Found cmi value using PolyGlot Comparision is "+str(cmiFound))

# print(line)
