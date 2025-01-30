import multiprocessing
import psutil
import subprocess
from collections import defaultdict

def get_stats():
    n_cpus = multiprocessing.cpu_count()
    out = subprocess.check_output(['top', '-b', '-n1', '-e', 'g']).decode('utf-8').split('\n')[7:-1]
    cpu = defaultdict(float)
    mem = defaultdict(float)
    for line in out:
        line = line.split()
        user = line[1]
        
        cpu[user] += float(line[8]) / n_cpus
        mem[user] += float(line[9])

    return {
        'n_cpus': n_cpus,
        'total_mem': psutil.virtual_memory().total / 1024**3,
        'cpu_usage': dict(cpu),
        'mem_usage': dict(mem),
    }
if __name__ == '__main__':
    print(get_stats())


