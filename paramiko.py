import paramiko

try:
    client = paramiko.client.SSHClient()
    client.load_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('127.0.01',
                    username='developer',
                    password='4linux',
                    port='2222')

except Exception as e:
    print(f'Erro conexão: {e}')
    exit()

    