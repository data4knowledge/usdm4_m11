from usdm4_m11.import_.m11_import import M11Import
from usdm4.api.wrapper import Wrapper
from simple_error_log.errors import Errors
from simple_error_log.error_location import KlassMethodLocation


class USDM4M11:
    MODULE = "src.usdm4_m11.__init__.USDM4M11"

    def __init__(self):
        self._errors = Errors()
        self._m11_import = None

    def from_docx(self, filepath: str) -> Wrapper:
        try:
            self._m11_import = M11Import(filepath, self._errors)
            self._m11_import.process()
            wrapper = self._m11_import.to_usdm()
            return wrapper
        except Exception as e:
            location = KlassMethodLocation(self.MODULE, "from_docx")
            self._errors.exception(
                f"Exception raised converting M11 '-docx' file '{filepath}'",
                e,
                location,
            )

    def extra(self) -> dict:
        try:
            return self._m11_import.extra()
        except Exception as e:
            location = KlassMethodLocation(self.MODULE, "extra")
            self._errors.exception(
                "Exception raised obraing extra information", e, location
            )

    @property
    def errors(self):
        return self._errors
