f=open("sample.txt",'r')
text1=f.readlines()
print(text1)
print(type(text1))
f.close()
f=open("integers.txt",'r')
s=0
for line in f:
    line=line.strip()
    line=int(line)
    s=s+line
print(s)
    
