interf =[{'interface': 'Ethernet0', 'ip': '1.1.1.1', 'status': 'up'},
        {'interface': 'Ethernet1', 'ip': '2.2.2.2', 'status': 'down'},
        {'interface': 'Serial0', 'ip': '3.3.3.3', 'status': 'up'},
        {'interface': 'Serial1', 'ip': '4.4.4.4', 'status': 'up'}]

print(f'Total interf: {len(interf)}')
print(f'{interf[1]["interface"]}: {interf[1]}')
print(f'Статус интерфйеса {interf[-1]["interface"]} : {interf[-1]["status"]}')

interf[0].setdefault('notes','need to reset')
print(interf[0])


interf.append({'interface': 'Ethernet2', 'ip': interf[2]['ip'], 'status': 'up'})
interf[2]['ip'] = '3.3.3.4'

print(interf[0]['notes'])
del interf[0]['notes']

interf[-1]['satus'] = 'down'
print(interf)
interf.pop(-1)

print(interf)
