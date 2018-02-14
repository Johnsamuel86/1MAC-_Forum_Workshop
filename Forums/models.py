import uuid

class Member():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Member Class is initialized successfully !!")

class Post():
    def __init__(self, title, content, uid=None):
        self.title = title
        self.content = content
        self.uid = uuid.uuid4().hex if uid is None else uid
        print("Post Class is initialized successfully !!")

