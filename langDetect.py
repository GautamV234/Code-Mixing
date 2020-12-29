from langdetect import detect
from langdetect import DetectorFactory
DetectorFactory.seed = 0
x =detect("Aapne us bande ko block kar diya ab kya fayda share karna ka")
print(x)