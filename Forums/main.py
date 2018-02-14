from Forums.models import Member,Post
from Forums.stores import MemberStore,PostStore

memberstore = MemberStore()
poststore = PostStore()

member1 = Member("John", 32)
memberstore.add(member1.name)
member2 = Member("Ahmed", 25)
memberstore.add(member2.name)

print(memberstore.get_all())

post1 = Post("Topic1", "This is the first topic !!!")
poststore.create(member1.name, post1.title, post1.content, post1.uid)
post2 = Post("Topic2", "This is the second topic !!!")
poststore.create(member1.name, post2.title, post2.content, post2.uid)
post3 = Post("Topic3", "This is the third topic !!!")
poststore.create(member2.name, post3.title, post3.content, post3.uid)


print(poststore.read("Topic2"))  # can be done with Id but it is easier with title
print(poststore.read("Topic3"))  # can be done with Id but it is easier with title
print(poststore.read("Topic"))   # should give error msg
print(poststore.read("Topic1"))  # can be done with Id but it is easier with title

print(poststore.get_all())

print(poststore.update("Topic2", "This is the new topic after modified !!"))
print(poststore.update("Topic", "This topic isn't exist yet !!"))  # should give error msg

print(poststore.delete("Topic"))  # should give error msg
print(poststore.delete("Topic3"))

print(poststore.get_all())
