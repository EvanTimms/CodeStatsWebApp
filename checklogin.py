from flask import Flask, flash, redirect, url_for
from functools import wraps


def check_login(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Please log in', 'danger')
            return redirect(url_for('signIn'))
    return wrap
