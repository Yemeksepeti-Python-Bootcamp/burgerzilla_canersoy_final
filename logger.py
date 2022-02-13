from datetime import datetime

def logEvent(log):
    file_object = open('logs.txt','a')
    file_object.write(f"{datetime.now().strftime('%B %d %Y - %H:%M:%S')} {log}\n")
    file_object.close()