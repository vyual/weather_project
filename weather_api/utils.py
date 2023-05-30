import subprocess
import datetime


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
        'available': available,
        'date': datetime.datetime.now().isoformat()
    }
    return data
