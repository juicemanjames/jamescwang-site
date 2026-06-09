---
title: "Does Licensed Signal Drive Web Conversion?"
category: "Product Analytics"
tags: "Causal Inference"
date: "May 2020"
summary: "Imagine you were having a great time at a football game. At the end of the game you took out your phone to call for an Uber. Unfortunately, so did everyone else around you."
thumbnail: "/assets/images/5ec20ea0f43c5a250695d76b_remote.jpg"
featured: true
order: 5
---

Imagine you were having a great time at a football game. At the end of the game you took out your phone to call for an Uber. Unfortunately, so did everyone else around you. The price had surged 300%. However, you noticed that Uber gave you another option. You can call a different driver for the normal price. The only catch here was that this driver did not have a driver’s license.

So what would you do here? You were a bit tipsy and definitely didn’t want to pay the ridiculous surge price. Plus this licenseless driver had been vetted by Uber, so he must be legit too, right? So how many of you would want to pay the premium and have a licensed driver to take your home? You might know which driver you would choose, but do you know what people looking at the App around you are thinking?

Now you can see how a pro license could impact customers’ decision in the Company T Marketplace, a platform for hiring local services, is tricky. Would our customers hire a licenseless handyman to fix their HVAC for cheaper? Would our customers even notice the license badge, or would they just assume, like when calling an Uber, that all Company T handymen had been verified? In addition, do customers even know which jobs are risky, that they should hire a licensed pro?

It is crucial to know how much customers care about licensed pros in Company T’s home construction category. In other words, how licenses impact customers’ choice. And do the benefits outweigh the costs?

For Company T, the license mapping verifying campaign across 50 states and over 50 risky categories is costly.  If we know for sure that customers care about licensed pros, we could not only scale our license verifying campaign, but also guide the customers towards safer pros through our redesigned service page.

> The Experiment:

To measure the license impact on customer’s CTR (click through rate), we launched an experiment tweaking a pro’s service page. In baseline, the license information was very limited. In treatment, we added a credential section to display license and background check information. The randomization is done at the visitor session level. It means that two visitors could see different designs for the same pro service page, one with credential section and one without. The same pro could appear in both treatment and control, dependent on the visitor assignment.

![](/assets/images/5eb6e4aaf92b5870b911dba4_BmzkUu0nE7B4ylYb87hY1JXpbBOCzRuX3uc7oQ9M0fN9jJFjtqh73XpTeS2GCDQOnzJSREqQCF-wRRX5_trMUTq1u2Vidq3vjFX41hCHZWflwPrnWG0jr5_H_1UUyr1Fxnwuh_HP.png)

In an aggregate level, we saw that the licensed pros in treatment had 2-7% increase in CTR. However, this difference was not statistically significant. Moreover, since we could not randomize pros, the difference in CTR could simply be a difference in pro make--the pros in treatment were better pros.

> Causal Inference: Fixed Effect (Panel Data) Model:

