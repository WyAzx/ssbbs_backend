from redis import StrictRedis

from django.conf import settings


class RedisClient(StrictRedis):
    """
    RedisClient的单例
    """

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '__instance__'):
            cls.__instance__ = super().__new__(cls)
        return cls.__instance__


def get_redis_client():
    assert settings.REDIS_CONFIG, (
        "Can't get redis config in settings.py"
    )
    redis_config = settings.REDIS_CONFIG
    return RedisClient(
        host=redis_config.get('HOST'),
        port=redis_config.get('PORT'),
        password=redis_config.get('PASSWORD'),
        db=redis_config.get('DB'),
        decode_responses=True
    )
