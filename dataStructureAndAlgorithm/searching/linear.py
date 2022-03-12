
element=[2,5,5,3,4,5,9,23,77]
print(element)
search_item=int(input("\nEnter the search item : "))

isFound=False
for i in range(len(element)):
    if(element[i]==search_item):
        isFound=True
        print(f"{search_item} is Found at Index[{i}]")
        break
if(isFound==False):
    print(f"Not Found")




