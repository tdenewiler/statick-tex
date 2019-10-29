"""Setup."""


from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()  # pylint: disable=invalid-name

TEST_DEPS = [
    'mock',
    'pytest',
]

EXTRAS = {
    'test': TEST_DEPS,
}

setup(
    author='Thomas Denewiler',
    name='statick_tool',
    description='Statick analysis plugins for TeX/LaTeX files and projects.',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    package_data={'statick_tool': ['rsc/*'],
                  'statick_tool.plugins.discovery':
                  ['*.yapsy-plugin'],
                  'statick_tool.plugins.tool':
                  ['*.yapsy-plugin']},
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=['statick'],
    tests_require=TEST_DEPS,
    extras_require=EXTRAS,
    url='https://github.com/tdenewiler/statick-tex',
    classifiers=[
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Testing",
    ],
)
