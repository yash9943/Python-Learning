import os

# select directory which content you want
directory_path = '/Web'

# use os module to list the directory
contents = os.listdir(directory_path)

# print the dirctorys
for item in contents:
    print(item)