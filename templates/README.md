# Swiss NeTEx Profile Templates

This folder contains XML templates used to generate documentation, schematron validation files, and examples for the Swiss NeTEX profile.

## Overview

The templates use special comment annotations to define the Swiss profile requirements. These annotations are processed by various tools to generate:

1. **Markdown documentation tables** (via `md_builder.py`)
2. **Schematron validation files** (via `template2schematron.py`)
3. **Example XML files** (directly usable templates)

## Template Structure

Each template is a valid NeTEx XML file with special comment annotations that define profile-specific requirements.

### Basic Structure

```xml
<?xml version="1.0" encoding="UTF-8"?>
<RootElement xmlns="http://www.netex.org.uk/netex">
    <!-- ch-start: Description of this section -->
    <ChildElement>
        <!-- ch-usage: mandatory|forbidden|optional|ignored|expected -->
        <!-- ch-note: Description of the element -->
        <!-- ch-notice: Additional information -->
        <!-- Other annotations... -->
        Content
    </ChildElement>
    <!-- ch-stop: Description of this section -->
</RootElement>
```

## Annotation Reference

### Region Markers

- `<!-- ch-start: description -->`: Marks the beginning of a processing region
- `<!-- ch-stop: description -->`: Marks the end of a processing region
> **TODO** Is ch-stop needed or useful? What is the description for?

### Documentation Annotations

- `<!-- ch-note: text -->`: Adds descriptive notes (appears in documentation and schematron comments)
- `<!-- ch-notice: text -->`: Adds additional information (treated like ch-note)
> **TODO** ch-notice should disappear.

### Usage Control Annotations

- `<!-- ch-usage: mandatory -->`: Element must be present in valid documents
- `<!-- ch-usage: forbidden -->`: Element must not be present in valid documents
- `<!-- ch-usage: optional -->`: Element is optional
- `<!-- ch-usage: ignored -->`: Element is ignored (not processed)
- `<!-- ch-usage: expected -->`: Element is expected but not strictly required
> **TODO** For ch-usage: Would it make sense to add. ", the data producer should be able to provide a justification if missing." ? Or would that be inappropriate?

> **TODO** For ch-ignored:
> What happens with ignored or if ch-usage unspecified?
>
> Cases:
> - (A) ch-usage: ignored
> - (B) ch-usage unspecified, but element is part of template
> - (C) element is not part of template (only in xsd)
> 
> Proposal:
> - (A) - ignored by Schematron, appears in table to explicitely show that the element will be ignored
> - (B)- ignored by Schematron, not figuring in table
> - (C) - ignored by Schematron, not figuring in table
>   
>  What do others think?

### Advanced Annotations

- `<!-- ch-referenced -->`: References another template with the same name
- `<!-- ch-referenced: filename.xml -->`: References a specific template file
- `<!-- ch-allowed-enums: value1 value2 value3 -->`: Restricts element to specific enumeration values
- `<!-- ch-deprecated -->`: Marks element as deprecated
- `<!-- ch-class-id-must-exist -->`: Requires that referenced element with ID exists in document
- `<!-- ch-attrs: attr1 attr2 attr3 -->`: Specifies which attributes are allowed
> **TODO** Attributes that are allowed or that are mandatory?

> **TODO** I (trurlurl) find ch-referenced difficult to interpret; easier would be ch-see-template, ch-externally-defined, or ch-external

> **TODO** I would prefer all keywords always ending with a colon


## Attribute Handling

### versionRef vs version

In NeTEX, reference elements often use `versionRef` instead of `version` attributes. The documentation and example generation tools automatically convert these:

- **Input**: `<ElementRef versionRef="1">`
- **Output**: `<ElementRef version="1">`

This conversion happens in both the markdown documentation and XML snippet generation tools.

## Template Types

### Top-Level Templates

These are the main entry points for processing different aspects of the Swiss profile:

- `ch-profile_export-timetable_file.xml`: Timetable data export profile
- `ch-profile_export_resource_file.xml`: Resource data export profile
- `ch-profile_import-*.xml`: Import profiles (various types)
- `ch-profile_psa_file.xml`: Passenger Stop Assignments
- `ch-profile_interactions_file.xml`: Journey Meetings and Interchange Rules

### Component Templates

These are referenced by top-level templates and define specific elements:

- `Operator.xml`, `ResponsibilitySet.xml`, `SiteFacilitySet.xml`, etc.
- Type definitions like `TypeOfNotice.xml`, `TypeOfProductCategory.xml`
- Complex elements that are reused across multiple contexts

## Creating New Templates

### Best Practices

1. **Start with valid NeTEx XML**: Ensure your template is valid according to the NeTEX schema
2. **Use clear region markers**: Mark processing regions with `ch-start` and `ch-stop`
3. **Document thoroughly**: Use `ch-note` to explain profile decisions
4. **Be consistent**: Apply usage annotations consistently across similar elements
5. **Modular design**: Break complex structures into separate templates using `ch-referenced`
6. **Test thoroughly**: Validate generated output with real data

### Example: Simple Template

