# source https://github.com/alfaarghya/alfa-leetcode-api
import requests

def get_leetcode_stats(username):
    api_url = f"https://leetcode-stats-api.herokuapp.com/{username}"

    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        if "totalSolved" in data:
            return {
                "username": username,
                "total_solved": data["totalSolved"],
                "easy_solved": data["easySolved"],
                "medium_solved": data["mediumSolved"],
                "hard_solved": data["hardSolved"],
            }
        else:
            raise ValueError("User Not Found！")
    else:
        raise Exception(f"Request Failed with Status Code：{response.status_code}")

username = "Jiang17832"
try:
    stats = get_leetcode_stats(username)
    print(f"LeetCode User {stats['username']}：")
    print(f"Problem Solved：{stats['total_solved']}")
    print(f"Easy：{stats['easy_solved']}")
    print(f"Medium：{stats['medium_solved']}")
    print(f"Hard：{stats['hard_solved']}")
except Exception as e:
    print(f"Error：{e}")
