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
    student_github = request.args.get("github")    # key in url, also the argument for get_s_b_g function
    student_name = hackbright_app.get_student_by_github(student_github)     #returns a single DB row
    grades_list = hackbright_app.grades_by_student(student_name[0], student_name[1])    #returns a list of rows
    html = render_template("student_info.html", first_name=student_name[0], last_name=student_name[1], 
        github=student_name[2], grades_list=grades_list)
    return html

# for particular project, list all students and their grades

# http://localhost:5000/project?project_title=Markov
@app.route("/project")
def get_project():  #this successfully returns github, grade for the requested project
    hackbright_app.connect_to_db()
    project_name = request.args.get("project_title")    # key in url
    # student_github = request.args.get("github")
    # student_name_return = hackbright.app.get_student_by_github(student_github)
    rows_return = hackbright_app.get_grades_by_project(project_name)    #returns a list of rows
    html = render_template("project_info.html", project_name=project_name, rows_return=rows_return)  # github, grade
    return html


if __name__ == "__main__":
    app.run(debug=True)
# Next step would be to render First Name, last_name, Grades for the given project
# requires joining the table by github, then rendering more fields in 47.