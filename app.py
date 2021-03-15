from flask import Flask,render_template,request,flash,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
# import flas

app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobposting.db'

db = SQLAlchemy(app)

class jobs(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    posted_by = db.Column(db.String(50),nullable = False)
    job_title = db.Column(db.String(100),nullable = False)
    company_name = db.Column(db.String(100),nullable = False)
    experience = db.Column(db.String(50),nullable = False)
    skills = db.Column(db.String(100),nullable = False)
    job_desc = db.Column(db.String(1024),nullable = False)
    roles_res = db.Column(db.String(1024),nullable = False)
    location = db.Column(db.String(100),nullable = False)
    apply_link = db.Column(db.String(100),nullable = False)

def __init__(self, posted_by,job_title,company_name,experience,skills,job_desc,roles_res,location,apply_link):
   self.posted_by = posted_by
   self.job_title = job_title
   self.company_name = company_name
   self.experience = experience
   self.skills = skills
   self.job_desc = job_desc
   self.roles_res = roles_res
   self.location = location
   self.apply_link = apply_link
  

@app.route('/viewjob')
def viewjob():    
    return render_template('viewjob.html',jobs = jobs.query.all())

@app.route('/')
@app.route('/postjob',methods = ['GET', 'POST'])
def postjob():
    if request.method == 'POST':
        postedby = request.form['posted_by']
        jobtitle = request.form['job_title']
        companyname = request.form['company_name']
        exp = request.form['experience']
        skill = request.form['skills']
        jobdesc = request.form['job_desc']
        roles = request.form['ros']
        jlocation = request.form['location']
        applylink = request.form['apply_link']
    
        job = jobs(posted_by =postedby,job_title =jobtitle ,company_name = companyname,
        experience = exp,skills =skill ,job_desc = jobdesc,roles_res = roles,
        location = jlocation,apply_link =applylink )
        db.session.add(job)
        db.session.commit()
        print('added')
            # flash('Record was successfully added')
        return redirect(url_for('viewjob'))


    return render_template('postjob.html')



if __name__=="__main__":
    app.run()