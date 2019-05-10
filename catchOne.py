#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import json
from io import StringIO
import time

print('fuxk you ')
COURSE_KEY='9f7f736f01cb1c28'
COMM_HEADERS={
        'Cookie':'liveChatId=zMtE3FJEf; liveChatAccount=yk_zMtE3FJEf; liveChatName=%E6%B8%B8%E5%AE%A2_zMtE3FJEf; liveChatLogin=0; Hm_lvt_f1d3b48491a1ba98688c81e330d19117=1555670285,1557123142,1557123179; Hm_lpvt_f1d3b48491a1ba98688c81e330d19117=1557125313',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Host':'www.eeo.cn',
        'Referer':'https://www.eeo.cn/webcast.php?courseKey=9f7f736f01cb1c28&lessonid=35287165',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'Origin':'https://www.eeo.cn',
}

pg1 = requests.post(url='https://www.eeo.cn/ajax/webcast.ajax.php?action=getLessonList',
                    data={
                        'courseKey': COURSE_KEY
                    }
                    , headers=COMM_HEADERS)
print(pg1.content)
lessonList=json.loads(pg1.content)
time.sleep(1)
for lesson in lessonList['lessonList']:
    print(lesson)
    pg2 = requests.post(url='https://www.eeo.cn/ajax/webcast.ajax.php?action=getLessonInfo',
                      data={
                          'lessonId':lesson['lessonId'],
                          'courseKey':COURSE_KEY
                      }
                      ,headers=COMM_HEADERS )
    print((pg2.content))
    objOnce = json.loads(pg2.content)
    if not objOnce is None:
        for vod in objOnce['vodList']:
            print(objOnce['vodList'][vod])
    time.sleep(1)
