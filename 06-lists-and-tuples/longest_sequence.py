Consecutive1 = input("Enter the first consecutive number: ")
Consecutive2 = input("Enter the second consecutive number: ")
Consecutive3 = input("Enter the third consecutive number: ")

Consecutive_list = []
Consecutive_list.append(Consecutive1)
Consecutive_list.append(Consecutive2)
Consecutive_list.append(Consecutive3)


Consecutive_list.sort(reverse = True)

print(Consecutive_list[0])