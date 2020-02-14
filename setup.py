from setuptools import setup, find_packages

setup(
    name='epic-path',
    version='0.0.2',
    url='https://github.com/ValentinVignal/EpicPath.git',
    license='MIT',
    author='Valentin Vignal',
    author_email='valentin.vignal.dev@outlook.fr',
    description='A simple high level library to work with Path',
    packages=find_packages(exclude=['tests', 'trash']),
    long_description=open('README.md').read(),
    zip_safe=False
)