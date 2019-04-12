"""Setup."""


try:
    from setuptools import setup
except:  # pylint: disable=bare-except # noqa: E722 # NOLINT
    from distutils.core import setup  # pylint: disable=wrong-import-order

with open('README.md') as f:
    long_description = f.read()  # pylint: disable=invalid-name

TEST_DEPS = [
    'pytest',
    'mock',
]

EXTRAS = {
    'test': TEST_DEPS,
}

setup(
    author='SSC Pacific',
    name='statick-tex',
    description='Tool for running static analysis tools against TeX/LaTeX.',
    version='0.1.1',
    packages=['statick_tool',
              'statick_tool.plugins.discovery.tex_discovery_plugin',
              'statick_tool.plugins.tool.chktex_tool_plugin',
              'statick_tool.plugins.tool.lacheck_tool_plugin'],
    package_dir={'statick_tool.plugins.discovery.tex_discovery_plugin':
                 'plugins/tex_discovery_plugin',
                 'statick_tool.plugins.tool.chktex_tool_plugin':
                 'plugins/chktex_tool_plugin',
                 'statick_tool.plugins.tool.lacheck_tool_plugin':
                 'plugins/lacheck_tool_plugin',
                 'statick_tool': '.'},
    package_data={'statick_tool.plugins.discovery.tex_discovery_plugin':
                  ['*.yapsy-plugin'],
                  'statick_tool.plugins.tool.chktex_tool_plugin':
                  ['*.yapsy-plugin'],
                  'statick_tool.plugins.tool.lacheck_tool_plugin':
                  ['*.yapsy-plugin'],
                  'statick_tool': ['rsc/*']},
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
