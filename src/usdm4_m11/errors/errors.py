import traceback
from d4k_sel.errors import Errors as BaseErrors
from d4k_sel.error_location import GridLocation, ErrorLocation


class Errors(BaseErrors):
    def error(self, message: str, location: GridLocation = None):
        location = location if location else ErrorLocation()
        self.add(message, location)

    def info(self, message: str, location: GridLocation = None):
        location = location if location else ErrorLocation()
        self.add(message, location, level=BaseErrors.INFO)

    def debug(self, message: str, location: GridLocation = None):
        location = location if location else ErrorLocation()
        self.add(message, location, level=BaseErrors.DEBUG)

    def warning(self, message: str, location: GridLocation = None):
        location = location if location else ErrorLocation()
        self.add(message, location, level=BaseErrors.WARNING)

    def exception(self, message: str, e: Exception, location: GridLocation = None):
        location = location if location else ErrorLocation()
        message = f"{message}\n\nDetails\n{e}\n\nTraceback\n{traceback.format_exc()}"
        self.add(message, location)
