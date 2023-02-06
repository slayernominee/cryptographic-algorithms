"""

Vigenere cipher

tutorial made by slayernominee

"""

text = "helloworldthisismymessageanditneedstobeabitlongerbecausethatmakesiteasiertoattackitxdsoletsgo"

password = "makeitsecret"

# the text will now be encrypted via the password 
# therefor it will get the index of the password letter + 1 (a = 1, b = 2, ...)
# and then it will add this to the text letters index with this value

from string import ascii_lowercase

def encrypt_text(text: str, password: str) -> str:
    encrypted_text = ""
    longer_password = password
    for i in range(int(len(text) / len(password))):
        longer_password += password
    for i, letter in enumerate(text):
        letter_index = ascii_lowercase.index(letter)
        password_index = ascii_lowercase.index(longer_password[i])
        
        combi_index= letter_index + password_index
        if combi_index > 25: combi_index -= 26
        encrypted_text += ascii_lowercase[combi_index]
    
    return encrypted_text
        

encrypted_text = encrypt_text(text, password)
print(text)
print(encrypted_text)

# ! attacking vector
# we use our computer resources to try out any passwords that are possible 
# then we check for words with each password and only list the ones that makes 
# a bit sense (e.g. a lot of common words are found) -> then the attacker select 
# which is the real one