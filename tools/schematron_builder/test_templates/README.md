# Test Templates for Schematron Builder

This folder contains test templates and generated files for testing the schematron builder functionality.

## Test Files

### Template Files

- **`test_simple.xml`**: Main test template following the proper NeTEX structure with PublicationDelivery root
- **`test_frame_content.xml`**: Referenced template demonstrating all supported ch-comment annotations
- **`test_template.xml`**: Comprehensive test showing all annotations (simpler structure)
- **`test_template_proper.xml`**: Alternative test with proper NeTEX structure
- **`test_valid.xml`**: Valid XML file that passes schematron validation

### Generated Schematron Files

- **`test_simple_output.sch`**: Generated schematron from test_simple.xml
- **`test_template_output.sch`**: Generated schematron from test_template.xml
- **`test_template_proper_output.sch`**: Generated schematron from test_template_proper.xml

## Running Tests

### Simple Python Test

The easiest way to test is using the Python test script:

```bash
python simple_test.py
```

This will:
1. Generate schematron from `test_simple.xml`
2. Verify the schematron file was created
3. Show the first few lines of the generated schematron

### Manual Testing

You can also test manually:

```bash
# Test with simple template
python ../template2schematron.py \
    -t test_simple.xml \
    -x ../../xsd/xsd/NeTEx_publication.xsd \
    -i . \
    -o test_simple_output.sch \
    -v

# Test with comprehensive template
python ../template2schematron.py \
    -t test_template.xml \
    -x ../../xsd/xsd/NeTEx_publication.xsd \
    -i . \
    -o test_template_output.sch \
    -v
```

### Test Schematron Validation

```bash
# Validate against generated schematron (should fail - missing mandatory elements)
python ../../check_schematron/check_schematron.py \
    -i test_simple.xml \
    -s test_simple_output.sch

# Validate with proper test file (should pass)
python ../../check_schematron/check_schematron.py \
    -i test_valid.xml \
    -s test_simple_output.sch
```

## Supported Annotations Demonstrated

The test templates demonstrate all supported ch-comment annotations:

### Basic Annotations
- `<!-- ch-start: description -->` / `<!-- ch-stop: description -->`
- `<!-- ch-note: text -->`
- `<!-- ch-notice: text -->`

### Usage Control
- `<!-- ch-usage: mandatory -->`
- `<!-- ch-usage: forbidden -->`
- `<!-- ch-usage: optional -->`
- `<!-- ch-usage: ignored -->`
- `<!-- ch-usage: expected -->`

### Advanced Features
- `<!-- ch-see -->`
- `<!-- ch-see: filename.xml -->`
- `<!-- ch-allowed-enums: value1 value2 value3 -->`
- `<!-- ch-deprecated -->`
- `<!-- ch-class-id-must-exist -->`

## Expected Results

### Schematron Generation
- Should generate schematron files with proper namespace declarations
- Should create rules for mandatory/forbidden elements
- Should include enumeration validation rules
- Should add deprecation warnings
- Should preserve comments as documentation

### Validation Results
- `test_simple.xml` against `test_simple_output.sch`: **FAIL** (missing mandatory elements)
- `test_valid.xml` against `test_simple_output.sch`: **SUCCESS** (all required elements present)

## Test Coverage

The test templates cover:

✅ **Basic structure**: Proper NeTEX XML with PublicationDelivery root
✅ **Region markers**: ch-start and ch-stop annotations
✅ **Documentation**: ch-note and ch-notice annotations
✅ **Usage control**: All usage variants (mandatory, forbidden, optional, ignored, expected)
✅ **Referenced templates**: ch-see with and without specific filenames
✅ **Enumerations**: ch-allowed-enums with multiple values
✅ **Deprecation**: ch-deprecated annotation
✅ **Cross-references**: ch-class-id-must-exist (when ID is present)
✅ **Validation**: Both positive and negative test cases

## Maintenance

When adding new features to the schematron builder:

1. **Add test cases**: Create or update test templates to cover new functionality
2. **Update documentation**: Add examples to this README
3. **Run tests**: Verify new features work with existing test infrastructure
4. **Add validation tests**: Include both positive and negative test cases

## Related Documentation

- **Main Schematron Builder Docs**: [`../README.md`](../README.md)
- **Templates Documentation**: [`../../templates/README.md`](../../templates/README.md)
- **Schematron Validator**: [`../../check_schematron/README.md`](../../check_schematron/README.md)