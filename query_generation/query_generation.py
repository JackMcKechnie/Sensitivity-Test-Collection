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
    ids = range(0, 26)
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


def save_results(r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20, r21, r22, r23, r24, r25, ids, attention1, attention2):
    user_id = str(uuid.uuid4())
    path_name = "./query_gen_results/" + user_id + ".csv"
    results = [[user_id, ids[0]+1, r1],
               [user_id, ids[1]+1, r2],
               [user_id, ids[2]+1, r3],
               [user_id, ids[3]+1, r4],
               [user_id, ids[4]+1, r5],
               [user_id, ids[5]+1, r6],
               [user_id, ids[6]+1, r7],
               [user_id, ids[7]+1, r8],
               [user_id, ids[8]+1, r9],
               [user_id, ids[9]+1, r10],
               [user_id, ids[10]+1, r11],
               [user_id, ids[11]+1, r12],
               [user_id, ids[12]+1, r13],
               [user_id, ids[13]+1, r14],
               [user_id, ids[14]+1, r15],
               [user_id, ids[15]+1, r16],
               [user_id, ids[16]+1, r17],
               [user_id, ids[17]+1, r18],
               [user_id, ids[18]+1, r19],
               [user_id, ids[19]+1, r20],
               [user_id, ids[20]+1, r21],
               [user_id, ids[21]+1, r22],
               [user_id, ids[22]+1, r23],
               [user_id, ids[23]+1, r24],
               [user_id, ids[24]+1, r25],
               [user_id, "attention1", attention1],
               [user_id, "attention2", attention2]]

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
    query_6 = texts[5]
    query_7 = texts[6]
    query_8 = texts[7]
    query_9 = texts[8]
    query_10 = texts[9]
    query_11 = texts[10]
    query_12 = texts[11]
    query_13 = texts[12]
    query_14 = texts[13]
    query_15 = texts[14]
    query_16 = texts[15]
    query_17 = texts[16]
    query_18 = texts[17]
    query_19 = texts[18]
    query_20 = texts[19]
    query_21 = texts[20]
    query_22 = texts[21]
    query_23 = texts[22]
    query_24 = texts[23]
    query_25 = texts[24]
    return query_1, query_2, query_3, query_4, query_5, query_6, query_7, query_8, query_9, query_10, query_11, query_12, query_13, query_14, query_15, query_16, query_17, query_18, query_19, query_20, query_21, query_22, query_23, query_24, query_25, ids


global query_1
global query_2
global query_3
global query_4
global query_5
global query_6
global query_7
global query_8
global query_9
global query_10
global query_11
global query_12
global query_13
global query_14
global query_15
global query_16
global query_17
global query_18
global query_19
global query_20
global query_21
global query_22
global query_23
global query_24
global query_25
global ids
global texts
ids, texts = get_paragraphs()
query_1 = texts[0]
query_2 = texts[1]
query_3 = texts[2]
query_4 = texts[3]
query_5 = texts[4]
query_6 = texts[5]
query_7 = texts[6]
query_8 = texts[7]
query_9 = texts[8]
query_10 = texts[9]
query_11 = texts[10]
query_12 = texts[11]
query_13 = texts[12]
query_14 = texts[13]
query_15 = texts[14]
query_16 = texts[15]
query_17 = texts[16]
query_18 = texts[17]
query_19 = texts[18]
query_20 = texts[19]
query_21 = texts[20]
query_22 = texts[21]
query_23 = texts[22]
query_24 = texts[23]
query_25 = texts[24]


@app.route("/", methods=["GET", "POST"])
def query_gen():
    global query_1
    global query_2
    global query_3
    global query_4
    global query_5
    global query_6
    global query_7
    global query_8
    global query_9
    global query_10
    global query_11
    global query_12
    global query_13
    global query_14
    global query_15
    global query_16
    global query_17
    global query_18
    global query_19
    global query_20
    global query_21
    global query_22
    global query_23
    global query_24
    global query_25
    global ids
    global texts
    if request.method == 'POST':
        if "done" in request.form:
            result1 = str(request.form['query_1'])
            result2 = str(request.form['query_2'])
            result3 = str(request.form['query_3'])
            result4 = str(request.form['query_4'])
            result5 = str(request.form['query_5'])
            result6 = str(request.form['query_6'])
            result7 = str(request.form['query_7'])
            result8 = str(request.form['query_8'])
            result9 = str(request.form['query_9'])
            result10 = str(request.form['query_10'])
            result11 = str(request.form['query_11'])
            result12 = str(request.form['query_12'])
            result13 = str(request.form['query_13'])
            result14 = str(request.form['query_14'])
            result15 = str(request.form['query_15'])
            result16 = str(request.form['query_16'])
            result17 = str(request.form['query_17'])
            result18 = str(request.form['query_18'])
            result19 = str(request.form['query_19'])
            result20 = str(request.form['query_20'])
            result21 = str(request.form['query_21'])
            result22 = str(request.form['query_22'])
            result23 = str(request.form['query_23'])
            result24 = str(request.form['query_24'])
            result25 = str(request.form['query_25'])
            attention1 = str(request.form['attention_1'])
            attention2 = str(request.form['attention_2'])

            save_results(result1, result2, result3, result4, result5, result6, result7, result8, result9, result10, result11, result12, result13,
                         result14, result15, result16, result17, result18, result19, result20, result21, result22, result23, result24, result25, ids, attention1, attention2)
            query_1, query_2, query_3, query_4, query_5, query_6, query_7, query_8, query_9, query_10, query_11, query_12, query_13, query_14, query_15, query_16, query_17, query_18, query_19, query_20, query_21, query_22, query_23, query_24, query_25, ids = get_new_paras()
            return redirect("http://www.google.com")
    return render_template("query_gen.html", query_1=query_1, query_2=query_2, query_3=query_3, query_4=query_4, query_5=query_5, query_6=query_6, query_7=query_7, query_8=query_8, query_9=query_9, query_10=query_10, query_11=query_11, query_12=query_12, query_13=query_13, query_14=query_14, query_15=query_15, query_16=query_16, query_17=query_17, query_18=query_18, query_19=query_19, query_20=query_20, query_21=query_21, query_22=query_22, query_23=query_23, query_24=query_24, query_25=query_25)
