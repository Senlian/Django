import json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SenLianRedis.settings")
django.setup()

from django.http import HttpResponse
from WebRedis.models import dbServer
from django.views.decorators.csrf import csrf_exempt
from common.pyredis.client import webRedisCli


def deal_parameters(request):
    args = {}
    if request.method.upper() == "POST":
        args = request.POST
    if request.method.upper() == "GET":
        args = request.GET
    if not args:
        args = json.loads(request.body)
    return args


def is_valid_redis(host, port, db=0):
    redisApi = webRedisCli(host, port, db)
    historyData = dbServer.objects.filter(host=host, port=port)
    keysCount = 0
    if redisApi.isRedis():
        status = "T"
        keysCount = int(redisApi.keysize())
    else:
        status = "F"
        redisApi = None
    if len(historyData) >= 1:
        itemData = dbServer.objects.get(host=host, port=port)
        itemData.status = status
        itemData.count = keysCount
        itemData.save()
    else:
        if status == "T":
            newData = dbServer(host=host, port=port, status=status)
            newData.count = keysCount
            newData.save()
    return status, redisApi


def get_dbs():
    dbList = list(dbServer.objects.all().values("host", "port", "count", "status").order_by("host"))
    for db in dbList:
        is_valid_redis(db["host"], db["port"])
    return list(dbServer.objects.all().values("host", "port", "count", "status").order_by("host"))


def scan_keys(redisApi, cursor=0, match="*", count=10):
    if not redisApi:
        return None
    keys = redisApi.scan(cursor, match, count)
    return keys


def main_entry(args):
    keys = args.keys()
    cursor, count = 0, 3
    print(args)
    for key in keys:
        if key.lower() == "host":
            host = args[key]
        if key.lower() == "port":
            port = int(args[key])
        if key.lower() == "db":
            db = int(args[key])
        if key.lower() == "cursor":
            cursor = int(args[key])
        if key.lower() == "count":
            count = int(args[key])
        if key.lower() == "operate":
            operate = args[key]

    if operate.lower() == "dbs":
        data = get_dbs()

    if operate.lower() in ["isredis", "scan"]:
        data, redisApi = is_valid_redis(host, port, db)
        if operate.lower() == "scan":
            data = scan_keys(redisApi=redisApi, cursor=cursor, count=count)
    return data


def query_data(request):
    args = deal_parameters(request)
    data = main_entry(args)
    print(data)
    return HttpResponse(content_type="application/json", content=json.dumps(data))


if __name__ == "__main__":
    # dbList = dbServer.objects.all().values("host", "port", "status").order_by("host")
    # print(json.dumps(list(dbList)))
    pass
