import requests
import time
from datetime import datetime
import json
import os

# adding header
HEADERS = {"User-Agent": "TrendPulse/1.0"}

# assigning the keywords to each category
Keywords_to_match = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

# assigning count of categories to 0 and return the result to final_stories in a list
counts = {"technology": 0, "worldnews": 0, "sports": 0, "science": 0, "entertainment": 0}
final_stories = []

#requesting url
print("Connecting to HackerNews...")
top_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
ids = requests.get(top_url, headers=HEADERS).json()[:500]
print(f"Found {len(ids)} potential stories to check.")

# We go through the IDs one by one
for id in ids:
    if len(final_stories) >= 125:
        break

    # Get the details for a specific story
    item_url = f"https://hacker-news.firebaseio.com/v0/item/{id}.json"
    try:
        story = requests.get(item_url, headers=HEADERS).json()
        
        # Sometimes stories are deleted, so we check if 'title' exists
        if story and 'title' in story:
            title_lower = story['title'].lower() # Make title lowercase to match keywords easily
            
            # Now we check each category one by one
            for category, words in Keywords_to_match.items():
                
                # now we check if we still need more stories for this category (Limit 25)
                if counts[category] < 25:
                    
                    # Check if any keyword matches the title
                    if any(word in title_lower for word in words):
                        new_entry = {
                            "post_id": story['id'],
                            "title": story['title'],
                            "category": category,
                            "score": story.get('score', 0),
                            "num_comments": story.get('descendants', 0),
                            "author": story.get('by', 'unknown'),
                            "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        }
                        
                        final_stories.append(new_entry)
                        counts[category] += 1
                        print(f"Added to {category}: {story['title'][:50]}...")
                        break 
    
    except Exception as e:
        print(f"Skipping story {id} due to error.")
        continue
    if len(final_stories) % 25 == 0 and len(final_stories) > 0:
        print("Waiting 2 seconds to be polite to the server...")
        time.sleep(2)

#checking file with name 'data' already exists
if not os.path.exists('data'):
    os.makedirs('data')
#creating a JSON file
filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"
with open(filename, 'w') as f:
    json.dump(final_stories, f, indent=4)

print(f"\nFINISHED! Collected {len(final_stories)} stories.")
print(f"File saved at: {filename}")

#Final check to see if all categories has 25 stories
category_totals = {}
for item in final_stories:
    cat = item['category']
    category_totals[cat] = category_totals.get(cat, 0) + 1

print("--- Category Report ---")
for cat, count in category_totals.items():
    print(f"{cat.capitalize()}: {count} stories") 
