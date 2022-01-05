import os
import time
import zipfile

sourse = ['C:\\Обмен', 'C:\\Distr']

target_dir = 'D:\\Temp'

today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

comment = input('Введите коментарий --> ')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print('каталог успешно создан')

zip_command = f"zip -qr {target} {' '.join(sourse)}"

if os.system(zip_command) == 0:
    print('Все норм')
else:
    print('Не получилось')
