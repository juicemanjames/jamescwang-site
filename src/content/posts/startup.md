---
title: "Is Your House On Sale? Door to Door Marketing"
category: "Entrepreneurship"
tags: "Geo Analysis"
date: "May 2018"
summary: "How my first startup died"
thumbnail: "/assets/images/5b25b8574636a77221cc6c95_IMG_5922.JPG"
---

In September 2017, I joined a local start up in Durham called GK (alias), valued 8 million, as its business analyst, to gain experience of making real world data-driven decisions.  When I came in, GK was struggling. It had not closed a deal in 3 months and was 6 months away from burning the last round of funding.

Working closely with COO, I offered all I could outside my school and club commitment to design, launch, and calibrate the door2door canvassing endeavor. We knocked on 11,376 doors, talked to 3,087 homeowners, and convinced 915 of them to list their houses in the GK platform in 4 months. Despite the promising leads, our sales team hit the bottleneck of converting leads into deal. The startup shut down in late February 2018.

![](/assets/images/5eb9a7d5277cf007570282c0_v2Rpq3VODQptvkcdi_et_T27NxgDaFI0fnV7aFoBS2ryECIUk0QKogM0504mYktNs0LFz03kON2oPBBaV9r6u3x6AXH-z31EmiRII10yEYIygqL6ZYEw11SLuDa40dDFTkXQ-kk.png)

Following the demise of GK, I shall reveal the data analysis we used to answer business questions to guide other endeavors: which neighborhood to canvass? when are the best times to knock on the doors for pitching? how to best motivate and incentivize canvassers?

> What is GK?

GK was an online marketplace to buy&sell houses instantly with ease, the Uber for trading real estates. It connected potential home-sellers, real estate agents, and investors off the Multiple Listing Service (MLS), quick, clean, and hassle free.****



**Background**

****Lead Generation was a huge success for GK. Prototyped in October and launched in November, the door2door canvassing attracted 915 potential sellers into the GK sales funnel within 3 month. In October, the CEO and COO knocked on 1000 doors to prototype the interaction script, and recruited a 10 people canvassing team that covered RDU and Charlotte area. In these months, I built Tableau Dashboard that automated integrate data and tracked canvasser performance, identified the best time and neighborhoods for canvassing, and restructured the canvasser incentive bonus system for them to worker harder.

> What is Door2door Canvassing?

It means going to the neighborhood and knock on people’s doors to make pitches. In the GK case, GK canvassers went to the single-family houses that fit the institutional buyers’ buy box criteria and tried to convince homeowners to sell their houses on the GK platform, if they were interested in selling at all. Usually, a single canvasser can knock on 20 + houses in an hour. ****

> Which neighborhood to canvass?

With the help of a real estate database company, we obtained 15,309 potential houses in the NC Triangle (Raleigh Durham Area). Each house was predicted a propensity score (0-100) about how likely the homeowner would like to sell, using machine learning.

After obtaining this dataset, I did the following analysis.

~Group the 15,309 houses into 300 neighborhoods, based on their location, using hierarchical clustering
~Calculate a neighborhood score to select only the best neighborhoods to canvass. 


Clustering:

![](/assets/images/5eb9a7d661b33b4004f491ec_TyjcmNni4mN2sw6hMCjalZQyzzmaUntcgVm2ThzHt369b269cAhPZ3BT0fbzQLpw60Sb84DFsWoI9hz-Y9LpYyVkJI4q2IXSmHjDKvOLamD1HIF-pbRcerMtDPf92SGgvYT4Pd0.png)
*300 neighborhoods clustered base on latitude and longitude*

> How to compare the neighborhoods?

From a canvasser’s perspective, there are 3 things that make a neighborhood a desired place to canvass: high potential that homeowners would like to sell, abundance of houses, and the adjacency of houses to each other. I calculated a weighted sum between those 3 metrics, and ranked the neighborhood by their scores.

![](/assets/images/5eb9a7d636e36c7e2823851b_VUT7Rryj0mZYHKBuABiHSpgfWSSdFKX5BZzq7dBqnEoaoTQgy3XifZXsU66eO-AfJviGCLjOuaj_ouvLkBrEfBhEpMXFFjt1ij6cqWIp1Nfe-adHVmELMVSYIzFkccwoa90CGxk.png)
*A green neighborhood represents 3 things: high potential that homeowners would like to sell, abundance of houses, and the adjacency of houses to each other*

