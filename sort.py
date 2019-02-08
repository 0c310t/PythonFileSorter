import os

loop = 'y'

while loop == 'y':
    count = 0

    fileType = input("What type of file would you like to sort? ")

    fileList = []

    for files in os.walk("."):
        for filename in files[2]:
            fileList.append(filename)

    for i in range(len(fileList)):
        if fileList[i].split('.')[1] == fileType:
            if i == 0:
                try:
                    os.mkdir(fileType)
                except FileExistsError:
                    print("File already exists, continuing...")
                    pass
            os.system("move "+fileList[i]+" "+fileType)
            count = count+1
        else:
            break

    if count != 0:
        print("Moved", count, "file(s) into folder:", fileType)
    else:
        print("No files matching that type.")
        
    loop = input("\nSort more files? (y/n): ")
