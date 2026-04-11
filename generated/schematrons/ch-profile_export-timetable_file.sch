<?xml version="1.0" encoding="UTF-8"?><sch:schema xmlns:sch="http://purl.oclc.org/dsdl/schematron" xmlns:netex="http://www.netex.org.uk/netex" queryBinding="xslt2">
  <sch:ns prefix="netex" uri="http://www.netex.org.uk/netex"/>
  <sch:title>Generated schematron from template</sch:title>
  <sch:pattern id="p1">
    <sch:rule context="//netex:PublicationDelivery">
      <sch:assert test="count(netex:PublicationTimestamp) > 0">PublicationTimestamp must be present</sch:assert>
      <sch:assert test="count(netex:ParticipantRef) > 0">ParticipantRef must be present</sch:assert>
      <sch:assert test="count(netex:dataObjects) > 0">dataObjects must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects">
      <sch:assert test="count(netex:CompositeFrame) > 0">CompositeFrame must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame">
      <sch:assert test="count(netex:frames) > 0">frames must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames">
      <sch:assert test="count(netex:ResourceFrame) > 0">ResourceFrame must be present</sch:assert>
      <sch:assert test="count(netex:TimetableFrame) > 0">TimetableFrame must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ResourceFrame">
      <sch:assert test="count(netex:responsibilitySets) > 0">responsibilitySets must be present</sch:assert>
      <sch:assert test="count(netex:typesOfValue) > 0">typesOfValue must be present</sch:assert>
      <sch:assert test="count(netex:organisations) > 0">organisations must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ResourceFrame/netex:responsibilitySets">
      <sch:assert test="count(netex:ResponsibilitySet) > 0">ResponsibilitySet must be present</sch:assert>
      <sch:assert test="count(netex:ResponsibilitySet) > 0">ResponsibilitySet must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ResourceFrame/netex:typesOfValue/netex:ValueSet/netex:values/netex:TypeOfNotice">
      <!-- TypeOfNotice with id="ch:1:TypeOfNotice:11" must exist somewhere in the document -->
      <sch:report test="count(//netex:TypeOfNotice[@id='ch:1:TypeOfNotice:11']) > 0">An element TypeOfNotice with id="ch:1:TypeOfNotice:11" must exist</sch:report>
      <!-- TypeOfNotice with id="ch:1:TypeOfNotice:1" must exist somewhere in the document -->
      <sch:report test="count(//netex:TypeOfNotice[@id='ch:1:TypeOfNotice:1']) > 0">An element TypeOfNotice with id="ch:1:TypeOfNotice:1" must exist</sch:report>
      <!-- TypeOfNotice with id="ch:1:TypeOfNotice:10" must exist somewhere in the document -->
      <sch:report test="count(//netex:TypeOfNotice[@id='ch:1:TypeOfNotice:10']) > 0">An element TypeOfNotice with id="ch:1:TypeOfNotice:10" must exist</sch:report>
      <!-- TypeOfNotice with id="ch:1:TypeOfNotice:3" must exist somewhere in the document -->
      <sch:report test="count(//netex:TypeOfNotice[@id='ch:1:TypeOfNotice:3']) > 0">An element TypeOfNotice with id="ch:1:TypeOfNotice:3" must exist</sch:report>
      <!-- TypeOfNotice with id="ch:1:TypeOfNotice:2" must exist somewhere in the document -->
      <sch:report test="count(//netex:TypeOfNotice[@id='ch:1:TypeOfNotice:2']) > 0">An element TypeOfNotice with id="ch:1:TypeOfNotice:2" must exist</sch:report>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ResourceFrame/netex:typesOfValue">
      <sch:assert test="count(netex:ValueSet) > 0">ValueSet must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ResourceFrame/netex:typesOfValue/netex:ValueSet">
      <sch:assert test="count(netex:values) > 0">values must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ResourceFrame/netex:typesOfValue/netex:ValueSet/netex:values">
      <sch:assert test="count(netex:TypeOfProductCategory) > 0">TypeOfProductCategory must be present</sch:assert>
      <sch:assert test="count(netex:TypeOfProductCategory) > 0">TypeOfProductCategory must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ResourceFrame/netex:typesOfValue/netex:ValueSet/netex:values/netex:TypeOfProductCategory">
      <sch:assert test="count(netex:alternativeTexts) > 0">alternativeTexts must be present</sch:assert>
      <sch:assert test="count(netex:Name) > 0">Name must be present</sch:assert>
      <sch:assert test="count(netex:ShortName) > 0">ShortName must be present</sch:assert>
      <sch:assert test="count(netex:alternativeTexts) > 0">alternativeTexts must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ResourceFrame/netex:typesOfValue/netex:ValueSet/netex:values/netex:TypeOfProductCategory/netex:alternativeTexts">
      <sch:assert test="count(netex:AlternativeText) > 0">AlternativeText must be present</sch:assert>
      <sch:assert test="count(netex:AlternativeText) > 0">AlternativeText must be present</sch:assert>
      <sch:assert test="count(netex:AlternativeText) > 0">AlternativeText must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ResourceFrame/netex:typesOfValue/netex:ValueSet/netex:values/netex:TypeOfProductCategory/netex:alternativeTexts/netex:AlternativeText">
      <sch:assert test="count(netex:Text) > 0">Text must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ResourceFrame/netex:organisations">
      <sch:assert test="count(netex:Operator) > 0">Operator must be present</sch:assert>
      <sch:assert test="count(netex:Operator) > 0">Operator must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ResourceFrame/netex:siteFacilitySets">
      <sch:assert test="count(netex:SiteFacilitySet) > 0">SiteFacilitySet must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ResourceFrame/netex:siteFacilitySets/netex:SiteFacilitySet/netex:validityConditions">
      <sch:assert test="count(netex:AvailabilityCondition) > 0">AvailabilityCondition must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ResourceFrame/netex:serviceFacilitySets/netex:ServiceFacilitySet">
      <sch:assert test="count(netex:accommodations) = 0">accommodations must NOT be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ServiceFrame">
      <sch:assert test="count(netex:directions) = 0">directions must NOT be present</sch:assert>
      <sch:assert test="count(netex:lines) > 0">lines must be present</sch:assert>
      <sch:assert test="count(netex:groupsOfLines) = 0">groupsOfLines must NOT be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ServiceFrame/netex:directions">
      <sch:assert test="count(netex:Direction) = 0">Direction must NOT be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ServiceFrame/netex:lines">
      <sch:assert test="count(netex:Line) > 0">Line must be present</sch:assert>
      <sch:assert test="count(netex:FlexibleLine) = 0">FlexibleLine must NOT be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ServiceFrame/netex:groupsOfLines">
      <sch:assert test="count(netex:GroupOfLines) = 0">GroupOfLines must NOT be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ServiceFrame/netex:connections">
      <sch:assert test="count(netex:Access) = 0">Access must NOT be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ServiceFrame/netex:stopAssignments">
      <sch:assert test="count(netex:PassengerStopAssignment) > 0">PassengerStopAssignment must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ServiceFrame/netex:stopAssignments/netex:PassengerStopAssignment">
      <sch:assert test="count(netex:ScheduledStopPointRef) > 0">ScheduledStopPointRef must be present</sch:assert>
      <sch:assert test="count(netex:StopPlaceRef) > 0">StopPlaceRef must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ServiceFrame/netex:notices">
      <sch:assert test="count(netex:Notice) > 0">Notice must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ServiceFrame/netex:notices/netex:Notice/netex:alternativeTexts">
      <sch:assert test="count(netex:AlternativeText) > 0">AlternativeText must be present</sch:assert>
      <sch:assert test="count(netex:AlternativeText) > 0">AlternativeText must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ServiceFrame/netex:notices/netex:Notice/netex:alternativeTexts/netex:AlternativeText">
      <sch:assert test="count(netex:Text) > 0">Text must be present</sch:assert>
      <sch:assert test="count(netex:Text) > 0">Text must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ServiceFrame/netex:notices/netex:Notice">
      <sch:assert test="count(netex:Text) > 0">Text must be present</sch:assert>
      <sch:assert test="count(netex:TypeOfNoticeRef) > 0">TypeOfNoticeRef must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:TimetableFrame/netex:vehicleJourneys/netex:ServiceJourney">
      <sch:assert test="count(netex:keyList) > 0">keyList must be present</sch:assert>
      <sch:assert test="count(netex:LineRef) > 0">LineRef must be present</sch:assert>
      <sch:assert test="count(netex:trainNumbers) > 0">trainNumbers must be present</sch:assert>
      <sch:assert test="count(netex:passingTimes) > 0">passingTimes must be present</sch:assert>
      <sch:assert test="count(netex:calls) = 0">calls must NOT be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:TimetableFrame/netex:vehicleJourneys/netex:ServiceJourney/netex:keyList">
      <sch:assert test="count(netex:KeyValue) > 0">KeyValue must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:TimetableFrame/netex:vehicleJourneys/netex:ServiceJourney/netex:keyList/netex:KeyValue">
      <sch:assert test="count(netex:Key) > 0">Key must be present</sch:assert>
      <sch:assert test="count(netex:Value) > 0">Value must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:TimetableFrame/netex:vehicleJourneys/netex:ServiceJourney/netex:ServiceAlteration">
      <sch:assert test="(. = 'planned')">Value must be one of: planned</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:TimetableFrame/netex:vehicleJourneys/netex:ServiceJourney/netex:DirectionType">
      <sch:assert test="(. = 'inbound' or . = 'outbound')">Value must be one of: inbound outbound</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:TimetableFrame/netex:vehicleJourneys/netex:ServiceJourney/netex:trainNumbers">
      <sch:assert test="count(netex:TrainNumberRef) > 0">TrainNumberRef must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:TimetableFrame/netex:trainNumbers">
      <sch:assert test="count(netex:TrainNumber) > 0">TrainNumber must be present</sch:assert>
      </sch:rule>
    </sch:pattern>
  </sch:schema>

