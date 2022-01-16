from flask import render_template, url_for, flash, redirect,request
from website import app
from website.forms import *

from werkzeug.utils import secure_filename
import os




@app.route("/", methods = ['GET','POST'])
def userinput():
    username_form = TwitterUserForm()
    topic_form = TwitterContentForm()


    #return render_template('inputform.html',text_title_form = text_title_form, URL_form=URL_form, image_form=image_form)
    return render_template('button_form_input.html',username_form = username_form, topic_form=topic_form)
    #return render_template('input_button_form.html',text_title_form = text_title_form, URL_form=URL_form, image_form=image_form)

@app.route("/about")
def about():
    return render_template('about.html', title='About')



@app.route("/result", methods = ['POST'])
def result():

    type = request.args.get("type")
    if type == "username":
        from website.ResultMethods import usernameOnly

        user_name = request.values['TwitterUsername']

        result_text, image_name,sub_pol_name,twitterAccount = usernameOnly(user_name)

        return render_template("results.html", result_text=result_text, type=type, image_name=image_name,
                               sub_pol_name=sub_pol_name,twitterAccount=twitterAccount)

    elif type == 'topic':
        from website.ResultMethods import topicOnly

        tweet_topic = request.values['TwitterTopic']

        clean_text,text_subjective,text_polarity,text_score,text = topicOnly(tweet_topic)

        return render_template("results2.html", clean_text=clean_text, type=type, text_subjective=text_subjective,
                               text_polarity=text_polarity,text_score=text_score,text=text)

        #return render_template('dummy.html')



