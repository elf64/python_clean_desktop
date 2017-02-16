import os
import time
import random

pukast = time.strftime('Desktop %Y-%m-%d')
user = raw_input('Input your user:')
desktop = 'C:\Users\{}\Desktop'.format(user)
new_dir = 'C:\Users\{}\Desktop\{}--{}'.format(user, pukast, str(random.randint(0,1024)))
all_files_name = os.listdir(desktop)
p = 0
# Verify user desktop path
if not os.path.isdir(desktop):
    print 'Specified path not found. ',
    print 'Path is \'{}\''.format(desktop)
    quit("Error 1")
# Verify if the current file we want to make is not allready created
if not os.path.exists(new_dir):
    os.makedirs(new_dir)
    print "New directory with name {} was made.".format(new_dir)
print '-------------------'
time.sleep(1)
for i in all_files_name:
    if p <= len(all_files_name):
        try:
            os.rename(desktop+'\\{}'.format(all_files_name[p]), new_dir+'\{}'.format(all_files_name[p]))
            p += 1
        except Exception as egg:
            print egg
            print all_files_name[p]
            quit()
print "Done."
