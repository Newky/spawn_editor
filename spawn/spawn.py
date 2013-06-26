#!/usr/bin/env python2.7
'''
Idea got from here:
http://stackoverflow.com/questions/10103359/vim-editor-in-python-script-tempfile
'''
import sys, tempfile, os
from subprocess import call

def get_editor_output(initial_message=""):
    EDITOR = os.environ.get('EDITOR','vim')
    output = ""
    with tempfile.NamedTemporaryFile(suffix=".tmp") as f:
        f.write(initial_message)
        f.flush()
        call([EDITOR, f.name])
        k = open(f.name, "r")
        output = k.read()
        k.close()
    return output
