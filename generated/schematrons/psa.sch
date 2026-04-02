<?xml version="1.0" encoding="UTF-8"?>
<sch:schema xmlns:sch="http://purl.oclc.org/dsdl/schematron"  xmlns:netex="http://www.netex.org.uk/netex" queryBinding="xslt2">
<sch:ns prefix="netex" uri="http://www.netex.org.uk/netex" />
  <sch:title>Generated schematron from template</sch:title>
  <sch:pattern id="p1">
    <sch:rule context="netex:ResourceFrame">
      <sch:assert test="count(.//netex:responsibilitySets) > 0">responsibilitySets must be present</sch:assert>
      </sch:rule>
    <sch:rule context="netex:responsibilitySets">
      <sch:assert test="count(.//netex:ResponsibilitySet) > 0">ResponsibilitySet must be present</sch:assert>
      </sch:rule>
    <sch:rule context="netex:values">
      <!-- TypeOfNotice with id="ch:1:TypeOfNotice:11" must exist somewhere in the document -->
      <sch:report test="count(.//netex:TypeOfNotice[@id='ch:1:TypeOfNotice:11']) > 0">An element TypeOfNotice with id="ch:1:TypeOfNotice:11" must exist</sch:report>
      <!-- TypeOfNotice with id="ch:1:TypeOfNotice:1" must exist somewhere in the document -->
      <sch:report test="count(.//netex:TypeOfNotice[@id='ch:1:TypeOfNotice:1']) > 0">An element TypeOfNotice with id="ch:1:TypeOfNotice:1" must exist</sch:report>
      <!-- TypeOfNotice with id="ch:1:TypeOfNotice:10" must exist somewhere in the document -->
      <sch:report test="count(.//netex:TypeOfNotice[@id='ch:1:TypeOfNotice:10']) > 0">An element TypeOfNotice with id="ch:1:TypeOfNotice:10" must exist</sch:report>
      <!-- TypeOfNotice with id="ch:1:TypeOfNotice:3" must exist somewhere in the document -->
      <sch:report test="count(.//netex:TypeOfNotice[@id='ch:1:TypeOfNotice:3']) > 0">An element TypeOfNotice with id="ch:1:TypeOfNotice:3" must exist</sch:report>
      <!-- TypeOfNotice with id="ch:1:TypeOfNotice:2" must exist somewhere in the document -->
      <sch:report test="count(.//netex:TypeOfNotice[@id='ch:1:TypeOfNotice:2']) > 0">An element TypeOfNotice with id="ch:1:TypeOfNotice:2" must exist</sch:report>
      <sch:assert test="count(.//TypeOfProductCategory) > 0">TypeOfProductCategory must be present</sch:assert>
      <!-- TypeOfProductCategory with id="ch:1:TypeOfProductCategory:TER" must exist somewhere in the document -->
      <sch:assert test="count(//TypeOfProductCategory[@id='ch:1:TypeOfProductCategory:TER']) > 0">An element TypeOfProductCategory with id="ch:1:TypeOfProductCategory:TER" must exist</sch:assert>
      </sch:rule>
    <sch:rule context="Operator">
      <sch:assert test="count(.//Operator) > 0">Operator must be present</sch:assert>
       <sch:assert test="count(.//PrivateCode) > 0">PrivateCode must be present</sch:assert>

      </sch:rule>
    <sch:rule context="keyList">
      <sch:assert test="count(.//KeyValue) > 0">KeyValue must be present</sch:assert>
      </sch:rule>
    <sch:rule context="Operator">
      <sch:assert test="count(.//Name) > 0">Name must be present</sch:assert>
      </sch:rule>
    <sch:rule context="Operator">
      <sch:assert test="count(.//ShortName) > 0">ShortName must be present</sch:assert>
      </sch:rule>
    <sch:rule context="organisations">
      <sch:assert test="count(.//Operator) > 0">Operator must be present</sch:assert>
      </sch:rule>
    <sch:rule context="ServiceFrame">
      <sch:assert test="count(.//directions) = 0">directions must NOT be present</sch:assert>
      </sch:rule>
    <sch:rule context="directions">
      <sch:assert test="count(.//Direction) = 0">Direction must NOT be present</sch:assert>
      </sch:rule>
    <sch:rule context="ServiceFrame">
      <sch:assert test="count(.//lines) > 0">lines must be present</sch:assert>
      </sch:rule>
    <sch:rule context="lines">
      <sch:assert test="count(.//Line) > 0">Line must be present</sch:assert>
      </sch:rule>
    <sch:rule context="lines">
      <sch:assert test="count(.//FlexibleLine) = 0">FlexibleLine must NOT be present</sch:assert>
      </sch:rule>
    <sch:rule context="ServiceFrame">
      <sch:assert test="count(.//groupsOfLines) = 0">groupsOfLines must NOT be present</sch:assert>
      </sch:rule>
    <sch:rule context="groupsOfLines">
      <sch:assert test="count(.//GroupOfLines) = 0">GroupOfLines must NOT be present</sch:assert>
      </sch:rule>
    <sch:rule context="connections">
      <sch:assert test="count(.//Access) = 0">Access must NOT be present</sch:assert>
      </sch:rule>
    <sch:rule context="PassengerStopAssignment">
      <sch:assert test="count(.//ScheduledStopPointRef) > 0">ScheduledStopPointRef must be present</sch:assert>
      </sch:rule>
    <sch:rule context="PassengerStopAssignment">
      <sch:assert test="count(.//StopPlaceRef) > 0">StopPlaceRef must be present</sch:assert>
      </sch:rule>
    </sch:pattern>
  </sch:schema>
