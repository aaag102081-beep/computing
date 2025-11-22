file = open("hello.txt", "r")
data = file.readline()
data2 = file.readline()
print((data+data2)*100)