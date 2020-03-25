from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)


@app.route('/')
def home():
    list1=['jarek', 'marek', 'skwarek']
    return render_template("index.html", list=list1)

@app.route('/<name>')
def first_website(name):
    var=23
    return render_template("login_page.html", content=name, variable=var)

@app.route('/test')
def test():
    return render_template("new_html_page.html")


# @app.route('/<name>')
# def user(name):
#     return "Hello %s" % name
#
# #Redirect to home page, when try to go to admin url
# @app.route('/admin')
# def admin():
#     return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(host="0.0.0.0", port="2340", debug=True)