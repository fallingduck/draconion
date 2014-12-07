# Draconion

UPDATE 6/12/14: Draconion now generates a static site instead of dynamically serving files.

Draconion is the premier, super-simple blogging engine that most definitely wasn't written in 30 minutes(TM).

1. Have Python 2.7 installed on your system.
2. `git clone https://github.com/fallingduck/draconion.git`
3. `cd draconion`

To make a new post, create a new `.tpl` file in the `posts/` directory. Then, edit your `index.json` and append the information on the new post into the `posts` array.

Before you make your blog live, I suggest editing the following:

1. `index.json`
2. `static/templates/header.tpl` - The layout of the site, also see `static/resources/global.css`

Draconion is proudly powered by the [Bottle](http://bottlepy.org) microframework's SimpleTemplateEngine, and a stable version of Bottle is provided in this very repository.

When your site is ready to be deployed, run the following command:

`$ python2 draconion.py`

This command will create (or clean) the `compiled/` directory, and will populate it with your site's static content and freshly rendered static `html` files. You can point your webserver (nginx, apache, or whatever) to the `compiled/` directory, or you can move the `compiled/` directory to wherever your files will be served from.

HINT: If you set up your web server to serve cleaner URIs (eg. removing the .html extension), you can specify a different `uri` format in `index.json`

HINT: Stick your `.htaccess` file in `static/resources/.htaccess`
