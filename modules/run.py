from flask import Flask, render_template, request, url_for, redirect, jsonify, Markup
import discogs_client

app = Flask(__name__)
client = None

@app.route('/')
def main():
    return redirect(url_for("home"))


@app.route('/home')
def home():
    global client
    return render_template('home.html', client=client)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html', authorize_url=None)
    elif request.method == "POST":
        global client
        key = request.form['key']
        if key:
            client.get_access_token(key)
            return redirect(url_for('home'))
        else:
            client = discogs_client.Client('ExampleApplication/0.1',
                            user_token="wuYMABvmUDdOMXerFacIXQBQJJphFkPgtivGgfLW")
        return redirect(url_for('home'))


@app.route('/generateUrl')
def generate_url():
    global client
    client = discogs_client.Client('ExampleApplication/0.1')
    client.set_consumer_key('CHcjnSdrYtRIRWPEjcfI',
                            'qasuBwasGGrraGIoMtOqKkssYnELwNMK')
    return jsonify(result=client.get_authorize_url()[2])


@app.route('/logout')
def logout():
    global client
    client = None
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

'''@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html', authorize_url=None)
    elif request.method == "POST":
        if request.form['login_type'] == 'user':
            return redirect(url_for('user_login'))
        elif request.form['login_type'] == 'common':
            global client
            client = discogs_client.Client('ExampleApplication/0.1',
                          user_token="wuYMABvmUDdOMXerFacIXQBQJJphFkPgtivGgfLW")
            return redirect(url_for('home'))


@app.route('/userLogin', methods=['GET', 'POST'])
def user_login():
    if request.method == 'GET':
        global client
        client = discogs_client.Client('ExampleApplication/0.1')
        client.set_consumer_key('CHcjnSdrYtRIRWPEjcfI',
                                'qasuBwasGGrraGIoMtOqKkssYnELwNMK')
        return render_template('login.html', authorize_url=client.get_authorize_url()[2])
    elif request.method == 'POST':
        client.get_access_token(request.form['acess'])
        return redirect(url_for('home'))'''