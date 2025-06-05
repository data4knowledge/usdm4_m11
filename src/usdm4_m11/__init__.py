import pathlib
from usdm4.api.wrapper import Wrapper
from usdm4.builder.builder import Builder
from raw_docx.raw_docx import RawDocx
from usdm4_m11.import_.m11_title_page import M11TitlePage
from usdm4_m11.import_.m11_inclusion_exclusion import M11InclusionExclusion
from usdm4_m11.import_.m11_sections import M11Sections
from usdm4_m11.import_.m11_to_usdm import M11ToUSDM
from usdm4_m11.import_.m11_styles import M11Styles
from usdm4_m11.import_.m11_estimands import M11IEstimands
from usdm4_m11.import_.m11_amendment import M11IAmendment
from usdm4_m11.import_.m11_miscellaneous import M11Miscellaneous
from usdm4_m11.import_.m11_utility import *
from usdm4_m11.errors.errors import Errors
from usdm4 import USDM4

class USDM4M11:
    def __init__(self, filepath):
        usdm4 = USDM4()
        self._builder = usdm4.builder()
        self._errors = Errors()
        self._raw_docx = RawDocx(filepath)
        self._title_page = M11TitlePage(self._raw_docx, self._builder)
        self._inclusion_exclusion = M11InclusionExclusion(self._raw_docx, self._builder)
        self._estimands = M11IEstimands(self._raw_docx, self._builder)
        self._amendment = M11IAmendment(self._raw_docx, self._builder)
        self._miscellaneous = M11Miscellaneous(self._raw_docx, self._builder)
        self._sections = M11Sections(self._raw_docx, self._builder)
        self._styles = M11Styles(self._raw_docx, self._builder)

    async def process(self):
        self._styles.process()
        await self._title_page.process()
        self._miscellaneous.process()
        self._amendment.process()
        self._inclusion_exclusion.process()
        self._estimands.process()
        self._sections.process()

    def to_usdm(self) -> Wrapper:
        usdm = M11ToUSDM(
            self._title_page,
            self._inclusion_exclusion,
            self._estimands,
            self._amendment,
            self._sections,
            self._builder,
        )
        return usdm.export()

    def extra(self):
        return {
            "title_page": self._title_page.extra(),
            "miscellaneous": self._miscellaneous.extra(),
            "amendment": self._amendment.extra(),
        }
