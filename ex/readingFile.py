
# open file with 'open('file', mode)' and store it inside var
random_file = open("random.txt", "r")   #'r' - read, 'w' - write, 'a' - append, 'r+' - r/w

# readable()
# print(random_file.readable()) # return boolean for 'r'
# read()
# print(random_file.read()) # print all file
# readline()
# print(random_file.readline()) #read individual line - the first line 
# print(random_file.readline()) #read individual line - the second line
# readlines()
# print(random_file.readlines()) # prints the list of the file - ['..\n','...\n','..\n',...]
# print(random_file.readlines()[1]) # prints specific element of the list

for el in random_file.readlines():
    print(el)


random_file.close()