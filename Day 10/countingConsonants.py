#Iterative method
def iterative_consonant(l):
    l = l.upper()
    return not (l == 'A' or l == 'E' or l == 'I' or l == 'O' or l == 'U') and ord(l) >= 65 and ord(l) <= 90
def count_of_consonants(str):
    count = 0
    for i in range(len(str)):
        if (iterative_consonant(str[i])):
            count += 1
    return count
str = 'seema saharan'
print(count_of_consonants(str))

#Recursive Method
def recursive_consonant(ch):
    ch = ch.upper()
    return not (ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U') and ord(ch) >= 65 and ord(ch) <= 90
def recursiveCount(string, n):
    if n == 1:
        return recursive_consonant(string[0])    
    return recursiveCount(string, n-1) + recursive_consonant(string[n-1])
string = 'Seema Saharan'
print(recursiveCount(string, len(string)))