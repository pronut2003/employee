class Contact:
    def __init__(self,phno,email):
        self.phone_no = "999999999"
        self.email = "xyz@gmail.com"
        self.set_phone(phno)
        self.set_email(email)

    def __str__(self):
        return f"{self.phone_no},{self.email}"

    def set_phone(self,phno):
        if len(phno) == 10:
            self.phone_no = phno
            return True
        else:
            print("invalid phone number")
            return False
    def set_email(self,email):
        if "@" in email and "." in email and " " not in email :
            self.email = email
            return True
        else:
            print("invalid email entered")
            return False







