# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

# Пример
from flask_restx import Resource, Namespace

from dao.model.schema import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')
genre_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenreView(Resource):
    def get(self):
        return genre_schema.dump(genre_service.get_genres()), 200


@genre_ns.route('/<int:uid>')
class GenreViews(Resource):
    def get(self, uid):
        return genre_schema.dump([genre_service.get_genre_by_id(uid=uid)]), 200

