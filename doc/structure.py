import ctypes


class Array:
    """
    Implements the Array ADT using array capabilities of the ctypes module.
    """
    def __init__(self, size):
        """
        Creates an array with size elements.
        :param size: size of array.
        """
        if size < 1:
            raise ValueError("Array size must be > 0")
        self._size = size
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()

    def __len__(self):
        """
        Returns the size of the array.
        :return: the size of the array. 
        """
        return self._size

    def __getitem__(self, index):
        """
        Gets the value of the element.
        :param index: the index of element.
        :return: value of the element.
        """
        if not 0 <= index < self._size:
            raise IndexError('Invalid index')
        return self._elements[index]

    def __setitem__(self, index, value):
        """
        Puts the value in the array element at index position.
        :param index: the index element.
        :param value: the value of element.
        """
        if not 0 <= index < self._size:
            raise IndexError('Invalid index')
        self._elements[index] = value

    def __iter__(self):
        """
        Returns the array's iterator for traversing the elements.
        :return: the array's iterator for traversing the elements. 
        """
        for i in range(len(self)):
            yield self._elements[i]


class DynamicArray:
    """
    A dynamic array class a simplified Python list.
    """
    def __init__(self):
        """
        Creates an empty array.
        """
        self._size = 0
        self._capacity = 1
        self._elements = Array(self._capacity)

    def __len__(self):
        """
        Returns the number of elements in the array.
        :return: the number of elements in the array. 
        """
        return self._size

    def __getitem__(self, index):
        """
        Gets the value of the element by index.
        :param index: the index of element.
        :return: the value of the element.
        """
        if not 0 <= index < self._size:
            raise IndexError('Invalid index')
        return self._elements[index]

    def __repr__(self):
        res = "["
        for i in self._elements:
            res += str(i) + ", "
        return res[:-2] + "]"

    def append(self, value):
        """
        Puts the value in the end of the array.
        :param value: the value of element.
        """
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._elements[self._size] = value
        self._size += 1

    def _resize(self, capacity):
        """
        Resize internal array to new capacity.
        :param capacity: new capacity of array.
        """
        new_elements = Array(capacity)

        for k in range(self._size):
            new_elements[k] = self._elements[k]
        self._elements = new_elements
        self._capacity = capacity
