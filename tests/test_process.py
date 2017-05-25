import unittest
import discogs_client
from modules import process


class TestPrecessMap(unittest.TestCase):
    def setUp(self):
        """
        Setup process.
        """
        client = discogs_client.Client('ExampleApplication/0.1',
                                       user_token="USER-TOKEN")
        self.processor = process.ProcessMap(client, "test_countries.txt")

    def test_creature(self):
        """
        Test correct creature of process.
        """
        self.assertEqual(len(self.processor), 3)

    def test_request(self):
        """
        Test correct request method in process.
        """
        self.processor.request_values("", read_file="test_request.txt", year=2016, style="ololo")
        self.assertEqual(self.processor.values_list(),
                         [["Australia", 34], ["Congo", 9], ["Ukraine", 37]])


if __name__ == '__main__':
    unittest.main()
