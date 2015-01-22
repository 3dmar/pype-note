#!/usr/bin/env python

import codecs
import os
from jinja2 import Environment, FileSystemLoader
from ConfigParser import ConfigParser
from datetime import date


config = ConfigParser()
config.read('config.ini')


def get_template(path):
    #tplenv = Environment(autoescape=False, loader=FileSystemLoader(os.path.join(path, 'templates')), trim_blocks=False)
    return(Environment(autoescape=False, loader=FileSystemLoader(os.path.join(path, 'templates')), trim_blocks=False))


def render_template(tplenv, tfilename, context):
    return(tplenv.get_template(tfilename).render(context))


def write_content(tplenv, contentpath, filename, article, context={}):
    with codecs.open(contentpath + filename, "w", encoding='utf-8') as fh:
        meta = list(dict(config.items('Metadata')))

        context['content'] = article
        context['Date'] = date.today().strftime("%Y-%m-%d %H:%M")

        for key in meta:
            if not config.get("Metadata", key):
                context[key] = str(raw_input("Enter the %s for article publish: " % (key))).decode('utf-8')
            else:
                context[key] = config.get("Metadata", key)

        new = render_template(tplenv, 'metadata.tpl', context)
        fh.write(new)
