<?xml version="1.0" encoding="UTF-8"?><sch:schema xmlns:sch="http://purl.oclc.org/dsdl/schematron" xmlns:netex="http://www.netex.org.uk/netex" queryBinding="xslt2">
  <sch:ns prefix="netex" uri="http://www.netex.org.uk/netex"/>
  <sch:title>Generated schematron from template</sch:title>
  <sch:pattern id="p1">
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ResourceFrame">
      <sch:assert test="count(netex:responsibilitySets) > 0">responsibilitySets must be present</sch:assert>
      <sch:assert test="count(netex:typesOfValue) > 0">typesOfValue must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ResourceFrame/netex:responsibilitySets">
      <sch:assert test="count(netex:ResponsibilitySet) > 0">ResponsibilitySet must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ResourceFrame/netex:typesOfValue">
      <sch:assert test="count(netex:ValueSet) > 0">ValueSet must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ResourceFrame/netex:typesOfValue/netex:ValueSet">
      <sch:assert test="count(netex:values) > 0">values must be present</sch:assert>
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
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ResourceFrame/netex:typesOfValue/netex:ValueSet/netex:values">
      <sch:assert test="count(netex:TypeOfProductCategory) > 0">TypeOfProductCategory must be present</sch:assert>
      <sch:assert test="count(netex:TypeOfProductCategory) > 0">TypeOfProductCategory must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ResourceFrame/netex:typesOfValue/netex:ValueSet/netex:values/netex:TypeOfProductCategory">
      <sch:assert test="count(netex:alternativeTexts) > 0">alternativeTexts must be present</sch:assert>
      <sch:assert test="count(netex:Name) > 0">Name must be present</sch:assert>
      <sch:assert test="count(netex:ShortName) > 0">ShortName must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ResourceFrame/netex:typesOfValue/netex:ValueSet/netex:values/netex:TypeOfProductCategory/netex:alternativeTexts">
      <sch:assert test="count(netex:AlternativeText) > 0">AlternativeText must be present</sch:assert>
      <sch:assert test="count(netex:AlternativeText) > 0">AlternativeText must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ResourceFrame/netex:organisations">
      <sch:assert test="count(netex:Operator) > 0">Operator must be present</sch:assert>
      <sch:assert test="count(netex:Operator) > 0">Operator must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames/netex:ResourceFrame/netex:organisations/netex:Operator">
      <sch:assert test="count(netex:keyList) > 0">keyList must be present</sch:assert>
      <sch:assert test="count(netex:PrivateCode) > 0">PrivateCode must be present</sch:assert>
      <sch:assert test="count(netex:Name) > 0">Name must be present</sch:assert>
      <sch:assert test="count(netex:ShortName) > 0">ShortName must be present</sch:assert>
      </sch:rule>
    <sch:rule context="//netex:PublicationDelivery/netex:dataObjects/netex:CompositeFrame/netex:frames">
      <sch:assert test="count(netex:SiteFrame) > 0">SiteFrame must be present</sch:assert>
      </sch:rule>
    </sch:pattern>
  </sch:schema>

