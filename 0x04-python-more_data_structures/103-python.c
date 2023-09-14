#include <Python.h>
#include <stdio.h>
#include <string.h>
#include "lists.h"

/**
 * print_python_list - Print information about a Python list object.
 *
 * This function takes a Python list object 'p' as input
 * and prints the following information:
 * - The size (length) of the list.
 * - The allocated space for the list.
 * - The type name of each element in the list.
 *
 * @p: The Python list object to inspect.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t list_size;
	PyListObject *list;
	int i;

	list_size = PyList_Size(p);
	list = (PyListObject *) p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", list_size);
	printf("[*] Allocated = %li\n", list->allocated);
	for (i = 0; i < list_size; i++)
		printf("Element %d: %s\n", i, PyList_GET_ITEM(p, i)->ob_type->tp_name);
}

/**
 * print_python_bytes - Print information about a Python list object.
 *
 * This function takes a Python list object 'p' as input
 * and prints the following information:
 * - The size (length) of the list.
 * - The allocated space for the list.
 * - The type name of each element in the list.
 *
 * @p: The Python object to inspect.
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes_ob;
	int i = 0;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	bytes_ob = (PyBytesObject *) p;
	printf("  size: %li\n", bytes_ob->ob_base.ob_size);
	printf("  trying string: %s\n", bytes_ob->ob_sval);
	printf("  first %li bytes: ",
				bytes_ob->ob_base.ob_size < 10 ? bytes_ob->ob_base.ob_size : 10);
	while (bytes_ob->ob_sval[i + 1] != '\0' && i < 9)
	{
		printf("%x ", bytes_ob->ob_sval[i]);
		i++;
	}
	printf("%x", bytes_ob->ob_sval[i]);
	printf("\n");
}
