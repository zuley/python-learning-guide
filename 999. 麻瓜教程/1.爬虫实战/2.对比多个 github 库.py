import requests

def get_names ():
  print('请输入库的名字，用空格割开')
  names = input()
  return names.split()

def check_repos (names):
  repo_api = 'https://api.github.com/search/repositories?q='
  ecosys_api = 'https://api.github.com/search/repositories?q=topic:'
  for name in names:
    repo_info = requests.get(repo_api+name).json()['items'][0]
    stars = repo_info['stargazers_count']
    forks = repo_info['forks_count']
    ecosys_info = requests.get(ecosys_api+name).json()['total_count']
    print(name)
    print('Stars: ' + str(stars))
    print('Forks: ' + str(forks))
    print('Ecosys: ' + str(ecosys_info))
    print('----------------------------')

check_repos(get_names())