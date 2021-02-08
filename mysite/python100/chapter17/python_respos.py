import requests

import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("status code:", r.status_code)

# 将API响应存在一个列表
response_dict = r.json()
# print("total repositories ", response_dict['total_count'])

# 搜索关于仓库的信息
repo_dicts = response_dict['items']
# print("repositories returned:", len(repo_dicts))

# 研究第一个仓库
# repo_dict = repo_dicts[0]
# print("\nkey:", len(repo_dict)) # 键值的个数
# for key in sorted(repo_dict.keys()):
#     print(key)


# print("\nselected information about first repository")
# print("Name:", repo_dict['name'])
# print("owner:", repo_dict['owner'])
# print("stargazer:", repo_dict['stargazers_count'])
# print("repository:", repo_dict['html_url'])
# print("created:", repo_dict['created_at'])
# print("updated:", repo_dict['updated_at'])
# print("description:", repo_dict['description'])


# print("\nselected information about each repository")
names, starts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    starts.append(repo_dict['stargazers_count'])
    # print("name:", repo_dict["name"])
    # print("owner:", repo_dict["owner"]["login"])
    # print("repository:", repo_dict['html_url'])
    # print("created:", repo_dict["created_at"])
    # print("updated:", repo_dict["updated_at"])
    # print("description:", repo_dict["description"])

# 可视化
my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()

my_config.x_labels_rotation = 90
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = "Most-starred Python Projects on Github"
chart.x_labels = names

chart.add("", starts)
chart.render_to_file("python_repos.svg")
