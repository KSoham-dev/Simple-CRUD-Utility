from flask_sqlalchemy import SQLAlchemy as sq
db = sq()

class student(db.Model):
    student_id = db.Column(db.Integer(), primary_key=True, )
    roll_number = db.Column(db.String(), unique=True, nullable=False)
    first_name = db.Column(db.String(), nullable=False)
    last_name=db.Column(db.String())

class course(db.Model):
    course_id = db.Column(db.Integer(), primary_key=True, )
    course_code = db.Column(db.String(), unique=True, nullable=False)
    course_name = db.Column(db.String(), nullable=False)
    course_description = db.Column(db.String())

class enrollments(db.Model):
    enrollment_id = db.Column(db.Integer(), primary_key=True)
    estudent_id = db.Column(db.Integer(), db.ForeignKey("student.student_id"), nullable=False)
    ecourse_id = db.Column(db.Integer(), db.ForeignKey("course.course_id"), nullable=False)