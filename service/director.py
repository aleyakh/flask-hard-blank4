# здесь бизнес логика, в виде классов или методов. сюда импортируются DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.

# Пример
from typing import List

from dao.director import DirectorDAO


class DirectorService:

    def __init__(self, director_dao: DirectorDAO):
        self.director_dao = director_dao

    def get_directors(self) -> List[DirectorDAO]:
        return self.director_dao.get_all_directors()

    def get_director_by_id(self, uid):
        return self.director_dao.get_director_by_id(uid)
