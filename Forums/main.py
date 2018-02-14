from Forums.models import Member,Post
from Forums.stores import MemberStore,PostStore

member1 = Member("John", 32)
MemberStore.add(member1.name)
member2 = Member("Ahmed", 25)
MemberStore.add(member2.name)

print(MemberStore.get_all())

post1 = Post("Topic1", "This is the first topic !!!")
PostStore.create(member1.name, post1.title, post1.content, post1.uid)
post2 = Post("Topic2", "This is the second topic !!!")
PostStore.create(member1.name, post2.title, post2.content, post2.uid)
post3 = Post("Topic3", "This is the third topic !!!")
PostStore.create(member2.name, post3.title, post3.content, post3.uid)


print(PostStore.read("Topic2"))  # can be done with Id but it is easier with title
print(PostStore.read("Topic3"))  # can be done with Id but it is easier with title
print(PostStore.read("Topic"))   # should give error msg
print(PostStore.read("Topic1"))  # can be done with Id but it is easier with title


print(PostStore.update("Topic2", "This is the new topic after modified !!"))
print(PostStore.update("Topic", "This topic isn't exist yet !!"))

print(PostStore.delete("Topic"))  # should give error msg
print(PostStore.delete("Topic3"))

print(PostStore.posts)
