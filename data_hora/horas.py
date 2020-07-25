from datetime import datetime

agora = datetime.now()

h = agora.hour
m = agora.minute
s = agora.second


print("%s:%s:%s" % (str(h).zfill(2), str(m).zfill(2), str(s).zfill(2)))
