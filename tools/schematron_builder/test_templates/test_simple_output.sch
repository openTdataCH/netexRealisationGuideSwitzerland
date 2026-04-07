<?xml version="1.0" encoding="UTF-8"?><sch:schema xmlns:sch="http://purl.oclc.org/dsdl/schematron" xmlns:netex="http://www.netex.org.uk/netex" queryBinding="xslt2">
  <sch:ns prefix="netex" uri="http://www.netex.org.uk/netex"/>
  <sch:title>Generated schematron from template</sch:title>
  <sch:pattern id="p1">
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:TestFrame">
      <sch:assert test="count(netex:MandatoryElement) > 0">MandatoryElement must be present</sch:assert>
      <sch:assert test="count(netex:ForbiddenElement) = 0">ForbiddenElement must NOT be present</sch:assert>
      <!-- DEPRECATED: DeprecatedElement is deprecated -->
      <sch:assert test="count(netex:DeprecatedElement) = 0">DeprecatedElement is deprecated and should not be used</sch:assert>
      <sch:assert test="count(netex:EnumElement) > 0">EnumElement must be present</sch:assert>
      <sch:assert test="count(netex:ElementWithBoth) > 0">ElementWithBoth must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:TestFrame/netex:EnumElement">
      <sch:assert test="(. = 'value1' or . = 'value2' or . = 'value3')">Value must be one of: value1 value2 value3</sch:assert>
      </sch:rule>
    </sch:pattern>
  </sch:schema>

