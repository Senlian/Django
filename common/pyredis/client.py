import redis
import types


class webRedisCli():
    def __init__(self, host="127.0.0.1", port=7800, passwd="", db=0):
        self.host = host
        self.port = port
        self.db = db or 0
        self.passwd = passwd
        self.client = self.connect()

    def isRedis(self):
        try:
            __client = redis.Connection(host=self.host, port=self.port, password=self.passwd)
            __client.connect()
            return True
        except Exception as e:
            print(e)
            return False

    def redisStatus(objFunc):
        if not isinstance(objFunc, types.FunctionType):
            return objFunc

        def newFunc(self, *args, **kwargs):
            if self.isRedis():
                return objFunc(self, *args, **kwargs)
            else:
                return False

        return newFunc

    @redisStatus
    def connect(self):
        pool = redis.ConnectionPool(host=self.host, port=self.port, password=self.passwd, db=self.db,
                                    decode_responses=True,
                                    socket_timeout=5,
                                    socket_connect_timeout=5)
        return redis.StrictRedis(connection_pool=pool).pipeline()

    def get(self, key):
        if self.client is False:
            return None
        self.client.get(key)
        return self.client.execute()[0]

    def set(self, key, value, ex=None, px=None, nx=True, xx=False):
        if self.client is False:
            return False
        self.client.set(key, value)
        return self.client.execute()[0]

    def keys(self):
        if self.client is False:
            return None
        self.client.keys()
        return self.client.execute()[0]

    def keysize(self):
        if self.client is False:
            return None
        self.client.dbsize()
        return self.client.execute()[0]

    def scan(self, cursor, match, count):
        self.client.scan(cursor, match, count)
        return self.client.execute()[0]


if __name__ == "__main__":
    cli = webRedisCli()
    print(cli.scan(0, "*", 10))
