from setuptools import Extension, setup

def main():
    setup(
        name = "my_demo_module",
        version ="0.8",
        author = "Nishant.Ghanate",
        ext_modules=[
            Extension(name="my_demo_module", sources=["functions_2.c"],
        )] # all sources are compiled into a single binary file
    )
    
if __name__ == '__main__':
    # $ CC=gcc python setup.py install
    main()