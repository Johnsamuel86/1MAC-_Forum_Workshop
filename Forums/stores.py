class MemberStore:
    members = []
    last_id = 1
    members_by_name = []


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

    def update(self, member):
        old_member = self.get_by_id(member.id)
        MemberStore.members[MemberStore.members.index(old_member)] = member

    def get_by_name(self, member_name):
        for member in self.get_all():
            if member.name == member_name:
                self.members_by_name.append(member)
        return self.members_by_name

    def entity_exists(self, member):
        return member == self.get_by_id(member.id)


    def delete(self, id):
        member = self.get_by_id(id)
        MemberStore.members.remove(member)


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

    def entity_exists(self, post):
        return post == self.get_by_id(post.id)

    def delete(self, id):
        post = self.get_by_id(id)
        PostStore.posts.remove(post)

    def update(self, post):
        old_post = self.get_by_id(post.id)
        PostStore.posts[MemberStore.members.index(old_post)] = post

