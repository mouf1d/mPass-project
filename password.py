class Password: 
    def __init__(self,password):
        if password.strip() == "":
            raise ValueError("Le mot de passe ne peut pas être vide.")
        self.password = password
        self.len = len(password)