---
title: "What does Facebook Know? Predicting Your Personalities"
category: "Machine Learning"
tags: "Recommender Engine"
date: "May 2018"
summary: "We designed an algorithm that used Facebook data to predict your IQ and personalities"
thumbnail: "/assets/images/5b25b896d01fe0d04f359d7c_IMG_5923.JPG"
featured: true
order: 3
---

3 things you will Learn from this post:

~ Your Facebook data has value, and bad guys are using it

~ We designed an algorithm that used Facebook data to predict your IQ and personalities

~ By using Matrix Completion technique in data preprocessing, we boosted our prediction by a lot!



Our* digital footprint* (the social media data) is huge. And our digital footprint is valuable, and extremely valuable to those big data companies.

![](/assets/images/5eb9b537450cf3433afc3036_ggJfIYCck8Yb-wSIQvk5dZIGa1Q_6pP-d-krdF-T3wpetMOXvJAYrCznCSf7GboxSfPvXlmsZb6AFLb72Piw2ElG3sOhfYhzt9xOlmXs9N3rDq8qbgiGKTvJdWwg4feH0Dnl6K8.png)

If you been on the news, you knew that you might be* one of the 87 million users* whose data was used by *Cambridge Analytica* for *target advertising for the Trump campaign*, and the data was accessed *illegally*.

![](/assets/images/5eb9b538945ba640d61cf422_FAxt719gp2JPaKiggYAXvqIg7ONCRXqTEVrUR-MIFgr40u4s5gJGQaN2BrGcaacdEOG2tkL2yVWehFSZO7q0Nrty7FJucWucVnbPmd_6urGVUHVJql1rhGkDX5qvx5-IQHTOD30.png)

And there are larger implications about your data.

What can FB data predict about you?

A lot, it turns out...

It can predict your demographic information (i.e. your age), your psychographic information (i.e. your personality), and your habits and background information, even your relationship status. Isn’t that scary?

![](/assets/images/5eb9b537d7f3243fa8d2adcc_aHNDw_sRFVYxoPsm0fBVps_hqq0ZfrWaDjzY9nB7Il5M0l9qk7LH8lOj4tx92KaJSPtEsEQ9R4m7I4UPQXJbLJsThVs-dsE8HnNsrpsg3UfTNbJ82--wP8zuiDWQ-M2DubxVw3A.png)

Before I talk about our research, I want to establish what type of previous research is out there for predicting attributes about rationality. *Kosinski et al *has introduced us this great scheme to use. It uses user-like sparse matrix of Facebook to predict people user’s personality, age, and gender.

![](/assets/images/5eb9b537f5aad4195ab4d841_efsjwMUCC3DsHMkH1B7UqJkAWgb8hgsk2qQxPXdROGgZeKIoEJTEK81tnWT6xJ2GZdF2XnXZX8NPnQm_o2PltlJJnko3aZicB_XBIY4fEfUAHYVArVtSQ4G7B6f_JPsmHYbElWI.png)

Their steps are as follows:

~ Trim the user-like sparse matrix to limit only Users with 50 + likes and (Facebook post) Likes with 150 + likes

~ Reduce the dimension of the data from high dimension (one hot encoding of Likes) to 50 linear components using SVD

~ Use linear regression to train, test, cross-validate, and predict personalities

![](/assets/images/5eb9b5370bba4be640e3e698_1weYW8hPgNLBSpdfKQQ_SmE1ODxOwaFwnKsbsxFgHXUj-J8UrtHKzw1S98QCfqUF8bdKcFot7ubPPnXs4A5pGR6jiq3lOJ_trFn6US3KxqbG_AEL1gvDxgHklhkVsrJrMb-oWhA.png)

Using linear regression, they were able to predict the *Big 5 Personality Test* scores (OCEAN score).   Each user here took the big 5 personality test online, and received a score.

