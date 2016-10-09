import redis

class RedisHelper:
    def __init__(self):
        self.__conn = redis.Redis('localhost')
        self.channel__sub = "FM107.5"
        self.channel__pub = "FM107.5"

    def get(self,key):
        return self.__conn.get(key)

    def set(self,key,value):
        return self.__conn.set(key,value)

    def publish(self,msg):
        self.__conn.publish(self.channel__pub,msg)

    def subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.channel__sub)
        pub.parse_response()
        while True:
            print(str(pub.parse_response()[2],encoding='utf8'))
        return pub

if __name__ == "__main__":
    redisHelper = RedisHelper()
    # redisHelper.set("age",18)
    # print(redisHelper.get("age"))
    redisHelper.publish("哈比")
    # pub = redisHelper.subscribe()
    # print(pub.get_message())