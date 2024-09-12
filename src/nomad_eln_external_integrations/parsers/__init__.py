from nomad.config.models.plugins import ParserEntryPoint


class ElabftwEntryPoint(ParserEntryPoint):
    def load(self):
        from nomad_eln_external_integrations.parsers.elabftw import ELabFTWParser

        return ELabFTWParser(**self.dict())


elabftw_parser_entry_point = ElabftwEntryPoint(
    name='parsers/elabftw',
    aliases=['parsers/elabftw'],
    code_name='elabftw',
    code_homepage='https://www.elabftw.net/',
    description='NOMAD parser for eln file formats.',
    mainfile_mime_re=r'text/plain|application/json|text/html',
    mainfile_name_re=r'.*ro-crate-metadata.json$',
)
