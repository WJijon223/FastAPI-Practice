from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate

app = FastAPI()

text_posts = {
    1: {
        "title": "New Post",
        "content": "cool test post"
    },
    2: {
        "title": "Learning Python",
        "content": "I've been learning Python recently and it's been a lot of fun!"
    },
    3: {
        "title": "My Weekend",
        "content": "Went hiking this weekend and somehow managed to get completely lost."
    },
    4: {
        "title": "Favorite Movies",
        "content": "What are some movies you think everyone should watch at least once?"
    },
    5: {
        "title": "First Day at Work",
        "content": "Started a new job today. Lots to learn, but I'm excited to see how it goes."
    },
    6: {
        "title": "Random Thought",
        "content": "Why does food always taste better when someone else makes it?"
    },
    7: {
        "title": "Project Update",
        "content": "Finally fixed the bug I've been stuck on for three days. It was one line of code."
    },
    8: {
        "title": "Coffee Recommendations",
        "content": "Looking for some good coffee recommendations. I usually prefer something not too bitter."
    },
    9: {
        "title": "Back to the Gym",
        "content": "First workout after taking a few weeks off. Tomorrow is going to hurt."
    },
    10: {
        "title": "Hello World!",
        "content": "Just joined and wanted to make my first post. Hello everyone!"
    }
}

@app.get("/posts")
def get_all_posts(limit: int):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts

@app.get("/posts/{id}")
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts.get(id)

@app.post("/posts")
def create_post(post: PostCreate):
    text_posts[max(text_posts.keys()) + 1] = {"title": post.title, "content": post.content}