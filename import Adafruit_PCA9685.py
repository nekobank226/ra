import Adafruit_PCA9685
import time

# 設定周波数（Hz）
SET_FREQ = 50

# LED接続ポート設定
LED_0 = 0
LED_1 = 1

# 点滅設定
WINKER_INTERVAL = 1.0
winker_status = 'on'

# Adafruit_PCA9685初期化
PCA9685 = Adafruit_PCA9685.PCA9685()
PCA9685.set_pwm_freq(SET_FREQ)

try:
	PCA9685.set_pwm(LED_0, 0, 4095)

	while True:
		if winker_status == 'on':
			PCA9685.set_pwm(LED_1, 0, 4095)
			time.sleep(WINKER_INTERVAL)
			winker_status = 'off'

		elif winker_status == 'off':
			PCA9685.set_pwm(LED_1, 0, 0)
			time.sleep(WINKER_INTERVAL)
			winker_status = 'on'

except KeyboardInterrupt:
	PCA9685.set_pwm(LED_0, 0, 0)
	PCA9685.set_pwm(LED_1, 0, 0)
	print("KeyboardInterrupt")
	pass