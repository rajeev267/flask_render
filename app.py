from flask import Flask, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, student
from forms import LoginForm, AddStudentForm, ChangePasswordForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.db'
app.config['SECRET_KEY'] = '123457890'
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    special_users = {
        'teacher': 'password123',
        'teacher2': 'password1234',
        'admin': 'adminpass'
    }

    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        if username in special_users and special_users[username] == password:
            flash('Login successful!', 'success')
            form = LoginForm()
            return render_template('teacher_dashboard.html', form=form)

        user = student.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            flash('Login successful!', 'success')
            return render_template('student_dashboard.html',
                                   username=user.username,
                                   dbms=user.dbms,
                                   coa=user.coa,
                                   iwt=user.iwt,
                                   ds=user.ds,
                                   cpp=user.cpp,
                                   sum_marks=user.dbms + user.coa + user.iwt + user.ds + user.cpp)

        flash('Invalid username or password', 'danger')

    return render_template('login.html', form=form)


@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    form = AddStudentForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)

        new_student = student(
            username=form.username.data,
            password=hashed_password,
            dbms=form.dbms.data,
            coa=form.coa.data,
            iwt=form.iwt.data,
            ds=form.ds.data,
            cpp=form.cpp.data
        )
        db.session.add(new_student)
        db.session.commit()
        flash('Student added successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('add_student.html', form=form)


@app.route('/change_password', methods=['GET', 'POST'])
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        user = student.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.old_password.data):
            user.password = generate_password_hash(form.new_password.data)
            db.session.commit()
            flash('Password changed successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or old password', 'danger')

    return render_template('change_pass.html', form=form)


@app.route('/logout')
def logout():
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))
@app.route('/show_students')
def show_students():
    students = student.query.all()
    return render_template('show_students.html', students=students)



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
