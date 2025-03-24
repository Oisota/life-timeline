import pytest

from app import util

@pytest.mark.parametrize('url, host, expected', [
    ('', '', False),
    ('https://foo.com/bar', 'foo.com', True),
    ('http://foo.com/bar', 'foo.com', False),
    ('http://badsite.com/bar', 'foo.com', False),
])
def test_url_has_allowed_host_and_scheme(url, host, expected):
    result = util.url_has_allowed_host_and_scheme(url, host)
    assert result == expected