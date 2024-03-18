from setuptools import setup, find_packages

setup(
    name='DSBPsychose',
    version='0.0.15',
    description='Overworked API for DSBMobile, requires some tweaking but still works.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Tim H.',
    author_email='zfq@tuta.io',
    url='https://github.com/zfqtim/DSBPsychose',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4>=4.9.3',
        'requests>=2.26.0',
        'Pillow>=9.0.0',
        'pytesseract>=0.3.9'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
