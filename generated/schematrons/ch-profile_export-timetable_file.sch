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
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ResourceFrame/netex:siteFacilitySets/netex:SiteFacilitySet/netex:validityConditions/netex:AvailabilityCondition">
      <sch:assert test="count(@id) > 0">Attribute "id" must be present on AvailabilityCondition</sch:assert>
      <sch:assert test="count(@version) > 0">Attribute "version" must be present on AvailabilityCondition</sch:assert>
      <sch:assert test="count(netex:IsAvailable) > 0">IsAvailable must be present</sch:assert>
      <sch:assert test="count(netex:ValidDayBits) > 0">ValidDayBits must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ResourceFrame/netex:siteFacilitySets/netex:SiteFacilitySet/netex:validityConditions/netex:AvailabilityCondition/netex:timebands/netex:Timeband">
      <sch:assert test="count(@id) > 0">Attribute "id" must be present on Timeband</sch:assert>
      <sch:assert test="count(@version) > 0">Attribute "version" must be present on Timeband</sch:assert>
      <sch:assert test="count(netex:StartTime) > 0">StartTime must be present</sch:assert>
      <sch:assert test="count(netex:EndTime) > 0">EndTime must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ResourceFrame/netex:serviceFacilitySets/netex:ServiceFacilitySet">
      <sch:assert test="count(netex:accommodations) = 0">accommodations must NOT be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ServiceFrame">
      <sch:assert test="count(netex:directions) = 0">directions must NOT be present</sch:assert>
      <sch:assert test="count(netex:lines) > 0">lines must be present</sch:assert>
      <sch:assert test="count(netex:groupsOfLines) = 0">groupsOfLines must NOT be present</sch:assert>
      <sch:assert test="count(netex:scheduledStopPoints) > 0">scheduledStopPoints must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ServiceFrame/netex:directions">
      <sch:assert test="count(netex:Direction) = 0">Direction must NOT be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ServiceFrame/netex:lines">
      <sch:assert test="count(netex:Line) > 0">Line must be present</sch:assert>
      <sch:assert test="count(netex:Line) > 0">Line must be present</sch:assert>
      <sch:assert test="count(netex:FlexibleLine) = 0">FlexibleLine must NOT be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ServiceFrame/netex:lines/netex:Line">
      <sch:assert test="count(@responsibilitySetRef) > 0">Attribute "responsibilitySetRef" must be present on Line</sch:assert>
      <sch:assert test="count(netex:keyList) > 0">keyList must be present</sch:assert>
      <sch:assert test="count(netex:Name) > 0">Name must be present</sch:assert>
      <sch:assert test="count(netex:TransportMode) > 0">TransportMode must be present</sch:assert>
      <sch:assert test="count(netex:PublicCode) > 0">PublicCode must be present</sch:assert>
      <sch:assert test="count(netex:AuthorityRef) > 0">AuthorityRef must be present</sch:assert>
      <sch:assert test="count(netex:TypeOfProductCategoryRef) > 0">TypeOfProductCategoryRef must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ServiceFrame/netex:groupsOfLines">
      <sch:assert test="count(netex:GroupOfLines) = 0">GroupOfLines must NOT be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ServiceFrame/netex:destinationDisplays/netex:DestinationDisplay/netex:Name">
      <sch:assert test="count(@lang) > 0">Attribute "lang" must be present on Name</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ServiceFrame/netex:destinationDisplays/netex:DestinationDisplay">
      <sch:assert test="count(netex:Name) > 0">Name must be present</sch:assert>
      <sch:assert test="count(netex:PrivateCode) > 0">PrivateCode must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ServiceFrame/netex:scheduledStopPoints/netex:ScheduledStopPoint/netex:scheduledStopPoints">
      <sch:assert test="count(netex:ScheduledStopPoint) > 0">ScheduledStopPoint must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ServiceFrame/netex:scheduledStopPoints/netex:ScheduledStopPoint/netex:scheduledStopPoints/netex:ScheduledStopPoint">
      <sch:assert test="count(netex:keyList) > 0">keyList must be present</sch:assert>
      <sch:assert test="count(netex:Name) > 0">Name must be present</sch:assert>
      <sch:assert test="count(netex:ShortName) > 0">ShortName must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ServiceFrame/netex:scheduledStopPoints/netex:ScheduledStopPoint/netex:scheduledStopPoints/netex:ScheduledStopPoint/netex:keyList">
      <sch:assert test="count(netex:KeyValue) > 0">KeyValue must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ServiceFrame/netex:scheduledStopPoints/netex:ScheduledStopPoint/netex:scheduledStopPoints/netex:ScheduledStopPoint/netex:keyList/netex:KeyValue">
      <sch:assert test="count(netex:Key) > 0">Key must be present</sch:assert>
      <sch:assert test="count(netex:Value) > 0">Value must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ServiceFrame/netex:connections">
      <sch:assert test="count(netex:Access) = 0">Access must NOT be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ServiceFrame/netex:connections/netex:SiteConnection">
      <sch:assert test="count(netex:WalkTransferDuration) > 0">WalkTransferDuration must be present</sch:assert>
      <sch:assert test="count(netex:From) > 0">From must be present</sch:assert>
      <sch:assert test="count(netex:To) > 0">To must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ServiceFrame/netex:connections/netex:SiteConnection/netex:WalkTransferDuration">
      <sch:assert test="count(netex:DefaultDuration) > 0">DefaultDuration must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ServiceFrame/netex:connections/netex:SiteConnection/netex:From">
      <sch:assert test="count(netex:StopPlaceRef) > 0">StopPlaceRef must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ServiceFrame/netex:connections/netex:DefaultConnection/netex:Extensions">
      <sch:assert test="count(netex:FromProductCategoryRef) > 0">FromProductCategoryRef must be present</sch:assert>
      <sch:assert test="count(netex:ToProductCategoryRef) > 0">ToProductCategoryRef must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ServiceFrame/netex:connections/netex:DefaultConnection">
      <sch:assert test="count(netex:TransferDuration) > 0">TransferDuration must be present</sch:assert>
      <sch:assert test="count(netex:From) > 0">From must be present</sch:assert>
      <sch:assert test="count(netex:To) > 0">To must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ServiceFrame/netex:connections/netex:DefaultConnection/netex:TransferDuration">
      <sch:assert test="count(netex:DefaultDuration) > 0">DefaultDuration must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ServiceFrame/netex:connections/netex:DefaultConnection/netex:From/netex:OperatorView">
      <sch:assert test="count(netex:OperatorRef) > 0">OperatorRef must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ServiceFrame/netex:connections/netex:DefaultConnection/netex:To/netex:OperatorView">
      <sch:assert test="count(netex:OperatorRef) > 0">OperatorRef must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ServiceFrame/netex:stopAssignments">
      <sch:assert test="count(netex:PassengerStopAssignment) > 0">PassengerStopAssignment must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ServiceFrame/netex:stopAssignments/netex:PassengerStopAssignment">
      <sch:assert test="count(netex:ScheduledStopPointRef) > 0">ScheduledStopPointRef must be present</sch:assert>
      <sch:assert test="count(netex:StopPlaceRef) > 0">StopPlaceRef must be present</sch:assert>
      <sch:assert test="count(netex:BoardingPositionRef) = 0">BoardingPositionRef must NOT be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ServiceFrame/netex:notices/netex:Notice">
      <sch:assert test="count(@id) > 0">Attribute "id" must be present on Notice</sch:assert>
      <sch:assert test="count(@version) > 0">Attribute "version" must be present on Notice</sch:assert>
      <sch:assert test="count(netex:PublicCode) > 0">PublicCode must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ServiceFrame/netex:notices/netex:Notice/netex:alternativeTexts">
      <sch:assert test="count(netex:AlternativeText) > 0">AlternativeText must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ServiceFrame/netex:notices/netex:Notice/netex:alternativeTexts/netex:AlternativeText">
      <sch:assert test="count(@id) > 0">Attribute "id" must be present on AlternativeText</sch:assert>
      <sch:assert test="count(@version) > 0">Attribute "version" must be present on AlternativeText</sch:assert>
      <sch:assert test="count(@attributeName) > 0">Attribute "attributeName" must be present on AlternativeText</sch:assert>
      <sch:assert test="count(@useForLanguage) > 0">Attribute "useForLanguage" must be present on AlternativeText</sch:assert>
      <sch:assert test="count(netex:Text) > 0">Text must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ServiceFrame/netex:notices/netex:Notice/netex:Text">
      <sch:assert test="count(@lang) > 0">Attribute "lang" must be present on Text</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:TimetableFrame">
      <sch:assert test="count(@id) > 0">Attribute "id" must be present on TimetableFrame</sch:assert>
      <sch:assert test="count(@version/versionRef) > 0">Attribute "version/versionRef" must be present on TimetableFrame</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:TimetableFrame/netex:vehicleJourneys/netex:ServiceJourney">
      <sch:assert test="count(@id) > 0">Attribute "id" must be present on ServiceJourney</sch:assert>
      <sch:assert test="count(@version) > 0">Attribute "version" must be present on ServiceJourney</sch:assert>
      <sch:assert test="count(@responsibilitySetRef) > 0">Attribute "responsibilitySetRef" must be present on ServiceJourney</sch:assert>
      <sch:assert test="count(netex:validityConditions) > 0">validityConditions must be present</sch:assert>
      <sch:assert test="count(netex:keyList) > 0">keyList must be present</sch:assert>
      <sch:assert test="count(netex:ServiceAlteration) > 0">ServiceAlteration must be present</sch:assert>
      <sch:assert test="count(netex:LineRef) > 0">LineRef must be present</sch:assert>
      <sch:assert test="count(netex:DirectionType) > 0">DirectionType must be present</sch:assert>
      <sch:assert test="count(netex:trainNumbers) > 0">trainNumbers must be present</sch:assert>
      <sch:assert test="count(netex:passingTimes) > 0">passingTimes must be present</sch:assert>
      <sch:assert test="count(netex:calls) = 0">calls must NOT be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:TimetableFrame/netex:vehicleJourneys/netex:ServiceJourney/netex:validityConditions">
      <sch:assert test="count(netex:AvailabilityCondition) > 0">AvailabilityCondition must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:TimetableFrame/netex:vehicleJourneys/netex:ServiceJourney/netex:validityConditions/netex:AvailabilityCondition">
      <sch:assert test="count(netex:FromDate) > 0">FromDate must be present</sch:assert>
      <sch:assert test="count(netex:ToDate) > 0">ToDate must be present</sch:assert>
      <sch:assert test="count(netex:IsAvailable) > 0">IsAvailable must be present</sch:assert>
      <sch:assert test="count(netex:ValidDayBits) > 0">ValidDayBits must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:TimetableFrame/netex:vehicleJourneys/netex:ServiceJourney/netex:keyList">
      <sch:assert test="count(netex:KeyValue) > 0">KeyValue must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:TimetableFrame/netex:vehicleJourneys/netex:ServiceJourney/netex:keyList/netex:KeyValue">
      <sch:assert test="count(netex:Key) > 0">Key must be present</sch:assert>
      <sch:assert test="count(netex:Value) > 0">Value must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:TimetableFrame/netex:vehicleJourneys/netex:ServiceJourney/netex:Extensions/netex:facilities/netex:Facility">
      <sch:assert test="count(netex:ServiceFacilitySetRef) > 0">ServiceFacilitySetRef must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:TimetableFrame/netex:vehicleJourneys/netex:ServiceJourney/netex:noticeAssignments/netex:NoticeAssignment">
      <sch:assert test="count(@id) > 0">Attribute "id" must be present on NoticeAssignment</sch:assert>
      <sch:assert test="count(@version) > 0">Attribute "version" must be present on NoticeAssignment</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:TimetableFrame/netex:vehicleJourneys/netex:ServiceJourney/netex:occupancies/netex:OccupancyView">
      <sch:assert test="count(@id) > 0">Attribute "id" must be present on OccupancyView</sch:assert>
      <sch:assert test="count(@version) > 0">Attribute "version" must be present on OccupancyView</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:TimetableFrame/netex:vehicleJourneys/netex:ServiceJourney/netex:occupancies/netex:OccupancyView/netex:FareClass">
      <sch:assert test="(. = 'firstClass' or . = 'secondClass' or . = 'unknown')">Value must be one of: firstClass secondClass unknown</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:TimetableFrame/netex:vehicleJourneys/netex:ServiceJourney/netex:occupancies/netex:OccupancyView/netex:OccupancyLevel">
      <sch:assert test="(. = 'unknown' or . = 'empty' or . = 'manySeatsAvailable' or . = 'fewSeatsAvailable' or . = 'standingRoomOnly' or . = 'crushedStandingRoomOnly' or . = 'full' or . = 'notAcceptingPassengers' or . = 'undefined')">Value must be one of: unknown empty manySeatsAvailable fewSeatsAvailable standingRoomOnly crushedStandingRoomOnly full notAcceptingPassengers undefined</sch:assert>
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
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:TimetableFrame/netex:vehicleJourneys/netex:ServiceJourney/netex:passingTimes/netex:TimetabledPassingTime">
      <sch:assert test="count(@id) > 0">Attribute "id" must be present on TimetabledPassingTime</sch:assert>
      <sch:assert test="count(@version) > 0">Attribute "version" must be present on TimetabledPassingTime</sch:assert>
      <sch:assert test="count(netex:StopPointInJourneyPatternRef) > 0">StopPointInJourneyPatternRef must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:TimetableFrame/netex:vehicleJourneys/netex:TemplateServiceJourney">
      <sch:assert test="count(@id) > 0">Attribute "id" must be present on TemplateServiceJourney</sch:assert>
      <sch:assert test="count(@version) > 0">Attribute "version" must be present on TemplateServiceJourney</sch:assert>
      <sch:assert test="count(@responsibilitySetRef) > 0">Attribute "responsibilitySetRef" must be present on TemplateServiceJourney</sch:assert>
      <sch:assert test="count(netex:keyList) > 0">keyList must be present</sch:assert>
      <sch:assert test="count(netex:ServiceAlteration) > 0">ServiceAlteration must be present</sch:assert>
      <sch:assert test="count(netex:LineRef) > 0">LineRef must be present</sch:assert>
      <sch:assert test="count(netex:trainNumbers) > 0">trainNumbers must be present</sch:assert>
      <sch:assert test="count(netex:calls) = 0">calls must NOT be present</sch:assert>
      <sch:assert test="count(netex:frequencyGroups) > 0">frequencyGroups must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:TimetableFrame/netex:vehicleJourneys/netex:TemplateServiceJourney/netex:keyList">
      <sch:assert test="count(netex:KeyValue) > 0">KeyValue must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:TimetableFrame/netex:vehicleJourneys/netex:TemplateServiceJourney/netex:keyList/netex:KeyValue">
      <sch:assert test="count(netex:Key) > 0">Key must be present</sch:assert>
      <sch:assert test="count(netex:Value) > 0">Value must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:TimetableFrame/netex:vehicleJourneys/netex:TemplateServiceJourney/netex:Extensions/netex:facilities/netex:Facility">
      <sch:assert test="count(netex:ServiceFacilitySetRef) > 0">ServiceFacilitySetRef must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:TimetableFrame/netex:vehicleJourneys/netex:TemplateServiceJourney/netex:ServiceAlteration">
      <sch:assert test="(. = 'planned')">Value must be one of: planned</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:TimetableFrame/netex:vehicleJourneys/netex:TemplateServiceJourney/netex:DirectionType">
      <sch:assert test="(. = 'inbound' or . = 'outbound')">Value must be one of: inbound outbound</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:TimetableFrame/netex:vehicleJourneys/netex:TemplateServiceJourney/netex:trainNumbers">
      <sch:assert test="count(netex:TrainNumberRef) > 0">TrainNumberRef must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:TimetableFrame/netex:vehicleJourneys/netex:TemplateServiceJourney/netex:TemplateVehicleJourneyType">
      <sch:assert test="(. = 'rhythmic' or . = 'headway')">Value must be one of: rhythmic headway</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:TimetableFrame/netex:vehicleJourneys/netex:TemplateServiceJourney/netex:frequencyGroups/netex:RhythmicalJourneyGroup">
      <sch:assert test="count(netex:FirstDepartureTime) > 0">FirstDepartureTime must be present</sch:assert>
      <sch:assert test="count(netex:LastDepartureTime) > 0">LastDepartureTime must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:TimetableFrame/netex:vehicleJourneys/netex:TemplateServiceJourney/netex:frequencyGroups/netex:HeadwayJourneyGroup">
      <sch:assert test="count(netex:FirstDepartureTime) > 0">FirstDepartureTime must be present</sch:assert>
      <sch:assert test="count(netex:LastDepartureTime) > 0">LastDepartureTime must be present</sch:assert>
      <sch:assert test="count(netex:ScheduledHeadwayInterval) > 0">ScheduledHeadwayInterval must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:TimetableFrame/netex:vehicleJourneys/netex:TemplateServiceJourney/netex:frequencyGroups/netex:HeadwayJourneyGroup/netex:HeadwayDisplay">
      <sch:assert test="(. = 'displayPassingTimesOnly' or . = 'displayInsteadOfPassingTimes' or . = 'displayAsWellAsPassingTimes')">Value must be one of: displayPassingTimesOnly displayInsteadOfPassingTimes displayAsWellAsPassingTimes</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:TimetableFrame/netex:trainNumbers">
      <sch:assert test="count(netex:TrainNumber) > 0">TrainNumber must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:TimetableFrame/netex:trainNumbers/netex:TrainNumber">
      <sch:assert test="count(@id) > 0">Attribute "id" must be present on TrainNumber</sch:assert>
      <sch:assert test="count(@version) > 0">Attribute "version" must be present on TrainNumber</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:TimetableFrame/netex:typesOfService/netex:TypeOfService">
      <!-- TypeOfService with id="ch:1:TypeOfService:1" must exist somewhere in the document -->
      <sch:report test="count(//netex:TypeOfService[@id='ch:1:TypeOfService:1']) > 0">An element TypeOfService with id="ch:1:TypeOfService:1" must exist</sch:report>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:TimetableFrame/netex:journeyMeetings/netex:JourneyMeeting">
      <sch:assert test="count(@id) > 0">Attribute "id" must be present on JourneyMeeting</sch:assert>
      <sch:assert test="count(@version) > 0">Attribute "version" must be present on JourneyMeeting</sch:assert>
      <sch:assert test="count(netex:AtStopPointRef) > 0">AtStopPointRef must be present</sch:assert>
      <sch:assert test="count(netex:FromJourneyRef) > 0">FromJourneyRef must be present</sch:assert>
      <sch:assert test="count(netex:ToJourneyRef) > 0">ToJourneyRef must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:TimetableFrame/netex:journeyMeetings/netex:JourneyMeeting/netex:Reason">
      <sch:assert test="(. = 'joining' or . = 'splitting' or . = 'tariffSection' or . = 'serviceFacility')">Value must be one of: joining splitting tariffSection serviceFacility</sch:assert>
      </sch:rule>
    </sch:pattern>
  </sch:schema>

