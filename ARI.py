# Imported argv from sys module.
from sys import argv

# unpacks the elements of the argv list into the variables
script, file_txt = argv

file = open(file_txt)
file_content=file.read()

words=len(file_content.split())
print("words :",words)

characters=len(file_content)
print("characters :",characters)

sentences=file_content.count(".") + file_content.count("?") + file_content.count("!")
print("sentences :",sentences)

ARI= 4.71*(characters/words) + 0.5 *(words/sentences) -21.43
print("ARI :",ARI)

if(ARI < 2):
    print("Kindergraten")
elif(ARI >= 2 and ARI < 3):
    print("First grade")
elif(ARI >= 3 and ARI < 4):
    print("Second grade")
elif(ARI >= 4 and ARI < 5):
    print("Third grade")
elif(ARI >= 5 and ARI < 6):
    print("Fourth grade")
elif(ARI >=6 and ARI < 7 ):
    print("Fifth grade")
elif(ARI >=7 and ARI < 8):
    print("Sixth grade")
elif(ARI >=8 and ARI <9 ):
    print("Seventh grade")
elif(ARI >=9 and ARI <10 ):
    print("Eight grade")
elif(ARI >= 10 and ARI <11 ):
    print("Nineth grade")
elif(ARI >=11 and ARI < 12 ):
    print("Tenth grade")
elif(ARI >=12 and ARI < 13 ):
    print("Eleventh grade")
elif(ARI >=13 and ARI <14 ):
    print("Twelfth grade")
else:
    print("college")
