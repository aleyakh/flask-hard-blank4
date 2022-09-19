from dao.model.models import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all_movies(self):
        return self.session.query(Movie).all()

    def get_movie_by_id(self, uid):
        return self.session.query(Movie).filter(Movie.id == uid).one()

    def get_by_kwargs(self, **kwargs):
        return self.session.query(Movie).filter_by(**kwargs).all()

    def create_movie(self, **kwargs):
        try:
            self.session.add(
                Movie(**kwargs)
            )
            self.session.commit()
            return True
        except Exception as error:
            print(error)
            self.session.rollback()
            return False


    def update_movie(self, **kwargs):
        try:
            self.session.query(Movie).filter(Movie.id == kwargs.get('id')).update(
                kwargs
            )
            self.session.commit()
            return True
        except Exception as error:
            print(error)
            self.session.rollback()
            return False

    def delete_movies(self, uid):
        try:
            self.session.query(Movie).filter(Movie.id == uid).delete()
            self.session.commit()
            return True
        except Exception as error:
            print(error)
            self.session.rollback()
            return False



