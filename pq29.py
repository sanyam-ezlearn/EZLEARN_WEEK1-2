'''Count Words in Text File in Python'''
c = 0

# Opening our text file in read only mode
with open(r'SampleFile.txt','r') as file:

    data = file.read()
    
    w = data.split()
    
    c += len(w)

print(c)