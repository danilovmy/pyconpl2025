
class Coroutined:

    def __init__(self, attr=None):
        self._attr = self._attr(attr)
        self.attr  #start coroutine

    def _attr(self, attr = None, *args, **kwargs):
        while True:
            val = yield attr
            if isinstance(val, tuple):
                attr = val[0]

    attr = property(lambda self: next(self._attr), lambda self, value: self._attr.send((value, )))

    # def coroutined_method(self, *args, **kwargs):
    #     ... #prepeare something based on args and kwargs
    #     response = None
    #     while True:
    #         val = yield response
    #         response = ...  # calculate result with val

    # def yielded_method(self, *args, **kwargs):
    #         response = ...  # calculate result
    #         yield response



coro = Coroutined()
print(coro.attr)
coro.attr = 'new value'
print(coro.attr)

#calc = coro.yielded_method(initial_data).send
#result = calc(new_val)

# calc = coro.coroutined_method(initial_data).send
# calc(None)
#result = calc(new_val)
