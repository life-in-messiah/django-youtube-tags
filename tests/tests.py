from django.test import TestCase
from django.template import Template, Context


class CustomTemplateTagTest(TestCase):
    def _try(self, template_string, expected_output):
        t = Template(template_string)
        empty = {}
        c = Context(empty)
        result = t.render(c)
        result = result.replace(' ', '').replace('\t', '').replace('\n', '')
        expected_output = expected_output.replace(' ', '').replace('\t', '').replace('\n', '')
        if result != expected_output:
            raise AssertionError("Expected:\n%s\nActual:\n%s" % (expected_output, result))

class YouTubeTagTestWithStyle(CustomTemplateTagTest):
    def test_tag(self):
        return self._try("{% load youtube %}{% youtube 'Wji-BZ0oCwg' %}", """
            <style>
                .embed-container {
                    position: relative;
                    padding-bottom: 56.25%;
                    height: 0;
                    overflow: hidden;
                    max-width: 100%;
                }
                .embed-container iframe,
                .embed-container object,
                .embed-container embed {
                    position: absolute;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    }
            </style>
            <div class='embed-container'>
                <iframe src='https://www.youtube.com/embed/Wji-BZ0oCwg' frameborder='0' allowfullscreen>
                </iframe>
            </div>""")

class YouTubeTagTestWithoutStyle(CustomTemplateTagTest):
    def test_tag(self):
        return self._try("{% load youtube %}{% youtube 'Wji-BZ0oCwg' False %}", """
            <div class='embed-container'>
                <iframe src='https://www.youtube.com/embed/Wji-BZ0oCwg' frameborder='0' allowfullscreen>
                </iframe>
            </div>""")


class YouTubeEmbedTagTest(CustomTemplateTagTest):
    def test_tag(self):
        return self._try("{% load youtube %}{% youtube_embed 'Wji-BZ0oCwg' %}", """
            <div class='embed-container'>
                <iframe src='https://www.youtube.com/embed/Wji-BZ0oCwg' frameborder='0' allowfullscreen>
                </iframe>
            </div>""")


class YouTubeStyleTagTest(CustomTemplateTagTest):
    def test_tag(self):
        return self._try("{% load youtube %}{% youtube_style %}", """
            <style>
                .embed-container {
                    position: relative;
                    padding-bottom: 56.25%;
                    height: 0;
                    overflow: hidden;
                    max-width: 100%;
                }
                .embed-container iframe,
                .embed-container object,
                .embed-container embed {
                    position: absolute;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    }
            </style>""")
