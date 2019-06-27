"""This module exports the dockerfilelint --lint util."""

from cuda_lint import Linter, util

class Dockerfilelint(Linter):

    """Provides an interface to dockerfilelint --lint"""
    cmd = None
    executable = 'dockerfilelint'
    multiline = False
    syntax = ('Dockerfile')
    regex = r'.*"line":"(?P<line>\d+)",.*"content":"(?P<error>.*)",.*"title":"(?P<message>.+)",'
    base_cmd = (' --json ')
    tempfile_suffix = 'dockerfile'
    error_stream = util.STREAM_STDOUT
    word_re = r'^(".*?"|[-\w]+)'


    def split_match(self, match):
   
        """Return the components of the error."""
        split_match = super(Dockerfilelint, self).split_match(match)

        match, line, col, error, warning, message, near = split_match
        return match, line, 0, '', '', message, ''
        


    def cmd(self):
        """Return the command line to execute."""
        result = self.executable + ' ' + self.base_cmd

        return result
