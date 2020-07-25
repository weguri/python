import time
import datetime

print("time.localtime:", time.localtime())

print()
print("Segundo: %d:%d:%d" % (time.localtime().tm_hour,
                             time.localtime().tm_min,
                             time.localtime().tm_sec))

time.sleep(1)

print()
print("time.asctime:", time.asctime())

print()
data_hora = datetime.datetime(2020, 7, 8, 18, 12, 9)
print("Data:", data_hora.date())
print("hora:", data_hora.time())

print()
for Segundo in range(3):
    time.sleep(1)
    print("%d Segundo" % Segundo)
