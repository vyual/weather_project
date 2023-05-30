import socket
import subprocess


def check_available_memory():
    output = subprocess.check_output(['free', '-h']).decode('utf-8')
    memory_info = output.split('\n')[1].split()[1:]
    total, used, free, shared, buff_cache, available = memory_info
    data = {
        'total': total,
        'used': used,
        'free': free,
        'shared': shared,
        'buff_cache': buff_cache,
        'available': available
    }
    return data


def run_server():
    server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    server.bind('/tmp/weather_socket')
    server.listen(1)
    print('Listening on Unix socket /tmp/weather_socket...')

    while True:
        connection, _ = server.accept()
        data = check_available_memory()
        connection.send(str(data).encode())
        connection.close()


# python weather_socket.py &
if __name__ == '__main__':
    run_server()

