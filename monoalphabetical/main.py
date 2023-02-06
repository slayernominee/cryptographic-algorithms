"""

Monoalphabetical Encryption

tutorial made by slayernominee

"""

mapping = {
    "a": "q",
    "b": "w",
    "c": "e",
    "d": "r",
    "e": "t",
    "f": "z",
    "g": "u",
    "h": "i",
    "i": "o",
    "j": "p",
    "k": "a",
    "l": "s",
    "m": "d",
    "n": "f",
    "o": "g",
    "p": "h",
    "q": "j",
    "r": "k",
    "s": "l",
    "t": "y",
    "u": "x",
    "v": "c",
    "w": "v",
    "x": "b",
    "y": "n",
    "z": "m"
}

def encrypt_text(text: str, mapping: dict) -> str:
    """change the characters like the mapping says

    Args:
        text (str): the original string
        mapping (dict): the monoalpabetical mapping

    Returns:
        str: the encrypted string
    """
    
    encrypted_text = text.lower()
    
    for letter, value in mapping.items():    
        encrypted_text = encrypted_text.replace(letter, f"&{letter}")
    
    for letter, value in mapping.items():
        encrypted_text = encrypted_text.replace(f"&{letter}", value)
        
    return encrypted_text
    
    
def decrypt_text(encrypted_text: str, mapping: dict) -> str:
    """redo the characters like the mapping says

    Args:
        encrypted_text (str): the encrypted string
        mapping (dict): the monoalpabetical mapping

    Returns:
        str: the decrypted string
    """

    text = encrypted_text.lower()
    
    for letter, value in mapping.items():    
        text = text.replace(value, f"&{value}")
    
    for letter, value in mapping.items():
        text = text.replace(f"&{value}", letter)
        
    return text
    
secret_message = "hello world this is a secret message with a q"
chiffre = encrypt_text(secret_message, mapping)
print(chiffre)
decrypted_message = decrypt_text(chiffre, mapping)
print(decrypted_message)

# ! the attack vector: frequency analyses
""" 
if the text is long enought then there is a certain 
distribution of letters e.g. the e is the most common
so you can get the value for the e and then you know 
the "the" is the most common word in the english language
so if you find a lot of  3 letter pack that ends with the 
mapping for e that you found out you can say with a high
guarantee that this word is the and so on then you know 3
letters and you can check if you can find other words and you
will get the mapping and decrypted text after a while
"""

from collections import Counter 

# ! solving the sample_decrypted_text
with open("monoalphabetical/sample_decrypted_text.txt", 'r') as f:
    sample_decrypted_text = f.read()

letter_list = list(sample_decrypted_text)
cnt = Counter(letter_list) 
e_encrypted  = cnt.most_common(2)[1][0] # the most common one here is the space (but this is here not encrypted) so I take the 2nd item
print(e_encrypted) # the most common letter

word_list = sample_decrypted_text.split(' ')
cnt = Counter(word_list)
print(cnt.most_common(1)[0]) # 3 letters and ending with the encrypted letter for e 
# this item is most likely the THE 
# JBL = THE
encryption = sample_decrypted_text.replace("J", "t")
encryption = encryption.replace("B", "h")
encryption = encryption.replace("L", "e")

print(encryption) # the text with the replacements

# see the Dt at the beginning I would guess it is "it" because it ends with t and has 2 letters and
# the next word starts with the D also which if its a "i" would make sense as the beginning would
# be "it is" so lets try this

encryption = encryption.replace("D", 'i')
encryption = encryption.replace("K", 's')

print(encryption)
# it is C QeXiWI WF SiGiU PCX. XeReU sQCSeshiQs, stXiHiET FXWZ C hiIIeE RCse, hCGe PWE theiX FiXst GiStWXO CTCiEst the eGiU TCUCStiS eZQiXe. IYXiET the RCttUe, XeReU sQies ZCECTeI tW steCU seSXet QUCEs tW the eZQiXe’s YUtiZCte PeCQWE, the IeCth stCX, CE CXZWXeI sQCSe stCtiWE Pith eEWYTh QWPeX tW IestXWO CE eEtiXe QUCEet. QYXsYeI RO the eZQiXe’s siEisteX CTeEts, QXiESess UeiC XCSes hWZe CRWCXI heX stCXshiQ, SYstWIiCE WF the stWUeE QUCEs thCt SCE sCGe heX QeWQUe CEI XestWXe FXeeIWZ tW the TCUCVO…

# after it is a single letter is most likely a a "it is a "
encryption = encryption.replace("C", 'a')
# also there are a lot of tW which could be good a to
encryption = encryption.replace("W", 'o')
print(encryption)

# now there is this theiX which is most likely a their
encryption = encryption.replace("X", 'r')
print(encryption)

# the seSret looks like secret
encryption = encryption.replace("S", 'c')
print(encryption)

# starshiQ = starship
encryption = encryption.replace("Q", 'p')
# siEister = sinister
encryption = encryption.replace("E", 'n')
print(encryption)

# perioI = period
encryption = encryption.replace("I", 'd')
# striHinT = striving? 
encryption = encryption.replace("H", 'v')
encryption = encryption.replace("T", 'g')
print(encryption)

# eZpire = empire
encryption = encryption.replace("Z", 'm')
# gaUactic = galactic
encryption = encryption.replace("U", 'l')
# dYring = during
encryption = encryption.replace("Y", 'u')
print(encryption)

# oF ciGil Par  = of civil war
encryption = encryption.replace("F", 'f')
encryption = encryption.replace("G", 'v')
encryption = encryption.replace("P", 'w')
print(encryption)

# victorO = victory
encryption = encryption.replace("O", 'y')
# Rattle = battle (a bit context because galactic empire spaceship evil and so on i guess)
encryption = encryption.replace("R", 'b')
print(encryption)

# galaVy = galaxy
encryption = encryption.replace("V", 'x')
print(encryption)

# the text is:
# it is a period of civil war. rebel spaceships, 
# striving from a hidden base, have won their first
# victory against the evil galactic empire. during
# the battle, rebel spies managed to steal secret
# plans to the empire’s ultimate weapon, the death
# star, an armored space station with enough power to
# destroy an entire planet. pursued by the empire’s
# sinister agents, princess leia races home aboard her
# starship, custodian of the stolen plans that can save
# her people and restore freedom to the galaxy…