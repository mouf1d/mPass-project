import math
ALPHABET_MIN = "abcdefghijklmnopqrstuvwxyz" #26
ALPHABET_MAJ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #26
CHIFFRES = "0123456789" #10
CARACTERES_SPECIAUX = r"""#$%&'!"()*+,-./:;<=>?@[\]^_`{|}~""" #32
ALPHABET_POSITION = {
    "a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5,
    "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11,
    "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17,
    "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23,
    "y": 24, "z": 25,

    "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5,
    "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11,
    "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17,
    "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23,
    "Y": 24, "Z": 25,

    "0": 0, "1": 1, "2": 2, "3": 3, "4": 4,
    "5": 5, "6": 6, "7": 7, "8": 8, "9": 9
}

class Password: 
    def __init__(self,password):
        self.password = password
        self.len = len(password)

class Checker:
    def __init__(self):
        pass

    def check_length(self,password):
        return password.len

    def check_caracteres_diff(self,password):
        letter = []
        for i in password.password:
            if i not in letter:
                letter.append(i)
        return len(letter)
    
    def check_caracteres_classes(self,password):
        lowercase = []
        uppercase = []
        digit = []
        special = []
        for i in password.password:
            if i in ALPHABET_MIN:
                lowercase.append(i)
            elif i in ALPHABET_MAJ:
                uppercase.append(i)
            elif i in CHIFFRES:
                digit.append(i)
            elif i in CARACTERES_SPECIAUX:
                special.append(i)
        compteur = 0
        if len(lowercase) >=1:
            compteur += 26
        if len(uppercase) >=1:
            compteur +=26
        if len(digit) >= 1:
            compteur += 10
        if len(special) >=1:
            compteur += 32
        return compteur

    def check_entropy(self,password):
        a = math.log2(self.check_caracteres_classes(password))
        b = password.len * a
        return b

    def check_repeated_char(self,password):
        d = {}
        l = []
        for i in password.password:
            if i not in d.keys():
                d[i] = 1
            else:
                d[i] += 1
        for j in d.values():
            l.append(j)
        l.sort()
        return l[-1]

    def check_sequences(self, password):

    # il y a une sequence quand 3 caracteres se suivent (exemple: 123, abc, cba)

        for i in range(len(password.password) - 2):

            if ALPHABET_POSITION[password.password[i + 1]] == ALPHABET_POSITION[password.password[i]] + 1:
                if ALPHABET_POSITION[password.password[i + 2]] == ALPHABET_POSITION[password.password[i + 1]] + 1:
                    return True

            if ALPHABET_POSITION[password.password[i + 1]] == ALPHABET_POSITION[password.password[i]] - 1:
                if ALPHABET_POSITION[password.password[i + 2]] == ALPHABET_POSITION[password.password[i + 1]] - 1:
                    return True

        return False

    def check_repeated_patterns(self,password):

    # cherche les motifs qui se repetent tout en se suivant
        repeated_patterns = {}
        liste = []
        n = password.len

        for i in range(2,int(n/2)):
            if n%i == 0:
                liste.append(i)
        
        for i in liste:
            j = int(n/i)
            p = password.password
            
            while j>0:
                m = len(p)
                pattern = p[:i]
                if pattern == p[i:i*2]:
                    if pattern not in repeated_patterns.keys():
                        repeated_patterns[pattern] = 1
                        j -= 1
                        p = p[:m-i]
                    else:
                        repeated_patterns[pattern] += 1
                        j -= 1
                        p = p[:m-i]
                else:
                    j -= 1
                    p = p[:m-i]

        if repeated_patterns:
            return True

        return False

    def check_dictionary(self,password):
        with open("wordlist.txt", "r") as lines:
            for line in lines:
                line =line.strip()
                if password.password == line:
                    return True
                if line in password.password:
                    return True
                
        return False

        
            
            









