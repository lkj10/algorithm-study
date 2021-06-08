import sys

log = {}

for _ in range(int(sys.stdin.readline())):
    name, attr = sys.stdin.readline().rstrip().split()
    if attr == 'enter':
        log[name] = 'enter'
    else:
        if log[name]:
            del log[name]

for person in sorted(log, reverse=True):
  print(person)
