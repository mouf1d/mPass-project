import math
import os
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
            if password.password[i] not in ALPHABET_POSITION or password.password[i + 1] not in ALPHABET_POSITION or password.password[i + 2] not in ALPHABET_POSITION:
                continue
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
        for i in range(2,int(n/2)+1):
            if n%i == 0:
                liste.append(i)

        for k in range(n):
            for i in liste:
                j = int((n-k)/i)
                p = password.password[k:]

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
        with open(os.path.join(os.path.dirname(__file__), "wordlist.txt"), "r") as lines:
            for line in lines:
                line =line.strip()
                if password.password == line:
                    return True
                if line in password.password:
                    return True
                
        return False

    def calculer_score(self,password):
        score = 0

        # notation en fonction de la longueur du mot de passe
        if self.check_length(password) < 8:
            pass
        elif self.check_length(password) >= 8 and self.check_length(password) <= 11:
            score += 5
        elif self.check_length(password) >= 12 and self.check_length(password) <= 15:
            score += 10
        elif self.check_length(password) >= 16 and self.check_length(password) <= 19:
            score += 15
        elif self.check_length(password) >= 20:
            score += 20

        # notation en fonction de la diversité des caractères
        diversite = self.check_caracteres_diff(password) / self.check_length(password)
        if diversite < 0.30:
            pass
        elif diversite >= 0.30 and diversite < 0.50:
            score += 5
        elif diversite >= 0.50 and diversite < 0.70:
            score += 9
        elif diversite >= 0.70 and diversite < 0.90:
            score += 12
        elif diversite >= 0.90:
            score += 15

        # notation en fonction des classes de caractères
        classes = self.check_caracteres_classes(password)
        if classes == 26 or classes == 10 or classes == 32:
            score += 3
        elif classes == 36 or classes == 42 or classes == 58:
            score += 7
        elif classes == 62 or classes == 68 or classes == 84:
            score += 11
        elif classes == 94:
            score += 15

        # notation en fonction de l'entropie
        entropy = self.check_entropy(password)
        if entropy < 40:
            pass
        elif entropy >= 40 and entropy < 60:
            score += 10
        elif entropy >= 60 and entropy < 80:
            score += 20
        elif entropy >= 80 and entropy < 100:
            score += 25
        elif entropy >= 100:
            score += 30

        # notation en fonction des caractères répétés
        repetition = self.check_repeated_char(password) / self.check_length(password)
        if repetition <= 0.20:
            score += 20
        elif repetition > 0.20 and repetition <= 0.30:
            score += 14
        elif repetition > 0.30 and repetition <= 0.40:
            score += 8
        elif repetition > 0.40:
            pass

        # malus en cas de séquence
        if self.check_sequences(password):
            score -= 10

        # malus en cas de motifs répétés
        if self.check_repeated_patterns(password):
            score -= 10

        # malus en cas de présence dans le dictionnaire
        if self.check_dictionary(password):
            score -= 20

        if score < 0:
            score = 0
        elif score > 100:
            score = 100

        return score