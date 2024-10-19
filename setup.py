from setuptools import setup, find_packages

VERSION = '0.0.1'

setup(
    name='dlzhcommon',
    version=VERSION,

    description='A common library in dlzhdata',
    long_description=long_description,
    author='Zihan Eric Tang',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',

        'Environment :: Console',

        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',

        'License :: OSI Approved :: MIT License',

        'Operating System :: OS Independent',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],

    packages=find_packages('.'),
    python_requires='>=3.6, <4',
    install_requires=[
        'pandas',
        'numpy',
    ],
)
