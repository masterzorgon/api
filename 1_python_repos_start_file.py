import requests
import json

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

response_dict = r.json()

outfile = open("output.json", "w")

json.dump(
    response_dict, 
    outfile, 
    indent=4
)

# print out the num of repos in this file
list_of_repos = response_dict['items']
print(len(list_of_repos))

# examine the first repo
first_repo = list_of_repos[0]

# print the num of keys in the repo
print(len(first_repo))

print(f"Name: {first_repo['name']}")
print(f"Owner: {first_repo['owner']['login']}")
print(f"Stars: {first_repo['stargazers_count']}")
print(f"Repo URL: {first_repo['owner']['url']}")
print(f"Last Update: {first_repo['updated_at']}")
print(f"Description: {first_repo['description']}")

from plotly.graph_objects import Bar
from plotly import offline

repo_names, stars = [], []

for repo in list_of_repos[:10]:
    repo_names.append(repo['name'])
    stars.append(repo['stargazers_count'])

data = [
    {
        "type": "bar",
        "x": repo_names,
        "y": stars,
        "marker": {
            "color": "rgb(60,100,150)",
            "line": {
                "width": 1.5,
                "color": "rgb(25, 25, 25)",
            },
        },
        "opacity": 0.6
    },
]

my_layout = {
    "title": "Most-Starred Python Project from GitHub",
    "xaxis": {
        "title": "Repository",
    },
    "yaxis": {
        "title": "Stars",
    },
}

fig = {
    "data": data,
    "layout": my_layout
}

offline.plot(fig, filename="python_repos.html")