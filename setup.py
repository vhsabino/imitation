import src.imitation  # pytype: disable=import-error
from setuptools import find_packages, setup

TF_VERSION = ">=1.15.0,<2.0"
TESTS_REQUIRE = [
    "seals~=0.1.0",
    "black",
    # remove pin once https://github.com/nedbat/coveragepy/issues/881 fixed
    "coverage==4.5.4",
    "codecov",
    "codespell",
    "flake8",
    "flake8-blind-except",
    "flake8-builtins",
    "flake8-debugger",
    "flake8-isort",
    "pytest",
    "pytest-cov",
    "pytest-shard",
    "pytest-xdist",
    "pytype",
]
DOCS_REQUIRE = [
    "sphinx",
    "sphinxcontrib-napoleon",
]
PARALLEL_REQUIRE = ["ray[debug,tune]~=0.8.5"]


def get_readme() -> str:
    """Retrieve content from README."""
    with open("README.md", "r") as f:
        return f.read()


setup(
    name="imitation",
    version=src.imitation.__version__,
    description="Implementation of modern IRL and imitation learning algorithms.",
    long_description=get_readme(),
    long_description_content_type="text/markdown",
    author="Center for Human-Compatible AI and Google",
    python_requires=">=3.7.0",
    packages=find_packages("src"),
    package_dir={"": "src"},
    package_data={"imitation": ["py.typed", "envs/examples/airl_envs/assets/*.xml"]},
    install_requires=[
        "awscli",
        "cloudpickle>=0.5.5",
        "gym[classic_control]",
        "matplotlib",
        "numpy>=1.15",
        "tqdm",
        "scikit-learn>=0.21.2",
        "stable-baselines~=2.10.0",
        "jax~=0.1.66",
        "jaxlib~=0.1.47",
        # Install from IDSIA/sacred@master once
        # https://github.com/IDSIA/sacred/pull/737 is merged.
        "sacred @ git+https://github.com/HumanCompatibleAI/sacred@0.8.1-with-imit-compat",  # noqa: E501
    ],
    tests_require=TESTS_REQUIRE,
    extras_require={
        "gpu": [f"tensorflow-gpu{TF_VERSION}"],
        "cpu": [f"tensorflow{TF_VERSION}"],
        # recommended packages for development
        "dev": [
            "autopep8",
            "ntfy[slack]",
            "ipdb",
            "isort",
            "jupyter",
            "pytype",
            "codespell",
            # for convenience
            *TESTS_REQUIRE,
            *DOCS_REQUIRE,
        ],
        "test": TESTS_REQUIRE,
        "docs": DOCS_REQUIRE,
        "parallel": PARALLEL_REQUIRE,
    },
    entry_points={
        "console_scripts": [
            ("imitation-expert-demos=imitation.scripts.expert_demos" ":main_console"),
            "imitation-train=imitation.scripts.train_adversarial:main_console",
        ],
    },
    url="https://github.com/HumanCompatibleAI/imitation",
    license="MIT",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
