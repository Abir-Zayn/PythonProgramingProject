#Input:
#Creating an console based project where user will enter a message where it will encrypted or decrypted. Ask for user direction whether 
#if he needs to encrypt a message or decrypted .If the user input is encrypted then starts shifting values to rightwards. If the
#user input is decrypted then shifting to leftwards. 
#If the user entered shifting value more than 10 then assign it with 10 .
#print out the encrypted or decrypted message. 
#Following that ask again if they want to run the program again .If yes run it again .If its no then stop.





#defining a function
def choice_decision(text,shift,direction): 
    final_text=""
    shift=int(shift)    #converting to int 
   

    if(direction =="encode"): #check for encode or decode
        if(shift >= 10 ):     #if the shift value greated than 10 reassign
            f_shift = 10
        
        else:               
            f_shift =shift
            for letter in text:
                if(letter in alphabet):             #check for letter in alphabet
                    postion =alphabet.index(letter)    #find its index
                    new_postion = postion+f_shift        #shifting by final shift value
                    new_letter = alphabet[new_postion]      #getting value by its position 
                    final_text = final_text+ new_letter         #adding values in the list

            
                if(letter in number):                        #check for letter in alphabet
                    positionNumeric = number.index(letter)
                    new_number_position = positionNumeric+f_shift
                    new_number = number[new_number_position]
                    final_text = final_text+new_number

                if(letter in symbol):                           #check for letter in alphabet
                    positionSymbol =symbol.index(letter)
                    new_symbol_position = positionSymbol+f_shift
                    new_symbol = symbol[new_symbol_position]
                    final_text = final_text+ new_symbol
            
    
        print(f"The encoded message is : {final_text}")
    
    elif(direction =="decode"):

        final_text=""

        if(shift >=10 ):
            f_shift = 10
        else:
            f_shift = shift
            for letter in text:
                if(letter in alphabet):
                    postion =alphabet.index(letter)
                    new_postion = postion-f_shift
                    new_letter = alphabet[new_postion]
                    final_text = final_text+ new_letter

            
                if(letter in number):
                    positionNumeric = number.index(letter)
                    new_number_position = positionNumeric-f_shift
                    new_number = number[new_number_position]
                    final_text = final_text+new_number

                if(letter in symbol):
                    positionSymbol =symbol.index(letter)
                    new_symbol_position = positionSymbol-f_shift
                    new_symbol = symbol[new_symbol_position]
                    final_text = final_text+ new_symbol
        
        print(f"The dencoded message is : {final_text}")
    
    else :
        print("The value you inserted is not valid.")


alphabet =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
'q','r','s','t','u','v','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
'q','r','s','t','u','v','x','y','z']

number=['0','1','2','3','4','5','6','7','8','9','0','1','2','3','4','5','6','7','8','9']

symbol =['@','#',' ','!','+','-','&','*','/','{','}','[',']','$','^','@','#',' ','!','+','-','&','*','/','{','}','[',']','$','^']

direction = input("Type 'encode' to encrypt and 'decode' to decrypt ")
user_text = input("Type your message: \n").lower()
user_shift = input("Type the shift number :\n ")



choice_decision(text=user_text, direction=direction, shift=user_shift)

run_again=True
while(run_again):
    print("Type 'yes' if you want to run again 'no' to exit the program. ")
    user_choice = str((input())).lower()
    if(user_choice == "yes"):
        direction = input("Type 'encode' to encrypt and 'decode' to decrypt ")
        user_text = input("Type your message: \n").lower()
        user_shift = input("Type the shift number :\n ")
        choice_decision(text=user_text, direction=direction, shift=user_shift)
    else :
        run_again=False



