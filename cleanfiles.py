
def cleanFiles(currentMem,exMem):
    '''
    currentMem: File containing list of current members
    exMem: File containing list of old members
    
    Removes all rows from currentMem containing 'no' and appends them to exMem
    '''
    header = ""
    currmembers = []
    with open(currentMem,"r+") as currmemfile: #I chose w+ as I start reading first, then write/seek
        with open(exMem,"a") as exmemfile:
            header = currmemfile.readline()   #store header, and put this back as first line
            
            for line in currmemfile:
                linelist = line.split()

                if(linelist[2]=="no"):
                    # append to exmemfile
                    exmemfile.write(line)
                else:
                    currmembers.append(line)

        currmemfile.seek(0,0)
        currmemfile.write(header)

        for m in currmembers:
            currmemfile.write(m)

        currmemfile.truncate()   #if mode r+


# Code to help you see the files
# Leave as is
memReg = 'members.txt'
exReg = 'inactive.txt'
cleanFiles(memReg,exReg)


headers = "Membership No  Date Joined  Active  \n"
with open(memReg,'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())
    
with open(exReg,'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())
                
    
