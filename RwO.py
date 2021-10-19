f=open("tushar.txt")
"""
content=f.read()
print(content)
"""
#if we print 3 words from a text file
#content=f.read(3)
#print(content)
"""for line in f:
    print(line,end="")
"""
#this is another method to print in line by line
"""print(f.readline())
print(f.readline())
print(f.readline())
"""
#this is list method
print(f.readlines())
f.close()