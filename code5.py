try :
    with open("data.txt" ,"r") as f:
        print(f.read())


except FileNotFoundError:
    print("File not found!")


finally :
    print("end of the porgram ")    
