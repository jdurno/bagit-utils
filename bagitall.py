import os
import bagit
import xml.etree.ElementTree as ET

directory = "/top/level/directory/of/contents/to/be/bagged"

print directory

#get a list of all the directories one level down from the top level
def get_immediate_subdirectories(directory):
    return [name for name in os.listdir(directory)
            if os.path.isdir(os.path.join(directory, name))]


subdirs = get_immediate_subdirectories(directory)
subdirs.sort()

#track the number of bags and how many we've made
numBags = len(subdirs)
print numBags
bagNum = 0

for subdir in subdirs:
	print subdir
	bagNum += 1
	
	currentDir = os.path.join(directory,subdir)
	#print currentDir
	
	myXml = os.path.join(directory, subdir, 'Metadata', subdir + '_Metadata.xml')
	#print myXml
	
	tree = ET.parse(myXml)
	root = tree.getroot()

	for original in root.findall('Original'):
		
		#Title
		title = original.find('Title')
		if title is None:
			title = "None"
		else:
			title = original.find('Title').text
			title = title.replace('\n', ' ').replace('\r', '')
		
		#Archive Number
		archiveNumber = original.find('ArchiveNumber')
		if archiveNumber is None:
			archiveNumber = "None"
		else:
			archiveNumber = original.find('ArchiveNumber').text
			archiveNumber = archiveNumber.replace('\n', ' ').replace('\r', '')
		
		#Markings
		markings = original.find('Markings')
		if markings is None:
			markings = "None"
		else:
			markings = original.find('Markings').text
			markings = markings.replace('\n', ' ').replace('\r', '')
		
		#Running Time
		runningTime = original.find('RunningTime')
		if runningTime is None:
			runningTime = "None"
		else:
			runningTime = original.find('RunningTime').text
			runningTime = runningTime.replace('\n', ' ').replace('\r', '')
		
		#Record Date
		recordDate = original.find('RecordDate')
		if recordDate is None:
			recordDate = "None"
		else:
			recordDate = original.find('RecordDate').text
			recordDate = recordDate.replace('\n', ' ').replace('\r', '')
		

	print title, archiveNumber, markings, runningTime, recordDate

	myMetadata = {}
	myMetadata['Source-Organization'] = 'University of Victoria Libraries';
	myMetadata['Organization-Address'] = 'McPherson Library University of Victoria PO Box 1800 STN CSC Victoria, BC, Canada V8W 3H5';
	myMetadata['Contact-Name'] = 'John Durno';
	myMetadata['Contact-Phone'] = '+1 250-472-5069';
	myMetadata['Contact-Email'] = 'jdurno@uvic.ca';
	myMetadata['External-Description'] = 'Videos from the University of Victoria Archives';
	myMetadata['Bagging-Date'] = '2015-01-08';
	myMetadata['External-Identifier'] = archiveNumber;
	myMetadata['Bag-Group-Identifier'] = 'UnivOfVictoriaLibrary_999_DRV01';
	myMetadata['Bag-Count'] = "%d of %d" % (bagNum, numBags);
	myMetadata['Title'] = title;
	myMetadata['Markings'] = markings;
	myMetadata['Running-Time'] = runningTime;
	myMetadata['Record-Date'] = recordDate;
	
	#print myMetadata


 	bag = bagit.make_bag(currentDir, myMetadata)

