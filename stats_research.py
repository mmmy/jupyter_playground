import numpy as np


def mock_once(win_rate, times, increase_percent, decrease_percent):
    rand_arr = np.random.random_sample([times, ])
    base = 100
    fund = base
    for v in rand_arr:
        if v < win_rate:
            fund = fund + base * increase_percent
        else:
            fund = fund + base * decrease_percent
        if fund <= 0:
            break
    return fund


sample_size = 100000
results = []
wins_count = 0

win_rate = 0.6
times = 1000
increase_percent = 1/20
decrease_percent = -(1/20 * 1)

mean_increase_per_time = win_rate * \
    increase_percent + (1-win_rate) * decrease_percent
print('{}%'.format(mean_increase_per_time * 100))

for i in range(sample_size):
    result = mock_once(win_rate, times, increase_percent, decrease_percent)
    if result > 0:
        wins_count = wins_count + 1

    results.append(result)


broken_rate = (sample_size - wins_count) / sample_size

print(sample_size, wins_count, (1 - broken_rate) * 100, broken_rate * 100)
