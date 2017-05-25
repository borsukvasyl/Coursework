import ctypes


class Array(object):
    """
    Implementation of array.
    """
    def __init__(self, size):
        """
        Creates an array with size elements.
        :param size: size of array.
        """
        if size < 1:
            raise ValueError("Invalid size")
        self._size = size
        array_type = ctypes.py_object * size
        self._elements = array_type()
        for i in range(len(self)):
            self._elements[i] = None

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


class Element(object):
    """
    Implementation of element for Array.
    """
    def __init__(self, item, value = None, additional=None):
        self.item = item
        self.value = value
        self.additional = additional

    def __str__(self):
        """
        Returns string representation.
        :return: str
        """
        return "({}, {}, {})".format(self.item, self.value, self.additional)
