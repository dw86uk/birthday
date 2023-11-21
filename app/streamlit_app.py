from collections import namedtuple
from PIL import Image
import altair as alt
import time
import pandas as pd
import numpy as np
import streamlit as st

opening_image = Image.open('app/Opener.png')
q2_image = Image.open('app/q2Image.jpg')
q3_image = Image.open('app/q3Image.gif')
q4_image = Image.open('app/q4Image.jpg')
q5_image = Image.open('app/q5Image.jpg')
q6_image = Image.open('app/q6Image.jpg')
q8_image = Image.open('app/q8Image.jpg')
q9_image = Image.open('app/q9Image.jpg')
q10_image = Image.open('app/q10Image.webp')
q11_image = Image.open('app/q11Image.jpg')



#st.markdown(
#    """
#    <style>
#    .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob,
#    .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137,
#    .viewerBadge_text__1JaDK {
#        display: none;
#    }
#    </style>
#    """,
#    unsafe_allow_html=True
#)

hide_github_icon = “”"
.css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob, .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137, .viewerBadge_text__1JaDK{ display: none; } #MainMenu{ visibility: hidden; } footer { visibility: hidden; } header { visibility: hidden; }

“”"
st.markdown(hide_github_icon, unsafe_allow_html=True)

st.header('There is a birthday...')
st.image(opening_image)
st.divider()

questions = {1: 'Are you ready to start'}
answers={ 1: 'It can\'t be that simple',
          2: 'MELLON',
          3: 227,
          4: 'MESSIER 87',
          5: 15,
          6: 2,
          7: 19,
          8: 'NCC-1701',
          9: 'SNEEZY',
         10: 'ORD',
         11: 'I SOLEMNLY SWEAR THAT I AM UP TO NO GOOD'}
responses = { 1: None,
              2: None,
              3: None,
              4: None,
              5: None,
              6: None,
              7: None,
              8: None,
              9: None,
             10: None,
             11: None}

keys = list(responses.keys())
success = True

### Question 1

responses[1] = st.radio(label='Are you ready to start?', options=['Yes', 'No', 'It can\'t be that simple'], index=None)

for i in range(1):
    success = True
    if responses[keys[i]] != answers[keys[i]]:
        success = False

### Question 2

if (success == True) & (responses[2] is None):
    st.divider()
    st.image(q2_image)

    responses[2] = st.text_input('Off you go then...').upper()

    for i in range(2):
        if responses[keys[i]] != answers[keys[i]]:
            success = False

### Question 3

if (success == True) & (responses[3] is None):
    st.divider()
    st.image(q3_image)
    responses[3] = st.number_input(label='You cant cheat maths... How many squares are there on a Scrabble board, plus 2?', min_value=0, max_value=1000)

    for i in range(3):
        if responses[keys[i]] != answers[keys[i]]:
            success = False

### Question 4

if (success == True) & (responses[4] is None):
    st.divider()
    st.image(q4_image)

    responses[4] = st.text_input('No googling... which was the first black hole to be imaged from Earth?').upper()

    for i in range(4):
        if responses[keys[i]] != answers[keys[i]]:
            success = False

### Question 5

if (success == True) & (responses[5] is None):
    st.divider()
    st.image(q5_image)
    responses[5] = st.number_input(label='How many Smarties are in the tube hiding inside Panda?', min_value=0, max_value=1000)

    for i in range(5):
        if responses[keys[i]] != answers[keys[i]]:
            success = False

### Question 6

if (success == True) & (responses[6] is None):
    st.divider()
    st.image(q6_image)
    responses[6] = st.number_input(label='And how many of those Smarties are orange (the best/only flavour?!)', min_value=0, max_value=1000)

    for i in range(6):
        if responses[keys[i]] != answers[keys[i]]:
            success = False

### Question 7

if (success == True) & (responses[7] is None):
    st.divider()
    responses[7] = st.number_input('The Scrabble score you\'d get if REBUSSED was a real word', min_value=0, max_value=1000)
    st.markdown('P.S. The B is on a triple and theres no doubling of this word')

    for i in range(7):
        if responses[keys[i]] != answers[keys[i]]:
            success = False

