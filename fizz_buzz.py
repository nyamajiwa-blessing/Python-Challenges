# Python code to solve Fizz-Buzz problem for numbers between 1 - 100
def fizz_buzz():
    for number in range(1,101):
        # test base case first
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz\n")
        elif number % 5 == 0:
            print("Buzz\n")
        elif number % 3 == 0:
            print("Fizz\n")
        else:
            print(number, " \n")

if __name__ == '__main__':
    fizz_buzz()