import socket

target_host = "localhost"
target_port = 9998

#ソケットオブジェクトの作成
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#サーバへ接続
client.connect((target_host,target_port))

#データの送信
client.send(b"test")

#データの受信
response = client.recv(4096)

print(response.decode())

client.close()