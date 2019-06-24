"""This module exports the Perl -c util."""

from cuda_lint import Linter, util
from cudatext import * 


class Dockerfilelint(Linter):

    """Provides an interface to dockerfilelint"""
    cmd = None
    executable = 'dockerfilelint --json'
    multiline = False
    syntax = ('Dockerfile')
    regex = (
        r'^.+?:(?P<line>\d+):'
        r'(?:(?P<error>Possible Bug|Deprecation|)|(?P<warning>Optimization|Clarity|)):'
        r'(?P<message>.+)$\r?\n'
    )
    base_cmd = ('')
    tempfile_suffix = 'erl'
    error_stream = util.STREAM_STDOUT
    word_re = r'^(".*?"|[-\w]+)'


    def split_match(self, match):
        print('plit_match')
        print(match)
   
        """Return the components of the error."""
        split_match = super(Dockerfilelint, self).split_match(match)

        match, line, col, error, warning, message, near = split_match
        return match, line, 0, '', '', message, ''
        


    def cmd(self):
        print('cmd')
        """Return the command line to execute."""
        result = self.executable + ' ' + self.base_cmd

        return result
