import settngs

class Model:
    _model_name_ = ""

    def save(self):
        settngs.DATA_BASE[self._model_name_].append(self)
