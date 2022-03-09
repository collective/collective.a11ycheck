import Acquisition
from plone import api
from plone.app.blocks import layoutbehavior
from plone.app.blocks import utils as blocks_utils
from plone.tiles.interfaces import ITileDataManager
from plone.transformchain import zpublisher
from repoze.xmliter import utils as xmliter_utils
from six.moves import urllib
from Testing.makerequest import makerequest
from zope import interface


def get_tile_html(context, request):
    """
    Gather HTML from all tiles on the page
    """
    lookup = layoutbehavior.ILayoutAware(context, None)
    layout = lookup.content_layout() if lookup else None
    encoding = zpublisher.extractEncoding(request.response)
    serializer = xmliter_utils.getHTMLSerializer(
        [layout], encoding=encoding)
    app = makerequest(
        Acquisition.aq_base(context.getPhysicalRoot()))
    portal = api.portal.get()
    interface.alsoProvides(
        app.REQUEST, *interface.providedBy(request))
    tile_html = ''
    for tileNode in blocks_utils.bodyTileXPath(serializer.tree):
        data_tile = urllib.parse.urlsplit(
            tileNode.attrib[blocks_utils.tileAttrib])
        tile_path = data_tile.path[2:]
        if data_tile.query:
            tile_path = tile_path + '?{}'.format(data_tile.query.split('&')[0])
        if 'standardtiles.field' in tile_path:
            base_tile = '@@plone.app.standardtiles.field'
            tile_name = tile_path.split('=')[-1].replace('-', '.')
            standardtiles = portal.restrictedTraverse('{0}/{1}'.format('/'.join(context.getPhysicalPath()), base_tile))
            try:
                tile_text = standardtiles._Tile__cachedData['form.widgets.{0}'.format(tile_name)]
            except KeyError:
                continue
            if 'IDublinCore.title' in tile_name:
                tile_html = tile_html + '<h1>{0}</h1>'.format(tile_text)
            else:
                tile_html = tile_html + tile_text
        else:
            tile = app.restrictedTraverse('{0}/{1}'.format('/'.join(context.getPhysicalPath()), tile_path))
            dataManager = ITileDataManager(tile)
            tile_html = tile_html + dataManager.tile()
    return tile_html

def mosaic_page_html(obj):
    request = obj.REQUEST
    # need page html, too
    tile_html = get_tile_html(obj, request)
    return tile_html
