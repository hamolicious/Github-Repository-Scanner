from github import Github
from time import time
from os import system ; clear = lambda : system('cls') ; clear()
from table import Table, Colours, fg, reset

#region login
title = fg(Colours.title_colour) + """   _____ _ _   _           _        _____ _        _          _____
  / ____(_) | | |         | |      / ____| |      | |        / ____|
 | |  __ _| |_| |__  _   _| |__   | (___ | |_ __ _| |_ ___  | (___   ___ __ _ _ __  _ __   ___ _ __
 | | |_ | | __| '_ \| | | | '_ \   \___ \| __/ _` | __/ __|  \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
 | |__| | | |_| | | | |_| | |_) |  ____) | || (_| | |_\__ \  ____) | (_| (_| | | | | | | |  __/ |
  \_____|_|\__|_| |_|\__,_|_.__/  |_____/ \__\__,_|\__|___/ |_____/ \___\__,_|_| |_|_| |_|\___|_|   """ + reset()

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
stats_table = Table(data, add_total_row=True, add_mean_row=True, add_mode_row=True)
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


