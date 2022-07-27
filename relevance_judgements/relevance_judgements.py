from flask import Flask, render_template, request
import glob
import os
import random
import pandas as pd

app = Flask(__name__)

def save_email_from_filename(filename):
    full_filename = glob.glob('./enron_with_categories/*/*' + str(filename) + '.txt')    
    email_contents = ""
    with open(full_filename[0]) as file:
        for line in file:
            email_contents = email_contents + line
    return email_contents

def list_all_filenames():
    globs = glob.glob('./enron_with_categories/*/*.cats')
    filenames = []
    for file in globs:
        filenames.append(os.path.splitext(os.path.basename(file))[0])
    return filenames

def get_random_email():
    filenames = list_all_filenames()
    random_choice = random.choice(filenames)
    return save_email_from_filename(random_choice).replace('\n', '<br>')

def get_random_query():
    topic_paragraphs = pd.read_csv("topic_paragraphs.csv")["text"]
    return random.choice(topic_paragraphs)

@app.route("/" , methods=["GET", "POST"])
def hello_world():
    if request.method == 'POST':
        if "done" in request.form:
            print(str(request.form["relevance"]))
    return render_template("relevance_judgements.html",query=get_random_query(), email=get_random_email())
