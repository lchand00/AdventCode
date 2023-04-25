with open('input.txt') as file:
    data = [i for i in file.read().strip().split("\n")]

#print(data)

max_sum=0
max_sum2=0
max_sum3=0
total=0
for item in data:
    if item=='':
        total=0
    else:
        num=int(item)
        total+=num

    if total > max_sum: 
        max_sum3 = max_sum2
        max_sum2 = max_sum
        max_sum = total
    elif total > max_sum2:
        max_sum3 = max_sum2
        max_sum2 = total    # Elf with second to most 
    elif total > max_sum3:
        max_sum3 = total    # Elf with third to most 



print(max_sum)

print(max_sum+max_sum2+max_sum3)
