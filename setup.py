from setuptools import setup,find_packages

setup(
    name = 'helang',
    version = '1.0.0',
    author = 'kifuan',
    packages = find_packages(),
    install_requires = [
        'tqdm'
        'pytest'
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'helang = helang.__main__:_main',
        ]
    },
)
