from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
from pywebio.input import *
from pywebio.output import *
import argparse
from pywebio import start_server


import pandas as pd

df= pd.read_csv(r"corpus.csv")

li= df.processed_text.tolist()

import spacy_sentence_bert

nlp = spacy_sentence_bert.load_model('en_stsb_roberta_large')

app= Flask(__name__)

def predict():
    
    
    doc1= input("Enter your text: ", type= TEXT)
    
    doc1= nlp(doc1)
    
    #doc2= input("Enter your second text: ", type=TEXT)
    
    for i in li:
        
    
        doc2= nlp(i)
        
        prediction= doc1.similarity(doc2[0:7])
        
    
        put_text("the score is: {} and text is {}".format(prediction, i))
    
        
        
app.add_url_rule('/rec', 'webio_view', webio_view(predict), methods= ["GET", "POST", "OPTIONS"])


#deployment to heroku use this
if __name__== "__main__":
    parser= argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args= parser.parse_args()
    
    start_server(predict, port= args.port)