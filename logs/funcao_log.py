from datetime import datetime

global log_msg
log_msg = str(datetime.now())
def log_script(texto):
    global log_msg
    print(texto)
    log_msg += '\n'
    log_msg += texto
    return log_msg

def salvar_log():
    timestamp_log = str(datetime.now()).replace('.','').replace(':','').replace(' ','').replace('-','')
    arquivo_log = open(r'log_{}.log'.format(timestamp_log),'w')
    arquivo_log.write(log_script( 'Arquivo log salvo.'))
    arquivo_log.close()