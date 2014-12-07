#!/usr/bin/env python2


__author__ = 'Jack VanDrunen'
__version__ = '0.3'


import lib.stpl as bottle
import json
import shutil
import os


bottle.TEMPLATE_PATH = ['./posts/', './static/content/', './static/templates/']


print 'Draconion {0} by {1}'.format(__version__, __author__)
print 'Cleaning and compiling to compiled/'


# First, clean ./compiled
if os.path.exists('./compiled'):
    shutil.rmtree('./compiled')


# Next, let's pull in all of the static resources
shutil.copytree('./static/resources/', './compiled/')


# Load index.json
with open('index.json', 'r') as f:
    index = json.load(f)


# If this *is* a blog...
if index.get('posts') is not None:

    # Render the posts
    for post in index['posts']:
        link = './compiled/{0}.html'.format(post['link'])
        with open(link, 'w') as f:
            f.write(bottle.template(post['link'], **index))

    # Render the RSS feed
    with open('./compiled/feed.xml', 'w') as f:
        f.write(bottle.template('rss', **index))

    # Render the archive, if one exists
    if index.get('archiveuri') is not None:
        with open('./compiled/{0}'.format(index['archiveuri']), 'w') as f:
            f.write(bottle.template('archive', **index))


# Render the error page
with open('./compiled/404.html', 'w') as f:
    f.write(bottle.template('error', **index))


# Render all of the extra pages included in index.json
for page in index['include']:
    link = './compiled/{0}.html'.format(page)
    with open(link, 'w') as f:
        f.write(bottle.template(page, **index))


print 'Done!'

