from aiocache import caches

caches.set_config(
    {
        "default": {
            "cache": "aiocache.RedisCache",  # Тип кешу - Redis
            "endpoint": "localhost",  # Адреса Redis сервера
            "port": 6379,  # Порт Redis сервера
            "timeout": 10,  # Час очікування на відповідь
            "serializer": {
                "class": "aiocache.serializers.PickleSerializer"
            },  # Сералізатор для кешування даних
        }
    }
)