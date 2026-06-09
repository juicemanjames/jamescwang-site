---
title: "When Pornhub Meets Data Science"
category: "Social Studies"
tags: "Web Scraping, Tree Models"
date: "May 2020"
summary: "I scraped pornhub.com to answer the million dollar question: does size matter?"
thumbnail: "/assets/images/5ec2d6adcd23dfa76d3c29ea_love-sex-book-cover.jpg"
featured: true
order: 1
---

*This project was presented during my final stats class at Duke. It was a hilarious joke project. While I relied on data to tell its story, don’t quote this as my personal sex view.* :)

I highly encourage you to checkout my [voiceover](https://www.youtube.com/watch?v=PZ8xDPjjtJY&feature=emb_title) of the web app for this project.

Sexual desires and preferences have been a hard topic to study due to their sensitivity and privacy. In this project, I scraped 21,557 videos from the top 573 pornstars on Pornhub.com, to gain insights about what contributes to success, to both a video and a pornstar, defined by the video views and video ratings. The models find big cup size, young age pornstar, short video length, short video title, and a monogamous scene are the most significant predictors to increase the favorability of the videos and pornstars. To better visualize the specialty of each star, a shiny app with TFIDF word cloud of video titles for each star is created.

> Does size matter?

Does size matter? What’s the optimal age for a star? Do people have better experience in watching many short videos, or skimming through just a few long videos, during a sitting? These are the questions both Pornhub and social scientists are trying to answer. However, if the study of public opinion in politics is difficult due to the survey constraints such as voluntary response bias and social desirability bias, the study of sexual preference, being a sensitive and private topic, is even more challenging. Yet, while people might falsify their preferences during surveys, they are by and large honest during private internet activities. In this project, I aim to identify the drivers of sexual desirability, at least in masturbation.

> How to webscrape 20k porns?

The data is collected through scraping the pornstar bio pages on pornhub.com, which contain not only the biological data of the pornstars but also at most 50 of their videos. There were over 15,000 pornstars listed, and my plan was to scrape all of their data. However, I realized that there were significant missing data problems even in the top ranked 50 stars. Believing that additional stars would not contribute to noise more than signal if I go too far down to the list, I ended at obtaining data for the top 573 stars, and their 21,557 videos.

During the web scraping, the website kicks me out when it identifies the scraper. In response, I put a time-out between each loop -- a random number sampled from a truncated normal distribution with a mean of 10 sec – to mimic natural browsing behavior.

The collected video dataset has these predictor variables: number of actors, video length, video title, and the number of characters in the title, which video rating as the response variable.

The pornstar dataset has mostly biological predictors: gender, dimensions (bust, waist, hip, and cup size), height, weight, active status (binary), and age, with total video view as the response. Although I have two other potential response candidates: ranking and number of subscribers, the video view variable is the one with the least missing data. In addition, the dimension variables are 73% missing on the site. To deal with this problem I used multiple imputation, because the dimension variables are indeed significant. The active status and gender variable were dropped, because over 99% of the stars are women and active artists.

> Fit a model on a (sex) model

I used GBM (gradient boosted regression tree model) because of its ability to fit nonlinear data. When I first fitted a logistic regression to predict video quality (Good: Rating > 80%), none of the coefficients beside cup-size were significant. This model misspecification failure is due to the fact that some of the predictors are not linearly associated with video quality. For example, we simply could not say that a 1-year increase in age associates with a 1% increase in odds of the video being good. It’s much more an inversely U shaped relationship intuitively.

![](/assets/images/5ec2d4759cdcb6462b308b67_JHUDYhKXRT4BifNMsAx2IqQyaqooXt_WmSVVUFdfYi_a2upJSKO-1aS7xQfhLELoda_Rfeap0n-4TSqMFd8upK3z7rfHE-zbq9ttDIQkuD1ZiMqYe2bhXx8WWDxn95CObXqcaNQ.png)
*Added Variable Plot of age provides zero insight*



Tree models, on the other hand, do not require the assumption of linearity. In addition, tree models also bypass the problem of multicollinearity between predictors, such as weight and height, and dimensional variables with weight and height.

I prefer GBM over random forest for its additivity. Because GBM iteratively fit weak trees on the residuals, it prevents overfitting while achieving a high predictive power. As we can see from the ROC curves, GBM outperforms logistic regression in prediction, while providing insights through partial dependence plot and relative variable influence.

![](/assets/images/5ec2d475cd23df902f3c2723_O-MKka9Rvh42FYCOdp0KfYEztYsULzat3xMYrskN0DDe4HUfy_BF5yAjE4P1i2bk-tgn2TIqthHvQi0AgKwPod0VaMhneipCYU8CpTR8fqGGoKyOW5aglxJ1RLG5c0ksbxE3JHY.png)

**Model Result--Part 1: Video rating **

![](/assets/images/5ec2d4753681de3d9b252af9_qaMPnh769uecaGPpmj7Ai6GyLkjmB4PU84krJ5IrkiP7uNfkz1wD8y67t2tes9nLO3xeeyAYEZrwk2Eul7zvuT3FCSEP6HWvoEUWfR_iqJffTdNijmCtJkhLR6yr3sk1gcgnxsM.png)
*Logistic regression model, was replaced by GBM while all the predictors remain the same*



For classifying video rating ( >= 80%), the GBM model outperformed logistic regression model in both AUC (area under the ROC curve) and true prediction rate (.71> .67). Given limited scrapable features from the website, the 71% true prediction rate is satisfactory.

The relative influence (variable importance) plot is generated by taking out the variable of interest and “scramble” all other variables, to measure the change in model deviance in order to gauge the relative influence of that variable. We see the length of the video and number of characters in the video title are the most influential variables.

![](/assets/images/5ec2d475ffeb707af43ca15f_-fC9yy2dkiFyKGnXPNsiS_gRhrq8oGfCjAqvR0AvMkKZjyaN8W0bc4WXGbTyao-J1fyDrh_DcSh31Fl8sEJ4gUS39c1-DwGq5o5eKEsfxhH5uONn4GIP8oYFN5eMa-7bv3KnHH4.png)

Partial Dependence Plot (pdp) calculated the relative trend of the prediction when changing the variable of interest, integrating out all other variables. It is somewhat analogous to the added variable plot for regression, except it relaxes linearity assumptions. From these pdp, we see videos with 3-5 min and 16-20 minutes rate higher; we also see people rate videos with shorter titles higher; it’s most interesting to see that viewers prefer either 2 or 4 actors in the same video, while a threesome or orgy (5 or more) are rated lower.

![](/assets/images/5ec2d47519d31121557d8eef_3gZFVdgDdD47NJzno6jjzvRmCkbjdTClFJErltIP2pNWjK9nd2gfBvRiQGOLug6_MaV0MPRNLz4OKRTZID3QBjmlu_8WCXnNbiHvx_e3WXZQ96VT1lfM3vCtO7YWo8pRwdad3rw.png)
*Videos with 3-5 min and 16-20 minutes rate higher*

![](/assets/images/5ec2d475137b1f115b10fac5_38gBCDQjlghfsMkeeLg96MRUSjR51NZWbBeVhyhovF14QoqRT5rppJdS1de1DZcQ9c69uN36IX9S1leRNE5Tvog5BqHASRwbiTv-h6TRzBxc9nawPiXfRQckkV8LnGEV6AqcTGY.png)
*Videos with shorter titles rate higher*

![](/assets/images/5ec2d4759683f62e76e03968_UOUL9ngO-zdWOf1ifbcoysymcnOpHoHRzaoCg-9cOCATsZqYijWhHYDQ2tKn_JEdjw98jkLmYXUxIjFeeV0OCMBcnLN3oE-NLan5l-zOwubgsIkUl3WfHlFD1ADc62TxXUNMDR8.png)
*Viewers prefer either 2 or 4 actors in the same video, while a threesome or orgy (5 or more) are rated lower.*

**Model Result Part 2--Porn Star Views:**

![](/assets/images/5ec2d475cc5f83d05bbcdb68_3UI4tLocfP4Z7ZJQBEeHGk2PMhDr8oEF-RKiD2tCDehtaa1KKA5Du9_5ohdE7q0rjiXkJfHCI_8fkP6CAjcZNeiYnK9-_oTRcrjdz9cW6-W_gP6vhxVlbl2UcVAzhRysSuBjfvM.png)
*Log-linear regression model, was replaced by GBM while all the predictors remain the same*

I used a GBM model to predict the log(video views) for each star, using their biological variables as predictors. Due to the significant missing data problem with the star’s dimension data, I used multivariate imputation, assuming the data of height and weight could provide information on the dimensions. As a result, I found cup size and age to be the most significant predictors for a star’s video views.

![](/assets/images/5ec2d475f5c210ab57024767_W2fcjFNJ8WDzo30jYLoIgSm6MnEF0euZ9PGRussHZVwJWNCLgizUT3-h0YFNRyD53jZJvETmgwonqZLox2srTsbMcaKA1CS52T7_ZyIktMIK5Ed6NY8ULrFCL3xyiRtxB3kHy2s.png)
*Cup size and age to be the most significant predictors for a star’s video views.  D1, D2, and D3 are the 3 dimension metrics.*

As the partial dependence plots indicate, the prime age for a pornstar is around 23. I believe since the biggest porn viewers are teenagers and young adults, they do prefer younger pornstars. A star accumulates popularity and skills after she enters the industry after the legal age of 18, and “ripe” when she is around 23. The age effect from 28 to 45 is nearly flat, signaling that middle age pornstars are in demand by many demographics, from young adult break up to middle-age crisis.

Does size matter? Yes. GBM model found that cup size D, followed by E, are the most coveted boob size for viewers. Unfortunately, stars with cup size A were at a disadvantage. However, this model could be biased significantly since the 73% of the cup size data were imputed.

![](/assets/images/5ec2d4753f7d0e1ccc596978_k993PCj6hcdL9RCkTk-uoNjxTrOUDQ4NGwk8mmxveti59p4C2ik9LFhwa4ZKU8fGhUV-l7dLconKl_ph66869mCN8TUqYxEywc0IpjUi3osGfWHyDNQnVpWSvQzLC2gKTC6zzRI.png)
*A star accumulates popularity and skills after she enters the industry after the legal age of 18, and “ripe” when she is around 23.*

![](/assets/images/5ec2d475de38e2d8b7eb74b6_su7-TtJ9eHVD5owBN9KNTL5ic-Zm_HtnOvb7-ShQKNWGCwXZeNENpQ-fDbltDfs45HD4mAWusC-ahFYgvIa2eQSokDGoGzHlcHk847-Plhd3ogLLK3ap3e9Y_5Lpm9okQZVn13o.png)
*Cup size D, followed by E, are the most coveted boob size for viewers*

> Visualization:

In order to visualize the specialty of each pornstar in a scalable way, I constructed a TFIDF word cloud based on texts from each star’s video title. In the bio page, each star has 0-50 videos with title. I tokenized all these titles into a bag of words, with each document denoting each star, and computed TfIdf (term frequency inverse document frequency) for the star vs token matrix. The text corpus underwent many steps of pre-processing, such as removing all the stop-words including pornstars’ names, stemming, and stripping punctuations.  In the Shiny App, when we select a pornstar, the code would visualize the star’s top 100 tokens ranked based on their TfIDf score in a word cloud. Playing between having a 1-3 words ngram tokenizer, I found that only 1 word produced the best word cloud, as the bigrams and trigrams are sometimes attaching two unmeaningful words together.

By and large, the wordcloud does a fair representation and differentiation of the pornstar, despite only using up to 50 of the videos listed on her bio-page. For example, the Duke student turned pornstar Belle Knox has a word cloud with most prominent tokens being “Duke '', “university”, and “tuition” (she started making porn in order to pay the Duke tuition).

![](/assets/images/5ec2d475a420270bb8a11502_GogMqMQTEfhUdjuxhlDIIdGluwGnpWUlI8gpHuFJ7ydErtS5h8YGhZns0g47dij3HQiLR4_wKrlj4zsdJ88ZrxPPC48HnHiGfOIt4pbauUYkr6s90wbBH2h5VTbzhJLDKDQiCPQ.png)
*Wordcloud for Belle Knox*

> What do I still need to know?

This project encountered unexpected challenges from html time out, missing data, and model misspecification, and was able to tackle them in a fairly clean way. However, the lack of informative features, absent from the website, such as race and video genre limited the predictive power of the models.  The age model also suffers from a small sample size problem  (n = 573). I believe had there been more pornstars with detailed bio pages, the model would have been more robust.

The sampling and representation bias is another unsolvable challenge for this project. Because 30% of the pornhub viewers are women (based on 2017 data), it is biased to extrapolate the pornhub viewer behavior to either men and women or just men. The age demographic is also unequally represented. In addition, since most of the pornstars are white women, it is hard to gauge the sexual preferences for the minority demographics.

<iframe width="560" height="315" src="https://www.youtube.com/embed/PZ8xDPjjtJY" frameborder="0" allowfullscreen></iframe>
