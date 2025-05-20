with open('output.txt','w') as file:
    file.write(input('Enter the text to write to the file: '))
    print('Data successfully written to output.txt.')
with open('output.txt','a') as file:
    file.write('\n'+input('Enter additional text to append: '))
    print('Data successfully appended.')
    print('Final content of output.txt:')
with open('output.txt','r') as file:
    print(file.read(),end='')