import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node,node2)

    def test_dif(self):
        node = TextNode("This is a text node", "italic","testurl.com")
        node2 = TextNode("This is a text node", "bold", "testurl.com")
        self.assertNotEqual(node,node2)

    def test_self_eq(self):
        node = TextNode("This is a text node", "italic","testurl.com")
        node2 = TextNode("This is a text node", "italic", "testurl.com")
        self.assertTrue(node.__eq__(node2))

    def test_not_self_eq(self):
        node = TextNode("This is a text node", "italic","testurl.com")
        node2 = TextNode("This is a text node", "bold", "testurl.com")
        self.assertFalse(node2.__eq__(node))


if __name__ == "__main__":
    unittest.main()