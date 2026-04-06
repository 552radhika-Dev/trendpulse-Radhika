import pandas as pd

# ---1. Load the JSON file---
file_path = "data/trends_20260406.json"
df = pd.read_json(file_path)
print(f"Loaded {len(df)}")

# ---2. Cleaning the Data---
# Removing duplicates from post_id column
Duplicates_removal = df.drop_duplicates(subset = ['post_id'])
print(f"After removing duplicates: {len(df)}")
# #removing null rows from post_id, title and score column
nulls_removal = df.dropna(subset = ['post_id','title','score'])
print(f"After removing nulls: {len(df)}")
#making sure score and num_comments are integers
df['score']= df['score'].astype(int)
df['num_comments']= df['num_comments'].astype(int)
print(df.dtypes)
#removing stories where score is less than 5
df=df[df['score']>=5]
print(f"After removing low scores: {len(df)}")
#strip extra spaces from the title column
df['title'] = df['title'].str.strip()

# ---3. saving the cleaned file---
#Saving the cleaned DataFrame to data/trends_clean.csv
output_file = "data/trends_clean.csv"
df.to_csv(output_file, index=False)
#Printing a confirmation message with the number of rows saved
print(f"Saved {len(df)} rows to {output_file}")
#printing a quick summary: how many stories per category
print("\nStories per category:")
print(df['category'].value_counts())
 
