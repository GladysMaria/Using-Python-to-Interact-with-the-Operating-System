host = [['work.local', '192.168.25.46'], ['web.cloud', '10.2.5.6']]
with open('host.csv', 'w') as host_csv:
    writer = csv.writer(host_csv)
    writer.writerows(host)