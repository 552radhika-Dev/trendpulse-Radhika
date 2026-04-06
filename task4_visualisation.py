import pandas as pd
import matplotlib.pyplot as plt
import os

# --- 1 — SETUP ---
# Load the analyzed data from Task 3
df = pd.read_csv("data/trends_analysed.csv")
print(df)
# Create the outputs folder if it doesn't exist
if not os.path.exists('outputs'):
    os.makedirs('outputs')

#---2.Chart 1: Top 10 Stories by Score---
plt.figure(figsize=(8, 6))
# Get the top 10 stories by score
top_10 = df.nlargest(10, 'score').copy()
short_titles = []
for title in top_10['title']:
    if len(title) > 50:
        short_titles.append(title[:47] + "...")
    else:
        short_titles.append(title)
top_10['display_title'] = short_titles
plt.barh(top_10['display_title'], top_10['score'], color='skyblue')
plt.xlabel('Score')
plt.title('Top 10 Stories by Score')
plt.tight_layout()
plt.savefig('outputs/chart1_top_stories.png')
plt.show()        

#---3.Chart 2: Stories per Category---
plt.figure(figsize=(8, 6))
category_counts = df['category'].value_counts()
# color list
colors = ['red', 'blue', 'green', 'orange', 'purple']
plt.bar(category_counts.index, category_counts.values, color=colors)
plt.title('Number of Stories per Category')
plt.xlabel('Category')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('outputs/chart2_categories.png')
plt.show()

#---4.Chart 3: Score vs Comments---
plt.figure(figsize=(8, 6))
# Simple filtering for Popular vs Regular
popular = df[df['is_popular'] == True]
regular = df[df['is_popular'] == False]
plt.scatter(popular['score'], popular['num_comments'], color='gold', label='Popular')
plt.scatter(regular['score'], regular['num_comments'], color='grey', label='Regular', alpha=0.5)
plt.title('Score vs Number of Comments')
plt.xlabel('Score')
plt.ylabel('Number of Comments')
plt.legend()
plt.tight_layout()
plt.savefig('outputs/chart3_scatter.png')
plt.show()

#---Bonus — Dashboard---
plt.figure(figsize=(8, 6))
plt.suptitle('TrendPulse Dashboard', fontsize=14)
# Plot 1: Top 10
plt.subplot(2, 2,1)
plt.barh(top_10['display_title'], top_10['score'], color='skyblue')
plt.title('Top 10 Stories')
# Plot 2: Categories
plt.subplot(2, 2,2)
plt.bar(category_counts.index, category_counts.values, color='green')
plt.title('Stories per Category')
# Plot 3: Scatter
plt.subplot(2, 2,3)
plt.scatter(df['score'], df['num_comments'], c='blue', alpha=0.5)
plt.title('Score vs Comments')
plt.xlabel('Score')
plt.ylabel('Comments')

plt.tight_layout()
plt.savefig('outputs/dashboard.png')
plt.show() 
 
 
