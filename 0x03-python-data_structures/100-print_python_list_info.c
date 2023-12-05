#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: Python list
 */
void print_python_list_info(PyObject *p)
{
	unsigned long size, allocated, i = 0;

	size = Py_SIZE(p);
	allocated = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %lu\n", size);
	printf("[*] Allocated = %lu\n", allocated);

	while (i < size)
	{
		printf("Element %lu: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
		i++;
	}
}
