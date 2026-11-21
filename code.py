''' f = open("sample.txt" , "r") #file objects 

data = f.read()
print(data)

f.close() #very imp '''

'''f = open("sample.txt" , "w")
f.write("Im going mad behind my life")
f.close()'''

'''f = open("sample.txt" , "a")
f.write("changing is one thing ; building trust is another")
f.close()'''

'''f = open("sample2.txt" , "x")
f.write("loving him was not plan : but it killed me from inside ")
f.close()'''


# r+ means read and write
# File must already exist
# It does not delete existing content
# Cursor starts at the beginning of the file

'''f = open("sample.txt", "r+")

print(f.read())  # Read existing content

f.write("Hello")  # Write from the current cursor position

f.close()'''

'''with open("sample.txt" , "r") as f:
    data = f.read()
    print(len(data))'''

'''import os
os.remove("sample2.txt")'''


data = True

with open("sample.txt" , "r") as f:
    while data:
        data = f.readline()

        if("python"in data):
            print("word found")
            break
        else:
            print("word not found")
            

        print(data)



