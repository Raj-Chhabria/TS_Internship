from django.http import HttpResponse
from django.shortcuts import render
#spacy
import spacy
from spacy.pipeline import EntityRuler
from spacy.lang.en import English
from spacy.tokens import Doc

#gensim
import gensim
from gensim import corpora

#Visualization
from spacy import displacy
# import pyLDAvis.gensim_models
from wordcloud import WordCloud
import plotly.express as px
import matplotlib.pyplot as plt

#Data loading/ Data manipulation
import pandas as pd
import numpy as np
import jsonlines

#nltk
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download(['stopwords','wordnet'])

#warning
import warnings 
warnings.filterwarnings('ignore')

from .models import ResumeData
from random import choice
from .forms import Skill

def show(request):
    res_data = ResumeData.objects.all()
    pks = ResumeData.objects.values_list('pk', flat=True)
    random_pk = choice(pks)
    random_obj = ResumeData.objects.get(pk=random_pk)




    return render(request,'app/index.html',{'random_obj':random_obj,'all_obj':res_data})


def skill_percent(request):
    
    if request.method == "POST":
        skill = Skill(request.POST)
        if skill.is_valid():
            s = skill.cleaned_data['skills']
            input_resume = skill.cleaned_data['resume_text']
            req_skills = s.lower().split(",")
            resume_skills = unique_skills(get_skills(input_resume.lower()))
            score = 0
            for x in req_skills:
                if x in resume_skills:
                    score += 1
            req_skills_len = len(req_skills)
            match = round(score / req_skills_len * 100, 1)
    else:
        skill = Skill()
    return render(request,'app/skill_input.html',{'skill':skill})