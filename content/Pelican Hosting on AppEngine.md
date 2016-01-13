Title: Pelican Hosting on AppEngine
Date: 2016-01-13 20:15
Modified: 2016-01-13 22:30
Category: Web Development
Tags: python, pelican, git, appengine
Slug: pelican-hosting-on-appengine
Authors: Craig J Perry
Summary: How I made a fast personal site and hosted it on Google AppEngine.

Google App Engine (GAE) hosting is fast! Here's how i setup my blog using the [Pelican](http://getpelican.com) static site generator and deployed it on [Google AppEngine](https://cloud.google.com/appengine/).

## Install Pelican & AppEngine

First I created an empty git repo. Then i created a Python virtualenv to host Pelican and the AppEngine SDK. This saves polluting my system with particular versions of pelican and appengine since i might want to use other versions in other projects.

    [me@s1 Code]$ git init blog
    [me@s1 Code]$ cd blog
    [me@s1 blog]$ virtualenv .venv
    (.venv)[me@s1 blog]$ echo ".venv" > .gitignore
    (.venv)[me@s1 blog]$ git add !$
    (.venv)[me@s1 blog]$ git commit -m 'chore(gitignore): Prevent transient virtualenv from being added to git.'
    (.venv)[me@s1 blog]$ git checkout -b 'setup'
    (.venv)[me@s1 blog]$ echo appengine-sdk > requirements.txt
    (.venv)[me@s1 blog]$ echo pelican >> requirements.txt
    (.venv)[me@s1 blog]$ echo markdown >> requirements.txt
    (.venv)[me@s1 blog]$ pip install -r requirements.txt

## Create An AppEngine Site

I created a new project in the [Google Developers Console](https://console.developers.google.com). I chose to host it in the EU datacentre (an option in the advanced menu).

Next i created the AppEngine "application"  which is nothing more than some static files in a directory with the `app.yaml` file to tell AppEngine how to serve the app.

#### Directory Structure

    blog/
      .git/
      .gitignore
      appengine/
        blog/
        app.yaml

#### app.yaml

    application: craigjperryblog
    version: 1
    runtime: python27
    api_version: 1
    threadsafe: yes

    handlers:

    - url: /
    static_files: blog/index.html
    upload: blog/index.html
    
    - url: /
    static_dir: blog

## Create The Blog

You can create a Pelican blog using the `pelican-quickstart` command but it creates a bunch of files i don't need. Instead, i just want the bare essentials: a `pelicanconf.py` file and a `content/` directory for my blog post sources.

#### Directory Structure

    blog/
      .git/
      .gitignore
      appengine/
        blog/
        app.yaml
      content/
      pelicanconf.py

#### pelicanconf.py

    #!/usr/bin/env python
    # -*- coding: utf-8 -*- #
    from __future__ import unicode_literals

    AUTHOR = u'Craig J Perry'
    SITENAME = u"Craig's Notebook"
    SITEURL = 'http://www.craigjperry.com'

    PATH = 'content'
    OUTPUT_PATH = 'appengine/blog'

    TIMEZONE = 'Europe/London'

    DEFAULT_LANG = u'en'

    FEED_ALL_ATOM = None
    CATEGORY_FEED_ATOM = None
    TRANSLATION_FEED_ATOM = None
    AUTHOR_FEED_ATOM = None
    AUTHOR_FEED_RSS = None

    DEFAULT_PAGINATION = False
    RELATIVE_URLS = True

## Adding A Theme

I [chose a theme](www.pelicanthemes.com) then added it to my git repo. For "vendor" code like this, i really don't like submodules in Git. There's a much better way:

    (.venv)[me@s1 blog]$ git remote add -f svbhack https://github.com/gfidente/pelican-svbhack.git
    (.venv)[me@s1 blog]$ git merge -s ours --no-commit svbhack/master
    (.venv)[me@s1 blog]$ git read-tree --prefix=themes/svbhack -u svbhack/master
    (.venv)[me@s1 blog]$ echo "THEME = 'themes/svbhack'" > pelicanconf.py
    (.venv)[me@s1 blog]$ git commit -m 'Import svbhack theme'

Now i can follow changes from upstream at my leisure. I can also conveniently maintain local changes. Even complex changes thanks to [git's "rerere" feature](https://git-scm.com/blog/2010/03/08/rerere.html). 

## Writing Content

When creating new posts i take a new branch in git. I write the markdown and add the static assets. As i go along i have pelican regenerating the site in the background:

    (.venv)[me@s1 blog]$ pelican --debug --autoreload &

I serve the site using AppEngine's local dev server:

    (.venv)[me@s1 blog]$ dev_appserver.py appengine/

## Publishing

I refresh the generated content then upload new site version using the AppEngine cli:

    (.venv)[me@s1 blog]$ pelican content/
    (.venv)[me@s1 blog]$ appcfg.py -A craigjperryblog update appengine/

## Extras

AppEngine supports versioning of your deployed app. You can trial new changes to your site without affecting the main site, or even just preview draft posts you're writing on a "beta" url. Just change the `version` attribute in your `app.yaml`.
