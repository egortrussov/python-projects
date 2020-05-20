import subprocess

a = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('cp866').split('\n')

a = [i.split(':')[1][1:-1] for i in a if "Все профили пользователей" in i]

for i in a:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('cp866').split('\n')

    results = [b.split(':')[1][1:-1] for b in results if "Содержимое ключа" in b]

    try:
        print("{:<30}: {:<}".format(i, results[0]))
    except IndexError:
        print("{:<30}: {:<}".format(i, ''))