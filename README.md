# Draconion

Draconion is the premier, super-simple blogging engine that most definitely wasn't written in 30 minutes(TM).

1. Have Python 2.7 installed on your system.
2. `git clone https://github.com/fallingduck/draconion.git`
3. `cd draconion`
4. `python2 draconion.py`

To make a new post, create a new `.tpl` file in the `posts/` directory. Then, edit your `index.json` and append the information on the new post into the `posts` array.

Before you make your blog live, I suggest editing the following:

1. `index.json` - Specifically the blog tagline, title, and url
2. `static/templates/header.html` - Look for the `<h1>` tag

---

Draconion is proudly powered by the [Bottle](http://bottlepy.org) microframework, and a stable version of Bottle is provided in this very repository.

You may want to use something other than Bottle's built-in server for a production environment.
