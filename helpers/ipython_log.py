# IPython log file

import csv
oemc = [ x for x in csv.DictReader(open('oemc.csv'))]
len(oemc)
#[Out]# 171317
oemcx = oemc[0]
oemcx
#[Out]# {'EventNumber': '2000100015',
#[Out]#  'EntryDate': '01/01/2020 00.00.52',
#[Out]#  'EventType': 'DISTME',
#[Out]#  'TypeDescription': 'MENTAL HEALTH DISTURBANCE',
#[Out]#  'FinalDisposition': '19B',
#[Out]#  'Location': '76XX  S HALSTED ST',
#[Out]#  'CPDUnitList': '621R',
#[Out]#  'CFDUnitList': ''}
oemcx = oemc[279]
oemcx
#[Out]# {'EventNumber': '2000209368',
#[Out]#  'EntryDate': '01/02/2020 15.40.22',
#[Out]#  'EventType': 'SUSPER',
#[Out]#  'TypeDescription': 'SUSPICIOUS PERSON',
#[Out]#  'FinalDisposition': '5BZ',
#[Out]#  'Location': '10XX  W BRYN MAWR AV',
#[Out]#  'CPDUnitList': '2023',
#[Out]#  'CFDUnitList': ''}
loc = oemcx['Location']
loc
#[Out]# '10XX  W BRYN MAWR AV'
locs = loc.split()
locs
#[Out]# ['10XX', 'W', 'BRYN', 'MAWR', 'AV']
locs[0]
#[Out]# '10XX'
locs[0].replace('X','0')
#[Out]# '1000'
locs[1]
#[Out]# 'W'
locs[2]
#[Out]# 'BRYN'
locs[-1]
#[Out]# 'AV'
len(locs)
#[Out]# 5
len(locs)
#[Out]# 5
locs[2:-1]
#[Out]# ['BRYN', 'MAWR']
oemcy = oemc[0]
locy = oemcy['Location']
locys = locy.split()
locys[2:-1]
#[Out]# ['HALSTED']
'@ 1234 XXX'.replace('@ ','')
#[Out]# '1234 XXX'
'1234 XXX'.replace('@ ','')
#[Out]# '1234 XXX'
direction = locy[1]
direction
#[Out]# '6'
direction = locys[1]
direction
#[Out]# 'S'
