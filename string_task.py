# Foundations 3: Python
# Task One


# In this task, the user should be given a story with gaps that the user should fill to complete the story.
#                                  So basically a game of mad libs.



print("Mad libs where libs get Mad")

#\n prints newline. 
print(" Start Below: \n")

#input() always saves a string. If the user enters 4, it will be saved in the variable as the string "4" not as int.
number = input("Number: ")
noun = input("Noun(plural): ")
name = input("Name: ")
sentence = input("Any sentence: ")
verb = input("Verb: ")

print("\n")
print("    It was " + number + " o'clock when I heard a knock at the door.")

#title() method returns a string with first letter of each word capitalized.
#\" prints double quotes
print("    I opened the door and there was a box full of " + noun +" with a note saying" + " \"From Mr. " + name.title() + "\".") 

#upper() method converts all lowercase characters into uppercase characters.
print("    Just as I closed the door I heard a scream \"" + sentence.upper() + "\".") 
print("    I froze in place and all I could do was " + verb + ".") 