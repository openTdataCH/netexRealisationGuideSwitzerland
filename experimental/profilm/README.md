# XML Language to define profile

Idea: Instead of Schematron or Example/Template, define schema changes in an XML document.

For this, a domain specific XML language is used. This is kind of a schema manipulation language, similar to DDL for databases.

## StopPlace Example
```xml
<?xml version="1.0" encoding="utf8" ?>
<profile>
    <Node type="complexType" name="StopPlaceType">
        <Change type="AddDocumentation">
            Adds a description to an annotation/documentation element with this description.
        </Change>
        <Change type="RemoveElement" name="Weighting"/>
        <Change type="RemoveAttribute" name="version"/>
        <Change type="AlterElement" name="Centroid" minOccurs="1"/>
        <Change type="AlterElement" name="Extensions">
            <xsd:element name="CustomExtension" type="xsd:string">
                 <xsd:annotation>
                    <xsd:documentation xml:lang="en">Description of custom element ...</xsd:documentation>
                </xsd:annotation>
            </xsd:element>
        </Change>
    </Node>
    
    <Node type="complexType" name="ExtensionsType">
        <Change type="AddElement" name="ValidBetween">
            <xsd:sequence>
                <xsd:element name="HafasPriority" minOccurs="0">
                    <xsd:complexType>
                        <xsd:sequence>
                            <xsd:element name="Value" type="xsd:int"/>
                        </xsd:sequence>
                    </xsd:complexType>
                </xsd:element>
            </xsd:sequence>
        </Change>
    </Node>
    
    <Node type="simpleType" name="bikeType">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:enumeration value="Gravel"/>
                <xs:enumeration value="Mountain"/>
                <xs:enumeration value="Race"/>
            </xs:restriction>
        </xs:simpleType>
     </Node>
    
</profile>

```