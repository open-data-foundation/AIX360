import setuptools

version = '0.1'

with open("aix360/version.py", 'w') as f:
    f.write('# generated by setup.py\nversion = "{}"\n'.format(version))

setuptools.setup(
	name='aix360',
	version=version,
    description='IBM AI Explainability 360',
    authos='aix360 developers',
    url='https://github.com/IBM/AIX360',
    author_email='aix360@us.ibm.com',
    packages=setuptools.find_packages(),
    license='Apache License 2.0',
    long_description=open("README.md", 'r').read(),
    install_requires=[
            'joblib>=0.11',
            'scikit-learn>=0.21.2',
            'torch',
            'torchvision',
            'cvxpy',
            'cvxopt',
            'Image',
            'keras',
            'matplotlib',
            'numpy',
            'pandas',
            'scipy>=0.17',
            'tensorflow==1.14',
            'xport',
            'scikit-image',
            'requests',
            'lime',
            'shap',
            'xgboost'
	], 
    package_data={'aix360': ['data/*', 'data/*/*', 'data/*/*/*', 'models/*', 'models/*/*', 'models/*/*/*']},
    include_package_data=True,
    zip_safe=False
)
