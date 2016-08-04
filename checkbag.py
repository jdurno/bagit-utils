import bagit

#validate contents of a single bag

bag = bagit.Bag('/bag/to/be/checked')

if bag.is_valid():
	print 'yay'
else:
	print 'boo'


