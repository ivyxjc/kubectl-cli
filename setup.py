from setuptools import setup

setup(
    name="kubectl simplifier",
    version="0.1",
    py_modules=["kc"],
    include_package_data=True,
    install_requires=["click"],
    entry_points="""
       [console_scripts]
       repo=kc:cli
   """,
)
