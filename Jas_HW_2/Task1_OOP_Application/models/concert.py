import datetime
from typing import Optional
from .artist import Artist


class Concert:

    def __init__(self, artist: Artist, date_str: str, venue: str, max_tickets: int, price: float = 100.0):
        self._artist = artist
        
        if not self.is_valid_date(date_str):
            raise ValueError(f"Invalid date format for '{date_str}'.")
        self._date = date_str
        
        self._venue = venue
        self._max_tickets = max_tickets
        self._sold_tickets = 0
        self._price = price

    def get_artist(self) -> Artist:
        return self._artist

    def set_artist(self, artist: Artist):
        self._artist = artist

    def get_venue(self) -> str:
        return self._venue

    def set_venue(self, venue: str):
        self._venue = venue

    def get_date(self) -> str:
        return self._date

    def set_date(self, date_str: str):
        if not self.is_valid_date(date_str):
            raise ValueError(f"Invalid date format for '{date_str}'.")
        self._date = date_str

    def get_max_tickets(self) -> int:
        return self._max_tickets

    def set_max_tickets(self, max_tickets: int):
        self._max_tickets = max_tickets

    def get_sold_tickets(self) -> int:
        return self._sold_tickets

    def set_sold_tickets(self, sold_tickets: int):
        self._sold_tickets = sold_tickets

    def get_price(self) -> float:
        return self._price

    def set_price(self, price: float):
        self._price = price

    @staticmethod
    def is_valid_date(date_text: str) -> bool:

        try:
            datetime.date.fromisoformat(date_text)
            return True
        except ValueError:
            return False

    def book_ticket(self) -> bool:
        if self._sold_tickets < self._max_tickets:
            self._sold_tickets += 1
            return True
        return False
        
    def cancel_ticket(self) -> bool:
        if self._sold_tickets > 0:
            self._sold_tickets -= 1
            return True
        return False

    def __str__(self) -> str:
        return f"{self._artist.get_name()} Concert at {self._venue} [{self._date}] (${self._price})"
    
    def __repr__(self) -> str:
        return self.__str__()