```xml
<?xml version="1.0" encoding="UTF-8"?>
<SimpleElement xmlns="http://www.netex.org.uk/netex" id="ch:example:Simple:1" version="1">
    <!-- ch-start: Simple element example -->
    
    <!-- Mandatory child element -->
    <RequiredChild>
        <!-- ch-usage: mandatory -->
        <!-- ch-note: This child element is required -->
        Required content
    </RequiredChild>
    
    <!-- Optional child element -->
    <OptionalChild>
        <!-- ch-usage: optional -->
        <!-- ch-note: This child element is optional -->
        Optional content
    </OptionalChild>
    
    <!-- Forbidden element (should not appear in valid documents) -->
    <ForbiddenChild>
        <!-- ch-usage: forbidden -->
        <!-- ch-note: This element should not be used -->
        Forbidden content
    </ForbiddenChild>
    
    <!-- ch-stop: Simple element example -->
</SimpleElement>
```

## Processing Templates

### Generating Schematron Files

```bash
# Process a single template
python tools/schematron_builder/template2schematron.py \
    -t templates/template_name.xml \
    -x xsd/xsd/NeTEx_publication.xsd \
    -i templates \
    -o generated/schematrons/output.sch \
    -v

# Process all templates
./tools/schematron_builder/build_schemas.sh
```

### Generating Markdown Documentation

```bash
# Generate markdown tables from templates
python tools/md_builder/md_builder.py \
    -i templates \
    -o generated/markdown \
    -x xsd/xsd/NeTEx_publication.xsd
```

## Validation

### Validating Templates

Templates should be valid NeTEx XML files. You can validate them using:

```bash
# Validate against NeTEx schema
xmllint --schema xsd/xsd/NeTEx_publication.xsd --noout templates/template_name.xml

# Validate generated schematron output
python tools/check_schematron/check_schematron.py \
    -i test_data.xml \
    -s generated/schematrons/output.sch
```

## Template Maintenance

### Adding New Elements

When adding new elements to the profile:

1. **Identify the appropriate template**: Find where the element should be defined
2. **Add the element with annotations**: Include usage, notes, and other relevant annotations
3. **Update references**: If the element is referenced elsewhere, update those templates
4. **Test the changes**: Generate output and validate with test data

### Deprecating Elements

To deprecate an element:

1. **Add deprecated annotation**: `<!-- ch-deprecated -->`
2. **Update usage if needed**: Often set to `optional` if not already
3. **Add deprecation note**: Explain when and why it was deprecated
4. **Document alternatives**: If available, mention replacement elements

```xml
<DeprecatedElement>
    <!-- ch-usage: optional -->
    <!-- ch-deprecated -->
    <!-- ch-note: Deprecated since v2.1, use NewElement instead -->
    Content
</DeprecatedElement>
```

## Common Patterns

### Mandatory Elements with Specific Content

```xml
<ElementWithSpecificContent>
    <!-- ch-usage: mandatory -->
    <!-- ch-allowed-enums: value1 value2 value3 -->
    <!-- ch-note: Must be one of the allowed values -->
    value1
</ElementWithSpecificContent>
```

### Referenced Elements

```xml
<ComplexElement>
    <!-- ch-usage: mandatory -->
    <!-- ch-referenced -->
    <!-- ch-note: See ComplexElement.xml for full definition -->
    <SimpleChild>content</SimpleChild>
</ComplexElement>
```

### Elements with Attribute Control

```xml
<ElementWithAttributes id="required-id" version="1" optionalAttr="value">
    <!-- ch-usage: mandatory -->
    <!-- ch-attrs: id version optionalAttr -->
    <!-- ch-note: Only specified attributes are allowed -->
    Content
</ElementWithAttributes>
```

## Troubleshooting

### Common Issues

1. **Template not found**: Ensure the template exists in the templates folder
2. **Invalid XML**: Validate your template against the NeTEX schema
3. **Missing annotations**: All processed elements need usage annotations
4. **Circular references**: Avoid templates that reference each other circularly
5. **Namespace issues**: Ensure proper namespace declarations

### Debugging Tips

- Use `-v` flag for verbose output
- Check the generated schematron/markdown files
- Validate intermediate XML files
- Test with small, simple templates first

## Test Templates

Comprehensive test templates demonstrating all annotations have been moved to the schematron_builder tool:
- [`../tools/schematron_builder/test_templates/`](../tools/schematron_builder/test_templates/)

These templates show examples of all supported comment annotations and provide a complete testing framework. See the [test documentation](../tools/schematron_builder/test_templates/README.md) for details.

## Related Tools

- **Schematron Builder**: [`../tools/schematron_builder/README.md`](../tools/schematron_builder/README.md)
- **Markdown Builder**: [`../tools/md_builder/README.md`](../tools/md_builder/README.md)
- **Schematron Validator**: [`../tools/check_schematron/README.md`](../tools/check_schematron/README.md)

## Profile Evolution

The Swiss NeTEx profile evolves over time. When making changes:

1. **Document changes**: Update the change log
2. **Maintain backward compatibility**: Where possible
3. **Deprecate, don't delete**: Mark old elements as deprecated rather than removing them
4. **Version templates**: Include version information in templates
5. **Test thoroughly**: Validate changes with existing data

## Contributing

When contributing new templates or modifications:

1. **Follow existing patterns**: Use the same style and conventions
2. **Document thoroughly**: Add comprehensive notes and explanations
3. **Test your changes**: Generate and validate output
4. **Update documentation**: Keep README files current
5. **Add examples**: Include sample data where helpful

## License

The templates and associated tools are licensed under the same terms as the main project. See the project's LICENSE file for details.
