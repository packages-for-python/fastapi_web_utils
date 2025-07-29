from setuptools import setup, find_packages

setup(
    name="fastapi_web_utils",  # 包的名称
    version="0.1.0",  # 版本号
    author="lei.wang",
    author_email="greatbestlei@gmail.com",
    description="fastapi web framework utils",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/packages-for-python/fastapi_web_utils",  # GitHub 仓库地址
    packages=find_packages(),  # 自动发现包
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
    install_requires=[
        "greenlet==3.2.3",
        "SQLAlchemy==2.0.41",
        "typing_extensions==4.14.1"
    ],
)
