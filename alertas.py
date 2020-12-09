import apizabbix, urllib3
urllib3.disable_warnings() 
from datetime import datetime

api = apizabbix.connect()

hostgroups = api.hostgroup.get(
    output=['id'],
    filter={
        'name': ' '
    },
)
events = api.event.get(
    output=[
        'clock',
        'value',
    ],
    groupids=hostgroups[0]['groupid'],
)
triggers = api.trigger.get ({
    'output':[
        'description',
        'priority'], 
})
severidades = [
    'Não classificada',
    'Informação',
    'Atenção',
    'Média',
    'Alta',
    'Desastre'
]
for event in events:
    hora_evento = datetime.fromtimestamp(
        int(event['clock'])).strftime('%Y-%m-%d %H:%M:%S')
    for trigger in triggers: 
        severidade = severidades[(int(trigger['priority']))]
        print('Trigger: ' + trigger['description'] + '\nAlertado em: ' + hora_evento + '\nSeveridade: ' + severidade)      
api.user.logout()
