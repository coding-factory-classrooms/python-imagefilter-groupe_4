from datetime import datetime

log_file = 'imagefilter.log'


def log(msg):
    now = datetime.now()
    timestamp = now.strftime('%d/%m/%Y %H:%M:%S')
    formatted = f'{timestamp} = {msg}'
    with open(log_file, 'a') as f:
        f.write(formatted + '\n')


def dump_log():
    with open(log_file, 'r') as f:
<<<<<<< HEAD
        print(f.read())

log("salut")
dump_log()
=======
        print(f.read())
>>>>>>> fe2291ae51e7f8953820488a7eab7aab290ef6a6
