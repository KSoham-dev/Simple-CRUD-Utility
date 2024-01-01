from flask import Flask, render_template, request, redirect
from models import *
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite3"

db.init_app(app)
app.app_context().push() # one for all modules

@app.route("/")
def all_students():
    all_students = student.query.all()
    if len(all_students) == 0:
        return render_template('no_student.html')
    return render_template('index.html', all_students=all_students)

@app.route("/student/create", methods=["GET","POST"])
def add_students():
    if request.method == "POST":
        st_fname = request.form.get("f_name")
        st_lname = request.form.get("l_name")
        st_roll = request.form.get("roll")
        co = request.form.getlist("courses")
        roll_numbers = [s.roll_number for s in student.query.all()]
        st=student(roll_number=st_roll, first_name=st_fname, last_name=st_lname)
        if st_roll in roll_numbers:
            return render_template("error.html")
        db.session.add(st)
        db.session.commit()
        st=student.query.filter_by(roll_number = st_roll).first()
        st_id = st.student_id
        if ("course_1" in co):
            co_id=course.query.filter_by(course_name = "MAD I").first().course_id
            en1 = enrollments(estudent_id=st_id, ecourse_id=co_id)
            db.session.add(en1)
            db.session.commit()
        if ("course_2" in co):
            co_id=course.query.filter_by(course_name = "DBMS").first().course_id
            en2 = enrollments(estudent_id=st_id, ecourse_id=co_id)
            db.session.add(en2)
            db.session.commit()
        if ("course_3" in co):
            co_id=course.query.filter_by(course_name = "PDSA").first().course_id
            en3 = enrollments(estudent_id=st_id, ecourse_id=co_id)
            db.session.add(en3)
            db.session.commit()
        if ("course_4" in co):
            co_id=course.query.filter_by(course_name = "BDM").first().course_id
            en4 = enrollments(estudent_id=st_id, ecourse_id=co_id)
            db.session.add(en4)
            db.session.commit() 
        return redirect("/")
    return render_template('add_student.html')

@app.route("/student/<int:id>/update", methods=["GET","POST"])
def update_student(id):
    this_student = db.session.get(student,id)
    if request.method == "POST":
        uptd_fname = request.form.get("f_name")
        uptd_lname = request.form.get("l_name")
        this_student.first_name = uptd_fname
        this_student.last_name = uptd_lname
        db.session.commit()
        co = request.form.getlist("courses")
        st_id = this_student.student_id
        enl = enrollments.query.filter_by(estudent_id = st_id).all()
        if len(enl) != 0:
            for en in enl:
                db.session.delete(en) 
                db.session.commit()
        if ("course_1" in co):
            co_id=course.query.filter_by(course_name = "MAD I").first().course_id
            en1 = enrollments(estudent_id=st_id, ecourse_id=co_id)
            db.session.add(en1)
            db.session.commit()
        if ("course_2" in co):
            co_id=course.query.filter_by(course_name = "DBMS").first().course_id
            en2 = enrollments(estudent_id=st_id, ecourse_id=co_id)
            db.session.add(en2)
            db.session.commit()
        if ("course_3" in co):
            co_id=course.query.filter_by(course_name = "PDSA").first().course_id
            en3 = enrollments(estudent_id=st_id, ecourse_id=co_id)
            db.session.add(en3)
            db.session.commit()
        if ("course_4" in co):
            co_id=course.query.filter_by(course_name = "BDM").first().course_id
            en4 = enrollments(estudent_id=st_id, ecourse_id=co_id)
            db.session.add(en4)
            db.session.commit()
        return redirect('/')
    return render_template("update_student.html",this_student=this_student)

@app.route("/student/<int:id>/delete")
def delete_student(id):
    this_student = db.session.get(student,id)
    st_id = this_student.student_id
    db.session.delete(this_student)
    db.session.commit()
    enl = enrollments.query.filter_by(estudent_id = st_id).all()
    if len(enl) != 0:
            for en in enl:
                db.session.delete(en) 
                db.session.commit()
    return redirect("/")

@app.route("/student/<int:id>")
def student_info(id):
    this_student = db.session.get(student,id)
    st_id = this_student.student_id
    enl = enrollments.query.filter_by(estudent_id = st_id).all()
    co_l = []
    for en in enl:
        co=course.query.filter_by(course_id = en.ecourse_id).first()
        co_l.append(co)
    return render_template("personal_details.html", s=this_student, co_l=co_l)

if __name__ == "__main__":
    app.run(debug=True)