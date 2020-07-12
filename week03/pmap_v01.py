# from ping3 import ping

from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import argparse
import json
import os
from itertools import product


def ping(ip):
    res = os.system(f"ping -c 1 -t 3000 {ip}")
    if res == 0:
        return ip
    else:
        print(f"=========此前ip: {ip} ping不通==========")
        return None


def ping_port(ip, port):
    response = os.system(f"nc -v -z {ip} {port}")
    if response == 0:
        print(f"=========主机 {ip} 端口{port} opened ==========")
        return port
        # return ip + ":" + str(port)
    else:
        # print(f"=========主机 {ip} 端口{port} closed ==========")
        return None


def ping_port_wrapper(t):
    (ip, port) = t
    return ping_port(ip, port)


def parse_ip_range(ip_range):
    hosts = []
    ips = ip_range.split('-')
    firstIPsplit = ips[0].split('.')
    lastIPsplit = ips[-1].split('.')
    # print(ips)
    cnt = int(lastIPsplit[-1]) - int(firstIPsplit[-1]) + 1

    for i in range(cnt):
        fourth = int(firstIPsplit[-1]) + i
        host = firstIPsplit[0] + "." + firstIPsplit[1] + "." + firstIPsplit[2] + "." + str(fourth)
        hosts.append(host)

    return hosts


def write_file(data, file_name):
    with open(file_name, 'w') as outfile:
        json.dump(data, outfile)


def main():
    p = argparse.ArgumentParser(description="Port Scanner")
    p.add_argument('-ip', required=True, help='ip address', type=str)
    p.add_argument('-n', default=8, help='concurrent counts', type=int)
    p.add_argument('-f', choices=['ping', 'tcp'], default='tcp', help="'only 'ping' or 'tcp'", type=str)
    p.add_argument('-w', help='save result', type=str)
    p.add_argument('-m', choices=['proc', 'thread'], default='proc', help='multiprocess or multiThread',
                   required=False)
    p.add_argument('-v', action='count', default=0, help='show elapsed time')

    args = p.parse_args()
    workers = args.n
    model = args.m
    ip_list = parse_ip_range(args.ip)

    if model == 'proc':
        Pool = ProcessPoolExecutor
    else:
        Pool = ThreadPoolExecutor

    results = {}
    if args.f == "tcp":
        for ip in ip_list:
            data = product([ip], range(1023, 65535))
            # data = product([ip], range(8000, 8081))
            with Pool(workers) as pool:
                raw_results = pool.map(ping_port_wrapper, data)

            mid_results = [r for r in raw_results if r is not None]
            if len(mid_results):
                results[ip] = sorted(mid_results)

    elif args.f == "ping":
        with Pool(workers) as pool:
            raw_results = pool.map(ping, ip_list)
        results = [r for r in raw_results if r is not None]

    print("=============================================================================================")
    print(results)
    if args.w:
        write_file(results, args.w)


if __name__ == '__main__':
    main()
