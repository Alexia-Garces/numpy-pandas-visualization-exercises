#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np


# In[6]:


from pydataset import data


# In[12]:


# 1.  Copy the code from the lesson to create a dataframe full of student grades.

np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})
print(df)


# In[16]:


# 1.a.  Create a column named passing_english that indicates whether each student has a passing grade in english.

df['passing_english'] = df.english >= 70
print(df)


# In[17]:


# 1.b.  Sort the english grades by the passing_english column. How are duplicates handled?

df.sort_values(by='passing_english')  #duplicates are ordered by false or true, grade, then by index


# In[21]:


# 1.c.  Sort the english grades first by passing_english and then by student name.
# All the students that are failing english should be first,
# and within the students that are failing english they should be ordered alphabetically. The same should be true for the students passing english,
# (Hint: you can pass a list to the .sort_values method)

df.sort_values(by=['passing_english', 'name'])


# In[23]:


# 1.d.  Sort the english grades first by passing_english,
# and then by the actual english grade, similar to how we did in the last step

df.sort_values(by=['passing_english', 'english'])


# In[25]:


# 1.e.  Calculate each students overall grade and add it as a column on the dataframe. 
# The overall grade is the average of the math, english, and reading grades.
df['overall_grade'] = ((df.math+df.english+df.reading)/3)
print(df)


# In[ ]:


# 2. Load the mpg dataset.
# Read the documentation for the dataset and use it for the following questions:


# In[7]:


# data('mpg', show_doc=True) # view the documentation for the dataset
mpg = data('mpg') # load the dataset and store it in a variable


# In[5]:


data('mpg', show_doc=True)


# In[20]:


# 2. a. How many rows and columns are there?
# there are 234 rows and 11 columns
mpg.shape


# In[9]:


# 2.b.  What are the data types of each column?

mpg.dtypes  #data types of each column can be seen below


# In[9]:


# 2.c.  Summarize the dataframe with .info and .describe

mpg.info()


# In[8]:


# 2.c.  Summarize with .describe.

mpg.describe()


# In[13]:


# 2.d.  Rename the cty column to city.

mpg.rename(columns={'cty': 'city'})


# In[14]:


# 2.e.  Rename the hwy column to highway.

mpg.rename(columns={'hwy': 'highway'})


# In[23]:


# 2.f.  Do any cars have better city mileage than highway mileage?

better_city = mpg.cty > mpg.hwy #set up variable to determine if city is better than hwy
better_city.head()


# In[26]:


better_city.sum() #run a sum to determing if there are any true values.
# because the sum is zero, there were no cars that had better city mpg than hwy mpg.


# In[29]:


# 2.g.  Create a column named mileage_difference
#       this column should contain the difference between highway and city mileage 
#       for each car.

mpg = mpg.assign(mileage_difference = mpg.hwy - mpg.cty) #create the coloumn
mpg.head() #check to see if column was created correctly


# In[33]:


# 2.h.  Which car (or cars) has the highest mileage difference?

mpg.nlargest(1, 'mileage_difference', keep='all') #use n.largest to show cars with highest mileage_differnce


# In[36]:


# 2.i.  Which compact class car has the lowest highway mileage? The best?

compact_class = mpg['class'] == "compact" #create variable to show cars in compact class
compact_class.head() #check results


# In[38]:


compact_cars = mpg[compact_class]  #create subset using variable created above
compact_cars.head() # review and validate results


# In[40]:


compact_cars.nsmallest(1, 'hwy', keep='all') #use nsmallest to return the worst


# In[42]:


# find best highway mileage.  Use nlargest.
compact_cars.nlargest(1, 'hwy', keep='all')  


# In[29]:


# 2.j.  Create a column named average_mileage 
#       that is the mean of the city and highway mileage.

mpg['average_mileage'] = ((mpg.cty+mpg.hwy)/2)
mpg


# In[30]:


# 2.k.  Which dodge car has the best average mileage? The worst?

dodge_series = mpg.manufacturer == 'dodge' #variable for series with only dodge cars
dodge_series.head #check output


# In[31]:


dodge_cars = mpg[dodge_series] #subset created
dodge_cars.shape


# In[33]:


dodge_cars.nlargest(1, 'average_mileage', keep='all') #best average mileage


# In[34]:


dodge_cars.nsmallest(1, 'average_mileage', keep='all') #worst average mileage dodges - 4 way tie


# In[44]:


# 3. Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:

mammals = data('Mammals') #import data set
mammals.head(5) #explore


# In[45]:


# 3. explore documentation
data('Mammals', show_doc =True)


# In[46]:


# How many rows and columns are there?
mammals.shape  #107 rows and 4 columns


# In[47]:


# What are the data types?
mammals.dtypes  #data types are floats and bools


# In[76]:


# Summarize the dataframe with .info and .describe

mammals.info


# In[85]:


mammals.describe


# In[66]:


# What is the weight of the fastest animal?

mammals.speed.max() #find value of max speed


# In[74]:


mammals.nlargest(1, 'speed', keep='all')   #weight of fastest animal is 55


# In[84]:


# What is the percentage of specials?
mammals_special = mammals.specials.sum()
mammals_special  #find number of special mammals


# In[86]:


#find total number of animals
total_mammals = len(mammals)
total_mammals


# In[90]:


percent_special = round(mammals_special / total_mammals * 100, 2)
percent_special # 9.35% of mammals are special


# In[92]:


print(f'{percent_special}% of mammals in this dataframe are specials.')  #add percent sign using f string


# In[105]:


# How many animals are hoppers that are above the median speed?  What percentage is this?

mammals.hoppers = mammals.hoppers


# In[110]:


median_speed = mammals.speed.median() #find median speed
median_speed


# In[ ]:





# In[114]:


hoppers_above_median = (mammals.speed > median_speed) & (mammals.hoppers == True)
hoppers_above_median.head() #check results of series


# In[115]:


hoppers_am = hoppers_above_median.sum() # get total number of hoppers above median with sum
hoppers_am


# In[116]:


percent_hopppers_am = round(hoppers_am / total_mammals * 100, 2)   #use total mammasl from above exercise to divide
percent_hopppers_am # 6.54% of mammals are special


# In[119]:


print(f'{percent_hopppers_am}% of mammals in this dataframe are hoppers with a speed above the median.')  #add percent sign using f string


# In[ ]:




