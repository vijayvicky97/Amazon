list1 = [15, 18, 2, 3, 6, 12]

def BSearch(list1,start,end):
    #find mid value
    mid = int((start+end)/2)
    #if mid+1 element is less than middle element mid is returned
    if mid < end and list1[mid+1] < list1[mid]:
        return mid+1
    #if mid element is less than middle element mid-1 middle is returned
    elif mid>start and list1[mid-1] > list1[mid]:
        return mid
    if list1[mid] < list1[end]:
        return BSearch(list1,start,mid-1)
    else:
        return BSearch(list1,mid+1,end)
print(BSearch(list1,0,len(list1)-1))