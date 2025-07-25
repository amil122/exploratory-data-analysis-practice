

# Import all modules needed.
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 
# import plotly.express as px

custom_params = {"axes.spines.right": False, "axes.spines.top": False}
sns.set_theme(style="ticks", rc=custom_params)

sns.set_style('whitegrid')

print("All Modules Initialized ")


# In[2]:


# Get the data.
heart_data = pd.read_csv("heart_failure_clinical_records_dataset.csv")


# In[3]:


# Print first 5 rows of data
heart_data.head(5)


# In[4]:


# Print last 5 rows of data
heart_data.tail(5)


# ## Some basic data cleaning and exploring via `Pandas & Numpy`.
# 
# Some info to keep in mind.
# 
# 1. **Anaemia:** 0 -> No || 1 -> Yes
# 2. **diabetes:** 0 -> No || 1 -> Yes
# 3. **high_blood_pressure:** 0 -> No || 1 -> Yes
# 4. **sex:** 0 -> Female || 1 -> Male
# 5. **smoking:** 0 -> No || 1 -> Yes
# 6. **DEATH_EVENT:** 0 -> No || 1 -> Yes
# 

# In[5]:


df_eda = pd.DataFrame()

df_eda["age"] = heart_data["age"]
df_eda["anaemia"] = np.where(heart_data["anaemia"] < 1, "No", "Yes")
df_eda["creatinine_phosphokinase"] = heart_data["creatinine_phosphokinase"]
df_eda["diabetes"] = np.where(heart_data["diabetes"] < 1, "No", "Yes")
df_eda["ejection_fraction"] = heart_data["ejection_fraction"]
df_eda["high_blood_pressure"] = np.where(heart_data["high_blood_pressure"] < 1, "No", "Yes")
df_eda["platelets"] = heart_data["platelets"]
df_eda["serum_creatinine"] = heart_data["serum_creatinine"]
df_eda["serum_sodium"] = heart_data["serum_sodium"]
df_eda["sex"] = np.where(heart_data["sex"] < 1, "Female", "Male")
df_eda["smoking"] = np.where(heart_data["smoking"] < 1, "No", "Yes")
df_eda["death_event"] = np.where(heart_data["DEATH_EVENT"] < 1, "No", "Yes")

df_eda.head()


# In[6]:


# Get some info on the dataset.
df_eda.info()


# In[7]:


# Remove un-needed data - time column
heart_data.drop(['time'], axis = 1, inplace = True) 
print("Successfully removed **time** column from dataset 🚀")


# In[8]:


# Get some description of the data.
heart_data.describe()

# Data Analysed.
# 1. Age -> Total values are 299. The mean(AVERGAE) age is 60-61. The minimum age is 40 and the maximum age is 95. Total ages = 55
# 2. Sex -> We see that, most of the candiates of the data are males, up to 60% and 40% females.
# 3. Smoking -> We see that around 30% of the candiates do smoke, the rest fortunately don't - I WILL VISUALISE TO SEE THIS DATA ENTRY BETTERLY
# 4. Death? -> 30% ended up dying, the rest fortuntely survived. So this could be a possiblity that the 30% who smoked died - but to make sure of this I will make a graph in the upcomming part of the notebook!


# In[9]:


# Shape of the Dataset
df_eda.shape # 299 Columns and 12 Rows


# ## A bit more of the inner exploration of data, fiddiling with the different columns and finding relationships between them via `Pandas`

# In[10]:


df_eda["sex"].value_counts()


# In[11]:


df_eda["high_blood_pressure"].value_counts()


# In[12]:


df_eda["diabetes"].value_counts()


# In[13]:


df_eda["smoking"].value_counts()


# In[14]:


df_eda["death_event"].value_counts()


# ## Visualise the Data, via `Matplotlib`
# Let's goo 🚀

# In[15]:


df_eda.head()


# In[25]:


# 0 (a). Showing the relationship of the whole dataset (with relation to death event)
sns.set()

# Plot
sns.pairplot(df_eda, hue='death_event', palette='cool')

# Show
plt.show()


# In[27]:


# 0 (b). Showing the relationship of the whole dataset (with relation to sex)
sns.set()

# Plot
sns.pairplot(df_eda, hue='sex', palette='rocket')

# Show
plt.show()


# In[16]:


# 1.Showing the relationship between categoric variable "sex" and its frequency
plt.figure(figsize=(5,5))
figure_1 = df_eda["sex"].value_counts(ascending = True).plot.barh(color=["salmon", "lightblue"])
plt.title("Male/Female Frequencies")
plt.ylabel("Sex")
plt.xlabel("Candidates")
plt.show()


# In[17]:


# 2.Showing the relationship between categoric variable "death_event" and its frequency
figure_2 = df_eda["death_event"].value_counts(ascending = True).plot.barh(color=["salmon", "lightblue"])
plt.title("Death Event Frequencies")
plt.ylabel("Death EVENT")
plt.xlabel("Number of Deaths")
plt.show()


# In[18]:


# 3. Death event per each sex
figure_3 = plt.bar(df_eda["sex"].value_counts().index, df_eda["death_event"].value_counts(), color=["salmon", "lightblue"])
plt.title("Death Number per sex")
plt.xlabel("Sex")
plt.ylabel("Deaths")
plt.show()


# In[19]:


# 4. Sex correlated with Death rate
plt.title("Sex correlated with Death rate")
sns.heatmap((heart_data["sex"].value_counts(), heart_data["DEATH_EVENT"].value_counts()), cmap='Dark2_r',linewidth=.5,square=True, center=0)
plt.xlabel("Sex") # MALE - 1 || FEMALE - 0
plt.ylabel("Death") # YES - 1 || NO - 0
plt.show()


# In[20]:


# 5. Relationship between age and platelets + sex
sns.lmplot(x = "age",
           y = "platelets",
           hue = "sex",
           data = df_eda).set(title='Relationship between age and platelets + sex')
plt.show()


# In[21]:


# 6. Smoking against Death
figure_4 = plt.barh(df_eda["smoking"].value_counts().index,df_eda["death_event"].value_counts(), color=["salmon", "lightblue"])
plt.title("Does smoking lead to death?")
plt.xlabel("Deaths")
plt.ylabel("Do they Smoke?")
plt.show()


# In[22]:


# 7. High blood pressure with age
sns.catplot(
    x = "high_blood_pressure",
    y = "age",
    hue = "sex",
    data = df_eda
).set(xlabel="High Blood Pressure", ylabel="Age of Candidate", title="Relationship of HBP with age per sex")
plt.show()


# In[23]:


# 8. Value Count for the deaths
sns.catplot(x='death_event', 
            data=df_eda, 
            kind="count")
plt.show()


# In[ ]:




