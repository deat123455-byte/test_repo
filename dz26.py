class MyDict:
    def __init__(self):
        self._keys = []
        self._values = []

    def __getitem__(self, key):
        for i in range(len(self._keys)):
            if self._keys[i] == key:
                return self._values[i]
        return None

    def __setitem__(self, key, value):
        if key in self._keys:
            index = self._keys.index(key)
            self._values[index] = value
        else:
            self._keys.append(key)
            self._values.append(value)

    def __delitem__(self, key):
            for i in range(len(self._keys)):
                if self._keys[i] == key:
                    self._keys.pop(i)
                    self._values.pop(i)
                    return

    def __contains__(self, key):
        return key in self._keys

    def keys(self):
        return self._keys[:]

    def values(self):
        return self._values[:]

    def items(self):
        return list(zip(self._keys, self._values))

    def __str__(self):
        pairs = []
        for i in range(len(self.keys())):
            pairs.append(f"{self.keys()[i]}: {self.values()[i]}")
        my_dicts = "{" + ", ".join(pairs) + "}"
        return my_dicts


my_dict = MyDict()
my_dict['name'] = 'Alice'
my_dict['age'] = 30
print(my_dict['name'])  # Вернет 'Alice'
print('city' in my_dict)  # Вернет False
del my_dict['age']
print(my_dict.keys())  # Вернет ['name']
print(my_dict.values())  # Вернет ['Alice']
