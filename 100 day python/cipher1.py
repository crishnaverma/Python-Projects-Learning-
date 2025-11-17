
logo ='''           88             88                                 
                    ""             88                                 
                                   88                                 
          ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
         a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
         8b         88 88       d8 88       88 8PP""""""" 88          
         "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
          `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
                       88                                             
                       88                                            '''

print(logo)



alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#Function That take input and make shift

def cipher(original_text, shift_ammount,encode_decode):
    cipher_text=""
    

    if encode_decode == "decode":
                shift_ammount *= -1
                
    for letter in original_text:
       
        if letter not in alphabet:
             cipher_text +=letter

        else:

            shifted_position=alphabet.index(letter)+shift_ammount
            shifted_position %= len(alphabet)
            cipher_text+=alphabet[shifted_position]
    
    print(f"Here's the {encode_decode}d result:{cipher_text}")



continue_s = True

while continue_s:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:")
    text = input("Type your message:")
    shift = int(input("Type the shift number:"))


    cipher(text,shift,direction)

    reply= input("Type 'yes' if you want to go again else type 'no' \n")

    if reply=="no":
        continue_s=False
        print("Goodbye")