### Question 8

if (success == True) & (responses[8] is None):
    st.divider()
    st.image(q8_image)

    responses[8] = st.text_input('What is the Enterprise\'s registration number?').upper()

    for i in range(8):
        if responses[keys[i]] != answers[keys[i]]:
            success = False

### Question 9

if (success == True) & (responses[9] is None):
    st.divider()
    st.image(q9_image)
    answer = st.text_input('Which of the seven dwarfs is last alphabetically?')
    responses[9] = answer.upper()

    for i in range(9):
        if responses[keys[i]] != answers[keys[i]]:
            success = False

### Question 10

if (success == True) & (responses[10] is None):
    st.divider()
    st.image(q10_image)
    answer = st.text_input('If the third child of Kim and Kanye had an airport, what would its code be??: ')
    responses[10] = answer.upper()

    for i in range(10):
        if responses[keys[i]] != answers[keys[i]]:
            success = False

### Question 11

if (success == True) & (responses[11] is None):
    st.divider()
    st.image(q11_image)
    answer = st.text_input('How do you open this piece of parchment?')
    responses[11] = answer.upper()

    for i in range(11):
        if responses[keys[i]] != answers[keys[i]]:
            success = False

if (success == True) & (responses[11] is not None):
    st.divider()
    st.markdown('But where are you going?')
    
    lat = 0
    long = 0
    
    left, right = st.columns(2)
    with left:
        lat_1 = st.number_input("If one = 3, two = 3, three = 5, four = 4, five = 4, then six = ?", value=0, min_value=-100, max_value=100)
        #3
    with right:
        long_1 = st.number_input("Solve the following equation: 9 – 3 ÷ 1/3 + 1 =?", value=0, min_value=-100, max_value=100)
        #1
    
    left, right = st.columns(2)
    with left:
        lat_2 = st.number_input("Joey had 6 siblings. All of them were born 2 years apart. The youngest is Chloe who is only 7 years old while Joey is the eldest. Calculate Joey’s age", value=0, min_value=-100, max_value=100)
        #19
    with right:
        long_2 = st.number_input("60 ounces of rice was divided equally and placed in 4 containers. How many pounds of rice were in each?", value=0.0, min_value=-100.0, max_value=100.0,step=1e-4, format="%.4f")
        #0.9375

    left, right = st.columns(2)
    with left:
        lat_3 = st.number_input("Solve: 3 + 2 x (8 – 3)", value=0, min_value=-100, max_value=100)
        #13
    with right:
        long_3 = st.number_input("If 1 = 5; 2 = 25; 3 = 325 and 4 = 4325; then 5 =?", value=0, min_value=-100, max_value=100)
        #1

    left, right = st.columns(2)
    with left:
        lat_4 = st.number_input("I am an odd number. Take away one letter and I become even. What number am I?", value=0, min_value=-100, max_value=100)
        #7
    with right:
        long_4 = st.number_input("Determine the solution to 2x + 15 = 8", value=0.0, min_value=-100.0, max_value=100.0,step=1e-1, format="%.1f")
        #-3.5

    left, right = st.columns(2)
    with left:
        lat_5 = st.number_input("(1/x)*15 = 1.576960067, what is x (to 6 d.p.)", value=0.0, min_value=-100.0, max_value=100.0,step=1e-6, format="%.6f")
        #9.511972
    with right:
        long_5 = st.number_input("Determine the solution to (1 - x) x 2 = 1.339", value=0.0, min_value=-100.0, max_value=100.0,step=1e-4, format="%.4f")
        #0.3305
    
    lat = round(lat_1 + lat_2 + lat_3 + lat_4 + lat_5, 6)
    long = round(long_1 + long_2 + long_3 + long_4 + long_5, 6)

    left, right = st.columns(2)
    with left:
        st.markdown(f'Latitude: {lat}')
    with right:
        st.markdown(f'Londitude: {long}')

    location = pd.DataFrame([[lat, long]], columns=['lat', 'lon'])

    st.map(location)

    if lat ==  51.511972 and long == -0.232000:
        st.balloons()
        st.title('Congratulations you\'re going to the Crystal Maze Live experience!! See you in the dome!')