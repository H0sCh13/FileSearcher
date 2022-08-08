import os


totalFiles = 0
totalDir = 0

print("FileSearcherPro 2.0\n")

print("Datatypes (Gif, JPG, PNG, TEXT)\n")
print("To search Text, type [TXT]")
print("To search JPEG, type [JPG]")
print("to search GIF, type [GIF]")
print("To search PNG, type [PNG]\n")
print("To clear text, type [clear]\n")

print("To exit, type [exit]\n")

Start = input("Welcome!")


while Start != "exit":

    x = input ("\nEntry:")
    
    if x == "TXT":
        for root, dirs, files in os.walk("C:\\"):
            for file in files:
                if file.endswith(".txt"):
            
            
                    totalFiles +=1
           
                    Data = open ("DataTypes.txt", "a") 
                    Data.write(os.path.join(root, file)) 
                    Data.close()
            
                    print(os.path.join(root, file)) 
                   
                 
                 

    elif x =="JPG":
        for root, dirs, files in os.walk("C:\\"):
            for file in files:
                if file.endswith(".jpg"):
                    
           
                    totalFiles +=1
           
                    Data = open ("DataTypes.txt", "a") 
                    Data.write(os.path.join(root, file))
                    Data.close()
            
                    print(os.path.join(root, file)) 
                        
                    
     
    elif x =="PNG":
        for root, dirs, files in os.walk("C:\\"):
            for file in files:
                if file.endswith(".png"):
            
           
                    totalFiles +=1
           
                    Data = open ("DataTypes.txt", "a") 
                    Data.write(os.path.join(root, file))
                    Data.close()
            
                    print(os.path.join(root, file)) 
                    
                    
    elif x == "GIF":
        for root, dirs, files in os.walk("C:\\"):
            for file in files:
                if file.endswith(".gif"):
                
                    totalFiles +=1
           
                    Data = open ("DataTypes.txt", "a") 
                    Data.write(file)
                    Data.close()
            
                    print(os.path.join(root, file)) 
                    
                    
    
    elif x == "clear":
        os.system("cls")
        print("FileSearcher\n")

        print("Datatypes (Gif, JPG, PNG, TEXT)\n")
        print("To search Text, type [TXT]")
        print("To search JPEG, type [JPG]")
        print("to search GIF, type [GIF]")
        print("To search PNG, type [PNG]\n")

        print("To exit, type [exit]\n")
        
    
    elif x =="exit":    
        break
     
    else:
       
        print("\nSorry?")
        print("\nFound:", totalFiles)     
        
print("\nHave a nice day!")
       
input()
       
