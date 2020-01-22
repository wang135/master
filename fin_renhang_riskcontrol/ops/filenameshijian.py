import datetime

def sjijian():
    today = datetime.datetime.today()
    aa = today.strftime("%Y-%m-%d")

    filename =aa+'.log'
    return filename