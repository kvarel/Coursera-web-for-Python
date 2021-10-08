# взвращает отсортированный список [возраст, кол-во друзей такого возраста] из вконтакте. Отсеиваются такие, у кого не указана дата рождения или не указан год
import requests
def calc_age(id):
    data = {}
    if not id.isdigit():
        id = search_id(id)
    URL = 'https://api.vk.com/method/friends.get'
    params = {'user_id': id, 'fields': 'bdate', 'v': 5.81, "access_token": ACCESS_TOKEN}
    rez = requests.get(URL, params).json()
    for i in rez['response']['items']:
        if 'bdate' in i and len(i['bdate']) > 5:
            if 2021 - int(i['bdate'][-4:]) in data:
                data[2021 - (int(i['bdate'][-4:]))] += 1
            else:
                data[2021 - (int(i['bdate'][-4:]))] = 1
    return sort_age(list(data.items()))

def search_id(id):
    URL = 'https://api.vk.com/method/users.get'
    params = {'v': 5.89, 'user_ids': id, "access_token": ACCESS_TOKEN}
    x = requests.get(URL, params=params).json()
    return x['response'][0]['id']

def sort_age(lst):
    return sorted(lst, key=lambda x: (-x[1], x[0]))

if __name__ == '__main__':
    ACCESS_TOKEN = '14a8293414a8293414a829343c14d1b46d114a814a8293475f7c1dfbf7f186e38dc7912'
    res = calc_age(input())
    print(res)
