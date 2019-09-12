"""Setup."""


from setuptools import setup

with open('README.md') as f:
    long_description = f.read()  # pylint: disable=invalid-name

TEST_DEPS = [
    'pytest',
    'mock',
]

EXTRAS = {
    'test': TEST_DEPS,
}

VERSION = '0.1.2'

setup(
    author='SSC Pacific',
    name='statick-tex',
    description='Tool for running static analysis tools against TeX/LaTeX.',
    version=VERSION,
    packages=['statick_tool',
              'statick_tool.plugins.discovery',
              'statick_tool.plugins.tool'],
    package_dir={'statick_tool': '.',
                 'statick_tool.plugins.discovery':
                 'plugins/tex_discovery_plugin',
                 'statick_tool.plugins.tool':
                 'plugins/tex_tool_plugins'},
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
        "Topic :: Software Development :: Testing",
    ],
)
