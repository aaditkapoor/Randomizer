class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.hashcode = hash(self.first_name) + hash(self.last_name) + hash(self.email)
    

    def hashcode(self):
        return self.hashcode




class UserData:
    def __init__(self, user: "User", clicked_items):
        self.user = user
        self.clicked_items = clicked_items
        s = ""
        for c in self.clicked_items:
            s += c + ","
        
        self.clicked_items_data = s

    def get_user(self): 
        return self.user
    
    def length(self):
        return len(self.clicked_items)


        
