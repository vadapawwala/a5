from flask import Flask, request, make_response, redirect
from datetime import datetime

app = Flask(__name__)

# Simple user storage (in real app, use database)
USERS = {'u1': True}

def check_auth():
    return request.cookies.get('user_id')

def get_current_time():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

@app.route('/')
def home():
    # Check if user is logged in via cookie
    user = check_auth()
    if not user:
        return redirect('/login')
    
    return f'''
    <html>
        <body>
            <h3>Welcome {user}</h3>
            <p>Current Date and Time (UTC): {get_current_time()}</p>
            <p>Current User's Login: {user}</p>
            <br>
            <a href="/logout">Logout</a>
        </body>
    </html>
    '''

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        
        if username in USERS:
            # Create response and set cookie
            resp = make_response(redirect('/'))
            resp.set_cookie('user_id', username)
            return resp
        
        return '''
        <html>
            <body>
                <h3>Invalid username</h3>
                <a href="/login">Try again</a>
            </body>
        </html>
        '''

    return '''
    <html>
        <body>
            <h3>Login</h3>
            <form method="post">
                <input type="text" name="username" placeholder="Enter username">
                <input type="submit" value="Login">
            </form>
        </body>
    </html>
    '''

@app.route('/logout')
def logout():
    resp = make_response(redirect('/login'))
    resp.delete_cookie('user_id')
    return resp

if __name__ == '__main__':
    app.run(debug=True)