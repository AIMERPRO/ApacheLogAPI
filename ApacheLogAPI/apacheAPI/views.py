from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

import pandas as pd

from apacheAPI.models import Log
from apacheAPI.serializers import LogFileSerializer


class LogFilesViewSet(viewsets.ModelViewSet):
    queryset = Log
    serializer_class = LogFileSerializer


class LogFileParse(APIView):
    def get(self, request):
        url_or_file = "../access.log"

        cols = ['ip', 'l', 'user_id', 'timestamp', 'tz', 'request', 'status', 'bytes', 'referer', 'useragent']

        df = pd.read_csv(url_or_file, delim_whitespace=True, names=cols).drop('l', 1)
        df["timestamp"] = df["timestamp"].str.lstrip("[") + " " + df.pop("tz").str.rstrip("]")

        for row in df.itertuples(index=False):
            log = Log(ip=row[0], user_id=row[1], timestamp=row[2],
                      request=row[3],
                      status=row[4], bytes=row[5], referer=row[6], useragent=row[7])
            log.save()

        return Response({'status': 'OK'})
