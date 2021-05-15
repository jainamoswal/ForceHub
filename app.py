# import all things.
from flask import Flask, render_template, url_for, redirect, request, jsonify, session, escape
from authlib.integrations.flask_client import OAuth
from pymongo import MongoClient
from config import var
from pytgauth import verify

# define app configs
app = Flask(__name__)
cluster = MongoClient(var.MONGO_URL)
db = cluster['github-bot']['data']
oauth = OAuth(app)
app.config['SECRET_KEY'] = var.FLASK_SECRET_KEY
app.config['GITHUB_CLIENT_ID'] = var.GITHUB_OAUTH_CLIENT_ID
app.config['GITHUB_CLIENT_SECRET'] = var.GITHUB_OAUTH_CLIENT_SECRET

# register github oAuth to call everytime.
github = oauth.register (
  name = 'github',
    client_id = app.config["GITHUB_CLIENT_ID"],
    client_secret = app.config["GITHUB_CLIENT_SECRET"],
    access_token_url = 'https://github.com/login/oauth/access_token',
    access_token_params = None,
    authorize_url = 'https://github.com/login/oauth/authorize',
    authorize_params = None,
    api_base_url = 'https://api.github.com/',
    client_kwargs = {'scope': 'user:email'},
)

# '/' will make user redirect to your GitHub Profile.
@app.route('/')
def main():
	return redirect('https://www.github.com/' + var.GITHUB_USERNAME)

# '/new' route will be 1st entry point.
@app.route('/new', methods=['GET'])
def new():
	if verify(request.args.to_dict(), var.BOT_TOKEN):
		session['id'] = request.args.get('id') # makes a session and adds userid as 'id' to get the session while adding it in 3rd step.
		return redirect(request.host_url + 'login')
	return redirect('https://http.cat/401')

# '/login' is 2nd entry pint from '/new'
# validates user and redirect user to login.
@app.route('/login', methods=['GET'])
def github_login():
    try:
        user_id = session['id']
        github = oauth.create_client('github')
        return github.authorize_redirect(url_for('github_authorize', _scheme='https', _external=True))
    except KeyError:
        return redirect('https://http.cat/401')

# 3rd entry point from '/login'
# makes user authorize and adds username with userid to our database.
@app.route('/login/github/authorize')
def github_authorize():
	try:
		github = oauth.create_client('github')
		token = github.authorize_access_token()
		username = github.get('user').json()['login']
		db.update_one({"user_id":session['id']},{"$set":{"github_username":username}}, upsert=True)
		return redirect(f'https://www.github.com/{var.GITHUB_USERNAME}')
	except Exception as e:
		print(e)
		return redirect('https://http.cat/502')

# defines __main__ and tells app to run the app.
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=var.PORT)
	
