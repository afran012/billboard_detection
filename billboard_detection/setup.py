from setuptools import setup, find_packages

setup(
    name='billboard_detection',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A project for detecting billboards in images using computer vision techniques.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/billboard_detection',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'numpy',
        'opencv-python',
        'tensorflow',
        'pandas',
        'scikit-learn',
        'pyspark',
        'matplotlib',
        'jupyter'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)