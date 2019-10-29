# Strings

# Concatenation
#    2 or more strings and put them together

firstName = "Wilma"
lastName = "Flintstone"

print(firstName + " " + lastName)

name = firstName + " " + lastName
lastFirst = lastName + ", " + firstName

print(lastFirst)

# Repetition
#   repetition operator: *

print("Hip "*2 + "Hooray!")

def rowYourBoat():
    print("Row, "*3 + "your boat")
    print("Gently down the stream")
    print("Merrily, "*4)
    print("Life is but a dream")


rowYourBoat()

# Indexing

name = "Roy G Biv"
firstChar = name[0]
print(firstChar)

middleCharIndex = len(name) // 2
print(middleCharIndex)
print(name[middleCharIndex])

print(name[-3])

for i in range(0, len(name)):
    print(name[i])

# Slicing and dicing

print(name[-4:8])

for i in range(0, len(name)+1):
    print(name[0:i])

# Searching

print("biv" in name)

if "y" not in name:
    print("y is not in name")
else:
    print("y is in name")

    # String Methods to investigate:
    # Method        Use Example         Explanation
    # center        aStr.center(w)
    # ljust         aStr.ljust(w)
    # rjust         aStr.rjust(w)
    # upper         aStr.upper()
    # lower         aStr.lower()
    # index         aStr.index(item)
    # rindex        aStr.rindex(item)
    # find          aStr.find(item)
    # rfind         aStr.rfind(item)
    # replace       aStr.replace(old, new)

    # Be sure to include multiple examples of all of them in use

# Character functions

print(chr(75))
print(ord('&'))

from mapper import *
print(letterToIndex('M'))

print(indexToLetter(44))


from crypto import *

print(scramble2Encrypt("THE MEETING IS AT FIVE OCLOCK"))
print(scramble2Encrypt("H ETN SA IEOLCTEMEIGI TFV COK"))
print(scramble2Decrypt(scramble2Decrypt(" T AIOCEEG F OHENS ELTMIITVCK")))