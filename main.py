from password import Password
from checker import Checker

mdp = input("Entrez votre mot de passe : ")

password = Password(mdp)
checker = Checker()

print(checker.calculer_score(password))