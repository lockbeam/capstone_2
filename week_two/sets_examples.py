# sets - unordered collection

cats = set() #creates empty set
cats.add('Lion')
cats.add('Tiger')
print(cats)
cats.add('Cheetah')
print(cats)



#order will change everytime it's printed because of how sets work
#doesn't allow duplicates

#another way of creating a set:
birds = {'owl', 'robin', 'swan'}
print(birds)
birds.add('robin')
print(birds) #robin doesn't get added again - only included once
birds.remove('owl')
birds.add('duck')
print(birds)

for bird in birds:
    print(bird + ' :)')


bird_list = ['owl', 'robin', 'swan', 'eagle', 'duck', 'swan', 'chickadee', 'duck']
#want to remove dups? convert to set and then back to list!
bird_list_no_duplicates = list(set(bird_list)) # new list of set of bird_list
# lose the order if doing the above, something to keep in mind if order is important