# server
import time
import urllib2
import socket
import json
import os
import platform
import sys

win = False
if platform.system() == 'Windows':
    win = True

address = ('0.0.0.0', 10202)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(address)
s.listen(5)


def execute(message):
    data = json.loads(message)
    print(json.dumps(data, indent=4))
    # data = json.loads(request.get_data())
    # print(data)
    res = []
    for cmd in data['cmds']:
        cmd_lines = cmd.split('\n')
        for line in cmd_lines:
            line_res = os.popen(line.encode('utf8'))
            read = line_res.read()
            res.append(read.decode('gbk').encode('utf8') if win else read)
            line_res.close()
    print(json.dumps(res, indent=4))
    return json.dumps(res, indent=4)


def onMessage(message, ss):
    print message
    ss.send(execute(message))


not_register = True
manager_host = '192.168.42.167'
manager_port = '8080'
print sys.argv

while not_register:
    mes = 'register to manager '+manager_host+' : '+manager_port
    print mes
    try:
        url = ''.join(['http://', manager_host,
                       ':', manager_port, '/register'])
        print url
        rq = urllib2.Request(url)
        rs = urllib2.urlopen(rq).read()
        print rs
        if rs == '200':
            not_register = False
            break
    except Exception as identifier:
        print 'Exception : ', identifier
    time.sleep(5)


while True:
    try:
        # print 'Wait conn...'
        ss, addr = s.accept()
        print 'got connected from', addr
        read = ss.recv(4096)
        if read.strip() == 'quit':
            ss.send('node closing.')
            break
        else:
            onMessage(read, ss)
            # print 'end'
    except Exception as e:
        print e
    finally:
        ss.close()
s.close()
