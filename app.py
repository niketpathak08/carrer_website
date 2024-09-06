from flask import Flask,render_template,jsonify

app = Flask(__name__)

JOBS = [
    {
        "id": 1,
        "title": "Software Engineer",
        "location": "San Francisco, CA",
        "salary": "$120,000"
    },
    {
        "id": 2,
        "title": "Data Scientist",
        "location": "New York, NY",
        "salary": "$110,000"
    },
    {
        "id": 3,
        "title": "Product Manager",
        "location": "Austin, TX",
        "salary": "$130,000"
    },
    {
        "id": 4,
        "title": "UX Designer",
        "location": "Seattle, WA",
        "salary": "$120,000"
    },
    {
        "id": 5,
        "title": "DevOps Engineer",
        "location": "Remote",
        "salary": "$115,000"
    }
]

@app.route("/")
def home():
    return render_template('home.html',jobs=JOBS)
    
@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True)