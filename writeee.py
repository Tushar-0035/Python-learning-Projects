#f=open("tush.txt","w")
#if we append or add something:
f=open("tush.txt","a")
a=f.write("tushar is a good boy\n")
print(a)
f.close()

#handle read and write both
f=open("tush.txt","r+")
print(f.read())
f.write("thankyou")
f.close()