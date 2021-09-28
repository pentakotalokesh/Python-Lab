import random
f=open("sample.txt",'w')
f.write("Iam Lokesh\nIam a Boy")
f.close()
f=open("integers.txt",'w')
for i in range(0,500):
    num=random.randint(0,500)
    ch=str(num)
    f.write(ch + '\n')
f.close()