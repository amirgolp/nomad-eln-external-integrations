from nomad.config.models.plugins import SchemaPackageEntryPoint


class OpenbisEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from nomad_eln_external_integrations.schema_packages.openbis.schema import (
            m_package,
        )

        return m_package


schema = OpenbisEntryPoint(
    name='openbis',
    description='NOMAD integration for mapping Openbis data to NOMAD schema',
)
