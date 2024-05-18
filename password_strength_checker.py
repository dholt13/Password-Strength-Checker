from tkinter import *

root = Tk()
root.title("Password Strength Checker")
root.geometry("1000x500")
root.config(bg="skyblue")

def Take_Input(password):

    # Get the length of the password
    password_length = len(password)

    hasLowercase = False
    hasUppercase = False
    hasDigit = False
    specialChar = False
    normalChar = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in range(password_length):
        if password[i].islower():
            hasLowercase = True
        if password[i].islower():
            hasUppercase = True
        if password[i].isdigit():
            hasDigit = True
        if password[i] not in normalChar:
            specialChar = True
    
    #Checks the strength of the password and displays the results
    if (hasLowercase and hasUppercase and hasDigit and specialChar and password_length >= 10):
        display_results.insert(END, "Strong")
    elif ((hasLowercase or hasUppercase) and specialChar and password_length >= 8):
        display_results.insert(END, "Moderate")
    else: 
        display_results.insert(END, "Weak")

#This section clears the text that are in the text boxes
def clear():
    input_text.delete("1.0", 'end-1c')
    display_results.delete("1.0", 'end-1c')

title = Label(root, text="Hello, this is a Password Strength Checker!")
title.config(font=("Candara", 14), bg="skyblue")
description = Label(root, text="For a password to be considered strong it satisfies the following criteria:")
description.config(font=("Candara", 14), bg="skyblue")
criteria = Label(root, text="1. It contains one lowercase character.\n 2. It contains one uppercase character.\n 2. It contains at least one special character The special characters are: !@#$%^&*()-+.\n 4. Its length is a least 10.\n 5. It contains at least one digit\n\n Enter a password below: ")
criteria.config(font=("Candara", 14), bg="skyblue")

#This section is for the user to enter the password and passing the input to the Take_input function
input_text = Text(root, height=2, width=25)
submit_button = Button(root, height=2, width=10, text="Submit", command=lambda:Take_Input(str(input_text.get("1.0", 'end-1c'))))

#This section outputs the passowrd strength checker results
output_text = Label(root, text="The password strengh: ")
output_text.config(font=("Candara", 14), bg="skyblue")
display_results = Text(root, height=2, width=25)

clear_button = Button(root, height=2, width=10, text="Clear", command=clear)
#Closes the program
exit_button = Button(root, height=2, width=10, text="Exit", command=root.destroy)


title.pack()
description.pack()
criteria.pack()
input_text.pack()
submit_button.pack()
output_text.pack()
display_results.pack()
clear_button.pack()
exit_button.pack()
root.mainloop()


