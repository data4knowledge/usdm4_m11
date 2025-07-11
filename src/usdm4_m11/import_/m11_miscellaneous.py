from raw_docx.raw_docx import RawDocx
from usdm4.builder.builder import Builder
from simple_error_log.errors import Errors


class M11Miscellaneous:
    def __init__(self, raw_docx: RawDocx, builder: Builder, errors: Errors):
        self._builder = builder
        self._errors = errors
        self._raw_docx = raw_docx
        self.sponsor_signatory = ""
        self.medical_expert_contact = ""
        self.sae_reporting_method = ""

    def process(self):
        section = self._raw_docx.target_document.section_by_ordinal(1)
        sig_item, sig_index = section.find_first_at_start("Sponsor Signatory")
        expert_item, expert_index = section.find_first_at_start("Medical Expert")
        sae_item, sae_index = section.find_first_at_start("SAE Reporting")
        amend_item, amend_index = section.find_first_at_start("Amendment Details")
        if sig_item and expert_item:
            self.sponsor_signatory = section.to_html_between(sig_index, expert_index)
        if expert_item and sae_item:
            self.medical_expert_contact = section.to_html_between(
                expert_index, sae_index
            )
        if sae_item and amend_item:
            self.medical_expert_contact = section.to_html_between(
                sae_index, amend_index
            )

    def extra(self):
        return {
            "sponsor_signatory": self.sponsor_signatory,
            "medical_expert_contact": self.medical_expert_contact,
            "sae_reporting_method": self.sae_reporting_method,
        }
