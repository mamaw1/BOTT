import json

class JSONDatabase:
    def __init__(self, filename):
        self.filename = filename
        self._data = self._load()

    def _load(self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save(self):
        with open(self.filename, 'w') as f:
            json.dump(self._data, f, indent=4)

    def get(self, key):
        return self._data.get(key)

    def set(self, key, value):
        self._data[key] = value
        self.save()

    def delete(self, key):
        if key in self._data:
            del self._data[key]
            self.save()
    
    def all(self):
        return self._data
