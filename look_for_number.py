numbers = [1,2,3,4,5,6,7,8,9,10]
x = int(input("Type in a number to search >>: "))
# for element in numbers:
#     if(x == element):
#         print("Found")
#     else:
#         print("Not found...")
flag = True
index = 0
while (flag) or (index <= 9):
    if(x == numbers[index]):
        print("Found")
        flag = False
    else:
        index = index + 1
        # flag = False
        # print("Not found")
if(index == 9):
    print("Not found")