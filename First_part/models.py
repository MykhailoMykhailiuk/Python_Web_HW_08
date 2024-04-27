from mongoengine import Document, ReferenceField
from mongoengine.fields import ListField, StringField, DateTimeField


class Authors(Document):
    full_name = StringField()
    born_date = DateTimeField()
    born_location = StringField()
    description = StringField()


class Quotes(Document):
    tags = ListField()
    author = ReferenceField(Authors)
    quote = StringField()
