# Copyright 2024 Evgenchick4434 (https://github.com/Evgenchick4434)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from config import Changelist


Version = 'V1.2 Beta'

changelist = f'''
          [+] Добавил функцию нажатия на кнопки
          [+] Добавил аналитику за день для крипты и фиатных валют
          [+] Добавил генерацию QR и штрих кодов
          [/] Фикснул ещё несколько крашей
'''

if Changelist == True:
     logo = f'''
╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╭╮╭╮
┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╭╯╰╮╱╱╱╱┃┃┃┃
┃╰━╯┣━━╮╭━━┳━━┳━╋╮╭╋━┳━━┫┃┃┃╭━━┳━╮
┃╭━━┫╭━╯┃╭━┫╭╮┃╭╮┫┃┃╭┫╭╮┃┃┃┃┃┃━┫╭╯
┃┃╱╱┃╰━╮┃╰━┫╰╯┃┃┃┃╰┫┃┃╰╯┃╰┫╰┫┃━┫┃
╰╯╱╱╰━━╯╰━━┻━━┻╯╰┻━┻╯╰━━┻━┻━┻━━┻╯
     {Version} by Evgenchick4434 & Georgyrs:
     {changelist}
     '''
else:
     logo = f'''
╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╭╮╭╮
┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╭╯╰╮╱╱╱╱┃┃┃┃
┃╰━╯┣━━╮╭━━┳━━┳━╋╮╭╋━┳━━┫┃┃┃╭━━┳━╮
┃╭━━┫╭━╯┃╭━┫╭╮┃╭╮┫┃┃╭┫╭╮┃┃┃┃┃┃━┫╭╯
┃┃╱╱┃╰━╮┃╰━┫╰╯┃┃┃┃╰┫┃┃╰╯┃╰┫╰┫┃━┫┃
╰╯╱╱╰━━╯╰━━┻━━┻╯╰┻━┻╯╰━━┻━┻━┻━━┻╯
     {Version} by Evgenchick4434 & Georgyrs
          '''