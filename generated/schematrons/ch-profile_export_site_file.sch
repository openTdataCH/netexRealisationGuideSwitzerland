<?xml version="1.0" encoding="UTF-8"?><sch:schema xmlns:sch="http://purl.oclc.org/dsdl/schematron" xmlns:netex="http://www.netex.org.uk/netex" queryBinding="xslt2">
  <sch:ns prefix="netex" uri="http://www.netex.org.uk/netex"/>
  <sch:title>Generated schematron from template</sch:title>
  <sch:pattern id="p1">
    <sch:rule context="//netex:PublicationDelivery">
      <sch:assert test="count(netex:PublicationTimestamp) > 0">PublicationTimestamp must be present</sch:assert>
      <sch:assert test="count(netex:ParticipantRef) > 0">ParticipantRef must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:FrameDefaults">
      <sch:assert test="count(netex:DefaultLocale) > 0">DefaultLocale must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:FrameDefaults/netex:DefaultLocale">
      <sch:assert test="count(netex:TimeZoneOffset) > 0">TimeZoneOffset must be present</sch:assert>
      <sch:assert test="count(netex:SummerTimeZoneOffset) > 0">SummerTimeZoneOffset must be present</sch:assert>
      <sch:assert test="count(netex:DefaultLanguage) > 0">DefaultLanguage must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames">
      <sch:assert test="count(netex:ResourceFrame) > 0">ResourceFrame must be present</sch:assert>
      <sch:assert test="count(netex:SiteFrame) > 0">SiteFrame must be present</sch:assert>
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
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:SiteFrame/netex:topographicPlaces">
      <sch:assert test="count(netex:TopographicPlace) > 0">TopographicPlace must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:SiteFrame/netex:topographicPlaces/netex:TopographicPlace">
      <sch:assert test="count(netex:Descriptor) > 0">Descriptor must be present</sch:assert>
      <sch:assert test="count(netex:TopographicPlaceType) > 0">TopographicPlaceType must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:SiteFrame/netex:topographicPlaces/netex:TopographicPlace/netex:Descriptor">
      <sch:assert test="count(netex:Name) > 0">Name must be present</sch:assert>
      <sch:assert test="count(netex:ShortName) > 0">ShortName must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:SiteFrame">
      <sch:assert test="count(netex:addresses) = 0">addresses must NOT be present</sch:assert>
      <sch:assert test="count(netex:accesses) = 0">accesses must NOT be present</sch:assert>
      <sch:assert test="count(netex:stopPlaces) > 0">stopPlaces must be present</sch:assert>
      <sch:assert test="count(netex:flexibleStopPlaces) = 0">flexibleStopPlaces must NOT be present</sch:assert>
      <sch:assert test="count(netex:navigationPaths) = 0">navigationPaths must NOT be present</sch:assert>
      <sch:assert test="count(netex:pointOfInterestClassifications) = 0">pointOfInterestClassifications must NOT be present</sch:assert>
      <sch:assert test="count(netex:pointOfInterestClassificationHierarchies) = 0">pointOfInterestClassificationHierarchies must NOT be present</sch:assert>
      <sch:assert test="count(netex:tariffZones) = 0">tariffZones must NOT be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:SiteFrame/netex:stopPlaces">
      <sch:assert test="count(netex:StopPlace) > 0">StopPlace must be present</sch:assert>
      <sch:assert test="count(netex:StopPlace) > 0">StopPlace must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:SiteFrame/netex:stopPlaces/netex:StopPlace">
      <sch:assert test="count(netex:keyList) > 0">keyList must be present</sch:assert>
      <sch:assert test="count(netex:Name) > 0">Name must be present</sch:assert>
      <sch:assert test="count(netex:PrivateCode) > 0">PrivateCode must be present</sch:assert>
      <sch:assert test="count(netex:Centroid) > 0">Centroid must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:SiteFrame/netex:stopPlaces/netex:StopPlace/netex:keyList">
      <sch:assert test="count(netex:KeyValue) > 0">KeyValue must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:SiteFrame/netex:stopPlaces/netex:StopPlace/netex:keyList/netex:KeyValue">
      <sch:assert test="count(netex:Key) > 0">Key must be present</sch:assert>
      <sch:assert test="count(netex:Value) > 0">Value must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:SiteFrame/netex:stopPlaces/netex:StopPlace/netex:Centroid">
      <sch:assert test="count(netex:Location) > 0">Location must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:SiteFrame/netex:stopPlaces/netex:StopPlace/netex:Centroid/netex:Location">
      <sch:assert test="count(netex:Longitude) > 0">Longitude must be present</sch:assert>
      <sch:assert test="count(netex:Latitude) > 0">Latitude must be present</sch:assert>
      <sch:assert test="count(netex:Altitude) > 0">Altitude must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:SiteFrame/netex:stopPlaces/netex:StopPlace/netex:alternativeNames">
      <sch:assert test="count(netex:AlternativeName) > 0">AlternativeName must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:SiteFrame/netex:stopPlaces/netex:StopPlace/netex:alternativeNames/netex:AlternativeName/netex:NameType">
      <sch:assert test="(. = 'alias' or . = 'translation')">Value must be one of: alias translation</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:SiteFrame/netex:stopPlaces/netex:StopPlace/netex:alternativeNames/netex:AlternativeName">
      <sch:assert test="count(netex:Name) > 0">Name must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:SiteFrame/netex:stopPlaces/netex:StopPlace/netex:alternativeNames/netex:AlternativeName/netex:Name">
      <sch:assert test="count(@lang) > 0">Attribute "lang" must be present on Name</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:SiteFrame/netex:stopPlaces/netex:StopPlace/netex:quays/netex:Quay">
      <sch:assert test="count(netex:keyList) > 0">keyList must be present</sch:assert>
      <sch:assert test="count(netex:Centroid) > 0">Centroid must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:SiteFrame/netex:stopPlaces/netex:StopPlace/netex:quays/netex:Quay/netex:keyList">
      <sch:assert test="count(netex:KeyValue) > 0">KeyValue must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:SiteFrame/netex:stopPlaces/netex:StopPlace/netex:quays/netex:Quay/netex:keyList/netex:KeyValue">
      <sch:assert test="count(netex:Key) > 0">Key must be present</sch:assert>
      <sch:assert test="count(netex:Value) > 0">Value must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:SiteFrame/netex:stopPlaces/netex:StopPlace/netex:quays/netex:Quay/netex:Centroid">
      <sch:assert test="count(netex:Location) > 0">Location must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:SiteFrame/netex:stopPlaces/netex:StopPlace/netex:quays/netex:Quay/netex:Centroid/netex:Location">
      <sch:assert test="count(netex:Longitude) > 0">Longitude must be present</sch:assert>
      <sch:assert test="count(netex:Latitude) > 0">Latitude must be present</sch:assert>
      <sch:assert test="count(netex:Altitude) > 0">Altitude must be present</sch:assert>
      </sch:rule>
    </sch:pattern>
  </sch:schema>

