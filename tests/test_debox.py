import unittest
from debox_chat import DeBox

class TestDeBox(unittest.TestCase):
    def setUp(self):
        self.debox = DeBox(api_key="test_api_key")

    def test_get_user_info(self):
        user_info = self.debox.get_user_info("user_id")
        self.assertIsNotNone(user_info)

    def test_get_group_info(self):
        group_info = self.debox.get_group_info("group_id")
        self.assertIsNotNone(group_info)

    def test_send_message(self):
        response = self.debox.send_message("user_id", "Hello!")
        self.assertEqual(response['status'], 'success')

    def test_send_group_text_message(self):
        response = self.debox.send_group_text_message("group_id", "user_id", "Title", "Content")
        self.assertEqual(response['status'], 'success')

    def test_send_group_graphic_message(self):
        response = self.debox.send_group_graphic_message("group_id", "user_id", "Title", "Content", "https://example.com/image.png", "https://example.com")
        self.assertEqual(response['status'], 'success')

    def test_send_graphic_message(self):
        response = self.debox.send_graphic_message("user_id", "Title", "Content", "https://example.com/image.png", "https://example.com")
        self.assertEqual(response['status'], 'success')

if __name__ == '__main__':
    unittest.main()

