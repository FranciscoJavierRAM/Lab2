# I want this program to ask the user for their first pets name. After that ask the user how old they were when they got said pet. Then print "Wow, you were only (age) when you first got (pets name). Thats awesome.".
# Step 1 Ask for the users first pet's name
print("What was your first pets name?")
#Step 2 Input the pets name and save it for later use
pet_name = input()
#Step 3 Ask how old were you when you got (pets name)
print ("How old were you when you got " + str(pet_name))
#Step 4 Input the users age when they got their first pet
age = input()
#Step 5 Say "Wow you were only (users age) when you got (pets name). Thats awesome."
print ("Wow, you were only " + str(age) + " when you got " + str(pet_name) + "." + " That's awesome.")