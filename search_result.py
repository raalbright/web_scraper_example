from dataclasses import dataclass


@dataclass
class SearchEntry:
    def __init__(self, title: str, price: str):
        self.title = title
        self.price = price
    
    def to_dict(self):
        self.__dict__()