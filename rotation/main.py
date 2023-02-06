"""

Cäsar / Roation Encryption / Decryption

tutorial made by slayernominee

"""

from string import ascii_uppercase

def rotate_string(text: str, rotation: int) -> str:
    """rotate characters of the text

    Only A-Z are allowed

    Args:
        text (str): the original text
        rotation (int): characters it should rotate

    Returns:
        str: the rotated string
    """
    
    chiffre = ""
    text = text.replace(' ', '').upper()
    
    for letter in text:
        index = ascii_uppercase.index(letter) + rotation
        if index > 25: index = index - 26
        chiffre += ascii_uppercase[index]
        
    return chiffre

def brute_force(chiffre: str) -> list:
    possible_solutions = []
    print('\npossible messages:\n')
    for i in range(26):
        possible_solution = rotate_string(chiffre, i)
        print(possible_solution)
        possible_solutions.append(possible_solution)
    return possible_solutions

text = "hello world this message is a secret"
rotation = 3
chiffre = rotate_string(text, rotation)
print(chiffre)

brute_force(chiffre)