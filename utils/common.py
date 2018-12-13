import secrets
from uuid import uuid3, uuid1, uuid4

import shortuuid


def get_random_id():
    return uuid3(uuid1(), uuid4().hex)


def get_random_code(length):
    return shortuuid.ShortUUID().random(length=length).lower()


def get_random_verify_code():
    return str(secrets.randbelow(1000000)).zfill(6)


def get_verify_phone_key(phone):
    return "{}:{}:{}".format('verify_code', 'phone', phone)


def get_verify_email_key(email):
    return "{}:{}:{}".format('verify_code', 'email', email)
