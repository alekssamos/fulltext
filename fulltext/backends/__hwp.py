from __future__ import absolute_import

from fulltext.backends import __html
from fulltext.util import run, assert_cmd_exists


def test():
    assert_cmd_exists('hwp5proc')


def _cmd(path, **kwargs):
    cmd = ['hwp5proc', 'xml']
    cmd.extend([path])
    return cmd


def to_text_with_backend(html):
    return __html._get_file(html)


def _get_path(path, **kwargs):
    encoding, errors = kwargs['encoding'], kwargs['encoding_errors']
    return to_text_with_backend(run(*_cmd(path, **kwargs)).decode(
        encoding, errors))
