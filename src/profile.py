class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.favourites = []

    def add_favourite(self, movie):
        self.favourites.append(movie)

    # def username(self):
    #     return ""
    
    # def password(self):
    #     return ""
    
    # def favourites(self):
    #     return []
        