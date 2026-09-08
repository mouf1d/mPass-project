from password import Password
from checker import Checker

print("╔══════════════════════════════════════╗")
print("║                mPASS                 ║")
print("║       Password Security Auditor      ║")
print("╚══════════════════════════════════════╝")
print()

mdp = input("Enter password: ")

password = Password(mdp)
checker = Checker()

print()
print("────────────────────────────────────────")
print("           SECURITY ANALYSIS")
print("────────────────────────────────────────")
print()

print(f"Length                 : {checker.check_length(password)} characters")
print(f"Unique characters      : {checker.check_caracteres_diff(password)}")
print(f"Character classes      : {checker.check_caracteres_classes(password)}")
print(f"Entropy                : {checker.check_entropy(password):.2f} bits")
print(f"Repeated character     : {checker.check_repeated_char(password)} time(s)")
print(f"Sequence               : {'✓ Not detected' if not checker.check_sequences(password) else '✗ Detected'}")
print(f"Repeated pattern       : {'✓ Not detected' if not checker.check_repeated_patterns(password) else '✗ Detected'}")
print(f"Dictionary             : {'✓ Not detected' if not checker.check_dictionary(password) else '✗ Detected'}")

score = checker.calculer_score(password)

print()
print("────────────────────────────────────────")
print(f"SECURITY SCORE         : {score}/100")

barre = "█" * (score // 5) + "░" * (20 - score // 5)
print(f"{barre}")
print("────────────────────────────────────────")

l = input("\nPress Enter to exit...")