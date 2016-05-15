from django import template
from django.utils.safestring import mark_safe

register = template.Library()

class YouTube:
    style = """
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
        </style>"""

    @staticmethod
    def get_embed(video_id):
        return """
            <div class='embed-container'>
                <iframe src='https://www.youtube.com/embed/{0}' frameborder='0' allowfullscreen>
                </iframe>
            </div>""".format(video_id)


@register.simple_tag(name='youtube')
def youtube(video_id, include_style=True):
    return mark_safe((YouTube.style + YouTube.get_embed(video_id)) \
        if include_style else YouTube.get_embed(video_id))

@register.simple_tag(name='youtube_style')
def youtube_style():
    return mark_safe(YouTube.style)

@register.simple_tag(name='youtube_embed')
def youtube_embed(video_id):
    return mark_safe(YouTube.get_embed(video_id))

@register.simple_tag(name='youtube_thumb')
def youtube_thumb(video_id):
    return "http://img.youtube.com/vi/{0}/0.jpg".format(video_id)
