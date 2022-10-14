
queries = {
    "cmd1": str,
    "value1": str,
}, {
    "cmd2": str,
    "value3": str,
}


qr = {}

qr['dic'] = list(queries)

for d in qr:
    a = d['cmd1']
    print(a)

