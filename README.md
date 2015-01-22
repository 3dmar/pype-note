**PyPe**-**Note**
Simple script to convert evernote notes on content for sites generated with the pelican framework.

##Install

Installation
Clone this repo with:

```bash
$ git clone https://github.com/adinanp/pype-note.git
$ cd pype-note
$ python setup.py install
```
_(Or click in "Clone in Desktop" button)_

##Usage

Simply on command line, type:
```bash
$ pypenote
````
_(This script is interactive, reply all questions and be happy.)_

##Tips

For example, my current theme requires on my content/post.md "author_gravatar". 

Thus, using the expansion added templates in my configuration file "/etc/pypenote/config.ini", the following line in the Metadata section.

author_gravatar ""

So to run the program I am asked about the image address.

Therefore, any information/metadata that should be added in posts in "content/post_example.md", can be added via the configuration file.
