from flask import render_template


def render(template: str, data: dict = {}):
    """Simple wrapper for render template to make it more how I like

    I.E.
    return render('foo.html', {
        'bar': bar,
    })
    insteadof of
    return render_template('foo.html', bar=bar)
    """
    return render_template(template, **data)


def url_has_allowed_host_and_scheme(url, host):
    """Validate next url param"""
    # TODO implement this
    return True
