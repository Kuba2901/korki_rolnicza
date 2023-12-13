import json
from models import BlogPostManager, BlogPost

# Example usage
man = BlogPostManager("posts.json")

def main():
	man.dump_to_file()
# 	running = True
# 	while running:
# 		print("""1 - Create post
# 2 - Update post
# 3 - View post
# 4 - Delete post
# 5 - Exit""")

# 		num = input("> ")
# 		if "1" in num:
# 			print("[*] Adding new post")
# 			print("[?] Please provide post details")
# 			values = input("[id], [title], [content], [author], [created_at]: ")
# 			values = values.split(", ")
# 			if len(values) != 5: continue
# 			man.add_post(values[0], values[1], values[2], values[3], values[4])
# 		if "2" in num:
# 			print("[*] Updating post")
# 			print("[?] Please provide post id")
# 			values = input("[id], [title], [content]: ")
# 			values = values.split(", ")
# 			if len(values) != 3: continue
# 			man.update_post(values[0], values[1], json.loads((values[2])))
# 		if "3" in num:
# 			print("[*] Viewing post")
# 			print("[?] Please provide post id")
# 			id = input("post_id: ")
# 			man.view_post(id)
# 		if "4" in num:
# 			print("[*] Deleting post")
# 			print("[?] Please provide post id")
# 			id = input("post_id: ")
# 			if man.delete_post(id):
# 				print("[X] Post deleted")
# 		if "5" in num:
# 			print("[Q] Exiting")
# 			break
		
# 'update post', 'view post', and 'delete post'
#"title": "nowy tytul",
# "content": {
#   "content": "nowy content"
# },
# "author": "new author",
# "created_at": "20:21"
main()