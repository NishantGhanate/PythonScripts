# METHOD 1

### In this we will convert `.c` code to `.so` using `-fPIC` . Then we can use python `ctypes` to import `.so'` and run it.
<br>

We will use wsl on windows to compile & generate .so 

```
1 - Write c code
2 - generate so using [cc -fPIC -shared -o functions.so functions.c]
```

Tip : In case you forgot for every chnage in .c code you will have generate .so again.