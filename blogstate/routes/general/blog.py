from blogstate import app
from blogstate.api import SecureAgent
from flask import (
    render_template,
    session
)

agent = SecureAgent()


@app.route('/<username>/')
def blog(username):
    """Fetch and display publically visible blog posts by an author"""
    posts = agent.fetch_posts_by_author(username)
    if posts:
        return render_template("posts.html",
                               user=session,
                               posts=posts,
                               author=username)
    return render_template("404.html")
