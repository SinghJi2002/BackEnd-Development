from flask import Flask,render_template,url_for,flash,redirect
from forms import RegistrationForm,LoginForm

app=Flask(__name__)

app.config['SECRET_KEY']='d448d275ef5e70a58940e6032a57b082'


post=[
    {
        "title":"Series In Pandas",
        "author":"Ashutosh Kumar Singh",
        "content":"Series object in pandas",
        "date_Posted":"24-1-2024"
    },
    {
        
        "title":"Pandas",
        "author":"Anirudh Kumar Singh",
        "content":"Pandas",
        "date_Posted":"25-1-2024"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("homepagecopy.html",post=post,title="title")

@app.route("/about")
def about():
    return render_template("aboutcopy.html")

@app.route("/register",methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!','success')
        return redirect(url_for('home'))
    #Updata layout template for messages to pop up
    return render_template('register.html',form=form,title='Register')

@app.route("/login")
def login():
    form=LoginForm
    return render_template('login.html')


if(__name__=="__main__"):
    app.run(debug=True)