# write a python code to find if the given number is odd or even?

def check_odd_even(number):
    if number % 2 == 0:
        return "The number is even."
    else:
        return "The number is odd."

number = int(input("Enter a number: "))
result = check_odd_even(number)
print(result)
