from setuptools import find_packages, setup

setup(name="transifex_api",
      version="0.0.2",
      install_requires=["requests", "six"],
      packages=find_packages('src'),
      package_dir={'': 'src'})
