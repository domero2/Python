from flask import Flask, redirect, url_for, render_template, request
from SEO_APP_DB.base import create_connection

DATABASE = r"/Users/albi/Library/DBeaverData/workspace6/.metadata/sample-database-sqlite-1/Chinook.db"
app = Flask(__name__)


@app.route('/')
def home():
    list1=['jarek', 'marek', 'skwarek']
    return render_template("index.html", list=list1)

# @app.route('/<name>')
# def first_website(name):
#     var=23
#     return render_template("login_page.html", content=name, variable=var)

@app.route('/login_page',  methods=['POST', 'GET'])
def login_page():

    if request.method == 'POST':
        try:
            nmk = request.form['nm']
            addr = request.form['add']
            city = request.form['city']
            pin = request.form['pin']

            with create_connection(DATABASE) as con:
                cur = con.cursor()
                cur.execute("INSERT INTO students (name,addr,city,pin)\
                VALUES(?, ?, ?, ?)",(nmk,addr,city,pin) )

                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"
        finally:
            con.close()
    return render_template("login_page.html")


@app.route('/test')
def test():
    m = []
    with create_connection(DATABASE) as conn:
        con2 = conn.cursor()
        res = con2.execute("select FirstName, LastName from Customer where FirstName like 'L%' ")

        for i in res:
            m.append(i)
    return render_template("new_html_page.html", clients=m)


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