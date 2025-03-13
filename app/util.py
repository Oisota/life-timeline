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

def get_slugger(field_mapping: dict):
    """Slugify given fields in mapping

    Field mapping should map source column to target slug column.
    EX: {'title': 'title_slug', 'foo': 'foo_slug'}
    """
    def handler(mapper, connection, target):
        """SQLA event handler"""
        for k, v in field_mapping:
            source = getattr(target, k)
            slug = slugify(source)
            setattr(target, v, slug)
    return handler
