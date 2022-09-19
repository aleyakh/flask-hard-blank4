from setup_db import db

from marshmallow import fields, Schema


class DirectorSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


class GenreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


class MovieSchema(Schema):
    id = fields.Int(dump_only=True)
    description = fields.Str()
    rating = fields.Float()
    title = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    director = fields.Nested(DirectorSchema)
    genre_id = fields.Nested(GenreSchema)
