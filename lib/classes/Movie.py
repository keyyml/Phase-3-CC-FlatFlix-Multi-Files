class Movie:

    all = []
     
    def __init__(self, title):
        self.title = title

        self._reviews = []
        self._reviewers = []

        Movie.all.append(self)

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        if type(title) == str and len(title) > 0:
            self._title = title
        else: 
            raise Exception("Titles must be of type str.Titles must be longer than 0 characters.")
        
    def reviews(self):
        return self._reviews

    def reviewers(self):
        return list(set(self._reviewers))

    def average_rating(self):

        if len(self._reviews) == 0:
            return None
        else:
            avg = sum([review.rating for review in self._reviews]) / len(self._reviews)
            return round(avg, 1)
        
    @classmethod
    def highest_rated(cls):
        top_movie = None
        top_rating = 0
        for movie in cls.all:
            average_rating = movie.average_rating()
            if average_rating > top_rating:
                top_movie = movie
                top_rating = average_rating

        return top_movie