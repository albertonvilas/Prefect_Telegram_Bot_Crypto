from time import gmtime, strftime

def date_now():
    date_now =  strftime("%Y-%m-%d %H:%M:%S", gmtime())
    return date_now
    