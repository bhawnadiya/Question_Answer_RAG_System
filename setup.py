from setuptools import find_packages, setup

setup(
    name = 'QApplication',
    version= '0.0.1',
    author= 'Bhumika Raheja',
    author_email= 'bhumikaraheja089@gmail.com',
    packages= find_packages(),
    install_requires = [
        'llama-index',
        'python-dotenv',
        'google-generativeai',
        'IPython'
    ]

)