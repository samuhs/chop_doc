from setuptools import setup

setup(
    name = 'Chop Doc',
    version = '0.1.0',
    author = 'Samuel Silva',
    author_email = 'samuel.silva@gmail.com',
    packages = ['chop_doc'],
    description = 'A easy way to split documentos in chuncks',
    long_description = 'A easy way to split documentos in chuncks '
                        + 'build with langchain compatible ',
                        + 'to help you chop your docs',
    url = 'https://github.com/yanorestes/aluratemp',
    project_urls = {
        'Código fonte': 'https://github.com/yanorestes/aluratemp',
        'Download': 'https://github.com/yanorestes/aluratemp/archive/1.0.0.zip'
    },
    license = 'MIT',
    keywords = 'conversor temperatura alura',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Internationalization',
        'Topic :: Scientific/Engineering :: Physics'
    ]
)