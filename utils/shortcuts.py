from account.models import SsUserCode
from utils.common import get_random_code


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
