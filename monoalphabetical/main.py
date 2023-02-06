"""

Monoalphabetical Encryption

made by slayernominee

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

# ! the attack vector:
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

