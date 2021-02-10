# Data Exploration and Analysis Projects

This is a repository of some personal data exploration and analysis projects. These projects – conducted in Python – were done in Jupyter Notebooks to provide ease of viewing and reproducibility.

## Table of Contents

### [Predicting Recurring Blood Donations Using Logistic Regression](https://github.com/natasharavinand/Data-Exploration-Projects/blob/main/Predicting%20Recurring%20Blood%20Donations%20Using%20Logistic%20Regression/Predicting%20Recurring%20Blood%20Donations%20Using%20Logistic%20Regression.pdf)

<i>Adapted from the DataCamp project Give Life: Predict Blood Donations </i>

In this project, I utilized data from blood dontations to create a logistic regression model predicting if a donor was likely to give blood again. 

From DataCamp:

> Blood transfusion saves lives - from replacing lost blood during major
> surgery or a serious injury to treating various illnesses and blood
> disorders. Ensuring that there’s enough blood in supply whenever
> needed is a serious challenge for the health professionals.

The dataset is from a mobile blood donation vehicle in Taiwan. The Blood Transfusion Service Center drives to different universities and collects blood as part of a blood drive. In this project, I used logistic regression to predict the likelihood of a donor giving blood at another drive.

<hr>

### [Predicting Heart Disease with Random Forests](https://github.com/natasharavinand/Data-Exploration-and-Analysis-Projects/tree/main/Predicting%20Heart%20Disease%20with%20Random%20Forests)

This project was a web application deployment of a random forest classifier model to predict heart disease in patients using medical data. The data is pulled from the [UCI Heart Disease dataset on Kaggle](https://www.kaggle.com/ronitf/heart-disease-uci). The web app is built using Streamlit. Selected columns include information on age, sex, chest pain, blood pressure, cholestrol, and blood sugar. 

The web deployment, ran in `app.py`, allows the users to input their own values in order to view whether they are likely to suffer from heart disease given their own health parameters. 

<hr>

### [Successful App Profiles for the Google Play and App Store Markets](https://github.com/natasharavinand/Data-Exploration-Projects/blob/main/Successful%20App%20Profiles%20for%20the%20Google%20Play%20and%20App%20Store%20Markets/Successful%20App%20Profiles%20for%20the%20Google%20Play%20and%20App%20Store%20Markets.pdf)

In this project, I attempted to find what creates a profitable app – specifically, what traits are common in apps that maximize user engagement with advertisements and generate profit. I used Python for data exploration, cleaning, and analysis. 

As of September 2018, there were about 2 million iOS apps available on the App Store, and 2.1 million Android apps on Google Play. I collected and analyzed data of mobile apps currently active on both the Google Play and App Store. I analyzed a sample of the total data (4 million apps total) by using two data sets via Kaggle. 

The first data set was a sample of approximately 10,000 Androids apps from the Play store from August 2018 – this can be downloaded [here](https://www.kaggle.com/lava18/google-play-storeapps) from Kaggle. The second data set was a sample of approximately 7,000 iOS apps from the App Store – this can be downloaded [here](https://www.kaggle.com/ramamet4/app-store-appledata-set-10k-apps). 

I went through 3 stages in the process: exploring the data, cleaning the data, and analyzing the data to generate actionable insights. For simplicity, I focused only on free apps presented in the English language.

<hr>

### [Analyzing Data Between NYC High Schools and SAT Results](https://github.com/natasharavinand/Data-Exploration-Projects-in-Python/blob/master/Analyzing%20Data%20Between%20NYC%20High%20Schools%20and%20SAT%20Performance.pdf)

The Scholastic Apitude Test, or SAT, is a standardized test for college entrance that millions of high-school students take each year. However, the SAT has long been under scrutiny – there have been many critics voicing the low efficacy of these tests in predicting who can succeed in college level coursework. In addition, many critics have commented on how the tests are unfair to certain groups with less resources, dispelling the meritocracy claims standardized tests make.

In this project, I analyzed the correlations between demographics (across race and gender specifically) and SAT scores. I also focused on New York City public high schools, because of their diversity and accessibility of data from the City of New York. 

<hr>

### [Exploring FiveThirtyEight’s Star Wars Survey](https://github.com/natasharavinand/Data-Exploration-Projects/blob/main/Exploring%20FiveThirtyEight%27s%20Star%20Wars%20Survey/Exploring%20FiveThirtyEight%27s%20Star%20Wars%20Survey.pdf)

In this project, I analyzed FiveThirtyEight’s Star Wars survey conducted before Star Wars: The Force Awakens was released in 2015. Their guiding question when conducting question was: does America believe Star Wars: The Empire Strikes Back is the best Star Wars film? The team used SurveyMonkey to obtain their data, receiving 835 total responses. The data can be downloaded [here](https://github.com/fivethirtyeight/data/tree/master/star-wars-survey) from their repository on Github.

<hr>

### [Exploring Trends in Hacker News Posts](https://github.com/natasharavinand/Data-Exploration-Projects/blob/main/Exploring%20Trends%20in%20Hacker%20News%20Posts/Exploring%20Trends%20in%20Hacker%20News%20Posts.pdf)

Hacker News is an online platform started by Y Combinator, and is extremely popular in circles of the tech community. Two main types of posts are often added: 

 - “Ask HN” posts, which are composed of a question directed towards
   the community
 - “Show HN” posts, which often seek to publicize a product, project, or an interesting development 

I sought to analyze a data set from Hacker News (from roughly September 2015 - September 26, 2016) in order to discern which kinds of posts get the most engagement (dataset can be found [here](https://www.kaggle.com/hacker-news/hacker-news-posts)). Additionally, I will analyze whether posting at certain times invites more engagement – all times are in EST.

<hr>

### [Visualizing the Gender Gap in Various College Majors](https://github.com/natasharavinand/Data-Exploration-Projects/blob/main/Visualizing%20the%20Gender%20Gap%20in%20Various%20College%20Majors/Visualizing%20the%20Gender%20Gap%20in%20Various%20College%20Majors.pdf)

In this project, I explored the gender gap across college majors through various visualizations in Matplotlib. My aim was to illustrate gender discrepancies between majors – especially those in STEM fields. The dataset used had been cleaned and provided by University of Pennslyvania professor Randal Olson, and can be found on his personal website [here](http://www.randalolson.com/percent-bachelors-degrees-women-usa/). It explores the percentages of men and women from 1968 to 2011 who have comprised different majors.