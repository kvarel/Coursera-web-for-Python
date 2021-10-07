def calc_age(id):
	''' если id является username, преобразуем username в id, иначе собираем данные с сайта, парсим ДР
	добавляем в словарь и сортируем'''

		
	ACCESS_TOKEN = '17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711'
	URL1 = 'https://api.vk.com/method/users.get'
	URL2 = 'https://api.vk.com/method/friends.get'
	params = {'v': 5.71, 'fields': 'bdate', 'user_id': id}
	data = {}
	rez = {}
	data = filter(data, bdate not is None)
	for i in data:
		if 2021 - i[bdate] in rez:
			rez[2021 - i[bdate]] += 1
		else:
			rez[2021 - i[bdate]] = 1
	rez = list(rez)
	
def name_to_id(id):
	import requests
	ACCESS_TOKEN = '17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711'
	URL1 = 'https://api.vk.com/method/users.get'
	params = {'v': 5.71, 'fields': 'bdate', 'user_id': id}
	x = requests.get(URL1, params=params)
	print(x.text)
	
	
def sort_age(lst):
	return sorted(lst, key=lambda x: (-x[1], x[0]))

def test():
	print(sort_age([(1,2), (2,3), (5,1), (4, 1)]))
	
if __name__ == '__main__':
    name_to_id('kvarel')
