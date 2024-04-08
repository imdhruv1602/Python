print("Hello World!")

n=str(input("Enter something: "))
print(n)

message="hey how are you"
print(message)

new_message="i am fine"
print(new_message)

name="banglore"
print(name.title())

name="banglore"
print(name.upper())
print(name.lower())

start_name="lucky"
last_name="grover"
full_name=f"{start_name} {last_name}"
print(full_name)

start_name="lucky"
last_name="grover"
full_name=f"{start_name} {last_name}"
print(f"hello {full_name.title()}")

tart_name="lucky"
last_name="grover"
full_name=f"{start_name} {last_name}"
message = (f"hello {full_name.title()}")
print(message)

print("python")
print("\tPython")

print("languages:\n\tPython\n\tC\n\tJava")

favourite_language='python '
n=favourite_language.rstrip()
print(n)

url="https.//google.com"
# similarly we can remove suffix also
n=url.removeprefix("https.//")                               
print(n)

# power
n=2**3
print(n)

# multiplication
n=2*3
print(n)

# addition
n=2+3
print(n)

# subtraction
n=2-3
print(n)

# division
m=2/3
n=2//3 
print(m)
print(n)

# equation
# Arithmetic Operators: From highest to lowest precedence, these are ** (exponential), * (multiplication), / (division), + (addition), - (subtraction).
# Comparison Operators: These include == (equal), != (not equal), <= (less than or equal to), >= (greater than or equal to), < (less than), > (greater than).
# Logical Operators: not has the highest precedence, followed by and, and then or.
# Bitwise Operators: Bitwise AND &, OR |, and XOR ^.
# Assignment Operators: The assignment operator = is used to set values, while += and -= are compound assignment operators that perform an operation and an assignment in a single step.
n=2*3/4+2-5
print(n)

n="he's so cute"
print(n)

# 2-3
name="Eric"
print(f"Hello {name}, would you like to learn some python today?")

# 2-4
name = "dhruv"
print(name.upper())
print(name.lower())
print(name.title())

# 2-5
n='Virat Kohli once said, "Success do nothing it only boosts you ego"'
print(n)

# 2-6
famous_person="Virat Kohli"
print(f'{famous_person} once said, "Success do nothing it only boosts you ego"')

# 2-7
name="\tdhruv"
name2="dhruv\t"
print(name)
print(name.lstrip())
print(name2)
print(name2.rstrip())
name3="\tdhruv\t"
print(name3)
print(name3.strip())

# 2-8
file_name="python_notes.txt"
print(file_name.removesuffix(".txt"))

# 2-9
print(5+3)
print(11-3)
print(2*4)
print(24//3)

# 2-10
favourite_number="2"
print(f"my favourite number is {favourite_number}")