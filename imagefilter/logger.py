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

        print(f.read())






