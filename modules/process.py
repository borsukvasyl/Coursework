import time
from discogs_client.exceptions import HTTPError
import modules.structure as structure


class ProcessMap(object):
    """
    ADT for requesting and calculating data.
    """

    # enter here params which must be changed in list methods
    change_params = {"UK": "England"}

    def __init__(self, client, filename):
        """
        :param client: client object (must have search method)
        :param filename: file with items.
        """
        self._client = client
        with open(filename, "r") as file:
            line = file.readline().strip()
            self._type = line
            line = file.readline()
            size = int(line)
            self._elements = structure.Array(size)
            for index in range(size):
                line = file.readline().strip()
                self._elements[index] = structure.Element(line)

    def __str__(self):
        """
        Returns string representation.
        :return: str
        """
        result = "["
        for i in self._elements:
            result += str(i) + ", "
        return result[:-2] + "]"

    def __len__(self):
        """
        Returns number of elements.
        :return: int
        """
        return len(self._elements)

    def _search(self, type_value, value, **keys):
        """
        Requests given values.
        :param type_value: value of base key
        :param value: value to be searched
        :param keys: key values of request
        :return: amount of found information
        """
        keys[self._type] = type_value
        while True:
            try:
                return self._client.search(value, **keys).count
            except HTTPError:
                time.sleep(5)

    def request_values(self, value="", read_file="", **keys):
        """
        Requests values of elements in ADT.
        :param value: value to be searched
        :param read_file: filename
        :param keys: key values of request
        :return: None
        """
        # reading from file
        if read_file:
            with open(read_file, "r") as file:
                type = file.readline().strip()
                line = file.readline()
                line = file.readline().strip()
                # checking whether
                while line:
                    line = line.split("\t")
                    if line[0].lower() == keys[type]:  # if type value in file
                        values = eval(line[1])
                        for num in range(len(self)):
                            self._elements[num].value = values[num]
                        return
                    line = file.readline().strip()
        for element in self._elements:
            element.value = self._search(element.item, value, **keys)

    def request_additional(self, value="", read_file="", **keys):
        """
        Requests additional values of elements in ADT.
        :param value: value to be searched
        :param read_file: filename
        :param keys: key values of request
        :return: None
        """
        # reading from file
        if read_file:
            with open(read_file, "r") as file:
                file.readline()
                values = eval(file.readline().strip())
                for num in range(len(self)):
                    self._elements[num].additional = values[num]
        else:
            for element in self._elements:
                element.additional = self._search(element.item, value, **keys)

    def values_list(self):
        """
        Calculates values.
        :return: list of lists which contain elements's items and values
        """
        if self._elements[0].value is None:
            raise ValueError("Firstly request values.")
        result = []
        index = 0
        while index < len(self):
            element = self._elements[index]
            try:
                if element.value:
                    result.append([self.change_params[element.item] if element.item in self.change_params
                                   else element.item, element.value])
                index += 1
            except HTTPError:
                # making request too quickly
                time.sleep(5)
        return result

    def percentage_list(self):
        """
        Calculates percentage.
        :return: list of lists which contain elements's items and percentages
        """
        if self._elements[0].value is None or self._elements[0].additional is None:
            raise ValueError("Firstly request both values.")
        result = []
        index = 0
        while index < len(self):
            element = self._elements[index]
            try:
                percentage = (element.value / element.additional) * 100
                if percentage:
                    result.append([self.change_params[element.item] if element.item in self.change_params
                                   else element.item, round(percentage, 2)])
                index += 1
            except ZeroDivisionError:
                # request was not found
                index += 1
            except HTTPError:
                # making request too quickly
                time.sleep(5)
        return result
