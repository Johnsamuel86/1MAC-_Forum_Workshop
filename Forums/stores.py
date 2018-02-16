class MemberStore:
    members = []
    last_id = 1


    def get_all(self):
        return self.members

    def add(self, member):
        member.id = self.last_id
        self.members.append(member)
        self.last_id += 1

    def get_by_id(self, id):
        for member in self.get_all():
            if member.id == id:
                return member

    def entity_exists(self, member):
        if member == self.get_by_id(member.id):
            return True

    def delete(self, id):
        member = self.get_by_id(id)
        self.members.remove(member)
        return "Member is removed successfully"


class PostStore:
    posts = []
    last_id = 1


    def get_all(self):
        return self.posts

    def add(self, post):
        post.id = self.last_id
        self.posts.append(post)
        self.last_id += 1

    def get_by_id(self, id):
        for post in self.get_all():
            if post.id == id:
                return post

    def entity_exists(self, post):
        if post == self.get_by_id(post.id):
            return True

    def delete(self, id):
        post = self.get_by_id(id)
        self.posts.remove(post)
        return "Post is removed successfully"
