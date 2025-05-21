# I want this program to ask the user for their first pets name. Ask their current age. Afterwards ask the user how old they were when they got said pet. Then print "Wow, you were only (age) when you got (pets name)! Finally the program will end by computing how many years ago the user got their first pet.
# Step 1 Ask for the users first pet's name.
print("What was your first pets name?")
#Step 2 Input the pets name and save it for later use.
pet_name = input()
# Step 3 Ask for the users current age.
print("How old are you now?")
# Step 4 Input the users current age and save it for later use.
current_age = input()
#Step 5 Ask the user how old were they when they got (pets name).
print ("How old were you when you got " + str(pet_name) + "?")
#Step 6 Input the users age when they got their first pet and save it for later use.
age = input()
#Step 7 Say "Wow, you were only (users age) when you got (pets name)!".
print ("Wow, you were only " + str(age) + " years old when you got " + str(pet_name) + "!")
#Step 8 Subtract age when user got their first pet from their current age to create str(time).
time = int(current_age)-int(age)
#Step 9 State how old the user was when they got their first pet.
print ("That means you got " + str(pet_name) + " " + str(time) + " years ago.")
print ("Crazy how fast time flies by.")