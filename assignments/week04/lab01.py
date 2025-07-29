"""
Personal Information Manager 

#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to:

Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)

"""

# Complete this program
def personal_info_manager():
    # Create initial person tuple
    person = ("Tharit", 20, "Bangkok", "TH")  # name, age, city, country
    hobbies = []

    while True:
        choice =input("Pls select(1.diplay 2.hobby 3.remove hobby 4.edit age 5.exit)")
        
        # Your code here
        if choice == "1":
            #display info

            print("Name : ",person[0])
            print("Age : ",person[1])
            print("City : ",person[2])
            print("Country : ",person[3])
            print("Hobbies : ",hobbies)

        elif choice =="2":
            # add hobby
            hobby =input ("What is your hobby?: ")
            hobbies.append(hobby)
        
        elif choice =="3":
            #remove hobby
            del hobbies[0]

        elif choice =="4":
            person_list =list(person)
            age =int(input("How old are you?: "))
            person_list[1] = age
            person = tuple(person_list)

        elif choice =="5":
            break
            
            

if __name__ == "__main__":
    personal_info_manager()