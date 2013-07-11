# Amy and Gowri, Hackbright exercise 7.10.13

import hackbright_app

# activate the framework, before we run it, create functions and install
# them as "handlers" for specific events

from flask import Flask, render_template, request

# if we run this without handlers, it creates a webserver at localhost:5000,
# but clients can't access it -> will get 404 errors

# need a handler for each event, including a browser accessing the server
app = Flask(__name__)


@app.route("/")
def get_github():
    return render_template("get_github.html")


# http://localhost:5000/?key1=val1&key2=val2

# our url
# http://localhost:5000/student?key=value

@app.route("/student")
def get_student():                  # defining handler
    hackbright_app.connect_to_db()  # connects to hackbright.db in current dir
    student_github = request.args.get("github")    # key in url
    bar = hackbright_app.get_student_by_github(student_github)
    grades_list = hackbright_app.grades_by_student(bar[0], bar[1])
    html = render_template("student_info.html", first_name=bar[0], last_name=bar[1], github=bar[2], grades_list=grades_list)
    # , first_name=row[0], last_name=row[1], github=row[2])
    return html


if __name__ == "__main__":
    app.run(debug=True)
