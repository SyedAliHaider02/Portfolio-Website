from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def man():
    return render_template('homepage.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__=="__main__":
    app.run()