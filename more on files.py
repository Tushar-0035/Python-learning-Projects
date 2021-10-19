f=open("tush.txt")
#f.tell func tells that where our file pointer.
#print(f.tell())
print(f.readline())
#print(f.tell())
#f.seek ka kaam hota hai ki ye function ko kaha se pdhna start kre.
f.seek(10)
print(f.readline())
#print(f.tell())
f.close()