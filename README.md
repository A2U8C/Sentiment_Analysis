# CHAPTER 1: INTRODUCTION

1.1 Problem Definition

Sentiment analysis is the technique of capturing the emotion behind the text. It applies natural language processing (NLP) and machine learning to detect, extract, and study people’s or customers’ perceptions about a product, topic, news, etc. In our project we aimed to analyse the sentiment of the tweets of various Twitter users. Such analysis is helpful for understanding the sentiment of various Twitter users towards various topics, and also for understanding whether the general consensus towards something is positive or negative. This can then be used to analyse and visualise the sentiments of a particular person’s latest tweets for better understanding of the data.
In this way, a particular person’s sentiment towards recent topics or issues can be understood by analysing their tweets’ sentiments. By doing so for a number of users, the sentiment analysis would help to understand the common consensus and sentiment at a particular point of time.

1.2 Scope of the project

Projects like these have a wide variety of scope when it comes to analysing reviews regarding products or services. 
Social unrest regarding issues can be avoided by detecting negative sentiment of Twitter users in advance. 
Similar platforms can be built for various other social media platforms to get more analysis.
A person’s opinion regarding certain products or current issues can be understood by analysing his or her most recent tweets.
The project can further be used to compare sentiments of different users.





1.3 Users and their requirements

Users of this system could be:
Various media organisations trying to understand sentiments regarding current affairs 
Government trying to avoid social unrest by detecting high negative sentiments on current affairs.

The requirements of the users include:
An interface where they can enter the username and get sentiments regarding the latest tweets of that user. 
An interface where the sentiments of the entered username are summarised and visualised with the help of graphs.


1.4 Technologies to be used
Python 3.6
TextBlob
Matplotlib
Flask Framework
Pandas
Natural Language Toolkit (nltk)
Tweepy


	










CHAPTER 2: LITERATURE SURVEY

2.1  Literature Survey
A Study on Sentiment Analysis Techniques of Twitter Data Abdullah Alsaeedi1 , Mohammad Zubair Khan2 Department of Computer Science, College of Computer Science and Engineering Taibah University Madinah, KSA 
Abstract --  This paper is a comparison of all the known methods and their working and accuracy. These models used either the twitter API or datasets of old existing tweets. Twitter is an enormously popular microblog on which clients may voice their opinions. In recent years, researchers in the field of sentiment analysis have been concerned with analyzing opinions on different topics such as movies, commercial products, and daily societal issues. Opinion investigation of Twitter data is a field that has been given much attention over the last decade and involves dissecting “tweets” (comments) and the content of these expressions. As such, this paper explores the various sentiment analysis applied to Twitter data and their outcomes. 
 
A. Sarlan, C. Nadam and S. Basri, "Twitter sentiment analysis," Proceedings of the 6th International Conference on Information Technology and Multimedia, Putrajaya, Malaysia, pp. 212-216, doi: 10.1109/ICIMU.2014.7066632.

Abstract -- This paper first discusses the two main approaches for extracting sentiment automatically which are the lexicon-based approach and machine-learning-based approach. The model will categorize sentiment into positive and negative (and null), which is represented in a pie chart and html page. Twitter is one of the social media that is gaining popularity. Twitter offers organizations a fast and effective way to analyze customers' perspectives toward the critical to success in the marketplace. This paper reports on the design of a sentiment analysis, extracting a vast amount of tweets. Prototyping is used in this development. Results classify customers' perspective via tweets into positive and negative, which is represented in a pie chart and html page. However, the program has planned to develop on a web application system, but due to limitations of Django which can be worked on a Linux server or LAMP, further this approach needs to be done.

S. A. El Rahman, F. A. AlOtaibi and W. A. AlShehri, "Sentiment Analysis of Twitter Data," 2019 International Conference on Computer and Information Sciences (ICCIS), 2019, pp. 1-4, doi: 10.1109/ICCISci.2019.8716464.
Abstract -- The aim of this paper was to present a model that can perform sentiment analysis of real data collected from Twitter. Data in Twitter is highly unstructured which makes it difficult to analyze. However, the model proposed here is different from prior work in this field because it combined the use of supervised and unsupervised machine learning algorithms. The process of performing sentiment analysis done here was follows: Tweet extracted directly from Twitter API. This was then followed by cleaning and discovery of data that was performed. After that the data was fed into several models for the purpose of training. Each tweet was classified based on its sentiment whether it is a positive, negative or neutral. Data was collected on two subjects, McDonalds and KFC to show which restaurant has more popularity. Different machine learning algorithms were used. The result from these models were tested using various testing metrics like cross validation and f-score. Moreover, this model demonstrates strong performance on mining texts extracted directly from Twitter. For validation and testing, several  metrics were used such as recall, precision and f score.

M. S. Neethu and R. Rajasree, "Sentiment analysis in twitter using machine learning techniques," 2013 Fourth International Conference on Computing, Communications and Networking Technologies (ICCCNT), 2013, pp. 1-5, doi: 10.1109/ICCCNT.2013.6726818.

Abstract :-  This paper uses machine learning techniques for general sentiment analysis. They are using 1200 tweets as their dataset which they collected from a period of 1 month. After the dataset is created, the features are extracted in two parts. The first part extracts information from tweets which are in the form of emoticons and hashtags. The second part extracts information from the text of the tweet. For text preparation, they are using the unigram approach which results in collection of words. Then they created a list of positive keywords, negative keywords and a list of different words that represent negation. The various keywords generated while list creation are not treated equally. So to overcome that, the authors are selecting a special character from the tweet. If a relevant part of speech can be determined for a keyword, then that is taken as a special keyword. Otherwise a keyword is selected randomly from the available keywords as a special keyword. Thus the feature vector is composed of 8 relevant features. The 8 features used are part of speech (pos) tag, special keyword, presence of negation, emoticon, number of positive keywords, number of negative keywords, number of positive hashtags and number of negative hashtags.



