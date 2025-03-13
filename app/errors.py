from app.util import render

def register_error_handlers(app):
    app.errorhandler(404)(not_found)

def not_found(e):
    return render('404.html', {
        'title': 'Not Found',
        'contents': 'The page could not be found.'
    })