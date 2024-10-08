import json

class dataset:

    

    def insert_user(self, name, email, password):
        # Check if email contains "@" and "." and if "@" comes before "."
        if "@" not in email or "." not in email or email.index("@") > email.index("."):
            return "Invalid email format."

        # Open the database file and load the data
        with open('/home/ghost/Python DS/NLPApp/db.json', 'r') as rf:
            database = json.load(rf)

        # Check if the email already exists in the database
        if email in database:
            return 0
        else:
            # Insert the new user data
            database[email] = [name, password]
            with open('/home/ghost/Python DS/NLPApp/db.json', 'w') as wf:
                json.dump(database, wf, indent=4)
                return 1



    def search(self,email,password):
        with open('/home/ghost/Python DS/NLPApp/db.json','r') as rf:
            database = json.load(rf)

        if email in database:
            if database[email][1] == password:
                return 1
            else:
                return 0
            
        else:
            return 0