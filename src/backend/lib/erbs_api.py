from enum import Enum

import requests


class ERBSApi:
    BASE_URL = 'https://open-api.bser.io'
    version = 'v1'

    def __init__(self, key: str, version: str = 'v1'):
        self.api_key = key
        self.version = version

    class MatchingTeamMode(Enum):
        SOLO = 1
        DUO = 2
        SQUAD = 3

    @property
    def api_url(self) -> str:
        return f'{self.BASE_URL}/{self.version}'

    @property
    def headers(self) -> dict:
        return {
            'accept': 'application/json',
            'x-api-key': self.api_key
        }

    def get_user_num_by_nickname(self, nickname: str = None) -> int:
        if nickname is None or nickname == '':
            raise ValueError('Nickname cannot be empty.')

        url = f'{self.api_url}/user/nickname'
        payload = {'query': nickname}

        res = requests.get(url, params=payload, headers=self.headers)
        r_json = res.json()

        if res.status_code != 200 or r_json['code'] != 200:
            raise ValueError(r_json['message'])

        return r_json['user']['userNum']

    def get_top_rankers_by_season(self, season_id: int = 1, matching_team_mode: int = 1) -> dict:
        url = f'{self.api_url}/rank/top/{season_id}/{matching_team_mode}'

        res = requests.get(url, headers=self.headers)
        r_json = res.json()

        if res.status_code != 200 or r_json['code'] != 200:
            raise ValueError(r_json['message'])

        return r_json['topRanks']

    def get_user_rank_by_season(self, user_num: int = None, season_id: int = 1, matching_team_mode: int = 1) -> dict:
        if user_num is None:
            raise ValueError('User number cannot be empty.')

        url = f'{self.api_url}/rank/{user_num}/{season_id}/{matching_team_mode}'

        res = requests.get(url, headers=self.headers)
        r_json = res.json()

        if res.status_code != 200 or r_json['code'] != 200:
            raise ValueError(r_json['message'])

        return r_json

    def get_user_games(self, user_num: int = None) -> dict:
        if user_num is None:
            raise ValueError('User number cannot be empty.')

        url = f'{self.api_url}/user/games/{user_num}'

        res = requests.get(url, headers=self.headers)
        r_json = res.json()

        if res.status_code != 200 or r_json['code'] != 200:
            raise ValueError(r_json['message'])

        return r_json

    def get_user_stats(self, user_num: int = None, season_id: int = 1) -> dict:
        if user_num is None:
            raise ValueError('User number cannot be empty.')

        url = f'{self.api_url}/user/stats/{user_num}/{season_id}'

        res = requests.get(url, headers=self.headers)
        r_json = res.json()

        if res.status_code != 200 or r_json['code'] != 200:
            raise ValueError(r_json['message'])

        return r_json
