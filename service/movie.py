from dao.movie import MovieDAO


class MovieService:

    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_movies(self):
        return self.movie_dao.get_all_movies()

    def get_movie_by_id(self, uid):
        return self.movie_dao.get_movie_by_id(uid)

    def get_movie_by_kwargs(self, **kwargs):
        return self.movie_dao.get_by_kwargs(**kwargs)

    def create_movie(self, **kwargs):
        return self.movie_dao.create_movie(**kwargs)

    def update_movie(self, **kwargs):
        return self.movie_dao.update_movie(**kwargs)

    def delete_movie(self, uid):
        return self.movie_dao.delete_movies(uid)
