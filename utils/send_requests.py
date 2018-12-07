import requests
from django.conf import settings

from exception.exceptions import WeChatConnectError


def get_wechat_session(code):
    app_id = settings.WECHAT_CONFIG.get('app_id')
    app_secret = settings.WECHAT_CONFIG.get('app_secret')
    url = settings.WECHAT_CONFIG.get('jscode2session_url')
    params = {
        'appid': app_id,
        'secret': app_secret,
        'js_code': code,
        'grant_type': 'authorization_code',
    }
    try:
        res = requests.get(url, params)
    except ConnectionError:
        raise WeChatConnectError('can not connect wechat api')
    return res.json()


def get_wechat_openid(code):
    session = get_wechat_session(code)
    open_id = session.get('openid')
    if not open_id:
        raise WeChatConnectError('get wechat openid fail, errmsg:{}'.format(session))
    return open_id
