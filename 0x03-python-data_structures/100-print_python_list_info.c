#include <Python.h>
#include <listobject.h>
#include <object.h>
#include <stdio.h>
#include "lists.h"

/**
 * print_python_list_info - Print information about a Python list object.
 *
 * This function takes a Python list object 'p' as input
 * and prints the following information:
 * - The size (length) of the list.
 * - The allocated space for the list.
 * - The type name of each element in the list.
 *
 * @p: The Python list object to inspect.
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t list_size;
	PyListObject *list;
	int i;

	list_size = PyList_Size(p);
	list = (PyListObject *) p;

	printf("[*] Size of the Python List = %li\n", list_size);
	printf("[*] Allocated = %li\n", list->allocated);
	for (i = 0; i < list_size; i++)
		printf("Element %d: %s\n", i, PyList_GET_ITEM(p, i)->ob_type->tp_name);
}
