text=str(input("enter a string: "))
print("the string is: ",text)
print("the length of the string is: ",len(text))
print("the string in uppercase is: ",text.upper())
print("the string in lowercase is: ",text.lower())
reversed_text=text[::-1]
print("the reversed string is: ",reversed_text)
text+=" World"
print("the updated string is: ",text)
print("the string starts with 'Hello': ",text.startswith("Hello"))
print("the string ends with 'World': ",text.endswith("World"))
print("the string contains 'lo Wo': ", "lo Wo" in text)
# --- IGNORE ---
print("the string after replacing 'Hello' with 'Hi': ",text.replace("Hello","Hi"))
print("the string after removing spaces: ",text.replace(" ",""))
#operation
A=10
B=5
C=A+B
print("The sum of A and B is: ",C)
D=A-B
print("The difference of A and B is: ",D)
E=A*B
print("The product of A and B is: ",E)
F=A/B
print("The quotient of A and B is: ",F)
g=A%B
print("The remainder of A divided by B is: ",g)
if A > B:
    print("A is greater than B")
elif A < B:
    print("A is smaller than B")
else:
    print("A is equal to B")
sunrise_time = "6:00 AM"
sunset_time = "6:00 PM"
print("The sunrise time is: ", sunrise_time)
print("The sunset time is: ", sunset_time)
sunny=input("Is it sunny today? (yes/no): ")
temperature=int(input("Enter the temperature in degrees Celsius: "))
if sunny.lower() == "yes" and temperature > 25:
    print("It's a great day to go outside and enjoy the sunshine.")
elif sunny.lower() == "no" and temperature < 20:
    print("It's a good day to stay indoors and read a book.")
else:
    print("It's a moderate day. You can do either activity.")
ch=input("Enter a character: ")
if ((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')):
    print("The character is a letter.")
else:
    print("The character is not a letter.")
    if ch.isdigit():
        print("The character is a digit.")
    else:
        print("The character is a special character.")
character=input("Enter a character: ")
anime=input("Enter your favorite anime: ")
print(f"The character {character} is from the anime {anime}.")

a=int (input("enter a number for a: "))
b=int (input("enter a number for b: "))
c=int (input("enter a number for c: "))
if a > b and a > c:
    print("a is the greatest number")
elif b > a and b > c:
    print("b is the greatest number")
else:
    print("c is the greatest number")

x=int (input("Enter a number for x: "))
y=int (input("Enter a number for y: "))
z=int (input("Enter a number for z: "))
B=int (input("Enter a number for B: "))
result = x + y * z / B
print("The result is:", result)
name=input("Enter your name: ")
age=int (input("Enter your age: "))
print("Hello,", name, "you are", age, "years old.")

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
d=int(input("Enter the distance in kilometers: "))
total_time = a + b + c
average_speed = d / total_time
print("The average speed is:", average_speed, "km/h")
if average_speed > 60:
    print("The average speed is above the speed limit.")
else:
    print("The average speed is within the speed limit.")