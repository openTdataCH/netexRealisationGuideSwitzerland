<?xml version="1.0" encoding="UTF-8"?>
<sch:schema xmlns:sch="http://purl.oclc.org/dsdl/schematron" queryBinding="xslt1" xmlns:ns="http://www.netex.org.uk/netex">
  <sch:title>Generated schematron from template</sch:title>
  <sch:pattern id="p1">
    <sch:rule context="ns:ResourceFrame">
      <sch:assert test="count(.//ns:responsibilitySets) &amp;gt; 0">responsibilitySets must be present</sch:assert>
      </sch:rule>
    <sch:rule context="ns:responsibilitySets">
      <sch:assert test="count(.//ns:ResponsibilitySet) &amp;gt; 0">ResponsibilitySet must be present</sch:assert>
      </sch:rule>
    <sch:rule context="ns:values">
      <!-- TypeOfNotice with id="ch:1:TypeOfNotice:11" must exist somewhere in the document -->
      <sch:assert test="count(//ns:TypeOfNotice[@id='ch:1:TypeOfNotice:11']) &amp;gt; 0">An element TypeOfNotice with id="ch:1:TypeOfNotice:11" must exist</sch:assert>
      </sch:rule>
    <sch:rule context="ns:values">
      <!-- TypeOfNotice with id="ch:1:TypeOfNotice:1" must exist somewhere in the document -->
      <sch:assert test="count(//ns:TypeOfNotice[@id='ch:1:TypeOfNotice:1']) &amp;gt; 0">An element TypeOfNotice with id="ch:1:TypeOfNotice:1" must exist</sch:assert>
      </sch:rule>
    <sch:rule context="ns:values">
      <!-- TypeOfNotice with id="ch:1:TypeOfNotice:10" must exist somewhere in the document -->
      <sch:assert test="count(//ns:TypeOfNotice[@id='ch:1:TypeOfNotice:10']) &amp;gt; 0">An element TypeOfNotice with id="ch:1:TypeOfNotice:10" must exist</sch:assert>
      </sch:rule>
    <sch:rule context="ns:values">
      <!-- TypeOfNotice with id="ch:1:TypeOfNotice:3" must exist somewhere in the document -->
      <sch:assert test="count(//ns:TypeOfNotice[@id='ch:1:TypeOfNotice:3']) &amp;gt; 0">An element TypeOfNotice with id="ch:1:TypeOfNotice:3" must exist</sch:assert>
      </sch:rule>
    <sch:rule context="ns:values">
      <!-- TypeOfNotice with id="ch:1:TypeOfNotice:2" must exist somewhere in the document -->
      <sch:assert test="count(//ns:TypeOfNotice[@id='ch:1:TypeOfNotice:2']) &amp;gt; 0">An element TypeOfNotice with id="ch:1:TypeOfNotice:2" must exist</sch:assert>
      </sch:rule>
    <sch:rule context="ns:values">
      <sch:assert test="count(.//ns:TypeOfProductCategory) &amp;gt; 0">TypeOfProductCategory must be present</sch:assert>
      </sch:rule>
    <sch:rule context="ns:values">
      <!-- TypeOfProductCategory with id="ch:1:TypeOfProductCategory:TER" must exist somewhere in the document -->
      <sch:assert test="count(//ns:TypeOfProductCategory[@id='ch:1:TypeOfProductCategory:TER']) &amp;gt; 0">An element TypeOfProductCategory with id="ch:1:TypeOfProductCategory:TER" must exist</sch:assert>
      </sch:rule>
    <sch:rule context="ns:Operator">
      <sch:assert test="count(.//ns:Operator) &amp;gt; 0">Operator must be present</sch:assert>
      </sch:rule>
    <sch:rule context="ns:keyList">
      <sch:assert test="count(.//ns:KeyValue) &amp;gt; 0">KeyValue must be present</sch:assert>
      </sch:rule>
    <sch:rule context="ns:Operator">
      <sch:assert test="count(.//ns:PrivateCode) &amp;gt; 0">PrivateCode must be present</sch:assert>
      </sch:rule>
    <sch:rule context="ns:Operator">
      <sch:assert test="count(.//ns:Name) &amp;gt; 0">Name must be present</sch:assert>
      </sch:rule>
    <sch:rule context="ns:Operator">
      <sch:assert test="count(.//ns:ShortName) &amp;gt; 0">ShortName must be present</sch:assert>
      </sch:rule>
    <sch:rule context="ns:organisations">
      <sch:assert test="count(.//ns:Operator) &amp;gt; 0">Operator must be present</sch:assert>
      </sch:rule>
    <sch:rule context="ns:ServiceFrame">
      <sch:assert test="count(.//ns:directions) = 0">directions must NOT be present</sch:assert>
      </sch:rule>
    <sch:rule context="ns:directions">
      <sch:assert test="count(.//ns:Direction) = 0">Direction must NOT be present</sch:assert>
      </sch:rule>
    <sch:rule context="ns:ServiceFrame">
      <sch:assert test="count(.//ns:lines) &amp;gt; 0">lines must be present</sch:assert>
      </sch:rule>
    <sch:rule context="ns:lines">
      <sch:assert test="count(.//ns:Line) &amp;gt; 0">Line must be present</sch:assert>
      </sch:rule>
    <sch:rule context="ns:lines">
      <sch:assert test="count(.//ns:FlexibleLine) = 0">FlexibleLine must NOT be present</sch:assert>
      </sch:rule>
    <sch:rule context="ns:ServiceFrame">
      <sch:assert test="count(.//ns:groupsOfLines) = 0">groupsOfLines must NOT be present</sch:assert>
      </sch:rule>
    <sch:rule context="ns:groupsOfLines">
      <sch:assert test="count(.//ns:GroupOfLines) = 0">GroupOfLines must NOT be present</sch:assert>
      </sch:rule>
    <sch:rule context="ns:connections">
      <sch:assert test="count(.//ns:Access) = 0">Access must NOT be present</sch:assert>
      </sch:rule>
    <sch:rule context="ns:PassengerStopAssignment">
      <sch:assert test="count(.//ns:ScheduledStopPointRef) &amp;gt; 0">ScheduledStopPointRef must be present</sch:assert>
      </sch:rule>
    <sch:rule context="ns:PassengerStopAssignment">
      <sch:assert test="count(.//ns:StopPlaceRef) &amp;gt; 0">StopPlaceRef must be present</sch:assert>
      </sch:rule>
    <sch:rule context="ns:stopAssignments">
      <sch:assert test="count(.//ns:DeckEntranceAssignment) = 0">DeckEntranceAssignment must NOT be present</sch:assert>
      </sch:rule>
    <sch:rule context="ns:stopAssignments">
      <sch:assert test="count(.//ns:NavigationPathAssignment) = 0">NavigationPathAssignment must NOT be present</sch:assert>
      </sch:rule>
    </sch:pattern>
  </sch:schema>
