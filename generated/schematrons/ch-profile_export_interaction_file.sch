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
      <sch:assert test="count(netex:TimetableFrame) > 0">TimetableFrame must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:TimetableFrame">
      <sch:assert test="count(netex:journeyMeetings) = 0">journeyMeetings must NOT be present</sch:assert>
      <sch:assert test="count(netex:interchangeRules) > 0">interchangeRules must be present</sch:assert>
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
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:TimetableFrame/netex:interchangeRules">
      <sch:assert test="count(netex:InterchangeRule) > 0">InterchangeRule must be present</sch:assert>
      </sch:rule>
    </sch:pattern>
  </sch:schema>

