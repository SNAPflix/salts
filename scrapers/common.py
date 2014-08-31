import urllib2
import xbmc
from salts_lib.constants import USER_AGENT
from salts_lib import log_utils
from salts_lib.db_utils import DB_Connection

def cached_http_get(url, base_url, timeout, cache_limit=8):
    log_utils.log('Getting Url: %s' % (url))
    db_connection=DB_Connection()
    html = db_connection.get_cached_url(url, cache_limit)
    if html:
        log_utils.log('Returning cached result for: %s' % (url), xbmc.LOGDEBUG)
        return html
    
    try:
        request = urllib2.Request(url)
        request.add_header('User-Agent', USER_AGENT)
        request.add_unredirected_header('Host', request.get_host())
        request.add_unredirected_header('Referer', base_url)
        response = urllib2.urlopen(request, timeout=timeout)
        html=response.read()
    except Exception as e:
        log_utils.log('Error (%s) during scraper http get: %s' % (str(e), url), xbmc.LOGWARNING)
    
    db_connection.cache_url(url, html)
    return html