Vishal.A.Kharde, Prof. Sheetal.Sonawane, “Sentiment Analysis of Twitter Data: A Survey of Techniques”, International Journal of Computer Applications (2016)

Abstract -- Sentiment analysis can be defined as a process that automates mining of attitudes, opinions, views and emotions from text, speech, tweets and database sources through Natural Language Processing (NLP). Sentiment analysis involves classifying opinions in text into categories like "positive" or "negative" or "neutral". Preprocessing of the dataset here includes removing all URLs, hashtags, targets, stopwords, punctuations, symbols, numbers and also all non-english tweets. Also, all acronyms are replaced with their sentiments and the acronyms are expanded. This entire process is then followed by feature extraction. Part of speech tags, words and their frequencies, opinion words and frequencies, position terms, etc are extracted. Finally various machine algorithms such as Naive Bayes, Maximum Entropy, Support Vector Machine are applied or lexicon based approaches like dictionary based or corpus based are used.











CHAPTER 3: CONCEPTUAL SYSTEM DESIGN

# 3.1 Conceptual system diagram

![Conceptual_Diagram](Images/Conceptual_Diagram.PNG)

				Fig 1.Conceptual Diagram

The above diagram shows the conceptual design of our system.  The first step includes loading the dataset to our system. The dataset we have used was based on a review dataset which had 3 labels in it, i.e. positive, neutral and negative. It includes 4 attributes: text, polarity, score and subjectivity.

The next step includes preprocessing of data using various methods of Lemmatization, removal of stop words and cleaning the data thoroughly so that it is ready for processing. After successfully preprocessing the data, we proceed to train our model.  

Modelling is the process of representing the patterns in an effective manner and then using the model and data for visualization. After that, we carry out successful testing for the data we have fed and obtain results.













3.2 Design of Modules in Detail
1.Load Data

2.Clean Data







3.Feature Engineering



4.Data Analysis

5.Modelling Reviews


CHAPTER 4: IMPLEMENTATION AND EVALUATION
4.1 Implementation
Determining Subjectivity and Polarity of tweets





User Interface:






















4.2 Evaluation 
WordCloud:




ROC Curve:

Precision Recall Curve:

 



CHAPTER 5: CONCLUSION AND FUTURE SCOPE

5.1 Conclusion 
The popularity of social media is now at an all time high. People voice their opinions on these platforms and this becomes very important for various organisations and other parties involved. The analysis of sentiments of these opinions voiced on social media is a very critical task for a variety of reasons. This can be to keep a check on social unrest, to understand sentiment of users regarding certain products or issues and also to understand the general consensus regarding a variety of ongoing issues.
The project we have implemented is specifically built for analysing Twitter data. Twitter being a social media platform where the main method of interaction is through tweets which are in the form of text, the voicing of opinions and reviews is the maximum here. A particular person’s sentiment towards recent topics or issues can be understood by analysing their tweets’ sentiments. By doing so for a number of users, the sentiment analysis would help to understand the common consensus and sentiment at a particular point of time. This proves to be vital for a lot of stakeholders like various media outlets, product manufacturers and sometimes even the government.

5.2 Future Scope

The project developed here is specific to a certain social media platform, that is Twitter. The same system cannot be used for overall analysis of sentiments over a number of social media platforms. Thus, there is a scope of improvement in the sense that either a new system can be built for each of the other platforms like Facebook, Instagram etc which can then be aggregated to find overall sentiment across various platforms, or a single system can be built that works for different social media platforms at the same time. 
At the same time with regards to Twitter itself, the project can be further extended to obtain sentiments pertaining to specific words or trends by obtaining general tweets from all over the world instead of doing that for an individual user's tweets. There can also be a higher level of visualisation of these sentiments with more complex graphs taking into account more variables like frequency of tweets and intensity of the words used, etc.




























CHAPTER 6. REFERENCES 

A Study on Sentiment Analysis Techniques of Twitter Data Abdullah Alsaeedi1 , Mohammad Zubair Khan2 Department of Computer Science, College of Computer Science and Engineering Taibah University Madinah, KSA

A. Sarlan, C. Nadam and S. Basri, "Twitter sentiment analysis," Proceedings of the 6th International Conference on Information Technology and Multimedia, Putrajaya, Malaysia, pp. 212-216, doi: 10.1109/ICIMU.2014.7066632.

S. A. El Rahman, F. A. AlOtaibi and W. A. AlShehri, "Sentiment Analysis of Twitter Data," 2019 International Conference on Computer and Information Sciences (ICCIS), 2019, pp. 1-4, doi: 10.1109/ICCISci.2019.8716464.

M. S. Neethu and R. Rajasree, "Sentiment analysis in twitter using machine learning techniques," 2013 Fourth International Conference on Computing, Communications and Networking Technologies (ICCCNT), 2013, pp. 1-5, doi: 10.1109/ICCCNT.2013.6726818.

Vishal.A.Kharde, Prof. Sheetal.Sonawane, “Sentiment Analysis of Twitter Data: A Survey of Techniques”, International Journal of Computer Applications (2016)

https://monkeylearn.com/blog/sentiment-analysis-of-twitter/

https://towardsdatascience.com/twitter-sentiment-analysis-classification-using-nltk-python-fa912578614c

https://www.analyticsvidhya.com/blog/2018/07/hands-on-sentiment-analysis-dataset-python/
