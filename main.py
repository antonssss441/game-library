import requests
import os
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv('API_KEY')
PARAMS = {
    'key': API_KEY,
    'page_size': 10,
    'metacritic': '90,100',
    'tags': 'multiplayer'
}


def get_games():
    url = 'https://api.rawg.io/api/games'
    response = requests.get(url, params=PARAMS)
    response.raise_for_status()
    games = response.json()['results']
    return games


def get_images(game_pk):
    url = f'https://api.rawg.io/api/games/{game_pk}/screenshots'
    response = requests.get(url, params=PARAMS)
    response.raise_for_status()
    games_images = response.json()['results']
    return games_images


def get_stores(game_pk):
    url = f'https://api.rawg.io/api/games/{game_pk}/stores'
    response = requests.get(url, params=PARAMS)
    response.raise_for_status()
    games_stores = response.json()['results']
    return games_stores


def main():
    games = get_games()
    for game in games:
        name = game['name']
        released = game['released']
        slug = game['slug']
        url_game = f'https://rawg.io/games/{slug}'
        game_images = get_images(slug)
        game_stores = get_stores(slug)
        print(f'\nНазвание игры: {name}')
        print(f'Дата выхода: {released}')
        print(f'Ссылка на игру: {url_game}')
        print(f'Скриншоты из игры:')
        for game_image in game_images:
            print(game_image['image'])
        print(f'Где купить:')
        for game_store in game_stores:
            print(game_store['url'])


if __name__ == '__main__':
    main()