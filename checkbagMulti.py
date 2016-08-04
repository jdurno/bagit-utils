import os
import bagit

#validate contents of multiple bags in a directory

directory = "/TLD/of/bags/to/be/checked"


def checkBag(bagDir):
	bag = bagit.Bag(bagDir)
	if bag.is_valid():
    		print "Valid Bag! Yay!"
	else:
    		print "BAD bag. Bad bad bag."

def get_immediate_subdirectories(directory):
    return [name for name in os.listdir(directory)
            if os.path.isdir(os.path.join(directory, name))]

subdirs = get_immediate_subdirectories(directory)

for subdir in subdirs:
	print subdir

	myBagDir = os.path.join(directory, subdir)
	checkBag(myBagDir)






