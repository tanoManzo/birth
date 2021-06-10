
import streamlit as st
import datetime
from PIL import Image

from streamlit import beta_util

flag_age=0
flag_date=0
flag_yes=0

st.title("Welcome to my Birthday Quiz")
st.write("""
   ## Let's start with the first question
""")

age=st.slider("How old will I turn this year ?",28,35)

if age==30:
    st.markdown("<h1 style='text-align: center; color: green;'>Wow, nice one!</h1>", unsafe_allow_html=True)
    flag_age=1
elif age <30:
        st.markdown("<h2 style='text-align: center; color: red;'>Whooooops!</h2>", unsafe_allow_html=True)
else:
        st.markdown("<h1 style='text-align: center; color: red;'>Are you CRAZYYY!</h1>", unsafe_allow_html=True)
    

if flag_age==1:
    st.write("""
    ## Yeah, Let's continue..
    """)
    d = st.date_input("When's my birthday?",datetime.date(2021, 6, 10))

    if d.month==6 and d.day==15:
        st.markdown("<h1 style='text-align: center; color: green;'>Wow, nice one!</h1>", unsafe_allow_html=True)
        flag_date=1
    elif  d.month==6 and d.day==19:
            st.markdown("<h2 style='text-align: center; color: red;'>That's the party's day. Whoops!</h2>", unsafe_allow_html=True)
    else:
            st.markdown("<h2 style='text-align: center; color: red;'>Whoops!</h2>", unsafe_allow_html=True)


if flag_date==1: 
    col1,col2=st.beta_columns([2,0.25])
    col1.write("""
    ## Nearly done, ready for the final question?
    """)
    col2.write("")
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}      </style>', unsafe_allow_html=True)
      
    ans=col2.radio("",('No','Yes'))
   

    if ans=="Yes":
        im1 = Image.open("bat.png")
        im2 = Image.open("dum.png")
        im3 = Image.open("giu.png")
       
        c1,c2,c3=st.beta_columns(3)
        c1.image(im1, caption='Image 1', use_column_width=True)
        c2.image(im2, caption='Image 2', use_column_width=True)
        c3.image(im3, caption='Image 3', use_column_width=True)
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}      </style>', unsafe_allow_html=True)
        
        choice=st.radio("Which of the above images is my Giulietta?",('Image 1','Image 2','Image 3'))
        if choice=='Image 1':
            st.markdown("<h2 style='text-align: center; color: red;'>That's Batman. Whoops!</h2>", unsafe_allow_html=True)
        if choice=='Image 2':
            st.markdown("<h2 style='text-align: center; color: red;'>My Giuly is fatter. Whoops!</h2>", unsafe_allow_html=True)

        if choice=='Image 3':
            st.markdown("<h1 style='text-align: center; color: green;'>Congratulation! You did it</h2>", unsafe_allow_html=True)
            st.write("""
            ### Feel free to add your +1. Pets are welcome!!
            """)
            st.write("check out this Doodle [link](https://doodle.com/poll/kvqik8vi35qtz8pg?utm_source=poll&utm_medium=link)")
            st.write("""
            #### if your share the link, we lost all the fun!
            """)