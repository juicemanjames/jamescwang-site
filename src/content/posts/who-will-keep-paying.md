---
title: "Neither A Borrower Nor A Lender Be -- Lending Club Loan Risk"
category: "Product Analytics"
tags: "Bayesian Inference"
date: "May 2020"
summary: "How to use Bayesian Inference to predict loan default risk?"
thumbnail: "/assets/images/5eb7020079f886d251404c7c_a9e2daf7dcb16fb2f763b67badafad94_lending-money-clipart_900-900.jpg"
---

> Neither a borrower nor a lender be. -- Shakespeare

Lending Club is a peer to peer micro-lending platform, where you can borrow or lend money. Lending Club enables borrowers to create unsecured personal loans between $1,000 and $40,000. The standard loan period is three years. Investors can search and browse the loan listings on Lending Club website and select loans that they want to invest in based on the information supplied about the borrower, amount of loan, loan grade, and loan purpose. Investors make money from interest. Lending Club makes money by charging borrowers an origination fee and investors a service fee. However, not all loans on Lending Club were eventually paid. When a debtor fails to pay consistently, the loan is categorized as *delinquent*.

Using Lending Club’s 2018 public data set, I will try to answer the question--who will keep paying--by understanding the nature of the loan and the debtor. Since plenty of posts had been written about predicting loan risk using machine learning, I try, instead, to approach this question with a more intuitive method: Bayesian Inference.

![](/assets/images/5eb6eeeeccd7e785f752ed62_5O6iOn0c70SePOijGdSPzQB-H04wg8gGqK3H5gmxKIw1Kj-x4wCixD6lys-otSdOdMmwd6VWd6rGY1MVSfctrHjqLoR8pdfFlnXrZnEhSxamCFDyBGVBqSIM-h_VX-OY1TafPwoa.jpeg)

First, let’s explore some factors that complicate our understanding of loan risk.

![](/assets/images/5eb6eeeef3dd36177db9f4fc_BSF13udOAX7OT_O_dmNQEBLDSr2dB-A-04EW4R6fESz1Jpv_ZuV64C1GrhVOj4AL7CloB-UGHwmlfsbgRQ8-hS6g9dLfnYQgr8saaZDMehFBi1TEOivWWr5SQ7NyFhS892tmuWlR.jpeg)

![](/assets/images/5eb6eeee620703754c68dcc7_w510EC_P3ItldaPEpRI2LkWVzh-Bn1E7tX8bRYzN4eeLaog76POgo1bD8IbO8QDjSKE0fpeN3fM4MTwjT6LlgaT9Cv7zl2XbqEDcX3-KlPFPT2N_dIzkWt01wAjkmRQUftpHvCDj.jpeg)

![](/assets/images/5eb6eeee79f886d3543f58ec_rx9a4KPE2WCl6AxSCrmTt6VqYCfXIrhg8I63AsFtu5VcQKuIroaO264Et5hMSHozPnOvbCmalkAgt3U8G05YZ4GRycHsqLFVXMycILjzMmD_dWlVfXiz9Jv2HY006Q5bds504ezM.jpeg)

![](/assets/images/5eb6eeef8205002507e17938_IMOZSOtkVZ1z_hNSk3TT6lAVuuvb90i_mvkp65n9s0b95E9XH0vN0IBNGJszf-4iuVvP7Vr6hd1smuAdwTu5BrT9AT0ijtOoRDRulWtgedNG1hwqnGI5NBFP3b3MnXN9ckwJbclr.jpeg)

![](/assets/images/5eb6eeee79f88605f73f58ed_A7u-CEkIJmLxLa5dqUTMglTnNb2j32BH1heNqscjglI7vPwLgf6_pMLBo2Ral_CiILYARhs71U9MD1CgeZBHg263E4ZylWGmySOabaVI2N7FYTOztCI-hUhGoGZ6nlGgOJZviFqM.jpeg)

All of the previous slides lead me to what I need to know, before predicting loan risk. Now, I propose a method to predict the loan risk based on our understanding.

![](/assets/images/5eb6eeee042e74373e0b3526_OSeB1tsgAriJBMFoqO53tIc793AdF4V56ItnkPdvqWnM9sa5XXc35mXWdZjx44x4rhLgA15Hc4Za7msxke1n6E6PF0VRI0-Z9ZijGxcSKe9NHNX8wUvNFJgUlex1xebKuo1MAThM.jpeg)

![](/assets/images/5eb6eeeea11928d70d00e43a_Kyy5girq65o-qPZYeqAF-mYQGixA_DJSsxpcz-XpZJ4qD7lluuc6va_kXJDZIuOmPZ4sD5mXj8x1nMebbW6tctQt9Z2oJjQH6vIELfRm6glQmvgrriMi0-Ez0VaoR0earj-ekFrd.jpeg)

![](/assets/images/5eb6eeee820500371ae17937_-neRqtijnTrj4F8-NKx19-TZxmqyTLOZCrK7_RlbUj9avdBGkeG53VFOdoPgk7tMpgPaU_FD0IR_wUkMkso8vCQXWYdR-VXscppa5_dt-t0WIaLT_m_-dUDR1vN8YGBTVBFewAht.jpeg)

![](/assets/images/5eb6eeef8b63032b6d3c52f9_pboSXqRQvGpVBQm5m9-fS0pkT7-0fGut5YVfXBftqWrBajRY9iFJC2sx0tLO1ps-QrfjDNQHghbdFv4iJaPU5pXW4iYEJSHMPZodCWLNd7NehXcoItBMV26uegwtJm44YnYe2DyU.jpeg)

All together, Bayesian Inference allows us to predict loan risk with confidence. But with more data, and a machine learning model, Lending Club could do so much more...

![](/assets/images/5eb6eeef8b6303774e3c52fa_OkVdtV2hDCHcvmKYo49p1pRUNad3perFGPFIGmFaDQRn7rr9toKNoRP0xPTpByXj2i_-6idScrxM_YKvkMaz8gsmimfV7v7zUedI5dIDo1RamtWZxX4C4rG9Jlle0Cy8NAYJVpSF.jpeg)

![](/assets/images/5eb6eeef631a1ea4fb11922a_HUtmznLUj8Y5jVsMh8ZUwLQwilDqAkX0zSBC8NDmeLC5VhHUgjZo6YJNg-9IlybhFdQ5bnrVfGX-foLDSn_VVlsUFsit77D8C2pFMZThF1BJDPF0WiyKtqhPn3d6pNsrgJlWKbji.jpeg)
