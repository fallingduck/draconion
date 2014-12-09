#!/usr/bin/env python2


__author__ = 'Jack VanDrunen'
__version__ = '0.4'


import lib.stpl as bottle
import json
import shutil
import os
import sys
import time


bottle.TEMPLATE_PATH = ['./posts/', './static/content/', './static/templates/']


print 'Draconion {0} by {1}'.format(__version__, __author__)


if len(sys.argv) > 1:

    if sys.argv[1] == 'write' or sys.argv[1] == 'edit':
        filepath = './posts/{0}.tpl'.format(sys.argv[2])
        title = sys.argv[2].replace('-', ' ').title()
        if not os.path.exists(filepath):
            with open(filepath, 'w') as f:
                f.write("% include('header.tpl', title='{0}')\n\n".format(title))
                f.write("<h2>{0}</h2>\n".format(title))
                f.write("<p>Lorem ipsum dolor sit amet...</p>\n\n")
                f.write("% include('footer.tpl')\n")

        os.system('nano {0}'.format(filepath))
        print 'Done!'
        sys.exit(0)

    elif sys.argv[1] == 'delete':
        filepath = './posts/{0}.tpl'.format(sys.argv[2])
        if os.path.exists(filepath):
            os.remove(filepath)
            print 'Done!'
        else:
            print 'File does not exist!'
            sys.exit(0)
        link = sys.argv[2]
        with open('index.json', 'r') as f:
            data = json.load(f)

        for index, post in list(data['posts']):
            if post['link'] == link:
                data['posts'].pop(index)
                print 'Retracted!'
                break
        else:
            print 'Not published!'
            sys.exit(0)

        with open('index.json', 'w') as f:
            f.write(json.dumps(data, indent=2))
        print 'Annotated index.json'

    elif sys.argv[1] == 'publish':
        filepath = './posts/{0}.tpl'.format(sys.argv[2])
        if not os.path.exists(filepath):
            print 'File does not exist!'
            sys.exit(0)

        link = sys.argv[2]
        title = raw_input('Title: ')
        tagline = raw_input('Tagline: ')
        pubdate = time.strftime('%B %d, %Y')
        with open('index.json', 'r') as f:
            data = json.load(f)
        data['posts'].insert(0, {'title': title, 'link': link, 'date': pubdate, 'tagline': tagline})
        with open('index.json', 'w') as f:
            f.write(json.dumps(data, indent=2))
        print 'Annotated index.json'

    elif sys.argv[1] == 'retract':
        filepath = './posts/{0}.tpl'.format(sys.argv[2])
        if not os.path.exists(filepath):
            print 'File does not exist!'
            sys.exit(0)

        link = sys.argv[2]
        with open('index.json', 'r') as f:
            data = json.load(f)

        for index, post in list(data['posts']):
            if post['link'] == link:
                data['posts'].pop(index)
                print 'Retracted!'
                break
        else:
            print 'Not published!'
            sys.exit(0)

        with open('index.json', 'w') as f:
            f.write(json.dumps(data, indent=2))
        print 'Annotated index.json'

    elif sys.argv[1] == 'help' or sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print 'Usage: draconion <command> [<file>]'
        print
        print 'Commands:'
        print 'write    Create or edit a blog post'
        print 'delete   Delete a blog post'
        print 'publish  Publish a blog post'
        print 'retract  Unpublish a blog post (does not delete the draft)'
        print 'compile  Generate your site (default)'
        print
        sys.exit(0)

    elif sys.argv[1] != 'compile':
        print 'Unknown command!'
        sys.exit(0)


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

