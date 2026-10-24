<?xml version="1.0" encoding="UTF-8"?>
<schema xmlns="http://purl.oclc.org/dsdl/schematron">
    <!-- Rule (a): The version attribute of no element can be "any" -->
    <pattern id="no_version_any">
        <rule context="*[@version]">
            <assert test="not(@version = 'any')">
                The version attribute cannot be "any" (element: <value-of select="name()"/>) 
            </assert>
        </rule>
    </pattern>

    <!-- Rule (b): The versionRef attribute of any element can't be "any" -->
    <pattern id="no_versionRef_any">
        <rule context="*[@versionRef]">
            <assert test="not(@versionRef = 'any')">
                The versionRef attribute cannot be "any" (element: <value-of select="name()"/>) 
            </assert>
        </rule>
    </pattern>

    <!-- Rule (c): If an element name ends in "Ref", then it must have a version or versionRef attribute (excluding ParticipantRef) -->
    <pattern id="ref_elements_require_version">
        <rule context="*[substring(name(), string-length(name()) - 2) = 'Ref' and name() != 'ParticipantRef' and not(contains(name(), ':ParticipantRef'))]">
            <assert test="@version or @versionRef">
                Elements ending with "Ref" must have either a version or versionRef attribute (element: <value-of select="name()"/>) 
            </assert>
        </rule>
    </pattern>
</schema>
