import tqdm
import time
import random
import sys


MUSICS = (
    'Kill You', 'Lighters', 'ZOOD', 'Love the Way You Lie',
    'The Monster', 'Numb Encore', 'Kinds Never Die', 'I Need a Doctor',
    'Lose Yourself', 'Mockingbird', 'Beautiful', 'Not Afraid',
    'Rap God', 'Phenomenal', 'Stan', 'Space Bound', 'Stan',
    'Guts Over Fear', 'Spade'
)

SUFFIXES = (
    '.mp3', '.ogg', '.flac'
)

MUSIC_SIZE_MB_RANGE = (10, 30)


APPS = (
    'Genshin Impact v3.0',
    'Arknights v1861',
    'Hetellij IDEA v2021.1',
    'Henity 3D v2022.1.13',
    'Hereal Engine v5.0.0',
)

APPS_SIZE_MB_RANGE = (16 * 1024, 30 * 1024)


SUMMARY_STRING = '''
=== HeLang protects your every pure download ===
Data used | {size}{unit}
Downloaded files | {count}
Location | BUPT Xitucheng Campus

=== HeLang protects your pure disk memory ===
All test files were deleted
Data freed | {size}{unit}
Deleted files | {count}
Location | BUPT Xitucheng Campus

5G speed test finished.
'''.strip()


def run_speed_test_music():
    print('Cyber DJ is downloading apps via 5G...')
    total_size = 0
    for music in MUSICS:
        curr_size = random.randint(*MUSIC_SIZE_MB_RANGE)
        file = music + random.choice(SUFFIXES)
        vip_suffix = '' if music == 'ZOOD' else ' [VIP]'
        print()
        print(f'    Downloading {file}...{vip_suffix}')
        for _ in tqdm.tqdm(range(curr_size), file=sys.stdout, total=curr_size, unit='MB'):
            # 1ms to 10ms
            time.sleep(random.randint(1, 10) / 1000)
        time.sleep(random.randint(30, 70) / 1000)
        total_size += curr_size
    print()
    print(SUMMARY_STRING.format(size=total_size, count=len(MUSICS), unit='MB'))


def run_speed_test_app():
    print('Cyber DJ is downloading apps via 5G...')
    print('Your VIP level: E-SMOKER-KING. Speeding up by 102400%...')
    total_size = 0
    for app in APPS:
        curr_size = random.randint(*APPS_SIZE_MB_RANGE) // 1024
        print()
        print(f'    Downloading {app}...')
        for _ in tqdm.tqdm(range(curr_size), file=sys.stdout, total=curr_size, unit='GB'):
            # 1ms to 10ms
            time.sleep(random.randint(1, 10) / 1000)
        time.sleep(random.randint(30, 70) / 1000)
        total_size += curr_size
    print()
    print(SUMMARY_STRING.format(size=total_size, count=len(APPS), unit='GB'))
