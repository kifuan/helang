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
    for music in MUSICS:
        count = random.randint(*MUSIC_SIZE_MB_RANGE)
        file = music + random.choice(SUFFIX)
        print(f'    Downloading {file}...')
        for _ in tqdm.tqdm(range(count), file=sys.stdout, total=count, unit='m'):
            # 1ms to 25ms
            time.sleep(random.randint(1, 25) / 1000)
