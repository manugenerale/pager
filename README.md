pager
============

A django module to manage content on websites.

## Requirements ##

Press Review is developed on a Ubuntu system running:
   * [Python](http://python.org) 2.7
   * [Django](http://djangoproject.com) 1.5
   * [Django-Mptt]()
   * [Pillow]()


## Installing it ##

To enable `pager` in your project you need to add it to `INSTALLED_APPS` in your projects `settings.py` file::

    INSTALLED_APPS = (
            ...
                    'pager',
                            ...
    )

## Basic use ##

    Install this app, go to admin interface and enjoy. First, create a page and then add block content.
    On your template, call {% load pager %} and show the element you want with the tag {% show_block_content 'block.slug' %}

## Getting Involved ##

Open Source projects can always use more help. Fixing a problem, documenting a feature, adding translation in your language. If you have some time to spare and like to help us, here are the places to do so:

- GitHub: https://github.com/pepourquier/pager

## Documentation ##

For the moment, there is no good documentation for this app.

## Next features ##
    
   * Write tests
   * Write documentation
   * A lot of things

## Credits and License ##

Pierre-Emmanuel Pourquier create this. 

This program is free software: you can redistribute it and/or modify it under
the terms of either the GNU GENERAL PUBLIC LICENSE. See the file `COPYING.md` for details.
All dependencies and requirements also are under the terms of an open source licence.
