import time
from discogs_client.exceptions import HTTPError


class InfoProcessing(object):
    """
    Represents different operations with data.
    """

    def __init__(self, client):
        """

        :param client: 
        """
        self.client = client
        self._info = None
        self._filtered_info = None

    def search(self, value, **keys):
        """
        Search data by client.
        :param value: 
        :param keys: 
        :return: None
        """
        self._info = self.client.search(value, **keys)
        print("search", self._info.count)

    @staticmethod
    def _get(obj, key):
        try:
            return obj.data[key]
        except KeyError:
            try:
                return getattr(obj, key)
            except AttributeError:
                raise ValueError("Incorrect key value")

    def filter_info(self, key):
        """
        Filter.
        :param info: 
        :return: None
        """
        self._filtered_info = {}
        obj_num = 0
        for obj_num in range(self._info.count):
            try:
                data = self._get(self._info[obj_num], key)
                if isinstance(data, list):
                    for element in data:
                        if element not in self._filtered_info:
                            self._filtered_info[element] = 0#structures.DynamicArray()
                        self._filtered_info[element] += 1#.append(obj)
                else:
                    if data not in self._filtered_info:
                        self._filtered_info[data] = 0#structures.DynamicArray()
                    self._filtered_info[data] += 1#.append(obj)
                obj_num += 1
            except HTTPError:
                print("sleep")
                time.sleep(5)
        print("filter " + str(obj_num))
        return self._filtered_info

    def number_of_uses(self):
        result = []
        for key in self._filtered_info:
            if "&" not in key:
                result.append([key, self._filtered_info[key]])
        return result

    def the_most_used(self):
        """
        Finds most used element in filtered info.
        :return: list of values
        """
        if not self._filtered_info:
            raise UserWarning("Firstly filter info")
        result, num = [], 0
        for item in self._filtered_info:
            result.append((item, self._filtered_info[item]))
            '''if len(self._filtered_info[item]) > num:
                result = [item]
                num = len(self._filtered_info[item])
            elif len(self._filtered_info[item]) == num:
                result.append(item)
        return result'''
        result.sort(key=lambda x: x[1])
        return [item[0] for item in result]

    def the_least_used(self):
        """
        Finds least used element in filtered info.
        :return: list of values
        """
        if not self._filtered_info:
            raise UserWarning("Firstly filter info")
        result, num = [], 0
        for item in self._filtered_info:
            if len(self._filtered_info[item]) < num or num == 0:
                result = [item]
                num = len(self._filtered_info[item])
            elif len(self._filtered_info[item]) == num:
                result.append(item)
        return result
