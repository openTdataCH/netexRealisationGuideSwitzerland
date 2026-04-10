<?xml version="1.0" encoding="UTF-8"?><sch:schema xmlns:sch="http://purl.oclc.org/dsdl/schematron" xmlns:netex="http://www.netex.org.uk/netex" queryBinding="xslt2">
  <sch:ns prefix="netex" uri="http://www.netex.org.uk/netex"/>
  <sch:title>Generated schematron from template</sch:title>
  <sch:pattern id="p1">
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ServiceFrame">
      <sch:assert test="count(netex:stopAssignments) > 0">stopAssignments must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ServiceFrame/netex:stopAssignments/netex:PassengerStopAssignment">
      <sch:assert test="count(netex:ScheduledStopPointRef) > 0">ScheduledStopPointRef must be present</sch:assert>
      <sch:assert test="count(netex:StopPlaceRef) > 0">StopPlaceRef must be present</sch:assert>
      </sch:rule>
    </sch:pattern>
  </sch:schema>

