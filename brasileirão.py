times = ('FLAMENGO','SANTOS', 'PALMEIRAS', 'GRÊMIO', 'ATHLETICO', 'SÃO PAULO', 'INTERNACIONAL', 'CORINTHIANS', 'FORTALEZA', 'GOIÁS', 'BAHIA', 'VASCO', 'ATLÉTICO-MG', 'FLUMINENSE', 'BOTAFOGO', 'CEARÁ', 'CRUZEIRO', 'CSA', 'CHAPECOENSE', 'AVAÍ',)
print (times[:5])
ultimos = len(times)-4
print (times[ultimos:])
print (sorted(times))
print (times.index('CHAPECOENSE')+1)