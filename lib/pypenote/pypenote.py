#!/usr/bin/python

from templates import *

from evernote.api.client import EvernoteClient
from os.path import abspath, dirname
from ConfigParser import ConfigParser
from html2text import HTML2Text
import sys
import evernote.edam.type.ttypes as Types
import evernote.edam.notestore.ttypes as NoteStore


config = ConfigParser()
config.read("/etc/pypenote/config.ini")


def to_unicode(note):
	try:
	    unicode(note, "ascii")
	except UnicodeError:
	    note = unicode(note, "utf-8")
	return(note)


def html_to_mdown(note):
	return(HTML2Text().handle(note))


def get_shared_note(notetitle, auth_token):
    try:
        client = EvernoteClient(token=auth_token, sandbox=False)
    except evernote.edam.error.ttypes.EDAMUserException:
        print("\n** Evernote API authenticate error. **\n")
        raise

    try:
        note_store = client.get_note_store()
        note_filter = NoteStore.NoteFilter()
        note_filter.words = 'intitle:"%s"' % (notetitle)
        notes_metadata_result_spec = NoteStore.NotesMetadataResultSpec()
        notes_metadata_list = note_store.findNotesMetadata(note_filter,
                0, 1, notes_metadata_result_spec)

        note_guid = notes_metadata_list.notes[0].guid
        note = note_store.getNote(note_guid, True, False, False, False)
        return(to_unicode(note.content))
    
    except IndexError:
        print("\n** Note not found in your shared notebook. **\n")
        raise


def main():
    notetitle = raw_input("Enter the note title to search: ")
    mynote = get_shared_note(notetitle, config.get("EvernoteAuth", "token"))
    article = html_to_mdown(mynote)

    template = get_template(dirname(abspath(config.get("Template", "path"))))
    write_content(template, config.get("Pelican", "content_path"), '%s.md' % (notetitle), article)


if __name__ == '__main__':
    main()