from setuptools import setup

setup(
    name='DSBPsychose',
    version='0.1',
    description='Erneuerte API für DSBMobile.',
    long_description='API für DSBMobile welche es ermöglicht Daten aus DSBMobile Stundenplänen zu extrahieren. ',
    url='https://github.com/deinBenutzername/DSBApi',
    author='Dein Name',
    author_email='deine@email.com',
    license='MIT',
    packages=['DSBApi'],
    install_requires=['requests', 'beautifulsoup4', 'pillow', 'pytesseract'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],
)
