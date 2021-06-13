import json
import random
from collections import defaultdict


class COIN:
    def __init__(
            self, coin='dataset/coin.json',
            missing='dataset/missing_videos.json', data_root='/data/coin'):
        with open(coin) as f:
            self.coin_data = json.load(f)['database']
        with open(missing) as f:
            self.missing = json.load(f)
        self.keys = list(self.coin_data.keys())
        self.data_root = data_root
    
    def random_pick(self):
        while True:
            key = random.choice(self.keys)
            if key not in self.missing:
                break
        return self.get(key)
        
    def get(self, key):
        coin = self.coin_data[key]
        return {
            'name': key,
            'coin': coin,
        }