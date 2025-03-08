import unittest
from producer.producer import send_message

class TestProducer(unittest.TestCase):
    def test_message_send(self):
        self.assertTrue(send_message('test_topic', {'test': 'message'}))

if __name__ == '__main__':
    unittest.main()
