from setuptools import setup, find_namespace_packages

setup(
    name="clean_folder",
    version="0.1",
    description="Tool to clean folders, use on Your own risk",
    url="http://github.com/WitekHun/clean_folder/",
    author="WitekH",
    author_email="witekh@me.com",
    license="MIT",
    packages=["file_sorter"],
    entry_points={"console_scripts": ["clean_folder=clean_folder.file_sorter:main"]},
)