> When are the Best Times to Knock?

Door2door canvasing is a delicate art. In theory, having a high contact rate / lead generating rate have a lot to do with when to knock. The CEO would like to know what day of the week/ time of the day to not send canvassers out knocking people’s doors.

We hypothesized that homeowners are more likely to be home and answer the door in the afternoon/evening after work, but not after 7pm when it was dark outside. Generally, weekends should be better than weekdays.

To test these hypothesis, we spent the November having canvassers out in the fields for all times for the purpose of data collection. I generated heatmaps to analyze the results.

![](/assets/images/5eb9a7d69296948b5ecf9952_FgBlbXqpvEhvBbdCR0yyzPvkiEv1hBTgjr1meJbR9fneHvmNWaAoGc8PpfVHqNdVE7pixe2YLgAfTg6Gbo5kfVH-JQpvc3IZbUEGQjcXCQgj2hyXnW1ldgJ0AA7nCKW1rn9OyzI.png)
*The conversion score is calculated by a weighted average of lead and contact generation (represented by the color). The label for each cell is the total number of leads for that hour.*

From the heatmap, we see afternoon after 15:00 consistently performed best (greener and more leads). As a result, we had our canvassers concentrate on knocking doors in the afternoons and evenings. ****

> How to best motivate and incentivize canvassers?

![](/assets/images/5eb9a7d6e7e915c02730ec5a_54VCjvzXiGS0H4Q9oornW9h20rL6OVBJHOUA5iaLBpMamW9o5U0RijBM8ZaHzD7Bxm9GT8TLTkxMIiD-YyU5-Z3BuAlL9RznyfKUH_cDQBLgNvw6QEn67jbx5hGG-HfxbiOfYE8.png)

We had over 30 canvassers over the course of 4 months with 50%-100% turnover rate each month. Although the canvassers varied drastically in their time commitment and performances, we used to pay them $12 an hour without bonus.

With data collected about their performance, we decided to adjust their payment structure to incentivize their higher performance. With limited cash in hand, we hope the new structure can reward high performers, push average performers, and scare away laggers to find another job. In sum, we want higher performance, without spending more money.

Using data of 4 weeks, I run simulations in 10 different scenario, decided on the best payment structure under our limited budget. I then produced bar charts of before and after the change, showing that even the average performance canvasser would earn more under the new structure.

![](/assets/images/5eb9a7d6495c104fa95e0468_Ik-I_EgQU5R326M2cyfpGYQvARfVDdA2X2Jd4u2uKLuz-LMtRdUuKLKGoTbxv7X30iz3ofF9TddNhtioep9opbBktJRcihKzdsUVqEBBiMLYMONKV3o1YzMFAjyHB2Fsnyce-rw.png)
*In this chart, Monta, Bryan, and Chris represent high, average, and low performers in our team. The bars represent the total salary they would each earn each week under 3 different scenarios. The blue (top) bar is our old structure ($0 bonus per lead + $12/hr base salary). The red and teal bars represent two simulated scenarios ($7.25 per lead + $8/hr ) and ($12 per lead + $5/hr).*

We show this chart to the canvassers in the next meeting and declared the new policy of option3: the teal. Our message to them was simple: if you work harder and smarter than Bryan (who is an average performer), you would be better off. Don’t believe it? Just look at Monta.

> Results

After the changes made in canvassing neighborhoods, time, and payment structure,  we see a spike of conversion rate from 21% to 47% in less than 2 months. In addition, we cut 10% of canvassing budgets by paying only those who deliverered.

![](/assets/images/5eb9a7d658abba3ce820ca48_LUrCGloo8rFOQVuMCqJ6UTFMM9NY1PDDowdrpcgLgwG26IcgdoUEXOlvFljmaBDaXcgYdEYeB_UeorHG28EywwhnTS8PuCzikjsjRjJKzSmSuvpUvBv8TQapmC0YkXGA4pHCSEU.png)
*Lead Generation spiked up 200% after the change of bonus in January. However, failing to convert leads to sales, the CEO suspended most of the canvassing efforts in the last weeks of GK.*



