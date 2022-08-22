from github import Github
from time import time
from os import system ; clear = lambda : system('cls') ; clear()
from table import Table, Colours, fg, reset

#region login
title = fg(Colours.title_colour) + \
"""
   ___ _ _   _           _       __ _        _         __
  / _ (_) |_| |__  _   _| |__   / _\ |_ __ _| |_ ___  / _\ ___ __ _ _ __  _ __   ___ _ __
 / /_\/ | __| '_ \| | | | '_ \  \ \| __/ _` | __/ __| \ \ / __/ _` | '_ \| '_ \ / _ \ '__|
/ /_\\\\| | |_| | | | |_| | |_) | _\ \ || (_| | |_\__ \ _\ \ (_| (_| | | | | | | |  __/ |
\____/|_|\__|_| |_|\__,_|_.__/  \__/\__\__,_|\__|___/ \__/\___\__,_|_| |_|_| |_|\___|_|
""" + reset()

print(title)
user = 'hamolicious'
with open('token.key', 'r') as file:
		key = file.read()
git_hub = Github(key)
#endregion

start_time = time()

#region get repos
repos = list(git_hub.get_user(user).get_repos())
repos.sort(key=lambda elem: elem.name)
#endregion

def get_stats_data():
		data = [['Repository Name', 'Stars', 'Views', 'Clones', 'Watchers', 'Forks']]
		for repo in repos:
				if repo.archived:
					continue

				data.append([
					repo.name,
					repo.stargazers_count,
					repo.get_views_traffic(per='week').get('count'),
					repo.get_clones_traffic(per='week').get('count'),
					repo.watchers_count,
					repo.forks_count,
				])

		return data

data = get_stats_data()
stats_table = Table(data, add_total_row=True, add_mean_row=True)
stats_table.update()

#region print info
system('color')
string = f"""
{title}

Total Repos: {len(repos)}
"""
clear()
print(string)
stats_table.display()
print(f'\nTime elapsed: {time() - start_time}')
#endregion

input() # keep console open


