#this script is to generate train.txt val.txt and test.txt for your dataset
#please put this file under ImageSets folder and run python Gentxt.py in cmd.


import re
import os


path = 'Main/'
filenames = os.listdir(path)

train = []
val = []
test = []
for file in filenames:
    content = ""
    with open(path + file, 'r') as f:
        if file.endswith('_train.txt'):
            content = f.read()
            get = re.findall(r'(\S+)[ ]+1\n', content)
            train += get
        if file.endswith('_val.txt'):
            content = f.read()
            get = re.findall(r'(\S+)[ ]+1\n', content)
            val += get
        if file.endswith('_test.txt'):
            content = f.read()
            get = re.findall(r'(\S+)[ ]+1\n', content)
            test += get
train = set(train)
print('find %d files for training.\n'%(len(train)))
val = set(val)
print('find %d files for validation.\n'%(len(val)))
test = set(test)
print('find %d files for testing.\n'%(len(test)))

with open(path + 'train.txt', 'w') as f:
    for item in train:
        f.write(item + '\n')
with open(path + 'val.txt', 'w') as f:
    for item in val:
        f.write(item + '\n')
with open(path + 'test.txt', 'w') as f:
    for item in test:
        f.write(item + '\n')
