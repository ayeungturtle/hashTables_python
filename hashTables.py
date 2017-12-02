def assignIndex(input):
  myHash=0
  for char in input:
    myHash+=ord(char)
  myHash %= 5;
  return myHash

myList = [[],[],[],[],[]]

def addToHash(key,value):
  index = assignIndex(key)
  global myList
  myList[index].append([key,value])
  
addToHash('app',345)
addToHash('no',3140)
addToHash('bab',223)
addToHash('tookeymeister',333)
addToHash('biblebelt',223)
addToHash('man',222)
addToHash('woman',923)
addToHash('booger',999)

# print(myList)

def find(key):
  index = assignIndex(key)
  global myList
  for entry in myList[index]:
    if (entry[0] == key):
      return entry[1]
  return "entry not found"

print(find('boogery'))
print(find('biblebelt'))
