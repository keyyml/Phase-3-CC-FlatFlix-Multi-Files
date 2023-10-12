class Viewer:
    def __init__(self, username):
        self.username = username

        self._reviews = []
        self._reviewed_movies = []

    @property
    def username(self):
        return self._username
    @username.setter
    def username(self, username):
        if type(username) == str and 6 <= len(username) <= 16:
            self._username = username
        else: 
            raise Exception 

    def reviews(self):
        return self._reviews

    def reviewed_movies(self):
        return list(set(self._reviewed_movies))

    def has_reviewed_movie(self, movie):
        return movie in self._reviewed_movies

    def add_review(self, movie, rating):
        from classes.Review import Review
        new_review = Review(self, movie, rating)
        return new_review