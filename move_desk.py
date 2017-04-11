# Python version 2.7
import os
import time
import random
import sys
#
# Re-write the script without the p2 and p cuz it's bad coded!
#
def run(argv):
    pukast = time.strftime('Desktop %Y-%m-%d')
    user = raw_input('Input your user:')
    desktop = 'C:\\Users\\{}\\Desktop'.format(user)
    public_desktop = 'C:\\Users\\Public\\Desktop'
    new_dir = 'C:\\Users\\{}\\Desktop\\{}--{}'.format(user, pukast, str(random.randint(0,1024)))
    p2 = 0
    p = 0
    if not os.path.isdir(desktop):
        print 'Specified path not found. ',
        print 'Path is \'{}\''.format(desktop)
        quit("Error 1")

    all_files_name = os.listdir(desktop)
    all_lnk_name = os.listdir(public_desktop)

    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
        print "New directory with name {} was made.".format(new_dir)
    print '-------------------'
    print sys.argv[2:]

    for i in all_lnk_name:
        if p2 <= len(all_lnk_name):
            if all_lnk_name[p2] not in sys.argv[2:]:
                os.rename(public_desktop+'\\{}'.format(all_lnk_name[p2]),
                    new_dir+'\{}'.format(all_lnk_name[p2]))
            else:
                pass
            p2 += 1
        else:
            break

    for i in all_files_name:
        if p <= len(all_files_name):
            if ((all_files_name[p] not in sys.argv[2:]) and
	    	(all_files_name[p] != os.path.basename(__file__))):
                os.rename(desktop+'\\{}'.format(all_files_name[p]),
                    new_dir+'\{}'.format(all_files_name[p]))
            else:
                pass
            p += 1
        else:
            break
    print "Done."

run(sys.argv[1:])
