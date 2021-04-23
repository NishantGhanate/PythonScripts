# Convert your Single python script to c

> pip install Cython

- Keep your script and setup.py in same folder 
  
- Make your script modular similar to Something.py
  
- Open setup.py and change  cythonize('yourscriptpy')
  
- now open terminal / cmd and run below command
  
> $  python setup.py build_ext --inplace

- Make an new folder and add build folder, something.c & .pyd init

- Make an main.py file in new folder 
  
- Look up main.py for systax and run   


# Note :
something.c has your python code in multiline comment.
