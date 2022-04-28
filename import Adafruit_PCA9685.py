import Adafruit_PCA9685
import time


# 設定周波数（Hz）
SET_FREQ = 50

#変数の設定
a = 1
b = 1
i = 0

# LED接続ポート設定
LED_0 = 0
LED_1 = 1

# 点滅設定
WINKER_INTERVAL = 1.0
winker_status = 'on'

# Adafruit_PCA9685初期化
PCA9685 = Adafruit_PCA9685.PCA9685()
PCA9685.set_pwm_freq(SET_FREQ)

#点灯のみ
#PCA9685.set_pwm(LED_0, 0, 4095)
#PCA9685.set_pwm(LED_1, 0, 4095)

#だんだん明るくなる
while i < 4090:
    i += 2
    print(i)
    a += 1
    b += 1
    PCA9685.set_pwm(LED_0, 0, a)
    PCA9685.set_pwm(LED_1, 0, b)