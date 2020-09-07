def gcd(no1,no2):
    if no2 == 0:
        return no1
    return gcd(no2,no1%no2)

def func(list1,gcd_value):
    for length in range(gcd_value):
        index = length
        temp_var = list1[length]
        for iterator in range(int(len(list1)/gcd_value)):
            if not (index+gcd_value) > (len(list1)-1):
                list1[index] = list1[index+gcd_value]
                index += gcd_value
            else:
                list1[index] = temp_var
                break

list1 = [1,2,3,4,5,6,7,8,9,10,11,12]
gcd_value = gcd(len(list1),2)
func(list1,gcd_value)