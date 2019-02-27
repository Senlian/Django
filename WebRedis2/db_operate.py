from django.http import HttpResponse
from WebRedis.models import dbServer
from django.views.decorators.csrf import csrf_exempt
from common.pyredis.client import webRedisCli
import json


# 此装饰器用于取消token校验
# @csrf_exempt
def check_status(host, port, db):
    redisApi = webRedisCli(host, port, db)
    if redisApi.isRedis():
        status = "T"
    else:
        status = "F"

    if len(dbServer.objects.filter(host=host, port=port)) == 1:
        database = dbServer.objects.get(host=host, port=port)
        database.status = status
        database.save()
    else:
        if status == "T":
            database = dbServer(host=host, port=port, status=status)
            database.save()
    return status, redisApi


def get_host(request):
    print("request.GET={0}".format(request.GET))
    print("request.POST={0}".format(request.POST))
    print("request.body={0}".format(request.body))
    host, port, db = None, None, None

    if request.method == "POST":
        host = request.POST.get("host")
        port = request.POST.get("port")
        db = request.POST.get("db")

    if request.method == "GET":
        host = request.GET.get("host")
        port = request.GET.get("port")
        db = request.GET.get("db")

    if ((not host) or (not port)):
        host = json.loads(request.body).get("host")
        port = json.loads(request.body).get("port")
        db = json.loads(request.body).get("db")
    if not db:
        db = 0
    return host, port, int(db)


def is_valid_redis(request):
    host, port, db = get_host(request)
    status = check_status(host, port, db)[0]

    data = {
        "host": host,
        "port": port,
        "status": status
    }

    return HttpResponse(content_type="application/json", content=json.dumps(data))
    # return render(request=request, template_name="WebRedis/index-aside.html")
    # return HttpResponse(json.dumps("ok"), mimetype='application/javascript')


def get_servers(request):
    dbList = list(dbServer.objects.all().order_by("host").values("host", "port", "status"))
    for db in dbList:
        db["status"] = check_status(db["host"], db["port"], 0)[0]
    return HttpResponse(content_type="application/json", content=json.dumps(dbList))


def get_keys(request):
    host, port, db = get_host(request)
    status, webRedisCli = check_status(host, port, db)
    keyList = None
    if status == "T":
        keyList = webRedisCli.keys()
    else:
        keyList = "F"
    print(keyList)
    return HttpResponse(content_type="application/json", content=json.dumps(keyList))
