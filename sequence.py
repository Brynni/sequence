n = int(input("Enter the length of the sequence: ")) # Do not change this line
sum_num=0
num_first=0
num_second=1
num_third=2
n=n+1

print (num_second)
print (num_third)
for number in range(3,n):
    sum_num=num_first+num_second+num_third

    
    if num_first<num_second and num_first<num_third:
        num_first=(num_first-num_first)+sum_num
        
    elif num_second<num_first and num_second<num_third:
        num_second= (num_second-num_second)+sum_num
        
    elif num_third<num_second and num_third<num_first:
        num_third = (num_third-num_third)+ sum_num

    
    print(sum_num)



    