In our dataset, each row is a customer session’s visit to a pro’s service page, which results in either a click to contact or not a click. If we simply fit a binary regression (equation 1) with the treatment variable (licensing), we wouldn’t be able to account for the differences among pro service pages (since one pro service page could be viewed by hundreds of visitors).  The pro service page effect is called the [Fixed Effect](https://towardsdatascience.com/understanding-panel-data-regression-c24cd6c5151e) (FE), the unvarying characteristic for each pro service page cluster, and this type of data is called panel data.  To control for FE, we add one more term, alpha j,  in the regression. Alpha j is a list of one hot encoding dummy variables for each pro service page j. We can consider alpha j as the individual intercept for each pro service page j.

Equation 1: Vanilla Binary Regression

![](/assets/images/5eb6e4aa0e0bc8b57564b399_r_ewN3Fw8y8MI2WwQTnNcqEZy1mnQtQ4wzGKLqC-rRh2SqKHUzIVT9QgSJGDfkHT3l-t1MhMe0YG-oKYbKWcdylFoIje6mYCzlSGOSRbCeM2m2T3XDrdQPM_Sk-CNOErU8ke16y2.png)
*Click_ij: customer i click on pro service page j*



Equation 2: Fixed Effect Binary Regression

![](/assets/images/5eb6e4aa631a1ead391139fe_VJ6r1dxwQRVHXV2y-L4PUR168uAPLrVLzuSgok_lJOfeARGhVnb8TxOi2wLKbjmsNIFeDkFtBOUl6I5qHWJn_Rjyh8jG3v0Y2EKVRB1vcCSIiYp15AZb-TQKRDdQ3bn77Eo8hDLU.png)
*Alpha_j: fixed effect for each pro service page j*



> Result:

![](/assets/images/5eb6e4aa79f8863ecc3f01e7_NVbq1zdozyq5rXtDkrDsjc1iZfKohP-Tq_G858CRp4IsyFvgsMIyPC5Z2_wgtcYk1B0D_9sxaD7Ky469dXtMAuml6m41vOi3Xgk_YPhHGYfBBeyYuru5n4KPHAakf6GRF3YC1blo.png)

![](/assets/images/5eb6e4aa042e7407490acfb8_Gy_tz2HZ-1ZQsQKShOWuMY_7B90qQIWnvP2tUDodaVEgA_47RT04uVOuj0OwU8MF4higuDOY0hhfuNaMZ55qyi72-KMQ16w9T7ZBK3gIhghzJ_rN_1eAtT0L2GQZLAqdRUwupbA6.png)

After running the model on five different threshold cuts of the data, we detect minimal to none effect from license treatment. Rather than drawing a conclusion that license has no impact on a customer’s CTR, the hypothesis above leads us to recommend a stronger experiment to kill off the lack of saliency assumption. This more focused experiment would put the license badge directly at the face of the visitors, too prominently to be ignored.

![](/assets/images/5eb6e4ab62070301f768a1eb_kMXyqz7vXf-PGY06ExNdWS0z1J7TPaHR_byReEd5BCOhhvsgFykiO1SQ4YLreV3rio7TpmaZXwKuh_Cv3D1ovB_wXDCfQPMq0vDEXFlduvNIkGJ3b6zSRLcHARrYAca_0a9vUIem.png)

Variant 1 would display a pro’s license badge, variant 2 would display a pro’s badge for something like ‘respond quickly’ or ‘high demand’. The ATE1 ( average treatment effect) of variant 2 to baseline would be the effect of any platform endorsement effect on pro. The ATE2 of variant 1 to variant 2 would be the license effect. If ATE1 is significant, we know that we could give licensed pros a boost if we choose to, changing the contact make of home construction categories to more safer. If ATE2 is significant, we know that the license badge itself has a positive impact and we should further push for this.

> Conclusion:

To answer a complex problem such as the license impact, we need a well-designed experiment coupled with causal inference modelling. We carry forward the lesson the next time we set up experiment design.

**Appendix**

This DAG illustrates the need for a fixed effect model. Each Yij here is the outcome variable (if visitor j contacts pro i). We are interested in measuring the correlation between Dij (treatment: licensed badge display) and Yij, which gives us the treatment effect. However, Yij are also correlated with ui, the unobserved variables for the pro service page quality (such as picture quality, review sentiment, etc), making Dij endogenous. To eliminate such confoundedness, we control for Xi, the dummy variable for each pro i. Thus, the only variation in Yij would come from Dij, the treatment effect.

![](/assets/images/5eb6e4aa79f8865cf63f01e8_tGsn76zMHkJxB6KGQEp_q8kd8bn8IChORrktFwlIEr3g06XhvDmgJZ8-M3LGaqUITvXfKhckt9_wSrGQRC77xRn8KoXfFTIbD5YmnGrF7noMZv5vXKylG7z4Rt2x-W8uYCR1o9D8.png)
