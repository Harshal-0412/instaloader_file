from flask import *
import instaloader

app = Flask(__name__)
x = instaloader.Instaloader()

USER = "daniel_potter_1234"
PASSWORD = "Harshal@123"
x.login(USER, PASSWORD)        # (login)
x.load_session_from_file(USER)

@app.route("/name", methods = ['POST'])
def login():
    AccountName = request.form['Name']
    profile = instaloader.Profile.from_username(x.context, AccountName)
    return f"{profile.profile_pic_url}"

if __name__ == "__main__":
    app.run()
