from flask import Flask, request, render_template, redirect
import os.path
import csv
from more_itertools import last
import pandas as pd
import numpy as np
import random
import uuid


app = Flask(__name__)
global user_id
user_id = None


def get_paragraphs():
    paras = pd.read_csv("topic_paragraphs.csv", encoding="utf-8")
    ids = range(0, 6)
    texts = []
    for id in ids:
        texts.append(paras["text"][id])
    return ids, texts


def generate_id():
    path_name = "./query_gen_results/query_gen_results.csv"
    df = pd.read_csv(path_name)
    last_id = df['Participant_ID'].max()
    if np.isnan(last_id):
        last_id = 0
    return last_id + 1


def save_results(r1, r2, r3, r4, r5, ids, attention1):
    user_id = str(uuid.uuid4())
    path_name = "./query_gen_results/" + user_id + ".csv"
    results = [[user_id, ids[0]+1, r1],
               [user_id, ids[1]+1, r2],
               [user_id, ids[2]+1, r3],
               [user_id, ids[3]+1, r4],
               [user_id, ids[4]+1, r5],
               [user_id, "attention1", attention1]]

    with open(path_name, 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(results)


def get_new_paras():
    ids, texts = get_paragraphs()
    query_1 = texts[0]
    query_2 = texts[1]
    query_3 = texts[2]
    query_4 = texts[3]
    query_5 = texts[4]
    return query_1, query_2, query_3, query_4, query_5, ids


global query_1
global query_2
global query_3
global query_4
global query_5
global ids
global texts
ids, texts = get_paragraphs()
query_1 = texts[0]
query_2 = texts[1]
query_3 = texts[2]
query_4 = texts[3]
query_5 = texts[4]

@app.route("/", methods=["GET", "POST"])
def query_gen():
    global query_1
    global query_2
    global query_3
    global query_4
    global query_5
    global ids
    global texts
    if request.method == 'POST':
        if "done" in request.form:
            result1 = str(request.form['query_1'])
            result2 = str(request.form['query_2'])
            result3 = str(request.form['query_3'])
            result4 = str(request.form['query_4'])
            result5 = str(request.form['query_5'])
            attention1 = str(request.form['attention_1'])
            save_results(result1, result2, result3, result4, result5, ids, attention1)
            query_1, query_2, query_3, query_4, query_5, ids = get_new_paras()
            return redirect("https://app.prolific.co/submissions/complete?cc=CSP88M3M")
    return render_template("query_gen.html", query_1=query_1, query_2=query_2, query_3=query_3, query_4=query_4, query_5=query_5)