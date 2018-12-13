import logging

from django.conf import settings
from django.core.mail import send_mail
from django.template import loader

from account.models import SsUserCode
from exception.exceptions import VerifyCodeError
from utils.common import get_random_code, get_random_verify_code, get_verify_email_key
from utils.redis_client import get_redis_client

LOG = logging.getLogger(__name__)


def get_random_user_name():
    length = 5
    user_code = get_random_code(length)
    while True:
        if SsUserCode.objects.filter(code=user_code).exists():
            if length < 8:
                length = length + 1
            user_code = get_random_code(length)
        else:
            SsUserCode.objects.create(code=user_code)
            return 'ss.{}'.format(user_code)


def send_verify_email(email):
    verify_code = get_random_verify_code()
    verify_code_key = get_verify_email_key(email)
    redis_db = get_redis_client()

    # cache verify code
    redis_db.set(verify_code_key, verify_code)
    redis_db.expire(verify_code_key, settings.VERIFY_CODE_EXPIRE)

    title = 'SSPKU论坛验证'
    content = loader.render_to_string(
        'email.html',
        {
            'address': email,
            'verify_code': verify_code
        }
    )
    try:
        email_from = '{} <{}>'.format(settings.EMAIL_FROM, settings.EMAIL_HOST_USER)
        send_mail(title, content, email_from, [email], html_message=content)
    except Exception as e:
        LOG.exception(e)


def verify_code(verify_code_key, input_code):
    redis_db = get_redis_client()
    if redis_db.exists(verify_code_key):
        code = redis_db.get(verify_code_key)
        if not code or code != input_code:
            raise VerifyCodeError(detail='wrong verify code!')
    else:
        raise VerifyCodeError(detail='verify code expired!')
