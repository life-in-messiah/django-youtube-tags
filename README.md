# django-youtube-tags  

[![Build Status](https://travis-ci.org/life-in-messiah/django-youtube-tags.svg?branch=master)](https://travis-ci.org/life-in-messiah/django-youtube-tags)  

Custom Django template tags to simplify embedding Youtube videos and thumbnails

# Installation and usage
Install via `pip`
```
$ pip install -u django-youtube-tags
```
or download the source, enter the directory, and
```
$ sudo python setup.py install
```

Make sure to include `django-youtube-tags` in your Django settings' `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
  'django-youtube-tags',
...
```

Lastly, make sure to declare `{% load youtube %}` at the top of the Django template(s) where you plan to use this library.

# Tags
## `{% youtube video_id include_style %}`
#### Example: `{% youtube 'Wji-BZ0oCwg' False %}`
`video_id` is the URL segment that uniquely identifies the YouTube video.  

`include_style` is `True` by default.  When `True`, it includes the CSS style inline.  Depending on your situation, this may not be a good practice.  The better practice may be to place `{% youtube_style %}` inside your template's `<head>` section and then use `{% youtube_embed %}` (see below)

## `{% youtube_embed video_id %}`
#### Example: `{% youtube_embed 'Wji-BZ0oCwg' %}`
Same as `{% youtube %}` with `include_style` set to `False`

## `{% youtube_style %}`
Renders needed CSS classes inside a `<style>` tag.
