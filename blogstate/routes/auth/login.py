from blogstate import app
from blogstate.api import SecureAgent
from flask import (
    render_template,
    redirect, request,
    session, url_for
)

agent = SecureAgent()


@app.route('/signin/')
@app.route('/login/', methods=['GET', 'POST'])
def login():
    """
    Handler logic for the `/login` route.

    On GET, renders the corresponding template.
    On POST, fetches validation status and user information.
    """
    if request.method == 'GET':
        return render_template("pre/login.html")

    # On POST request #
    credentials = {
        "username": request.form.get('username'),
        "passwd": request.form.get('passwd')
    }
    status = agent.login(credentials)
    if status:
        # Proceed to setting session variables,
        # and redirect to dashboard or something.
        session['logged_in'] = True
        session['username'] = request.form.get('username')
        session['user_id'] = status['user_id']
        return redirect(url_for('home'))

    return render_template('pre/login.html',
                           issue='Incorrect username or password')
