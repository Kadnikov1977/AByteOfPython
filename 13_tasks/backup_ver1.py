import os
import time

sourse = ['C:\\Distr', 'C:\\Обмен']

target_dir = 'D:\\Temp'

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = "zip -qr " + target + ' ' + sourse[0] + ' ' + sourse[1]

print(zip_command)

if os.system(zip_command) == 0:
    print('Ok')
else:
    print('No')

