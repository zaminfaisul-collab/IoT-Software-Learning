import random
import time
import pandas as pd

def get_temperature():
    return round(random.uniform(20.0, 35.0), 2)  # 模拟温度20-35℃

def get_humidity():
    return round(random.uniform(40.0, 80.0), 2)   # 模拟湿度40-80%

print("模拟物联网传感器数据：")

for i in range(5):  # 采集5次
    temp = get_temperature()
    hum = get_humidity()
    print(f"第{i+1}次采集 -> 温度: {temp}℃, 湿度: {hum}%")
    time.sleep(1)  # 每秒采集一次

def test_temperature_range():
    temp = get_temperature()
    assert 20.0 <= temp <= 35.0, f"温度超出范围: {temp}"
    print("温度范围测试通过！")

test_temperature_range()

def test_humidity_range():
    hum = get_humidity()
    assert 40.0 <= hum <= 80.0,f"湿度超出范围：{hum}"
    print("湿度范围测试通过")

test_humidity_range()
