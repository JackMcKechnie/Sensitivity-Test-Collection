from flask import Flask, request, render_template, redirect
import os.path
import csv
from more_itertools import last
import pandas as pd
import numpy as np
import random

app = Flask(__name__)
global user_id
user_id = None

def get_paragraphs():
    paras = pd.read_csv("topic_paragraphs.csv",encoding="utf-8")
    m = paras["id"].max()
    ids = random.sample(range(m), 3)
    texts = []
    for id in ids:
        texts.append(paras["text"][id])
    return ids, texts

def generate_id():
    path_name = "./query_gen_results/query_gen_results.csv"
    df=pd.read_csv(path_name)
    last_id = df['Participant_ID'].max()
    if np.isnan(last_id):
        last_id = 0
    return last_id + 1

def save_results(r1,r2,r3,ids):
    path_name = "./query_gen_results/query_gen_results.csv"
    global user_id
    if user_id == None:
         user_id = generate_id()
    results = [[user_id,ids[0]+1,r1],[user_id,ids[1]+1,r2],[user_id,ids[2]+1,r3]]
    with open(path_name, 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(results)

def get_new_paras():
    ids, texts = get_paragraphs()
    query_1 = texts[0]
    query_2 = texts[1]
    query_3 = texts[2]
    return query_1, query_2, query_3, ids

global query_1
global query_2
global query_3
global ids
global texts
ids, texts = get_paragraphs()
query_1 = texts[0]
query_2 = texts[1]
query_3 = texts[2]

@app.route("/",methods=["GET","POST"])
def query_gen():
    global query_1
    global query_2
    global query_3
    global ids
    global texts
    if request.method == 'POST':
        if "done" in request.form:
            result1 = str(request.form['query_1'])
            result2 = str(request.form['query_2'])
            result3 = str(request.form['query_3'])
            save_results(result1,result2,result3,ids)
            query_1, query_2, query_3, ids = get_new_paras()
            return redirect("http://www.google.com")
        elif "more" in request.form:
            result1 = str(request.form['query_1'])
            result2 = str(request.form['query_2'])
            result3 = str(request.form['query_3'])
            save_results(result1,result2,result3,ids)
            query_1, query_2, query_3, ids = get_new_paras()    
    return render_template("query_gen.html",query_1=query_1,query_2=query_2,query_3=query_3)


# NEED TO MAKE MAKE IDS, TEXT AND QUERY VARIABLES GLOBAL?