> The Postmortem of A Start-Up -- My reflections

**What Happened:**

I joined GK in September, and watch its gradually demise in 6 months. 5 of the 9 full time staffs left the company, many of them had been with GK for more than a year. In these 6 months, although GK reached out and attracted tens of thousands potential house sellers through its canvassing operation, it failed to sell a single house and generate any substantial revenue. Having raised $1.8 M in February 2017 (4.5M total) and once valued at 8M , GK missed the critical 2017 to prove to investors the viability of its business model. In February 2018, when its old investor Lowe’s (whose lead investment many other smaller investors was contingent upon) declined on any further investment, even with a down evaluation, the CEO of GK decided to shut down the company.

![](/assets/images/5eb9a7dbfc5bfc42a9f3f407_8l-ytDtyr8oOWMDGbuyvteyDWcFVebqjdEit4nXU87oZpkqQYvvwQWJXm2jymi5oJ1e9_hlCtos6M3Rer9it8fc-N8AikoJWVL3nTsUZfh-TU0ZGIIgK3dvHcMDiVSJJ1u-NyUA.png)

**Business Model**

GK failed to generate revenue, let along securing health cash flow.

Revenue generation is the heart of startup business. It is the most important metric to measure growth and attract next rounds of investment.

Selling a house is different than selling a car. It involves a lot of debate and back and forth between the owners and the buyer/agent, and within the owners’ family. To tap into this house selling market as a late comer of Redfin and Zillow, GK simply couldn’t win buyers’ trust fast enough to achieve conversion
****

**Market Condition**

Owners were not ready to sell. The RDU housing market has grown 200% in the last 5 years. Selling a house at this time while the price keeps rising is not ideal to most rational buyers. GK was waiting on a correction in the housing market, but it hasn’t come. Therefore, although GK generated numerous hot leads, it couldn’t convert the leads into actual sells.****

**Strategy Failure**

****Not concentrating all resources on the bottle neck —customer conversion— wasted valuable time and resources in the last 6 months.

GK spent a lot of resources on automation in CRM and sales management.  Those scalable effort were important for a growing business, but not instrumental for a startup getting from 0 to 1. For example, GK paid its computer engineer 10k/month salary in SF, and he spent at least 3 months developing an app for integrated canvassing CRM, before leaving the company because its cash flow problems. The app was never finished.

Looking back, GK should have spent all the resources in the 6 months before January to “do things that don’t scale” to break the conversion bottleneck. Had GK converted 5 customers, it would have been a much better position to raise the next round of funding. ****

**The Fatal Flaw of Fundraising**

Facing the pressure of fundraising, the CEO might not have given enough attention to the business operation.

One of the biggest challenge of running a startup is the fact that founders are often torn apart between fundraising and running the business, both of which are crucial to the venture’s survival. However, product and marketing always come first before fundraising. Without the MVP that could generate revenue, the CEO found himself in vain pitching to investors. ****



**CRM: In case you are interested: **

![](/assets/images/5eb9a7d7402e88572dba9d13_pbGBUphoz8TuRK0s5NufNB_FwHDuuKaOPq5cJJUt46wmQSe0mC6wtawIPBrMx5hLG_ttEMGBFQbRNvaOH5UwOXGyiNBr7Q4NOlzc5RtkhgBfjk6hxbFCNo0bykeDp5Mht2Rqq5c.png)
*Maps for customer acquisition funnel.*

![](/assets/images/5eb9a7d7b7ef1adadb308691_5A1xM63FYR9mVmOSiluTEQ30_-qchwGK3FInTh21RXNftGj74zJJ_4etejcecfo8PGFFPiBcPdpmRPjABNCo4Ia16juowVj_iBwESzZgzis1cLmOTZ9DOX_gSq1MXudzmzxvLKE.png)
*Decision Tree for Internal Sales Team*

![](/assets/images/5eb9a7d723f6e7039b542ce9_JiPrioihbO917cOfjqe-anghvkwsWqtk-rPrX8KJ4JJxRPmRpWJJEZ25jzr3_SC2lyOQ2-hEjHE-M98KskVh_9RMioFGftPKqJZGmD4l4pSGjFAVvvinqDpIZ1wUQDm7_zWx7SA.png)
*Decision Tree for Agents*