![](/assets/images/5eb9b5374e5f145fa9565e88_Xj6neo2XAd2PMSaG4OTgZQRHdBok6EV7J9Pl5prVI0tngVSrItaA68NvPv353zpPcR7PI5fIRlS7WAepPTnADJGtrHoBvuI4hPNingqnuV7oktjIbTSFtMlktyXkAxVd3QXbk9Y.png)

Here’s the [Big5 test](https://www.truity.com/test/big-five-personality-test) if you want to take it

Comparing its prediction to its true score (which is based on their online test and is arbitrary), *Kosinski et al* gets a decent correlation (r). It shows how well the prediction values correlate with the true data.

Here's how they perform. And we are going to reintroduce them when we are showing our values

![](/assets/images/5eb9b5385ab01a61e97efbad_raWM-aIJqq3CF5zZKp6RzyvoM5chJck6PW9wwD2OCv6c-o_qvd0KmwWQ10p8ZvCgDRpKyR3oGp7Qdrwii4jqIquIyYBLFsbcPPk60X7XW6FqAh7_dHwnFLG39lNTKfVq1NoLHsU.png)

**What we are curious is that how can we improve its prediction? Should we use better model? Or can we pre-process the data better?**

![](/assets/images/5eb9b538bf81970ad1b7cf14_b4FbES4CopuOND_mNa0_yG9_7bOwdtpsl6w44I7D5qSpLHOco-g8ChLkq7qb0sBZnmDVs8yAUH6V6mXohwiaQzBPWN6qDsTjzZOPkt1gKsBLGg7eYdYGDofFr5ajsNJLCOz1asE.png)

Take a step back, and I want to introduce you to my friend Joe. Joe is a fictional character that we created. Although he’s my friend, I don’t know him very well. In fact, the only information I have about him are the 26 Facebook posts that he clicked “Like”.

I know that he likes posts such as “Coca-Cola”, “Fly the American Flag”, and “Disney”. So he get a “1” on those cells.

![](/assets/images/5eb9b538657acc9f8301ed7d_wlfNwTS-hldVrGDp1j4elOTrqYU8Mjlv8iOlhdK44l9iC7npFqha4ttQfyDAeQTwnA4E4yfp9dJD7g8C2YP5Tz3ueC3KxNSRTdOjjxZm6_OhBkqyMFhoSmjloK2LS-V6qDIZhdA.png)

But we have no idea on Joe’s opinion on the Beatles or Katie Perry. So he got a “0” on all other 36,000 cells.

Previously, those cell has been treated as the value 0, meaning that Joe has seen every single of the 36,000 Likes but liked only 26 of them, that’s not a good way of coding it.

![](/assets/images/5eb9b538e188aba53535c7ad_RTCYoSG0wj7YRwuLC_I5oKjOtk3a-neqgHEi7wtIy7Rn4-IGMllVZcysh0pYNcEMsI_164zYr_Wmy4oOfPc-s-uPouOyySnxgupLHC-8u0U6Diqkx88syY83y1eM9y26_uc0Pvw.png)

Since we do not know whether Joe has seen the posts but not Liked it, or he has not seen it at all, it’s better to err on the side that he hasn’t seen them at all. It’s not likely that he has seen even 7,000 (5%) of those 36,000 specific posts.

Wouldn’t it be nice to know what’s the chance that he like the other 36,000 posts?

And that’s exactly what we did. With our algorithm, we predict that Joe has 39% probability to like Katie Perry, 37% probability to like the Beatle, and only 1% chance to like the Hayao Miyazaki, the anime god. But how did we do that?

![](/assets/images/5eb9b538b78d5feffb12166d_yhoNi-TDePZdiJ1Bub68MHMqtfNIzkm6mDlCAeyD5k5cA_4FcNG-XcXPpxWt82nO_bKopZP-vWtbta3jM715oV84LHm2xYkk4013HqLfftE5icLB-mHBiYLHyGwI7TcRYFt7o3c.png)

Here we encounter the problem of **missing data** and **sparse matrix**. Sparse matrix is a matrix that has a lot of “0”s. In this user-like matrix, 99.6% of the cells are “0”.  But if we treat those “0”s as missing data, how can we guess a value for each and impute them?

It is at this point that we realize our problem is not unlike the[Netflix Challenge](https://en.wikipedia.org/wiki/Netflix_Prize), a classic matrix completion problem. Basically Netflix wanted to improve its movie recommendation algorithm. So it throw out this massive sparse matrix of user-movie data, and offered $1 million to the team that could best predict how users would rate each of their unseen movies.

![](/assets/images/5eb9b538809313d37b164eef_BLIKYrQlLanrtKfMDZBDpONkomddIMGrqg85F40bH1UlEuvjjuPUrezUIzQEh8C1XGQo22x3NzDGKEAJeL0J8IvTsQbWHpfFs_yuksLGWbKMwYCqIvP6M4FS9JltsRBMf_WsVgk.png)

The winning team used a statistical method called Alternate Least Squares (ALS).

Here’s the algorithm (a YouTube [tutorial](https://www.youtube.com/watch?v=FgGjc5oabrA)) :

~ factoring (SVD) Matrix R into matrix U for Users and matrix L for Likes

~ iteratively fill in the U and L until error is minimized

~ Multiply U and L together to get back R_imputed.

~ All the missing cells are now imputed with a number between 0 - 1 (for probability of like)

![](/assets/images/5eb9b538b4d60b070eeeff92_nlMWJK0a1W-dDLoFyv56Pk8M1vn2CRSjTgmeefw6sWJcznGGeSbUTDShtm0wX_ffiQMTJMiu9-cMCpRDVVjH4S_MktFXwRToZQ2l_9ZVumGzgH1dK6KKz5oWaaBeHeGN6jR1UnM.png)

A famous Stanford professor by the name of Trevor Hastie wrote a package called *softImpute*,  which revolutionized the computation and accuracy to realize the ALS matrix completion.

![](/assets/images/5eb9b53827ee12c34c1719d8_xYpsDuGSKWtIzeiREgmo5o1-JRPZ1Io3CWhPjjzt0jqcgFe7jn2HBzRJcqa-tOQAegEmeRJxe5HqILLV9deqKkXkdl7mSWRJT30wF9VOtynhchCGtryTQmau1vxmgnloWSYM0c4.png)

The code is actually really easy.  For the full implementation, see this other blog post I write.

library(softImpute)
M1 = as(M,"Incomplete") # change dgCMatrix type to incomplete
fit = softImpute(M1, rank.max = 10,type = 'als', lambda = 15, trace.it = TRUE, maxit = 10)
Mimp=complete(M1,fit)

So, how does our model perform?

Just by this pre-possessing step along, we are able to have an at least 10% improvement on features Age, IQ, Openness, and Neuroticism.

![](/assets/images/5eb9b539b6f406d5d4bf7bb0_9v0ghU4-IiAjOLXvwqPVSMJInuCGdukMvjBfUaHiegbwNBdkjhot_vEfF4sM03qqgxgP_A106jM4koFhihw9-pK1lAxI5xSqRsILWGsdnC56sT7vQGK2ClgopKnpC7TFIgyB6eY.png)

So, what do you think Joe’s IQ is? Does he have a low IQ, or a high IQ? Based on those likes.

![](/assets/images/5eb9b53916bca8081b65b8ff_yKHVQQmhmx3ovtOWC2DubrNaUq52VaD_6Eet2s0LSTq0jH47fBXokTLCI91g20i5jOjTW6kpwJpsYXxGTzEuCWAmRWwm0L9INq-Hc_JcmpGDv0ux5kXNhTSspnGHn17hdaNwJVY.png)

Well, we predicted that Joe has a low IQ (the blue line), one standard deviation (std) below of the median IQ (the grey line)  of our sample. And actually, Joe has one of the lowest IQ in our data (the green line) . His IQ is only 87, two standard deviations from the median.

![](/assets/images/5eb9b53957871349059421f6_Ff6YH0bgbwOJpOyzuBdLflmFJF5lf1g47P8Woqx-6u4WDwWZT7uNczB8sJeKKuVbw1jwtXIcwhNWdwva-Y9VK4niezROr-Ru23uaa9hXMxgkuAMLJW7mwypqQMqkOX4TYA2CGJI.png)

We can do the same for all his personality traits. If you look at the arrow of the prediction, all are pointing at the same direction as the true value.

![](/assets/images/5eb9b53927ee1220811719d9_3FHyj3CTjKr_rTFJnAhKFA8qcD-TPOEesgQFoxLWgXzBXmTqfd8f-Am44JWhjS3Mg6xMURFYuvraki8DC1wu18bhb9A10B8DgWX6TdJs-TPLDfHAihIUe7o38ybDjLZbAUobfYE.png)

It shows that if all use all our predictions as the binary classifier of the features, we would have predicted "correctly" that Joe is low in Openness, Extraversion, and Conscientiousness. He is high on Neuroticism. We did not correctly predict that he is low on agreeableness.

The accuracy of this classification is not a coincidence. It does not hold only for Joe. for attributes for all users, 63% of the classifications were predicted correctly.

**After becoming omniscient gods, what can we do with it?**

![](/assets/images/5eb9b53adc07c2538f2057e0_-fC4GGd806rkZf4hjR9uAehiBsAXhUARTeWcQO-5BqFE1dXAyCks_cm1XwMxHTw0vVhVHRUBji3dWr7lmkYejdvmYCOnmn3DdXPzUI4tIsprQr14FoGTpdqK_fI4hi-5HB2x2TU.png)

Today, May 3, 2018, as I’m writing this blog, Cambridge Analytica shut down, 2 months after the data leak scandal. We do not tolerate companies like Cambridge Analytica to exploit social media data for voter manipulation. But by correctly predicting your personality and intelligence informations, Organization can also make the world a better place.

![](/assets/images/5eb9b53947ed8f22a52015ef_-KH2IreE0qTIxw_dVPVPczl7KlN-sOjI3fYhY9zdRYSbRmal3nUtMNHL_HDGYWsJTdLCc8YLPSzoflSO2s4tFDSuwTqdFKnxhn4MDwt2CriwlFw_UX6lIEVUrV3ecreZ13ItW08.png)
*Dating apps like Tinder can enhance matching-making by connecting people with compatible personalities*

![](/assets/images/5eb9b539f617ef6e4bacd9e8_Jy8GX0zbUK2FwUCFwbI40A667T66RkOAyn-f9tM2Ls3u8k_rC4RYQzRnSSncbK-LDwKIQ7dKjsHGFSxusnabeUKQTryWLDYLhoLuiepPbScXq4eoUyCHeMjilTnOUVjB8ow_u3U.png)
*Ecommerce giants like Amazon can email you coupon of the goods you actually want to buy.*

![](/assets/images/5eb9b53a00d8fc1fbd763ebb_qtCfoSqO1SiPq58FIbgOWQ8tm3gb2SS33WCdZuxyVWT8tp53lxjNpoiXaprEAH3riBCTuZzfHKw1osiFrX46sMXowQPXda3wZOwKNYArxGV7ex6EF9UpOODzj-qAldwK9HEdCFY.png)
*Non-profits like the Gates Foundation can connect people with charities whose cause they truly care about.*

So, after seeing what the good guys and the bad guys can do using your Facebook data, would you be willing to share it, or hide it?

<iframe width="560" height="315" src="https://www.youtube.com/embed/AkCe0a6vSMY" frameborder="0" allowfullscreen></iframe>
