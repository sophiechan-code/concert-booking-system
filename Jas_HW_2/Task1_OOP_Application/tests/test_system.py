import unittest
from models.user import Fan, VIPFan
from models.artist import Artist
from models.concert import Concert
from models.booking import Booking
from data_structures.heap import MaxHeap
from algorithms.heap_sort import heap_sort

class TestKPopBookingSystem(unittest.TestCase):

    def setUp(self):
        Fan.total_fans = 0
        Booking.total_bookings = 0
        
        self.artist = Artist("TEST_GROUP", "TEST_AGENCY")
        self.concert = Concert(self.artist, "2024-12-31", "TEST_VENUE", 1, 100.0)
        self.regular_fan = Fan("Regular", "reg@test.com")
        self.vip_gold = VIPFan("Gold Member", "gold@test.com", "Gold")
        self.vip_plat = VIPFan("Platinum Member", "plat@test.com", "Platinum")

    def test_inheritance_and_polymorphism(self):
        self.assertIsInstance(self.regular_fan, Fan)
        self.assertIsInstance(self.vip_gold, Fan)

        self.assertIn("Regular Fan", self.regular_fan.display_info())
        self.assertIn("VIP Fan (Gold)", self.vip_gold.display_info())
        self.assertIn("VIP Fan (Platinum)", self.vip_plat.display_info())

        self.assertEqual(self.regular_fan.get_priority(), 10)
        self.assertEqual(self.vip_gold.get_priority(), 50)
        self.assertEqual(self.vip_plat.get_priority(), 100)

    def test_concert_booking_logic(self):
        self.assertTrue(self.concert.book_ticket())
        self.assertEqual(self.concert.get_sold_tickets(), 1)

        self.assertFalse(self.concert.book_ticket())

    def test_max_heap_priority_queue(self):
        heap = MaxHeap()

        booking_reg = Booking(self.regular_fan, self.concert)

        import time; time.sleep(0.01)
        booking_gold = Booking(self.vip_gold, self.concert)
        time.sleep(0.01)
        booking_plat = Booking(self.vip_plat, self.concert)

        heap.insert(booking_reg)
        heap.insert(booking_plat)
        heap.insert(booking_gold)

        first_out = heap.extract_max()
        self.assertEqual(first_out.get_fan().get_priority(), 100)
        self.assertEqual(first_out.get_fan().get_name(), "Platinum Member")
        
        second_out = heap.extract_max()
        self.assertEqual(second_out.get_fan().get_priority(), 50)
        
        third_out = heap.extract_max()
        self.assertEqual(third_out.get_fan().get_priority(), 10)
        
        self.assertTrue(heap.is_empty())

    def test_heap_sort(self):
        arr = [12, 11, 13, 5, 6, 7]
        heap_sort(arr)
        self.assertEqual(arr, [5, 6, 7, 11, 12, 13])

        c1 = Concert(self.artist, "2024-01-01", "V1", 10, 200.0)
        c2 = Concert(self.artist, "2024-01-02", "V2", 10, 50.0)
        c3 = Concert(self.artist, "2024-01-03", "V3", 10, 150.0)
        
        class ConcertWrapper:
            def __init__(self, c): self.c = c
            def __lt__(self, other): return self.c.get_price() < other.c.get_price()
            
        wrappers = [ConcertWrapper(c) for c in [c1, c2, c3]]
        heap_sort(wrappers)
        sorted_concerts = [w.c for w in wrappers]

        self.assertEqual(sorted_concerts[0].get_price(), 50.0)
        self.assertEqual(sorted_concerts[1].get_price(), 150.0)
        self.assertEqual(sorted_concerts[2].get_price(), 200.0)

if __name__ == '__main__':
    unittest.main()
