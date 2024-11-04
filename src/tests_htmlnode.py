import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div", 
            "Hello, world!", 
            None, 
            {"class": "greeting", "href": "https://boot.dev"})
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repl(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

class TestLeafNode(unittest.TestCase):
    def test_to_html_no_children(self):
        leaf = LeafNode("p", "This is a paragraph.")
        self.assertEqual(
            leaf.to_html(),
            '<p>This is a paragraph.</p>',
        )

    def test_to_html_with_children(self):
        leaf = LeafNode("a", "Click here!", {"href": "https://www.google.com"})
        self.assertEqual(
            leaf.to_html(),
            '<a href="https://www.google.com">Click here!</a>',
        )

    def test_to_html_no_tag(self):
        leaf = LeafNode(None, "Hello, world!")
        self.assertEqual(leaf.to_html(), "Hello, world!")

if __name__ == "__main__":
    unittest.main()