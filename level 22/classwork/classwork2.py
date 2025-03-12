
# 1
num = 1
while num <= 5:
    print(num)
    num += 1



#2

num = 1
sum_numbers = 0

while num <= 10:
    sum_numbers += num
    num += 1

print("total:", sum_numbers)


#3

n = int(input("enter your number: "))
num = 1

while num <= n:
    print(num)
    num += 1



#4
correct_password = "1234"
password = ""

while password != correct_password:
    password = input("enter your password: ")

print("password is right !!")



#5

correct_number = 7
guess = -1  

while guess != correct_number:
    guess = int(input("guess the numbers: "))

print("you guessed the number right !!.")






