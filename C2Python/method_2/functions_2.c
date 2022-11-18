#include <Python.h>

static PyObject *get_even(PyObject *self, PyObject *args){
    /*
        The function PyArg_ParseTuple() in the Python API
        checks the argument types and converts them to C values.
        PyArg_ParseTuple() returns true (nonzero)

        O - get one argument as a sequence         
    */
   
   PyObject *listObj;
    if(!PyArg_ParseTuple(args, "O", &listObj)){
        return 0;
    }
    
    listObj = PySequence_Fast(listObj, "argument must be iterable");
    if(!listObj)
        return 0;

    int nums_len = PyList_Size(listObj);
    printf("List size = %d\n", nums_len);

    PyObject *even_nums = PyList_New(0);

    for(int i=0; i<nums_len; i++){
        PyLongObject *item = PyList_GetItem(listObj, i);
        long num = PyLong_AsLong(item);
        int vOut = (int)num;
        printf("index = %d | value = %d\n", i, vOut);

        if(vOut % 2 == 0){
            PyList_Append(even_nums, Py_BuildValue("i", vOut));
        }
    }

    return even_nums;
}

static PyMethodDef DemoMethods[] = {
    {"get_even",  get_even, METH_VARARGS, "Find even numbers from given list"},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef my_demo_module = {
    PyModuleDef_HEAD_INIT,
    "my_demo_module",   /* name of module and should be same as funnction */
    "Module docs",    /* module documentation, may be NULL */
    -1,              /* size of per-interpreter state of the module or -1 if the module keeps state in global variables. */
    DemoMethods
};

PyMODINIT_FUNC PyInit_my_demo_module(void) {
    PyObject *module = PyModule_Create(&my_demo_module);
    return module;
}

