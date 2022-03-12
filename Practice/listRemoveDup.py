
numbers=[2,4,2,6,3,4,5,6,4,5,7]
uniques=[]
for item in numbers:
    if item not in uniques:
        uniques.append(item)
print(uniques)