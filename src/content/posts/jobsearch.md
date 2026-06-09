---
title: "What's the Best City to Work? And Which Industries?"
category: "Geo Analysis"
tags: "Tableau Visualization"
date: "Jun 2018"
summary: "1.8 Million Indeed.com job data revealed which of the 151 metropolitans is your dream destination."
thumbnail: "/assets/images/5b25b881a3234f3e87a9c006_IMG_5924.JPG"
featured: true
order: 2
---

One Dashboard Shows You Why San Francisco isn’t the #1 hot metropolitan for internet industry in America.

**Challenge: **Visualizing the Indeed.com dataset

**Skills used:** data wrangling, spatial analysis, data visualization, use/join outside data

**Key Software:** R, Tableau

> If I want to work in the internet & software industry, where should I land my job?

This blog post is a description for the winner presentation of Duke DataFest 2018.  Indeed.com has provided us with a rich dataset of economic opportunity in the form of jobs, across America.  (n = 1.6M)

![](/assets/images/5ec2c76242e4ab2439d54e6a_NTsAAzNwbuGj-siZAfmMg7yC77T3g3_EGOvi0nUumcpYfqE6j9OtrvDdxPvT9bdcfIteQeB2Da6vwzqm4DA7iYAVy5nzYBPtSP0toa93-vDugH27gXWiWzYSjYX1UdEqXxvLk4E.png)

Using this dataset we have made a unique model that when visualized provides key insights into American industry and accessibility for any potential job seeker.

In an age where it is very easy to move location, we believe our visualization could be of great value to make future job seekers wonder where in the US they might the best fit for their talents.

![](/assets/images/5ec2c763d2114a399ce029ff_3mDPEt7AIj8sHUfrZ6CVlAM6pOQZfP4fSl-PBW8daoIA7AVYEzJHcrbQvlsNegIlCeQOepktN7ALMT2vjCUKpJHK2IdPsoBZOlgEkjp11_orc3MR7FA1e1H-TWrUSF8lvWxfYZk.png)

Our first and main visualization shows US metropolitan areas and the unique concentration of industries that each has and lacks. The second visualization reveals a strong inverse correlation between the number of local clicks each job gets and its education requirements.

![](/assets/images/5ec2c763b0fa59fdc4156bca_DuRcEBz1ajMMXHf6xDE1n0Te5LmvQ4WzWUT8aoRtYdRXI8u1xLApQNK3iUC8Kvb6feSfkuxDEfkfLDK48JHTamRCxeaL1clh1dD_DR8CGrg4EADaENKgc27G8C8SwikzAm1rhOw.png)

To create this dashboard, here’s our workflow.

~ spatial-join individual cities into metro(politan) area, using Census Bureau shapefiles

~ join metro population data with our dataset

~ calculate industry favorability score for each city

![](/assets/images/5ec2c763b68c351854878fbe_udyQ4CLIxrtN7DScetGNLBp1Gj0vCxRldmeagC9ZLTBxkOmqH6oINNbv08R1gRtYNJ8B603lw4zpkID76Gsjb7luONV_-WtRD8Pj75lCfWES4Gd6JDW1flE7eATtiSEJdSwaAPk.png)

Using our model we found non traditional areas with many opportunities for different industries.

While these locations we have identified currently have a large number of opportunities in their respective industries. It is important to remember that the health of the local economy as a whole and the ability for anybody to access these jobs is not as exciting.

Additional analysis we have performed has found that there is a strong inverse correlation between the number of local job clicks a job is getting and the educational requirement that the job has.

This graph shows that areas that have many jobs with low education requirements are receiving the highest number of local clicks in proportion to total clicks. This means that many of the areas we have recommended, as they are more idiosyncratic, are likely to have higher inequalities between the kinds of jobs available and whether locals or outsiders are applying for and winning them.

The blue areas are those which require the least amount of educational attainment and receive the largest amount of local clicks. Areas in red require the highest degree of educational attainment and receive the smallest amount of local clicks.

From this interactive map, we painted a vibrant story of America workforce. Whether it’s the policy maker in the nation’s capital, the blue collars in the port side along the Mississippi river, or the news anchormen projecting in media speaking out the voice of America, the story they told, the sweat they had, and the joy they earned, painted drops and veins on the canvas of American dream, a story we share throughout generations

![](/assets/images/5ec2c7630d22dc07c7d1a895_-bG5q4y7Y1QXwq-puo9wyjGa0fWZnNT4s9ukg2Ke-yKOr1O1GB_L6DtczXAFKAs1_YLfFF1cM3d306IATq-dKlp_dVZUN9Xmzs9TSbtiHYP_ufPNVXXK5h2AY9OIpf8KgjmBHZs.png)
*American Gothic by Grant Wood, 1930*



<iframe width="560" height="315" src="https://www.youtube.com/embed/FyXB8TXiAlE" frameborder="0" allowfullscreen></iframe>
