class MemberStore:
    members = []


    def get_all(self):
        return MemberStore.members

    def add(self, member):
        MemberStore.members.append(member)


class PostStore:
    posts = []

    def create(self, member_name, post_title, post_content, uid):
        PostStore.posts.append([member_name, post_title, post_content, uid])

    def get_all(self):
        return PostStore.posts

    @staticmethod
    def find_post(title):
        for post in PostStore.posts:
            if post[1] == title:
                return post


    def read(self, title):
        if PostStore.find_post(title) is not None:
            return PostStore.find_post(title)
        return "No post found that match your input to read"

    def update(self, title, new_content):
        post = PostStore.find_post(title)
        if post is not None:
            post[2] = new_content
            return post
        return "No post found that match your input to update"

    def delete(self, title):
        post = PostStore.find_post(title)
        if post is not None:
            return PostStore.posts.pop(PostStore.posts.index(post))
        return "No post found that match your input to delete"
