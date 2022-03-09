# import bs4 as BeautifulSoup
from bs4 import BeautifulSoup
from Products.statusmessages.interfaces import IStatusMessage
from zope.annotation.interfaces import IAnnotations

from .mosaic import mosaic_page_html


def check_html(obj, event=None):
    """validate the rendered HTML of the page
    """
    if 'ObjectAddedEvent' in str(event.__class__):
        obj = event.object
        # skip check specified types
        skip_types = ['people_listing', 'groups_listing',
            'Event', 'seminar', 'News Item']
        if obj.portal_type in skip_types:
            return
    elif not getattr(event, 'descriptions', ''):
        # When an item is added, the parent triggers
        # the modified event, but has no descriptions.
        # Skip checking accessibility on the parent
        return

    messages = IStatusMessage(obj.REQUEST)

    if 'layout' in obj.defaultView():
        soup = BeautifulSoup(mosaic_page_html(obj), 'html.parser')
    else:
        soup = BeautifulSoup(obj(), 'html.parser')

    headings = soup.findAll('h1')
    headings_list = [x.text.replace('\n', '').strip() for x in headings \
        if x.text != 'Debug information']
    if not len(headings_list):
        messages.add(
            f'Accessibility error: Page has no H1 tags', type='error')
    elif len(headings_list) > 1:
        headings_text = ', '.join(headings_list)
        messages.add(
            f'Accessibility error: Page has more than one H1 tag ({headings_text})',
            type='error')
    for image in soup.findAll('img'):
        if not image.get('alt', ''):
            messages.add(f'Accessibility error: Image [{image.get("src")}] is missing alt text', type='error')

# create separate functions for each check