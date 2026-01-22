import random
import time
import pandas as pd

def get_temperature():
    return round(random.uniform(20.0, 35.0), 2)  # 模拟温度20-35℃

def get_humidity():
    return round(random.uniform(40.0, 80.0), 2)   # 模拟湿度40-80%

# 初始化列表存储5次采集的温度和湿度
temperatures = []
humidities = []

print("模拟物联网传感器数据：")

for i in range(5):  # 采集5次
    temp = get_temperature()
    hum = get_humidity()
    # 将每次采集的数值存入对应列表
    temperatures.append(temp)
    humidities.append(hum)
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
    print("湿度范围测试通过!")

test_humidity_range()

data = {
    "采集次数":[1,2,3,4,5],
    "温度":temperatures,
    "湿度":humidities,
}
df = pd.DataFrame(data)
df.to_csv("D:/Project/pythonProject/Git/learn_data.csv", index=False, encoding='utf-8')
print("\n生成的传感器数据表格：")
print(df)