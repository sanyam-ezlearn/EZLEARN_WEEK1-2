'''Python Program to Replace Text in a File'''

s = input("Enter text to replace the existing contents:")
f = open("file.txt", "r+")

f.truncate(0)
f.write(s)
f.close()
print("Text successfully replaced")