Author: Charles Lamb
Contact Information: charlamb@gmail.com

Problem Statement:  Script optimizes two linear programs.  Problem 1 and 2 described below.

Problem 1: Determine a minimum cost diet.  The diet includes five different foods described later in this readme.  The diet must comply with the FDA suggested nutritional intake for sodium (<= 5000 mg), energy (>= 2000 kg), protein (>= 50 g), vitamin D (>= 20 mcg), calcium (>= 1300 mg), (>- 18 mg )iron, and (>= 4700 mg) potasium.

Problem 2: Deterimine a minium cost diet.  Diet includes the same five foods as Problem 1.  Diet is subject to the same constraints as Problem 1, with the additional constraints of requiring >=900 mcg of vitamin A and >= 90 mg of Vitamin C.

Foods:  whole milk (m), mixed nuts (b), kidney beans (b), canned tuna (t), and orange juice (o)

Data:  Vectors of nutritional values, serving size, and cost for each food isprovided below. 
In order values represnt: sodium (mg), calories (kcal), protein (g), vitamin D (mcg), 
calcium (mg), iron (mg), potasium (mg), vitamin a (mcg), vitamin c (mg), vitamine e (mg), vitamin k (mcg), zinc (mg), vitamin b6 (mcg), vitamin b12 (mcg),
serving size per container, price per container (USD), and price per serving (USD).
   
Whole_Milk = [125,150,8,2,325,0,376,90,0,0,0,0,0,0,16,2.99,0.19]
Mixed_Nuts = [90,170,6,0,40,1.2,200,0,0,3.4,0,1,0,0,56,15.18,0.27]
Kidney_Beans = [270,130,8,0,80,2.4,480,0,0,0,0,0,0,0,3.5,1.67,0.48]
Canned_Tuna = [360,90,20,2,0,1.44,188,0,0,0,0,0,0.17,2.88,4,4.99,1.25]
Orange_Juice = [0,110,2,5,455,0,450,0,90,0,0,0,0.068,0,7,4.79,0.68]

servings size: kidney beans (130g), whole milk (236 ml), mixed nuts (28 g), orange juice (240 ml), and canned tuna (113g)


Solution to problem 1: optimzed by 7.5 sevings of kidney beans and 10 servings of milk.  total daily cost of this diet is 5.50 USD
Solution to problem 2:  optimized by 5.3 servings of kidney beans, 7.5 sevings of milk, 4.4 servings of mixed nuts, and 1 serving of orange juice.  total daily price of this diet is 5.84 usd