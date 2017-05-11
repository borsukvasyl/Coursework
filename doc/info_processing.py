import doc.structure as structures


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
        for obj in self._info:
            data = self._get(obj, key)
            if isinstance(data, list):
                for element in data:
                    if element not in self._filtered_info:
                        self._filtered_info[element] = structures.DynamicArray()
                    self._filtered_info[element].append(obj)
            else:
                if data not in self._filtered_info:
                    self._filtered_info[data] = structures.DynamicArray()
                self._filtered_info[data].append(obj)

    def the_most_used(self):
        """
        Finds most used element in filtered info.
        :return: list of values
        """
        if not self._filtered_info:
            raise UserWarning("Firstly filter info")
        result, num = [], 0
        for item in self._filtered_info:
            if len(self._filtered_info[item]) > num:
                result = [item]
                num = len(self._filtered_info[item])
            elif len(self._filtered_info[item]) == num:
                result.append(item)
        return result

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
