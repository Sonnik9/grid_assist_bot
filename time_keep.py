import time

def kline_waiter(interval):
    wait_time = 0  
    interval = interval.strip()
    kline_time, time_frame = float(interval.split('/')[0].strip()), interval.split('/')[1].strip()

    if time_frame == 'm':
        wait_time = ((60*kline_time) - (time.time()%60) + 1)
    elif time_frame == 'h':
        wait_time = ((3600*kline_time) - (time.time()%3600) + 1)
    elif time_frame == 'd':
        wait_time = ((86400*kline_time) - (time.time()%86400) + 1)

    return str(round((wait_time / 60), 2)) + ' ' + 'minut'

# python -m UTILS.wait_candle