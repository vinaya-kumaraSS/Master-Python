import os

#check file exist or not
def check(check_file):
    if(not os.path.exists(check_file)):
        return 0
    else:
        return 1
    
    
#main code
print("*********File operation*********")
print("1.Check the folder exist\n2.Create folder\n3.Rename the folder\n4.Delete folder")
choice=input("Enter choice:")
match choice:
    case '1':
        check_file=input("Enter file name:")
        val=check(check_file)
        if(val==1):
            print("File Exist")
        else:
            print("File not Exist")
    case '2':
        folder_name=input("Enter the folder name:")
        val=check(folder_name)
        if(val==1):
            print("Folder Exist")
        else:
            os.mkdir(folder_name)
            print(f"folder {folder_name} Created Successfully")
    case '3':
        folder_name=input("Enter the folder name:")
        val=check(folder_name)
        if(val==1):
            rename=input("Enter rename:")
            os.rename(folder_name,rename)
            print("Rename Succesuffly")
        else:
            print("Folder Not Exist")
    case '4':
        folder_path=input("Enter the folder path:")
        if os.path.exists(folder_path):
            os.remove(folder_path)
            print("Delete Successfully")
        else:
            print("Delete Unsuccessfully")
    case _:
        print("Enter the valid choice")
        



