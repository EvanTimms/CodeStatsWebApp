from flask import Flask, flash, redirect, url_for, session
from functools import wraps

#decorator that prevents a user from accessing pages while not logged in
def check_login(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            #if user logged in, simply return the function being wrapped
            return f(*args, **kwargs)
        else:
            flash('Please log in', 'danger')
            return redirect(url_for('signIn'))
    return wrap
