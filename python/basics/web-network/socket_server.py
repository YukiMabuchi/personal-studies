import socket

# wellknown port: (0 - 1023)
# 登録済みポート: (1024 - 49151)
# 動的・プライベートポート: (49152 - 65535)

"""
TCP
"""
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # withを使って最後クローズするように
#     s.bind(('127.0.0.1', 50007))
#     s.listen(1)
#     while True:
#         conn, addr = s.accept()
#         with conn:
#             while True:
#                 data = conn.recv(1024)
#                 if not data:
#                     break
#                 print(f'data: {data}, addr: {addr}')
#                 conn.sendall(b'Received: ' + data) # binary

"""
UDP
"""
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(('127.0.0.1', 50007))
    while True:
        data, addr = s.recvfrom(1024)
        print(f'data: {data}, addr: {addr}')