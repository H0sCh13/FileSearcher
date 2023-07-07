import os
from tabulate import tabulate


#File/Directory Counting

totalFiles = 0  #Number of Files
totalDir = 0    #Number of Directories

searchList = []


def program():

    """ This Program lets you search for different Datatypes. Just type in your preferred Datatype, e.g. "txt" and the directory you want to search in for. """


#######################################################################################

#Index-Layout

print("**FileSearch Pro 2.0**\n")

KeyWordTableSEARCH = [["[txt]", "[clear]"],
                      ["[jpg]", "[help]"],
                      ["[gif]", "[save]"],
                      ["[png]", ""]]
                     
                      
                      


KeyWordCategoriesSEARCH = ["Datatypes", "Miscellanous"]


print(tabulate (KeyWordTableSEARCH, headers= KeyWordCategoriesSEARCH, tablefmt = "github"))


########################################################################################

#Loop-Start

print("")

Entry = input("\nPress any Button to continue...\n")

while Entry != "ABORT":

    x = input ("\nWhich Datatype? ")
    
    if x == "txt":
    
        x = input("\nWhich Path? (Example: C:\\) ")
        
        print("\n - Search in Path [" + x + "] -\n")
        
        input()
        
        
        for root, dirs, files in os.walk(x):
            for file in files:
                if file.endswith(".txt"):
            
         
                    totalFiles +=1
           
                   
                    print(os.path.join(root, file)) 
                    searchList.append(os.path.join(root, file))
                    
                    print("Found: ", totalFiles) 
                    print("")
                   

    elif x == "jpg":
    
        x = input("\nWhich Path? (Example: C:\\) ")
        
        print("\n - Search in Path [" + x + "] -\n")
        
        input()
        
        
        for root, dirs, files in os.walk(x):
            for file in files:
                if file.endswith(".JPG"):
            
           
                    totalFiles +=1
           
            
                    print(os.path.join(root, file)) 
                    searchList.append(os.path.join(root, file))
                    
                    print("Found: ", totalFiles) 
                    print("")
                    
     
    elif x =="png":
    
        x = input("\nWhich Path? (Example: C:\\) ")
        
        print("\n - Search in Path [" + x + "] -\n")
        
        input()
        
        
        for root, dirs, files in os.walk(x):
            for file in files:
                if file.endswith(".png"):
            
           
                    totalFiles +=1
           
            
                    print(os.path.join(root, file)) 
                    searchList.append(os.path.join(root, file))
                    
                    print("Found: ", totalFiles) 
                    print("")
                    
                    
    elif x == "gif":
    
        x = input("\nWhich Path? (Example: C:\\) ")
        
        print("\n - Search in Path [" + x + "] -\n")
    
        input()
    
    
        for root, dirs, files in os.walk(x):
            for file in files:
                if file.endswith(".gif"):
                
                    totalFiles +=1
           
            
                    print(os.path.join(root, file)) 
                    
                    print("Found: ", totalFiles) 
                    print("")
                    
                    
                    
    elif x == "save":
    
        with open ("FileSearch.txt" , "w") as savefile:
            for item in searchList:
                savefile.write(item + ", \n")
    
        
                    
                    
                    
    elif x == "clear":
    
        os.system("cls")
        
        print("**FileSearch Pro 2.0**\n")
        
        print(tabulate (KeyWordTableSEARCH, headers= KeyWordCategoriesSEARCH, tablefmt = "github"))
        
        
    elif x == "help":
    
        print("")
    
        help(program)
    
        
   

############################################################################

#Loop-End                  
                    
    elif x == "exit":    
        
        break
     
    
    else:
    
        print("\nError...")
        

print("\nHave a nice Day!")
       
input()
       
