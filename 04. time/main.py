import time

# time starts from 1.1.1970 called "epoch"

epoch_time = time.time()
print(epoch_time)

y = time.ctime(1668049947.297472)  # default, ctime()= ctime(time.time())
print(y)
