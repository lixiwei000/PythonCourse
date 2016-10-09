import redis

conn = redis.Redis("localhost")
conn.set("name","Niko")
print(conn.get("name"))
