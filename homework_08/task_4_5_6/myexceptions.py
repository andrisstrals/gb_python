
class ErrorNotAnEqupment(Exception):
    def __init__(self, item):
        self.__item = item

    def __str__(self):
        return f"Object '{self.__item}' is not an office equipment item!"

