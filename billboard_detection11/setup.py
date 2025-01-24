from setuptools import setup, find_packages

setup(
    name="Copybillboard_detection",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A project for detecting billboards using computer vision and Spark.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/Copybillboard_detection",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pyspark==3.3.0',
        'tensorflow==2.9.0',
        'opencv-python==4.7.0',
        'numpy==1.23.5',
        'easyocr==1.6.2',
        'pillow==9.5.0'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)