from setuptools import setup

def readme():
    with open('README.rst', encoding='utf-8') as f:
        return f.read()

setup(name='fuzzy_grassmann_numbers',
    version='0.1',
    description='Library for the mathematics of Fuzzy Grassmann Numbers.',
    long_description=readme(),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Text Processing :: Linguistic',
    ],
    project_urls={
        'Website': '',
        'Documentation': '',
        'Source': 'https://github.com/caveljan/fuzzy-grassmann-numbers',
        'Tracker': 'https://github.com/caveljan/fuzzy-grassmann-numbers/issues',
    },
    keywords='fuzzy grassmann numbers',
    url='https://github.com/caveljan/fuzzy-grassmann-numbers',
    label='fuzzy grassman numbers',
    author='Jan Cavel',
    author_email='mail@caveljan.com',
    license='MIT',
    packages=['fuzzy_grassmann_numbers'],
    entry_points = {
        'console_scripts': [''],
    },
    python_requires='>=3',
    test_suite='tests',
    tests_require=['py.test'],
    include_package_data=True,
    zip_safe=False)
