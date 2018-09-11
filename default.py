import json
import xbmc
import xbmcaddon

ADDON = xbmcaddon.Addon()
ADDON_ID = ADDON.getAddonInfo('id')
ADDON_NAME = ADDON.getAddonInfo('name')
ADDON_VERSION = ADDON.getAddonInfo('version')

def writeLog(message, level=xbmc.LOGDEBUG):
    try:
        xbmc.log('[%s %s]: %s' % (ADDON_ID, ADDON_VERSION, message), level)
    except Exception:
        xbmc.log('[%s %s]: %s' % (ADDON_ID, ADDON_VERSION, 'Fatal: Could not log message'), xbmc.LOGERROR)
    
def jsonrpc(query):
    querystring = {"jsonrpc": "2.0", "id": 1}
    querystring.update(query)
    try:
        response = json.loads(xbmc.executeJSONRPC(json.dumps(querystring, encoding='utf-8')))
        if 'result' in response: return response['result']
    except TypeError, e:
        writeLog('Error executing JSON RPC: %s' % (e.message), xbmc.LOGERROR)
    return False

if __name__ == '__main__':
    query = dict()
    query.update({'method': 'Input.ExecuteAction', 'params': {'action': 'volumeamplification'}})
    res = jsonrpc(query)
    if res == 'OK':
        writeLog('Command sent successfully')