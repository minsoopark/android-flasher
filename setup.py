from setuptools import setup, find_packages

setup(
    name='android-flasher',
    packages=find_packages(),
    version='1.2',
    description='Flash the Android factory image without removing your data.',
    long_description=open('README.rst').read(),
    license='MIT License',
    author='Minsoo Park',
    author_email='minsoo1003@gmail.com',
    url='https://github.com/minsoopark/android-flasher',
    keywords=['flasher', 'android-flasher'],
    include_package_data=True,
    install_requires=[
        'Click'
    ],
    entry_points='''
        [console_scripts]
        android-flasher = flasher.cli:generate_script
    '''
)

