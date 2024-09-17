from nomad.config.models.plugins import SchemaPackageEntryPoint


class ElabftwNormalizerEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from nomad_eln_external_integrations.schema_packages.elabftw.schema import (
            m_package,
        )

        return m_package


schema = ElabftwNormalizerEntryPoint(
    name='elabftw2',
    description='NOMAD integration for mapping elabftw data to NOMAD schema',
)
