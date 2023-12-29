from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_num = random.randint(0,10)
    now = datetime.now()
    current_year = now.year
    return render_template("index1.html", num=random_num, year=current_year)


@app.route('/guess/<name>')
def guess(name):
    age = requests.get(f"https://api.agify.io?name={name}").json()
    age_result = age["age"]
    gender = requests.get(f"https://api.genderize.io?name={name}").json()
    gender_result = gender["gender"]
    name_given = gender["name"].capitalize()
    return render_template("age_index.html", age=age_result, gender=gender_result, name=name_given)


@app.route('/blog')
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blogs.html", posts=all_posts)




if __name__ == "__main__":
    app.run(debug=True)
