import pandas as pd

class Result:
    def __init__(self, filters, result_description, result):
        self.filters = filters
        self.result_description = result_description
        self.result = result

    def overview(self):
        return pd.DataFrame(self._raw_result())

    def _raw_result(self):
        return list(map(lambda x: x.to_raw(), self.result))
