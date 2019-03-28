import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


def mock_once(win_rate, times, increase_percent, decrease_percent):
    rand_arr = np.random.random_sample([times, ])
    base = 100
    fund = base
    fund_hist = []

    draw_back = 0
    draw_backs = []
    for v in rand_arr:
        if v < win_rate:
            increase = base * increase_percent
            fund = fund + increase
            if draw_back < 0:
                draw_back = draw_back + increase
        else:
            decrease = base * decrease_percent
            fund = fund + decrease
            draw_back = draw_back + decrease
        fund_hist.append(fund)
        draw_backs.append(draw_back)
    return fund_hist, draw_backs


win_rate = 0.6
times = 100000
increase_percent = 1/20
decrease_percent = -(1/20 * 0.9)

max_draw_back_times = -1 / decrease_percent
risk_ruin = ((1 - win_rate) / win_rate) ** round(max_draw_back_times)
print('risk of ruin: {}%'.format(risk_ruin * 100))

mean_increase_per_time = win_rate * \
    increase_percent + (1-win_rate) * decrease_percent
print('{}%'.format(mean_increase_per_time * 100))

result, draw_backs = mock_once(
    win_rate, times, increase_percent, decrease_percent)

xs = range(times)
max_draw_back = min(draw_backs)
print('max draw back {}'.format(max_draw_back))

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 15))
ax1.grid(True)
ax1.plot(xs, result, '-')
ax2.grid(True)
ax2.plot(xs, draw_backs, '-')
# plt.show()
