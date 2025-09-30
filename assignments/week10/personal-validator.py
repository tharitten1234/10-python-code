"""
Create a Personal Information Validator program that:
    Asks user for their name, age, and phone number
    Validates that name contains only alphabetic characters and spaces
    Converts age from string to integer and validates it's between 18-65
    Validates phone number contains exactly 10 digits
    
    Uses appropriate string methods for validation
    Displays formatted output with proper string formatting
    
    USE: isalpha(), isdigit(), upper(), string formatting with % or .format()
    
Example Result

=== PERSONAL INFORMATION VALIDATOR ===
Enter your name: John Doe
Enter your age: 25
Enter your phone number: 9876543210

Validation Results:
Name: Valid (contains only letters and spaces)
Age: Valid (25 years old)
Phone: Valid (10-digit number)

Formatted Information:
Name: JOHN DOE
Age Group: Young Adult (18-30)
Phone: +91-9876543210

"""

print("=== PERSONAL INFORMATION VALIDATOR ===")
name = input("Enter your name: ")
age = input("Enter your age: ")
phone_number = input("Enter your phone number: ")

#name = "John Doe"
#age = "25"
#phone_number = "9876543210"



# validate name
nameFlag =True

for char in name:
    print(char, char.isalpha())
    if char.isalpha() or char !=" ":
        nameFlag = True
    else:
        nameFlag = False
        break

#validate age
ageFlag = True
if int(age) < 18 or int > 65:
    ageFlag = False

#validate phone number
phoneFlag = True
if len(phone_number) != 10:
    phoneFlag = False
else:
    for char in phone_number:
        if char.isdigit() == False:
            phoneFlag = False
            break

print("Validation Results:")

if nameFlag == True:
    print("Name: Valid (contains only letters and spaces)")
else:
    print("Name: Invalid (contains only letters and spaces )")

if ageFlag == True:
    print(f"Age: Valid ({age} year old)")
    print("Age: Valid (%d year old)" % int(age))
else:
    print("Age: Invalid (less then 18 or more than 65)")

if phoneFlag == True:
    print("Phone: Valid (10-digit number)")
else:
    print("Phone: Invalid (not 10-digit number)")

print("Formatted Information:")
print("Name: %s" % name.upper())
#print(name.upper(), name.lower(), name.title(), name.capitalize)
if int(age) >= 18 and int(age) <= 30:
    print("Age Group: Young Adult (18-30)")
else:
    print("Age Group: not Young Adult")
print(F"Phone: +66{phone_number}")