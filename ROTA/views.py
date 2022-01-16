from django.shortcuts import render,HttpResponse

from django.shortcuts import render, HttpResponse
import datetime
import calendar
from rest_framework.decorators import api_view
from rest_framework.response import Response


def next(date_time_obj,type,group):
    date_time_obj=date_time_obj+datetime.timedelta(days=1)
    s = datetime.date(day=1, year=2020, month=1)
    a = (date_time_obj.date())
    c = 0
    l = ["Morning", "Evening", "Night", "OFF", "General", "Morning", ]
    part = ["Morning", "Evening", "Night", "OFF", "Morning", "Evening", "Night"]


    main = []
    delta = a - s
    deltadays = delta.days
    m23 = type
    if type == "Executive":

        d = {
            s - datetime.timedelta(days=1): "Evening"
        }

        for i in range(deltadays):
            m = d[s - datetime.timedelta(days=1)]
            k = l[l.index(m) + 1]
            d[s] = k
            main += [k]
            s += datetime.timedelta(days=1)

            if k == "OFF":

                d[s] = "General"
                main += ["General"]
                s += datetime.timedelta(days=1)
            else:
                d[s] = k
                main += [k]
                s += datetime.timedelta(days=1)
        k = d[a]
        pop = False
        if k == "General":
            k = "OFF"
            pop = True
        if group == "A":
            s = k
            if pop:
                s = "General"
        if group == "B":
            s = part[part.index(k) + 1]
        if group == "C":
            s = part[part.index(k) + 2]
        if group == "D":
            s = part[part.index(k) + 3]
        return (s)

    else:

        d = {
            s - datetime.timedelta(days=1): "General"
        }

        for i in range(deltadays):
            if calendar.day_name[s.weekday()] == "Sunday":
                m = d[s - datetime.timedelta(days=1)]
                k = l[l.index(m) + 1]
                d[s] = k
                main += [k]

                s += datetime.timedelta(days=1)

                d[s] = k
                main += [k]
                s += datetime.timedelta(days=1)
                if k == "OFF":

                    d[s] = "General"
                    main += ["General"]
                    s += datetime.timedelta(days=1)
                else:
                    d[s] = k
                    main += [k]
                    s += datetime.timedelta(days=1)

            else:
                m = d[s - datetime.timedelta(days=1)]
                k = l[l.index(m) + 1]
                d[s] = k
                main += [k]
                s += datetime.timedelta(days=1)

                if k == "OFF":

                    d[s] = "General"
                    main += ["General"]
                    s += datetime.timedelta(days=1)
                else:
                    d[s] = k
                    main += [k]
                    s += datetime.timedelta(days=1)

        k = d[a]
        if k == "General":
            k = "OFF"
            pop = True
        if group == "A":
            s = k

        if group == "B":
            s = part[part.index(k) + 1]
        if group == "C":
            s = part[part.index(k) + 2]
        if group == "D":
            s = part[part.index(k) + 3]

        if s == "OFF" and date_time_obj.weekday() % 2 != 0:
            s = "General"


        return  s
def shift(date_time_str,type,group):
    s = datetime.date(day=1, year=2020, month=1)

    date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d')

    a = (date_time_obj.date())
    c = 0
    flag=True
    l = ["Morning", "Evening", "Night", "OFF", "General", "Morning", ]
    part = ["Morning", "Evening", "Night", "OFF", "Morning", "Evening", "Night"]


    main = []
    delta = a - s
    deltadays = delta.days
    m23 = type
    if type == "Executive":

        d = {
            s - datetime.timedelta(days=1): "Evening"
        }

        for i in range(deltadays):
            m = d[s - datetime.timedelta(days=1)]
            k = l[l.index(m) + 1]
            d[s] = k
            main += [k]
            s += datetime.timedelta(days=1)

            if k == "OFF":

                d[s] = "General"
                main += ["General"]
                s += datetime.timedelta(days=1)
            else:
                d[s] = k
                main += [k]
                s += datetime.timedelta(days=1)
        k = d[a]
        pop = False
        if k == "General":
            k = "OFF"
            pop = True
        if group == "A":
            s = k
            if pop:
                s = "General"
        if group == "B":
            s = part[part.index(k) + 1]
        if group == "C":
            s = part[part.index(k) + 2]
        if group == "D":
            s = part[part.index(k) + 3]
        if next(date_time_obj,type=type,group=group)=="Morning" and s=="OFF":
            s="General"
        return s

    else:

        d = {
            s - datetime.timedelta(days=1): "General"
        }

        for i in range(deltadays):
            if calendar.day_name[s.weekday()] == "Sunday":
                m = d[s - datetime.timedelta(days=1)]
                k = l[l.index(m) + 1]
                d[s] = k
                main += [k]

                s += datetime.timedelta(days=1)

                d[s] = k
                main += [k]
                s += datetime.timedelta(days=1)
                if k == "OFF":

                    d[s] = "General"
                    main += ["General"]
                    s += datetime.timedelta(days=1)
                else:
                    d[s] = k
                    main += [k]
                    s += datetime.timedelta(days=1)

            else:
                m = d[s - datetime.timedelta(days=1)]
                k = l[l.index(m) + 1]
                d[s] = k
                main += [k]
                s += datetime.timedelta(days=1)

                if k == "OFF":

                    d[s] = "General"
                    main += ["General"]
                    s += datetime.timedelta(days=1)
                else:
                    d[s] = k
                    main += [k]
                    s += datetime.timedelta(days=1)

        k = d[a]
        if k == "General":
            k = "OFF"
            pop = True
        if group == "A":
            s = k

        if group == "B":
            s = part[part.index(k) + 1]
        if group == "C":
            s = part[part.index(k) + 2]
        if group == "D":
            s = part[part.index(k) + 3]

        if s == "OFF" and date_time_obj.weekday() % 2 != 0:
            s = "General"
        u = date_time_str

        if next(date_time_obj,type=type,group=group) == "Morning" and s=="OFF":
            s = "General"
        return s


@api_view(['GET'])
def index(request,pk):
    flag="Tatwas"
    if request.method == "GET":

        date_time_str = pk

        try:
            date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d')


            executive=[shift(date_time_str,group="A",type="Executive")]
            executive+=[shift(date_time_str,group="B",type="Executive")]
            executive+=[shift(date_time_str,group="C",type="Executive")]
            executive+=[shift(date_time_str,group="D",type="Executive")]
            nonexecutive=[shift(date_time_str,group="A",type="ne")]
            nonexecutive+=[shift(date_time_str,group="B",type="ne")]
            nonexecutive+=[shift(date_time_str,group="C",type="ne")]
            nonexecutive+=[shift(date_time_str,group="D",type="ne")]
            flag=False
            return Response({"ea":executive[0],"eb":executive[1],"ec":executive[2],"ed":executive[3],"na":nonexecutive[0],"nb":nonexecutive[1],"nc":nonexecutive[2],"nd":nonexecutive[3],"dateq":date_time_str,"flag":flag})
        except:
            flag=True
            s="Please Enter date after 01-01-2020"
            return Response({"s":s,"dateq":date_time_str,"flag":flag})





    return (Response({"flag":flag}))