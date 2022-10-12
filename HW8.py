import requests
import json
from pprint import pprint



def heros_list():
        url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api//all.json'
        params = {'name': 'Hulk'}
        response = requests.get(url, params = params, timeout = 5)
        heros = response.json()

        return heros


def heros_int():

        int_list = []
        for hero in heros_list():
                if hero['name'] == 'Hulk' or hero['name'] == 'Thanos' or hero['name'] == 'Captain America':
                        int_list.append(hero['powerstats']['intelligence'])

        max_int = max(int_list)                            
        return max_int


def heros_diktes():
        list_dictes = []
        for hero in heros_list():
                if hero['name'] == 'Hulk' or hero['name'] == 'Thanos' or hero['name'] == 'Captain America':
                        hero_dikt = {hero['name']:hero['powerstats']['intelligence']}
                        list_dictes.append(hero_dikt)
                        if {hero['name']:heros_int()} in list_dictes:
                                return hero['name']

pprint(heros_diktes())


############################################################################

class Load:
        def __init__(self, token):
                self.token = token


        def get_headers(self):
                return {'ContentType': 'application/json', 'Autorization':'OAuth{}'.format(self.token)}
                

        def upload_link(self, disk_file_path):
                upload_url = 'http://cloud-api.yandex.net/v1/disk/resources/upload'
                headers = self.get_headers()
                params = {'path': disk_file_path, 'owerwrite': 'true'}
                response = requests.get(upload_url, headers = headers, params = params, timeout = 5)
                return response.json()    


        def upload_file(self, disc_file_path, filename):
                href = self.upload_link(disk_file_path = disc_file_path).get('href', '')
                response = requests.put(href, data = open(filename, 'rb'))

                # response.raise_for_status()
                
                        


if __name__ == '__main__':
        ya = Load(token = TOKEN)
        pprint
        ya.upload_file(r'C:\Users\Андрей-сан\Desktop\Homeworks\READMY.md', 'READMY.md')



       