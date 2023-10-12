class Review:

    all = []

    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating

        viewer._reviews.append(self)
        viewer._reviewed_movies.append(movie)

        movie._reviews.append(self)
        movie._reviewers.append(viewer)

        Review.all.append(self)

    @property
    def viewer(self):
        return self._viewer
    @viewer.setter
    def viewer(self, viewer):
        from classes.Viewer import Viewer
        if isinstance(viewer, Viewer):
            self._viewer = viewer
        else:
            raise Exception("Viewier must be an instance of the viewer class.")
        
    @property
    def movie(self):
        return self._movie
    @movie.setter
    def movie(self, movie):
        from classes.Movie import Movie
        if isinstance(movie, Movie):
            self._movie = movie
        else: 
            raise Exception("Movie must be an instance of the movie class.")
        
    @property
    def rating(self):
        return self._rating
    @rating.setter
    def rating(self, rating):
        if type(rating) == int and 1 <= rating <= 5 and not hasattr(self, "rating"):
            self._rating = rating
        else: 
            raise Exception("Ratings must be of type int. Ratings must be between 1 and 5, inclusive")