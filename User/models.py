from mongoengine import Document, SequenceField, StringField, EmailField


class User(Document):
    userId = SequenceField(required=False, primary_key=True)
    name = StringField(required=True, max_length=50)
    email= EmailField(required=True)
    password = StringField(required=True, max_length=50)
    

   