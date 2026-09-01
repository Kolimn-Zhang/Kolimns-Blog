import unittest

import app


class HomepageTests(unittest.TestCase):
    def setUp(self):
        app.app.config["TESTING"] = True
        self.client = app.app.test_client()

    def test_homepage_is_personal_card(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        html = response.data.decode("utf-8")
        self.assertIn("Kolimn", html)
        self.assertIn("Builder of AI Workflows, Tools and Notes", html)
        self.assertIn("AI Workflow", html)
        self.assertIn("Agent Tools", html)

    def test_homepage_has_confirmed_quick_links(self):
        response = self.client.get("/")
        html = response.data.decode("utf-8")
        self.assertIn("https://github.com/Kolimn-Zhang", html)
        self.assertIn('href="/blog"', html)
        self.assertIn('href="/category/skills"', html)
        self.assertIn('href="/category/tools"', html)

    def test_blog_route_keeps_original_article_listing(self):
        response = self.client.get("/blog")
        self.assertEqual(response.status_code, 200)
        html = response.data.decode("utf-8")
        self.assertIn("Personal AI Notes", html)
        self.assertIn("Skills", html)
        self.assertIn("Tools", html)

    def test_homepage_shows_two_random_notes(self):
        response = self.client.get("/")
        html = response.data.decode("utf-8")
        self.assertEqual(html.count('class="home-note-card"'), 2)

    def test_nav_has_blog_link(self):
        response = self.client.get("/")
        html = response.data.decode("utf-8")
        self.assertIn('href="/blog"', html)
        self.assertIn(">Blog<", html)


if __name__ == "__main__":
    unittest.main()
