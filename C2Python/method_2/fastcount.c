#include <Python.h>

int c_prime_counter(int frm, int til) {

  int primecount = 0;
  for (int num = frm; num <= til; num++) {
    int flag = 0;

    if (num > 1) {

      for (int candidate = 2; candidate < num; candidate++) {
        if ((num % candidate) == 0) {
          flag = 1;
          break;
        }
      }

      if (flag == 0) {
        primecount++;
      }
    }
  }
  return primecount;
}

static PyObject *py_primecounter(PyObject *self, PyObject *args) {

  // Declare two pointers
  int *n_frm, *n_til = NULL;


  // Parse arguments - expects two integers that will be mapped to n_frm and n_til
  if (!PyArg_ParseTuple(args, "ii", &n_frm, &n_til)) {
    return NULL;
  }

  // Call c-function
  int found_primes = c_prime_counter(n_frm, n_til);


  return PyLong_FromLong(found_primes);
}

static PyMethodDef CountingMethods[] = {
  {"primecounter", py_primecounter, METH_VARARGS, "Function for counting primes in a range in c"},
  {NULL, NULL, 0, NULL}
};


static struct PyModuleDef fastcountmodule = {
  PyModuleDef_HEAD_INIT,
  "Fastcount", // module name
  "C library for counting fast",
  -1,
  CountingMethods
};


PyMODINIT_FUNC PyInit_Fastcount(void) {
  return PyModule_Create(&fastcountmodule);
};
