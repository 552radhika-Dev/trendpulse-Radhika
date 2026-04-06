import pandas as pd
import numpy as np

#---1. Load and Explore---
file_path = "data/trends_clean.csv"
df = pd.read_csv(file_path)
print(df.head())
print(df.shape)
#Printing the average score and average num_comments across all stories
print(f"avg score: \n {df['score'].mean()}")
print(f"avg num_comments: \n {df['num_comments'].mean()}")

#---2.Basic Analysis with NumPy---
#finding mean, median, and standard deviation of score column
score_arr = df['score'].values
mean_score = np.mean(score_arr)
print(f"mean of score column: \n {mean_score}")
median_score = np.median(score_arr)
print(f"median of score column: \n {median_score}")
sdev_score = np.std(score_arr)
print(f"std deviation of score column: \n {sdev_score}")
#finding highest score and lowest score
max_score = np.max(score_arr)
print(f"highest score: \n {max_score}")
min_score = np.min(score_arr)
print(f"lowest score: \n {min_score}")
#finding which category has the most stories
top_category = df['category'].value_counts().idxmax()
category_count = df['category'].value_counts().max()
print(f"Most stories in {top_category} category:{category_count}")
#printing which story has the most comments
highest_comments = df['num_comments'].idxmax()
story = df.loc[highest_comments]
print(f"Most commented story: '{story['title']}' — {story['num_comments']} comments")

# ---3.Add New Columns---
df['engagement'] = df['num_comments'] / (df['score'] + 1)
df['is_popular'] = df['score'] > df['score'].mean()
print(df)
print(df.info())

#---4.Save the Result---
output_file = "data/trends_analysed.csv"
df.to_csv(output_file, index=False)
print(f"\nSaved to {output_file}")

 
