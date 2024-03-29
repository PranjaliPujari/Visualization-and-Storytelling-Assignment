#!/usr/bin/env python
# coding: utf-8

# ## AirBnB Assignment Part II Stub File

# #### Guidelines
# 
# - Go through the data dictionary thoroughly before starting the assignment. That will give you a good idea of what each column represents before you begin the analysis.
# 
# 
# - Read each instruction carefully, identify the task to be performed, and only then write the required code. The assignment is meant to be straightforward. You do not need to perform additional analyses that are not requested explicitly. However you are encouraged to perform a few additional analyses to get deeper into the insights
# 
# 
# - Some of the tasks might require using functions you may not have used previously. In such cases, you should rely on the library documentation you referred to in the modules. Please understand that completing this assignment is a learning process, and research is part of it.
# 
# 
# - Always run the cells of the Notebook sequentially, restart the kernel, and run all the cells to avoid runtime errors.
# 
# 
# - For each of the tasks, there's a code cell where you are supposed to write the code and a markdown cell below it mentioning to either write the answer or mention your observations/insights from the output of the code.
# 
# 
# - Many of the questions will require you to view them from multiple angles. You have been asked to **observe any trends in the visualizations and provide insights for these trends**. In other words, there will be no fixed answers. You are expected to apply your problem-solving skills to come up with solutions and also document your work appropriately; both of these are part of the assignment grading.

# In[1]:


##Import the libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# Extra
import warnings
warnings.filterwarnings(action="ignore")


# In[2]:


#Load the dataset
dataframe = pd.read_csv("airbnblistings.csv")


# In[3]:


#check the top 5 rows
dataframe.head()


# ### Task 1 
# Basic Descriptive Statistics 
# - 1.1 How many AirBnB listings are there in the city of Amsterdam?

# In[4]:


##Write your code here
dataframe.id.count()
#counting of AirBnB listings in the city of Amsterdam


# **Answer**: There are 6173 AirBnB listings inthe city of Amsterdam.

# - 1.2 What is the average price of all the AirBnB listings in Amsterdam?

# In[5]:


##Write your code here
dataframe.price.mean()
#calculating the average price of all the AirBnB listings in Amsterdam


# **Answer**: The average price of all the AirBnB listings in Amsterdam is 198.01960149036125.
# 

# - 1.3 - What is the average rating received by all the AirBnB listings in Amsterdam? *Hint* - Use the `review_scores_rating` column for answering this question

# In[6]:


##Write your code here
dataframe.review_scores_rating.mean()
#calculating the average reting received by all the AirBnB listings in Amsterdam


# **Answer**: The average rating received by all the AirBnB listings in Amsterdam is 4.800856170517622.
# 

# ### Task 2
# 
# Plot a histogram for the following variables and observe their distribution. Choose the parameters like bin width, number of bins, etc. as per your choice.
# 
# - `price`
# - `number_of_reviews`
# - `review_scores_rating`

# In[7]:


##Write your code here for plotting the distribution of price
sns.histplot(dataframe["price"],bins=[50,100,150,200,250,300])     
#plotting the histogram of price


# **Observation**: Histograms are  graphical reprentation used to show the frequency distribution of the given data. In this dataset, we have data of the Airbnb listings in the city of Amsterdam. We are plotting the histogram of price distribution.
# After the observing this histogram, it is clear that there is high demand for properties which price range is 100 to 150. This distribution is called symmetric, uniform, distribution if, as in the histograms above, the distribution forms an approximate mirror image with respect to the center of the distribution.
# 
# 
# 

# In[8]:


##Write your code here for plotting the distribution of reviews
bin_start = 50
bin_end = 900
bin_width = 5
ax = sns.histplot(dataframe["number_of_reviews"], color="grey",
     bins=range(bin_start, bin_end, bin_width))               
#plotting the histogram of number of reviwes 


# **Observation**: Histograms are  graphical reprentation used to show the frequency distribution of the given data. In this dataset, we have data of the Airbnb listings in the city of Amsterdam. We are plotting the histogram of number of reviews. One way to measure the spread (also called variability or variation) of the distribution is to use the approximate range covered by the data. From looking at the histogram, we can approximate the smallest observation (min), and the largest observation (max), and thus approximate range. This distribution is called skewed right if, as in the histogram above, the right tail (larger values) is much longer than the left tail (small values).In this histrogram we can see the highest range of reviews is 50 to 100.
# 
# 

# In[9]:


##Write your code here for plotting the distribution of ratings
ax = sns.histplot(dataframe["review_scores_rating"], color="green", bins=10)     
#plotting the histogram of review score rating


