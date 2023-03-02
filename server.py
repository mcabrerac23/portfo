from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('./web_server/database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n{email},{subject},{message}")
        print(email)
        print(database)

def write_to_csv(data):
    with open('./web_server/database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])
        
            
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST': 
        data = request.form.to_dict()
        write_to_csv(data) 
        print(data)
        return redirect('/thankyou.html')
    else:
        return "something went wrong. Try again!"


#...use this code when there is a username and ID assigned to a person:
#@app.route("/<username>/<int:post_id>")
#def hello_world(username=None, post_id=None):
#    return render_template('index.html', name=username, post_id=post_id)


#@app.route("/blog/2023/dogs")
#def blog2():
#    return "This is my dog"

