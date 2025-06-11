import time

def calculate_average(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    average = total / len(numbers)
    return average

def greet_users(users):
    for i in range(0, len(users)):
        print("Hello " + users[i])

def countdown(n):
    while n >= 0:
        print(n)
        time.sleep(1)

def main():
    numbers = [10, 20, 30, 40]
    avg = calculate_average(numbers)
    print("Average is: " + avg)

    users = ["Alice", "Bob", "Charlie"]
    greet_users(users)

    countdown("5")

main()
