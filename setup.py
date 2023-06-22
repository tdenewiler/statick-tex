"""Setup."""


from setuptools import setup

with open("README.md", encoding="utf-8") as fid:
    long_description = fid.read()  # pylint: disable=invalid-name

TEST_DEPS = [
    "mock",
    "pre-commit",
    "pytest==7.1",
]

EXTRAS = {
    "test": TEST_DEPS,
}

setup(
    author="Thomas Denewiler",
    name="statick-tex",
    description="Statick analysis plugins for TeX/LaTeX files and projects.",
    version="0.3.5",
    packages=[
        "statick_tool",
        "statick_tool.plugins.discovery",
        "statick_tool.plugins.tool",
    ],
    package_dir={
        "statick_tool": ".",
        "statick_tool.plugins.discovery": "src/statick_tex/plugins/discovery",
        "statick_tool.plugins.tool": "src/statick_tex/plugins/tool",
    },
    package_data={
        "statick_tool": ["rsc/.*", "rsc/*"],
        "statick_tool.plugins.discovery": ["*.yapsy-plugin"],
        "statick_tool.plugins.tool": ["*.yapsy-plugin"],
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["statick"],
    tests_require=TEST_DEPS,
    extras_require=EXTRAS,
    url="https://github.com/tdenewiler/statick-tex",
    classifiers=[
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Testing",
        "Topic :: Text Processing :: Markup :: LaTeX",
        "Typing :: Typed",
    ],
)
