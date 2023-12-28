from models import BlogPost, PostsManager

manager = PostsManager(1)
print(manager.get_json_res())