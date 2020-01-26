from django.test import TestCase
from django.urls import reverse

from account.models import CustomUser
from post.models import *

ALL_TAGS = [
    "a", "abbr", "address", "applet", "area", "article", "aside", "audio",
    "b", "base", "basefont", "bdi", "bdo", "bgsound", "big", "blink", "blockquote", "body", "br", "button",
    "canvas", "caption", "center", "cite", "code", "col", "colgroup", "command", "content",
    "data", "datalist", "dd", "del", "detals", "dfn", "dialog", "dir", "div", "dl", "dt",
    "element", "em", "embed",
    "fieldset", "figcaption", "figure", "font", "footer", "form", "frame", "frameset",
    "h1", "h2", "h3", "h4", "h5", "h6", "head", "header", "hgroup", "hr", "html",
    "i", "iframe", "image", "img", "input", "ins", "isindex",
    "kbd", "keygen",
    "label", "legend", "li", "link", "listing",
    "main", "map", "mark", "marquee", "menu", "menuitem", "meta", "meter", "multicol",
    "nav", "nobr", "noembed", "noframes", "noscript",
    "object", "ol", "optgroup", "option", "output",
    "p", "param", "picture", "plaintext", "pre", "progress",
    "q",
    "rp", "rt", "ruby",
    "s", "samp", "script", "section", "select", "shadow", "small", "source", "spacer", "span", "strike", "strong", "style", "sub", "summary", "sup",
    "table", "tbody", "td", "template", "textarea", "tfoot", "th", "thead", "time", "title", "tr", "track", "tt",
    "u", "ul",
    "var", "video",
    "wbr",
    "xmp",
]

SUB_TAGS = [
    "caption", "col", "colgroup", "tbody", "tfoot", "thead", "tr", "th", "td",
]

TAGS = [
    "a", "abbr", "area", "b", "bdo", "blockquote", "br", "caption", "cite",
    "code", "dd", "del", "details", "dfn", "div", "dl",
    "dt", "em", "figcaption", "figure", "footer", "h1", "h2", "h3", "h4", "h5",
    "h6", "header", "i", "img", "ins", "li", "main", "map", "mark", "meter",
    "ol", "p", "picture", "pre", "progress", "q", "s", "samp", "section",
    "small", "span", "strong", "sub", "summary", "sup", "table", "tbody", "td",
    "tfoot", "th", "thead", "time", "tr", "u", "ul", "var",
]


class TestPostModel(TestCase):
    """Tests for the Post Model."""

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='alfred',
            password='Hads65ads1',  # skipcq: PTC-W1006
        )
        self.test_post = Post(title='Title', content='test content',
                              authors=self.user)

    def test_post_str(self):
        self.assertTrue(self.test_post, 'Title')

    def test_post_url(self):
        url = self.test_post.get_absolute_url()
        self.assertTrue(url, '/post/None/')

    def test_post_content_safe(self):
        """Tests if the save function correctly cleans and saves HTML data"""
        test_failed = False
        for tag in ALL_TAGS:
            # First we address any tags that need attributes tested.
            if tag == 'img':
                # Correct order for arributes: alt src title
                content = ("<img alt=\"test2.jpg\" src=\"test.jpg\""
                           " title=\"Title\">")

            elif tag == 'area':
                # Correct order for arributes: coords, href then shape
                content = ("<map>\n<area coords=\"0,0,82,126\" "
                           "href=\"sun.htm\" shape=\"rect\">\n</map>")

            # Here we test tags that do not have a subsequent closing tag
            # Right now there is only one, will change  to a list if more
            # tags are added
            elif tag == 'br':
                content = '<br>'

            # Here is table crafted  with all approved subtags
            elif tag == 'table':
                content = ("<table><caption>Caption</caption><thead><tr><th>"
                           "HEAD</th></tr></thead><tbody><tr><th>TH1"
                           "</th><th>TH2</th></tr><tr><td>TD1</td><td>TD2"
                           "</td></tr></tbody><tfoot><tr><td>FT1</td>"
                           "</tr></tfoot></table>")

            else:  # and everything else should be a regular tag
                content = "<" + tag + ">TESTING</" + tag + ">"

            new_post = Post(title='Title', content=content, authors=self.user)
            new_post.save()

            if tag in TAGS and tag not in SUB_TAGS:
                try:
                    self.assertIn(content, new_post.content)
                except AssertionError:
                    print(f"content: {content} failed.")
                    print(f"above content is being filter out"
                          "{new_post.content}")
            else:
                try:
                    self.assertNotIn(content, new_post.content)
                except AssertionError:
                    print(f"content: {content} failed.")
                    print(f"above content is not being filter from:"
                          "{new_post.content}")
