from typing import Optional

from nomad.config.models.plugins import ParserEntryPoint
from pydantic import Field


class EntryPoint(ParserEntryPoint):
    parser_class_name: str = Field(
        description="""
        The fully qualified name of the Python class that implements the parser.
        This class must have a function `def parse(self, mainfile, archive, logger)`.
    """
    )
    level: int = Field(
        0,
        description="""
        Order of execution of parser with respect to other parsers.
    """,
    )
    code_name: Optional[str]
    code_homepage: Optional[str]
    code_category: Optional[str]

    def load(self):
        from nomad.parsing import MatchingParserInterface

        return MatchingParserInterface(**self.dict())


elabftw_parser_entry_point = EntryPoint(
    name='parsers/elabftw',
    aliases=['parsers/elabftw'],
    description='NOMAD parser for eln file formats.',
    python_package='nomad-eln-external-integration.parsers.elabftw',
    mainfile_mime_re=r'text/plain|application/json|text/html',
    mainfile_name_re=r'.*ro-crate-metadata.json$',
    parser_class_name='nomad-eln-external-integration.parsers.ElabftwParser',
    code_name='elabftw',
    code_homepage='https://www.elabftw.net/',
)
