# You are given	an array and some number S. Determine if any two numbers within the array sum to S.
numbers = [1,2,3,4,5,6,7,8,9,10]
sum = 10
def two_sum(x):
    print("Test")
    for i in x:
        if(i + (i + 1) == sum):
            print(i, " and ", (i+1), " add up to ", sum)
        else:
            continue

if __name__ == '__main__':
    two_sum(numbers)
