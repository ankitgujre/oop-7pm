# for i in "MyBlog":
#     print(i, "?")

# for i in range(5):
#     print(i)

# for i in range(10, 15):
#     print(i)

# for i in range(0, 10, 2):
#     print(i)

# for i in range(10, 0, -2):
#     print(i)

# wap to print table

# n = int(input("Enter a number: "))

# for i in range(1,11):
#     print(n, "x", i, "=", n*i)



# wap to to find sum of the digits of a number

num = int(input("Enter a number: "))
sum = 0
while num > 0:
    digit = num % 10
    sum += digit
    num //= 10
print("The sum of the digits is:", sum)
