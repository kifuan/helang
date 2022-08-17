import tqdm
import time
import random
import sys

MUSICS = [
    'Kill You', 'Lighters', 'ZOOD', 'Love the Way You Lie',
    'The Monster', 'Numb Encore', 'Kinds Never Die', 'I Need a Doctor',
    'Lose Yourself', 'Mockingbird', 'Beautiful', 'Not Afraid',
    'Rap God', 'Phenomenal', 'Stan', 'Space Bound', 'Stan',
    'Guts Over Fear', 'Spade'
]

SUFFIX = [
    '.mp3', '.ogg', '.flac'
]


MUSIC_SIZE_MB_RANGE = (10, 30)


def run_speed_test():
    print('Cyber DJ is downloading musics via 5G...')
    random.shuffle(MUSICS)
    countAll = 0
    for music in MUSICS:
        count = random.randint(*MUSIC_SIZE_MB_RANGE)
        file = music + random.choice(SUFFIX)
        print('-----')
        if music == 'ZOOD':
            print(f'Downloading {file}...')
        else:
            print(f'Downloading {file}...' + ' [VIP]')
        print('Calculating the size of the file...\r', end="")
        time.sleep(random.randint(100, 200) / 1000)
        for _ in tqdm.tqdm(range(count), file=sys.stdout, total=count, unit='MB'):
            # 1ms to 10ms
            time.sleep(random.randint(1, 10) / 1000)
        time.sleep(random.randint(30, 70) / 1000)
        countAll += count
    print(f'''\n===HELANG protect your every pure download===
Data used | {countAll}MB
Download files | {len(MUSICS)}
Location | BUPT Xitucheng Campus
=============================================''')
