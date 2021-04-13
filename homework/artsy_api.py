import requests
from operator import itemgetter

client_id = '79db6d45a533e2a39a58'
client_secret = '959f5beea1cfd73e1b43bb58baec80a6'
artists_dict = {}

token = requests.post('https://api.artsy.net/api/tokens/xapp_token',
                      data={
                          'client_id': client_id,
                          'client_secret': client_secret
                      }).json()['token']

with open('dataset_24476_4.txt') as artist_ids:
    for id in artist_ids:
        id = id.strip()
        artist_info = requests.get(f'https://api.artsy.net/api/artists/{id}', headers={'X-Xapp-Token': token}).json()
        artists_dict[artist_info['sortable_name']] = artist_info['birthday']
    artists_list = sorted(artists_dict.items(), key=itemgetter(1, 0))
    print(artists_list)

    for _ in range(len(artists_list)):
        print(artists_list[_][0])