# **Observation**: Histograms are  graphical reprentation used to show the frequency distribution of the given data. In this dataset, we have data of the Airbnb listings in the city of Amsterdam. We are plotting the histogram of review score rating.This  distribution is called skewed left if, as in the histogram above, the left tail (smaller values) is much longer than the right tail (larger values). In this histogram we can observe a least rating and highest rating and thus approximate the range of review score rating.There is highest range of review score rating is 4.5 to 5. And this seems to be very good for growing the business. 
# 

# ### Task 3
# 
# Plot a visualization to show the number of listings for each `room_type`
# 
# Which `room_type` has the highest number of listings?

# In[10]:


sns.histplot(dataframe["room_type"])        
#plotting histplot to visualize the number of listings for each room type.


# **Observation** - The entire home/apt has most demand. After that there is demand for Private room. There is least demand for shared rooms.

# ### Task 4
# 
# You want to observe the relationship between the reviews(given by `number_of_reviews`) and the ratings received (`review_scores_rating`) by different AirBnB listings.
# 
# For this, plot both a scatterplot and a jointplot. What can you say about the relationship between ratings and reviews?

# In[11]:


##Write your code here for scatterplot
sns.scatterplot(dataframe["number_of_reviews"],dataframe["review_scores_rating"])  
#plotting scatterplot to visualize relation between number of reviews and review score rating.


# In[12]:


##Write your code here for jointplot
ax = sns.jointplot(data=dataframe, x="number_of_reviews", y="review_scores_rating")  
#plotting jointplot to visualize relation between number of reviews and review score rating.


# **Observation** -We are plotting scatterplot and jointplot to observe the relationship between the reviews and the ratings received by different AirBnB listings.A scatter plot shows a positive trend that review_scores_rating tends to increase as number_of_reviews increases. 

# ### Task 5
# 
# AirBnB has been adding quite a few listings in the city of Amseterdam since they started operating in 2008. Plot a lineplot to observe how the average `review_scores_rating` has changed across the different years (use `host_since_Year` column) AirBnB has been operating in the city.

# In[13]:


### Write your code for lineplot here
fig, ax = plt.subplots() # Create the figure and axes object
# Plot the first x and y axes:
dataframe.plot(x = 'host_since_Year', y = 'review_scores_rating', ax = ax) 
# Plot the second x and y axes. By secondary_y = True a second y-axis is requested:
dataframe.plot(x = 'host_since_Year', y = 'review_scores_rating', ax = ax, secondary_y = False) 
#plotting lineplot to observe how the average review scores rating has changed across the different years .


# ### Task 6
# 
# You wish to identify the relationship between the various ratings each of the listing has received from the customers.
# These ratings have been summarized below:

# In[14]:


review_columns = ['review_scores_rating',
 'review_scores_accuracy',
 'review_scores_cleanliness',
 'review_scores_checkin',
 'review_scores_communication',
 'review_scores_location',
 'review_scores_value']


# Plot a heatmap of the correlation matrix of the above ratings variables and document your observations. You can use this link to understand these variables further - https://www.airbnb.co.in/help/article/1257/star-ratings

# In[15]:


sns.heatmap(dataframe[review_columns].corr(),annot=True)   
#plotting heatmap toidentify the relationship betwwen the various ratings each of the listing has received from the customers. 


# **Observation** - Here is our heatmap. As you can see, each color represents correlation.The color with 1 value shows a highly positive correlation.
# Each square shows the correlation between the variables on each axis. Correlation ranges from -1 to +1. The close to 1  correlation is more positively correlated, that is as one increases so does the other and this shows stronger relationship between them.For the rest the larger the number and darker the color the higher the correlation between the two variables. The plot is also symmetrical about the diagonal since the same two variables are being paired together in those squares.

# ### Task 7 

# Analyze the listings' prices across the following neighborhoods using a categorical boxplot
# - 'Westerpark', 'Oud-Noord', 'Noord-West','Zuid'

# In[16]:


nc = ['Westerpark', 'Oud-Noord', 'Noord-West','Zuid']


# In[17]:


### Write your code for subsetting the data for only the above neighborhoods here
subset_data =  dataframe[(dataframe['neighbourhood'] == 'Westerpark')  | (dataframe['neighbourhood'] == 'Noord-West') | (dataframe['neighbourhood'] == 'Oud-Noord') | (dataframe['neighbourhood'] == 'Zuid')]
#creating the subset of data 


# **Observation** - Mostly below listed neighbourhood have prices less than 300 approx. There are more outliers with high price. 

# In[18]:


### Write your code for plotting the categorical boxplot here
sns.boxplot(subset_data['neighbourhood'],subset_data['price'])   
#plotting boxplot of subset to Analyze the listings' prices across the neighborhoods

