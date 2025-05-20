try :
    file = open('sample.txt','r')
    content = file.readlines()
    lineNumber = 1
    for i in content:
        print('Line',str(lineNumber)+':',i,end='')
        lineNumber += 1
    file.close()
except FileNotFoundError:
    print('Error: The file \'sample.txt\' was not found.')