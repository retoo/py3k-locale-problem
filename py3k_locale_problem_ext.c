#include <Python.h>

#include <stdlib.h>
#include <stdio.h>

struct module_state {
	PyObject *error;
};

#if PY_MAJOR_VERSION >= 3
#define GETSTATE(m) ((struct module_state*)PyModule_GetState(m))
#else
#define GETSTATE(m) (&_state)
static struct module_state _state;
#endif

static
PyObject *
py3k_locale_problem_ext_convert(PyObject *self, PyObject *args) {
	const char *input;
	float f;

	if (!PyArg_ParseTuple(args, "s", &input))
		return NULL;

	f = atof(input);

	return Py_BuildValue("f", f);
}

static
PyMethodDef py3k_locale_problem_ext_methods[] = {

	{"convert",  py3k_locale_problem_ext_convert, METH_VARARGS,
	 "converts a string to a float."},

	{NULL, NULL, 0, NULL}        /* Sentinel */
};

#if PY_MAJOR_VERSION >= 3

static int
py3k_locale_problem_ext_traverse(PyObject *m, visitproc visit, void *arg) {
	Py_VISIT(GETSTATE(m)->error);
	return 0;
}

static int
py3k_locale_problem_ext_clear(PyObject *m) {
	Py_CLEAR(GETSTATE(m)->error);
	return 0;
}


static struct
PyModuleDef moduledef = {
	PyModuleDef_HEAD_INIT,
	"py3k_locale_problem_ext",
	NULL,
	sizeof(struct module_state),
	py3k_locale_problem_ext_methods,
	NULL,
	py3k_locale_problem_ext_traverse,
	py3k_locale_problem_ext_clear,
	NULL
};

#define INITERROR return NULL

PyObject *
PyInit_py3k_locale_problem_ext(void)

#else
#define INITERROR return

void
initpy3k_locale_problem_ext(void)
#endif
{
#if PY_MAJOR_VERSION >= 3
	PyObject *module = PyModule_Create(&moduledef);
#else
	PyObject *module = Py_InitModule("py3k_locale_problem_ext", py3k_locale_problem_ext_methods);
#endif
	struct module_state *st;

	if (module == NULL)
		INITERROR;
	st = GETSTATE(module);

	st->error = PyErr_NewException("py3k_locale_problem_ext.Error", NULL, NULL);
	if (st->error == NULL) {
		Py_DECREF(module);
		INITERROR;
	}

#if PY_MAJOR_VERSION >= 3
	return module;
#endif
}
