cars=["bmw", "audi", "porsche"]
for car in cars:
    if car=="bmw":
        print(car.upper())
    else:
        print(car.title())

# 5-1
x='5'
if x=='5':
    print("yes")
else:
    print("no")

x="6"
if x!="8":
    print("not equal")
else:
    print("equal")

a='1'
if a > "0":
    print("yes")
else:
    print("no")

a='1'
if a < "0":
    print("yes")
else:
    print("no")

a='1'
if a > "0" and a < "2":
    print("yes")
else:
    print("no")

a='1'
if a < "0" or a < "-1":
    print("yes")
else:
    print("no")

a=10
b=20
if a > 5 and b  > 15:
    print("True")
else:
    print("hmm")

age = 19
if age >= 18:
    print("You are old enough to vote!")

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

# 5-3
alien_colour="red"
if alien_colour=="red":
    print("the player just earned 5 points")

alien_colour="red"
if alien_colour=="green":
    print("the player just earned 5 points")

# 5-4
alien_colour="green"
if alien_colour=="yellow":
    print("the player just earned 5 points")
else:
    print("the player just earned 10 points")

# 5-5
alien_colour="yellow"
if alien_colour=="red":
    print("the player just earned 5 points")
elif alien_colour=="green":
    print("the player just earned 10 points")
else:
    print("the player just earned 15 points")

# 5-6
age = 18
if age < 2:
    print("the person is a baby")
elif age >= 2 and age < 4:
    print("the person is a toddler")
elif age >= 4 and age < 13:
    print("the person is a kid")
elif age >= 13 and age < 20:
    print("the person is a teen")
elif age >= 20 and age < 65:
    print("the person is a adult")
else:
    print("the person is a elder")

# 5-7
favourite_fruits=["banana", "apple", "kiwi"]
print(favourite_fruits)
for favourite_fruit in favourite_fruits:
    if favourite_fruit=="banana":
        print("i really like banana")
    if favourite_fruit=="apple":
        print("i really like apple")
    if favourite_fruit=="kiwi":
        print("i really like kiwi")
if favourite_fruit!="orange":
    print("it is not my favourite fruit")
if favourite_fruit!="dragon fruit":
    print("it is not my favourite fruit")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")

# 5-8
usernames=[ "naman6", "admin" , "dhesi69", "dhruv1602", "katik123" ]
for username in usernames:
    if username=="admin":
        print("Hello admin, would you like to see the status report")
    else:
        print(f"Hello {username}, thank you for logging in again ")

# 5-9
usernames=[]
if usernames:
    for usename in usernames:
        print(f"Hello {username}, thank you for logging in again ")
else:
    print("We need to find some users")

# 5-10
current_usernames=[ "naman6", "admin" , "dhesi69", "dhruv1602", "katik123" ]
new_usernames=["madhusudhan146", "hello123", "parth216", "dhruv1602", "katik123"]
current_usernames_lower = [usernames.lower() for usernames in current_usernames]

# Check uniqueness of new usernames
for usernames in new_usernames:
    if usernames.lower() in current_usernames_lower:
        print(f"Sorry, the username '{usernames}' is already taken. Please choose another one.")
    else:
        print(f"The username '{usernames}' is available. You can proceed with this username.")

# 5-11
nums=[1,2,3,4,5,6,7,8,9]
for num in nums:
    if num == 1:
        print("1st")
    if num == 2:
        print("2nd")
    if num == 3:
        print("3rd")
    if num == 4:
        print("4th")
    if num == 5:
        print("5th")
    if num == 6:
        print("6th")
    if num == 7:    
        print("7th")
    if num == 8:
        print("8th")
    if num == 9:
        print("9th")


