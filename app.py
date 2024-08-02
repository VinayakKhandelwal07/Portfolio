from flask import Flask, redirect,render_template,url_for,request
import sqlite3 

app = Flask(__name__)

@app.route('/') # https://127.0.0.1:5000/
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/thank')
def thank():
    return render_template('thank.html')

@app.route('/submit_form',methods=['GET','POST'])
def submit_form():
    if request.method == "POST": 
        

        name = request.form['name']
        email = request.form['email']
        message = request.form['message']


        user_data = (name,email,message)
        ## database 
        conn =  sqlite3.connect("userdata.db")
        insert_data_query = """
        insert into user_record values(?,?,?)
        """

        cur = conn.cursor()
        cur.execute(insert_data_query,user_data)
        print("You have successfully inserted your data into table : ",user_data)
        conn.commit()
        cur.close()
        conn.close()
       
         # Redirect to the thank you page
        return render_template('thank.html')
    


if __name__ == "__main__":
     app.run(debug=True)