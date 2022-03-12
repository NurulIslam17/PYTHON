
def binary_search(list,item):
    first=0
    last=len(list)-1
    mid=0

    while(first<=last):
        mid=(first+last)//2

        if (item < list[mid]):
            last = mid - 1
        elif(item>list[mid]):
            first = mid + 1
        else:
            return mid
        # element was not present , return -1
    return -1
list=[2,3,4,5,7,8,9]
item=7

result=binary_search(list,item)

if(result!=-1):
    print(f"{item} is found at index[{str(result)}]")
else:
    print(f"{item} not found")


