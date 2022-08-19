import tqdm
import time
import random
import sys
from .exceptions import BadStatementException

MUSICS = [
    'Kill You', 'Lighters', 'ZOOD', 'Love the Way You Lie',
    'The Monster', 'Numb Encore', 'Kinds Never Die', 'I Need a Doctor',
    'Lose Yourself', 'Mockingbird', 'Beautiful', 'Not Afraid',
    'Rap God', 'Phenomenal', 'Stan', 'Space Bound', 'Stan',
    'Guts Over Fear', 'Spade'
]

SUFFIXES = [
    '.mp3', '.ogg', '.flac'
]

MUSIC_SIZE_MB_RANGE = (10, 30)


APPS = [
    'Apple Store', 'Speedtest'
    ]

APPS_VER = [
    "V5.17", "V4.4.3"
    ]

APPS_SIZE = [
    84,	107
    ]


SUMMARY_STRING = '''
=== HeLang protects your every pure download ===
Data used | {}MB
Downloaded files | {}
Location | BUPT Xitucheng Campus

=== HeLang protects your pure disk memory ===
All test files were deleted
Data freed | {}MB
Deleted files | {}
Location | BUPT Xitucheng Campus

5G speed test finished.
'''.strip()


def run_speed_test_music():
    print('Cyber DJ is downloading apps via 5G...')
    random.shuffle(MUSICS)
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
    print(SUMMARY_STRING.format(total_size, len(MUSICS), total_size, len(MUSICS)))


def run_speed_test_app():
    print('Cyber DJ is downloading apps via 5G...')
    total_size = 0
    for app in APPS:
        curr_size = APPS_SIZE[APPS.index(app)]
        file = app + " " + APPS_VER[APPS.index(app)]
        print()
        print(f'    Downloading {file}...')
        for _ in tqdm.tqdm(range(curr_size), file=sys.stdout, total=curr_size, unit='MB'):
            # 1ms to 10ms
            time.sleep(random.randint(1, 10) / 1000)
        time.sleep(random.randint(30, 70) / 1000)
        total_size += curr_size
    print()
    print(SUMMARY_STRING.format(total_size, len(APPS), total_size, len(APPS)))
