class MemberStore:
    members = []

    @staticmethod
    def get_all():
        return MemberStore.members

    @staticmethod
    def add(member):
        MemberStore.members.append(member)


class PostStore:
    posts = []

    @staticmethod
    def create(member_name, post_title, post_content, uid):
        PostStore.posts.append([member_name, post_title, post_content, uid])

    @staticmethod
    def find_post(title):
        for post in PostStore.posts:
            if post[1] == title:
                return post


    @staticmethod
    def read(title):
        if PostStore.find_post(title) is not None:
            return PostStore.find_post(title)
        return "No post found that match your input to read"

    @staticmethod
    def update(title, new_content):
        post = PostStore.find_post(title)
        if post is not None:
            post[2] = new_content
            return post
        return "No post found that match your input to update"

    @staticmethod
    def delete(title):
        post = PostStore.find_post(title)
        if post is not None:
            return PostStore.posts.pop(PostStore.posts.index(post))
        return "No post found that match your input to delete"
