# example of a class doing too much work
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save_user(self):
        """sql logic"""
        print(f"{self.name} has been saved in the database")

    def validate_email(self):
        """nice regex logic"""
        print(f"{self.email} has been validated")

# better example of seperated concerns

class NewUser:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class SaveUser:
    def save(self, user):
        print(f"{user.name} has been saved in our database")

class ValidateEmail:
    def validate(self, user):
        print(f"{user.email} has been validated")