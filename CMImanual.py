#  This file contains the CMI value corresponding to Original Annotation
import os.path
file = open("Hinglish_train_14k_split_conll.txt","r",encoding='utf-8')
lines = file.readlines()
engCount = 0
hinCount = 0
numOfTokens =0
u=0
n=0
cmi=0
maxW=0
for line in lines:
  if 'Eng' in line:
  	# print(line)
  	engCount+=1
    # engCount+=1
  elif 'Hin'in line:
  	# print(line)
  	hinCount+=1
for line in lines:
	for word in line.split():
		if word!='' and word!='Hin' and word!='Eng' and word!='meta' and word!='positive' and word!='negative' and word!='neutral' and word!='O' and word.isdigit()==False:
			numOfTokens+=1
			# print(word)
		# print(word)
for line in lines:
	for word in line.split():
		if word!=' ' and word.isalpha()==False:
			u+=1;
			# print(word)
			
print("number of tokens is "+str(numOfTokens))	
n = numOfTokens
print("A")
print(str(n-engCount-hinCount))
print(str(u))
print("B")
# u=n-u
# u=engCount+hinCount
maxW = max(engCount,hinCount)

print(hinCount)
print(n)
print(u)
print(str(maxW/(n-u)))
print("n = "+str(numOfTokens)+" , maxW = "+str(maxW))

# cmi = 100 * (1-(maxW/(n-u)))
cmi = 100 * (1-(maxW/(engCount+hinCount)))
print("u is "+str(u))
print("engCount is "+ str(engCount)+", Hindi Count is "+str(hinCount))
print("cmi value is "+str(cmi))

# print(line)