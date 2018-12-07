from uuid import uuid3, uuid1, uuid4

import shortuuid


def get_random_id():
    return uuid3(uuid1(), uuid4().hex)


def get_random_code(length):
    return shortuuid.ShortUUID().random(length=length).lower()
