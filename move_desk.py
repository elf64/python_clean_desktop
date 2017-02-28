import os
import time
import random
import sys
def run(argv):
    pukast = time.strftime('Desktop %Y-%m-%d')
    user = raw_input('Input your user:')
    desktop = 'C:\Users\{}\Desktop'.format(user)
    new_dir = 'C:\Users\{}\Desktop\{}--{}'.format(user, pukast, str(random.randint(0,1024)))
    p = 0
    if not os.path.isdir(desktop):
        print 'Specified path not found. ',
        print 'Path is \'{}\''.format(desktop)
        quit("Error 1")

    all_files_name = os.listdir(desktop)
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
        print "New directory with name {} was made.".format(new_dir)
    print '-------------------'
    print sys.argv[2:]
    for i in all_files_name:
        if p <= len(all_files_name):
            if all_files_name[p] not in sys.argv[2:]:
                os.rename(desktop+'\\{}'.format(all_files_name[p]), new_dir+'\{}'.format(all_files_name[p]))
            else:
                pass
            p += 1
        else:
            break
    print "Done."

run(sys.argv[1:])
