from Forums.models import Member,Post
import Forums.stores

memberstore = Forums.stores.MemberStore()
poststore = Forums.stores.PostStore()

member1 = Member("John", 32)
memberstore.add(member1)
print(memberstore.get_by_id(1).name)

member2 = Member("Ahmed", 25)
memberstore.add(member2)
print(memberstore.get_by_id(2).name)
print(memberstore.get_all())

print(memberstore.entity_exists(member2))
print(memberstore.delete(2))
print(memberstore.get_all())

post1 = Post("Topic1", "This is the first topic !!!")
poststore.add(post1)
post2 = Post("Topic2", "This is the second topic !!!")
poststore.add(post2)
post3 = Post("Topic3", "This is the third topic !!!")
poststore.add(post3)

print(poststore.get_all())
print(poststore.get_by_id(3))
print(poststore.delete(1))
print(poststore.get_all())
