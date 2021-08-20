from itertools import permutations as p

def gen(lst):
    y = [[a for a in p(lst,y)] for y in range(1,len(lst)+1)]

    this = []
    for i in y:
        while len(i)>0:
            this.append(i.pop())
    return [b''.join(x) for x in this]

a = 'ا'
b = 'ب'
c = 'پ'

encodedUnicodeA = a.encode("utf8")
encodedUnicodeB = b.encode("utf8")
encodedUnicodeC = c.encode("utf8")

a = gen([encodedUnicodeA,encodedUnicodeB,encodedUnicodeC])

# Function to convert  
def listToString(s): 
    
    # initialize an empty string
    str1 = b"" 
    
    # traverse in the string  
    for ele in s: 
        str1 += b'\r\n' + ele  
    
    # return string  
    return str1 
    
a = listToString(a)

a_file = open("textfile.txt", "wb")
a_file.write(a)