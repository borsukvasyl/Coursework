import doc.structure as arr


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

    def filter_info(self, info):
        """
        Filter.
        :param info: 
        :return: None
        """
        self._filtered_info = {}
        for obj in self._info:
            if isinstance(obj.data[info], list):
                for element in obj.data[info]:
                    if element in self._filtered_info:
                        self._filtered_info[element].append(obj)
                    else:
                        self._filtered_info[element] = arr.DynamicArray()
                        self._filtered_info[element].append(obj)
            else:
                if obj.data[info] in self._filtered_info:
                    self._filtered_info[obj.data[info]].append(obj)
                else:
                    self._filtered_info[obj.data[info]] = arr.DynamicArray()
                    self._filtered_info[obj.data[info]].append(obj)

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
