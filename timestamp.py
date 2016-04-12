import datetime
import sys

now = datetime.datetime.now();
before = datetime.datetime(
    now.year,now.month,now.day,
    int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))
print(now-before)
