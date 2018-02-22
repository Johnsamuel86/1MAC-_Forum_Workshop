from Forums import models
class MemberStore:
    members = []
    last_id = 1


    def get_all(self):
        return MemberStore.members

    def add(self, member):
        member.id = self.last_id
        MemberStore.members.append(member)
        self.last_id += 1

    def get_by_id(self, id):
        for member in self.get_all():
            if member.id == id:
                return member
        return None

    def update(self, member):
        old_member = self.get_by_id(member.id)
        MemberStore.members[MemberStore.members.index(old_member)] = member

    def get_by_name(self, member_name):
        members_by_name = []
        for member in self.get_all():
            if member.name == member_name:
                members_by_name.append(member)
        return members_by_name

    def entity_exists(self, member):
        try:
            return member == self.get_by_id(member.id)
        except:
            print("Member Can't be None")


    def delete(self, id):
        member = self.get_by_id(id)
        MemberStore.members.remove(member)

    def get_members_with_posts(self,posts):
        models.Member.posts = [post for member in self.get_all() for post in posts if member.id == post.id]
        return (member for member in self.get_all())

    def get_top_two(self, posts):
        members_with_posts = self.get_members_with_posts(posts)
        sorted_members = sorted(members_with_posts, key=lambda member: len(member.posts), reverse=True)
        return sorted_members[:2]

class PostStore:
    posts = []
    last_id = 1


    def get_all(self):
        return PostStore.posts

    def add(self, post):
        post.id = self.last_id
        PostStore.posts.append(post)
        self.last_id += 1

    def get_by_id(self, id):
        for post in self.get_all():
            if post.id == id:
                return post
        return None

    def entity_exists(self, post):
        try:
            return post == self.get_by_id(post.id)
        except:
            print("Post Can't be None")

    def delete(self, id):
        post = self.get_by_id(id)
        PostStore.posts.remove(post)

    def update(self, post):
        old_post = self.get_by_id(post.id)
        PostStore.posts[MemberStore.members.index(old_post)] = post

