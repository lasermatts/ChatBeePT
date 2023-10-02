import requests
import json
from datetime import datetime

# URL to fetch the top story IDs from HackerNews
TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"

def get_story_detail(story_id):
    """
    Fetch and return the title and URL of a story given its ID.
    """
    STORY_URL = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json?print=pretty"
    response = requests.get(STORY_URL)
    if response.status_code == 200:
        story_detail = response.json()
        return f"Title: {story_detail['title']}\nURL: {story_detail['url']}\n"
    else:
        return "Failed to retrieve story details.\n"

def main():
    """
    Fetch and display the details of the top 5 stories from HackerNews.
    """
    try:
        response = requests.get(TOP_STORIES_URL)
        if response.status_code == 200:
            top_stories = response.json()
            # Getting the current time
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # Displaying the top 5 stories along with the current time
            print(f"\nTop 5 HackerNews Stories [{current_time}]:\n")
            for i, story_id in enumerate(top_stories[:5]):
                print(f"Story {i + 1}:")
                print(get_story_detail(story_id))
        else:
            print("Failed to retrieve top stories.")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {str(e)}")
    except json.JSONDecodeError:
        print("Failed to parse the response.")

if __name__ == "__main__":
    main()
