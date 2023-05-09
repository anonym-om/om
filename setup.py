from setuptools import setup

setup(
    name='om',
    version='0.6.6',
    packages=['om'],
    url='https://github.com/anonym-om/om',
    license='',
    author='guilherme',
    author_email='anonym.ontmatch@gmail.com',
    description='Ontology Matching Utilities',
    install_requires=['numpy', 'rdflib', 'pandas', 'tqdm', 'termcolor', 'multiprocessing_on_dill', 'nltk']
)
