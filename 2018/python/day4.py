#!/usr/bin/env python3

from collections import defaultdict
from datetime import datetime, timedelta
import re
from operator import *
from itertools import *
from functools import *

working = 1
sleeping = 2

d = defaultdict(int)

relevant = defaultdict(list)

# ekkmeingott how nasty
def load():
    with open("../data/day4.input") as fd:
        guard = None
        last_ts = None
        asleep = 0
        for ts, action in sorted(re.findall("\[([^]]+)\] (.+)", fd.read())):
            timestamp = datetime.strptime(ts, "%Y-%m-%d %H:%M")
            if 'Guard' in action:
                if guard is not None:
                    d[guard] += asleep
                    asleep = 0
                guard = int(re.findall("[^\d]+(\d+) .+", action)[0])
            elif 'wakes up' in action:
                if last_ts.hour == 0:
                    asleep += timestamp.minute - last_ts.minute
                    relevant[guard].extend([x for x in range(last_ts.minute, timestamp.minute)])
                else:
                    asleep += 60 - timestamp.minute
                    relevant[guard].extend([x for x in range(0, timestamp.minute)])

            elif 'asleep' in action:
                pass
            else:
                raise SystemExit
            last_ts = timestamp
            print(timestamp.hour, timestamp.minute)

load()
minutes_by_ids = list(sorted(d.items(), key=itemgetter(1)))

r = defaultdict(int)
for x in relevant[minutes_by_ids[-1][0]]:
    r[x] += 1

selected_id = list(sorted(r.items(), key=itemgetter(1)))

print("Hoo")
print(minutes_by_ids[-1][0])
print(selected_id[-1][0])
print("heee")
print((minutes_by_ids[-1][0] * selected_id[-1][0]) == 98680)

f = defaultdict(list)
for guard, mins in relevant.items():
    for minute, times in sorted([(x,len(list(y))) for x,y in groupby(sorted(mins))], reverse=True, key=itemgetter(1)):
        f[minute].append((guard, times))

s = []
for k,v in f.items():
    guard, times = sorted(v, key=itemgetter(1), reverse=True)[0]
    s.append((k, guard, times))

minute, guard, times = sorted(s, key=itemgetter(2), reverse=True)[0]
print(minute, guard)
print((minute * guard) == 9763)
