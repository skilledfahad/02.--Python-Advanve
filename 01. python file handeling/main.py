# ============== Read only ==============
dayespath = "dayes.text"
file1 = open(dayespath, 'r')

# print(file1.read())
#
# print(file1.readline(), end="")  # use end for removing line gape
# print(file1.readline())
# print(file1.readline(2))
#
# print(file1.readlines())

# ============== write only ==============
file2= open("myself.text","w")
file2.write("name: MD Fahad Hossen \nage: 25\n")

# ============== append  ==============
file2= open("myself.text","a")
file2.write("city: Chittagong\n")

# ============== copy data file to file  ==============
for data in file1:
    file2.write(data)

# ============== Read img ==============
imgfile= open("img/fahad_fier.png","rb")
img2= open("img/img2.jpg","wb")

for data in imgfile:
    img2.write(data)

# ============== Read and write r+ a+==============
file3= open("file3/textdoc.text", "r+")

file3.write("hello")
file3.seek(0) # auto seek 0
file3.write("hello")
print(file3.read()) #hello missing coz read-1st wrrite-later

file3= open("file3/textdoc.text", "a+")
# file3.write("hi")
file3.close()

