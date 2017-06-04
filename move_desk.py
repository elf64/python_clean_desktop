# Python version 2.7
import os
import time
import random
import sys
def run(argv):
	pukast = time.strftime('Desktop %Y-%m-%d')
	user = raw_input('Input your user:')
	desktop = 'C:\\Users\\{}\\Desktop'.format(user)
	public_desktop = 'C:\\Users\\Public\\Desktop'
	new_dir = 'C:\\Users\\{}\\Desktop\\{}--{}'.format(
		user,
		pukast,
		str(random.randint(0,1024))
	)
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
	move_files(
		all_files_name,
		desktop,
		new_dir
	)
	move_files(
		all_lnk_name,
		public_desktop,
		new_dir
	)
	print "Done."

def move_files(x, y, z):
	"""
	x -> list of all the files/folders
	y -> desktop path
	z -> new folder path
	"""
	p = 0
	for i in x:
		if p <= len(x):
			if ((x[p] not in sys.argv[2:]) and
				(x[p] != os.path.basename(__file__))):
				os.rename(
					"{}\\{}".format(y, x[p]),
					"{}\\{}".format(z, x[p])
				)
			else:
				pass
			p += 1
		else:
			break

run(sys.argv[1:])
