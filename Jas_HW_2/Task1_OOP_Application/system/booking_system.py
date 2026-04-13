from models.user import Fan, VIPFan
from models.artist import Artist
from models.concert import Concert
from models.booking import Booking
from data_structures.heap import MaxHeap
from algorithms.heap_sort import heap_sort


class BookingSystem:

    def __init__(self):
        self.fans = []
        self.artists = []
        self.concerts = []
        self.bookings = []

        self.waitlist = MaxHeap()

    def add_artist(self, name: str, agency: str):
        artist = Artist(name, agency)
        self.artists.append(artist)
        return artist
        
    def add_fan(self, name: str, email: str, is_vip: bool = False, vip_level: str = "Gold"):
        if is_vip:
            fan = VIPFan(name, email, vip_level)
        else:
            fan = Fan(name, email)
        self.fans.append(fan)
        return fan

    def create_concert(self, artist_name: str, date: str, venue: str, max_tickets: int, price: float):
        artist = next((a for a in self.artists if a.get_name() == artist_name), None)
        if not artist:
            print(f"Artist {artist_name} not found")
            return False
            
        try:
            concert = Concert(artist, date, venue, max_tickets, price)
            self.concerts.append(concert)
            return concert
        except ValueError as e:
            print(f"Error creating concert: {e}")
            return False

    def view_all_concerts(self, sort_by_price: bool = False):
        if not self.concerts:
            print("No concerts available.")
            return

        display_list = self.concerts.copy()
        
        if sort_by_price:
            class ConcertWrapper:
                def __init__(self, concert):
                    self.concert = concert
                def __lt__(self, other):
                    return self.concert.get_price() < other.concert.get_price()
                    
            wrappers = [ConcertWrapper(c) for c in display_list]
            heap_sort(wrappers)
            display_list = [w.concert for w in wrappers]

        for i, c in enumerate(display_list, 1):
            if c.get_sold_tickets() < c.get_max_tickets():
                status = "AVAILABLE"
            else: status = "SOLD OUT"
            print(f"{i}. {c} - Tickets: {c.get_sold_tickets()}/{c.get_max_tickets()} [{status}]")
            
        return display_list

    def request_booking(self, fan: Fan, concert: Concert):
        booking = Booking(fan, concert)
        
        if concert.book_ticket():
            print(f"\nSUCCESS, {fan.get_name()} successfully booked a ticket for {concert.get_artist().get_name()}!")
            self.bookings.append(booking)
        else:
            print(f"\nSOLD OUT, {concert.get_artist().get_name()} at {concert.get_venue()} is full.")
            print(f"Adding {fan.get_name()} to the waitlist...")
            self.waitlist.insert(booking)

    def process_waitlist(self):
        if self.waitlist.is_empty():
            print("The waitlist is currently empty.")
            return

        total_in_queue = self.waitlist.get_size()
        print(f"Currently {total_in_queue} fans in waitlist.")

        highest_priority_booking = self.waitlist.extract_max()
        fan = highest_priority_booking.get_fan()

        print(f"Next in line: {fan.get_name()} with Priority: {fan.get_priority()}.")
        print("Since tickets are sold out, they need to wait for cancellations.")
        return highest_priority_booking
