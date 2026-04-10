<schema xmlns="http://purl.oclc.org/dsdl/schematron">
  <title>Swiss NeTEx RG 2.0 profile checks</title>

  <!-- NeTEx namespace; change if your documents use a different URI -->
  <ns prefix="n" uri="http://www.netex.org.uk/netex"/>

<!--------------------------------------------------------------------------------------------------------------------------->
<!-- Check ServiceJourney -->
  <pattern id="servicejourney-profile">
    <rule context="n:ServiceJourney">

      <!-- OperatorRef is mandatory -->
      <assert test="n:OperatorRef">
        ServiceJourney must contain OperatorRef.
      </assert>

      <!-- validityConditions must include an AvailabilityCondition with all three fields -->
      <assert test="n:validityConditions/n:AvailabilityCondition[n:FromDate and n:ToDate and n:ValidDayBits]">
        ServiceJourney validityConditions must include an AvailabilityCondition with FromDate, ToDate, and ValidDayBits.
      </assert>

      <!-- calls are forbidden -->
      <assert test="not(n:calls)">
        calls are not allowed in ServiceJourney; use passingTimes instead.
      </assert>

      <!-- passingTimes must be present -->
      <assert test="n:passingTimes">
        ServiceJourney must contain passingTimes.
      </assert>

      <!-- Mode restriction (if Mode element is present) -->
      <assert test="not(n:Mode) or
                    translate(normalize-space(n:Mode), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz') = 'rail' or
                    translate(normalize-space(n:Mode), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz') = 'tram' or
                    translate(normalize-space(n:Mode), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz') = 'bus'">
        Mode (if present) must be one of: rail, tram, bus.
      </assert>

      <!-- Also cover TransportMode element (some profiles use this name) -->
      <assert test="not(n:TransportMode) or
                    translate(normalize-space(n:TransportMode), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz') = 'rail' or
                    translate(normalize-space(n:TransportMode), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz') = 'tram' or
                    translate(normalize-space(n:TransportMode), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz') = 'bus'">
        TransportMode (if present) must be one of: rail, tram, bus.
      </assert>

      <!-- And a possible @transportMode attribute -->
      <assert test="not(@transportMode) or
                    translate(normalize-space(@transportMode), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz') = 'rail' or
                    translate(normalize-space(@transportMode), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz') = 'tram' or
                    translate(normalize-space(@transportMode), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz') = 'bus'">
        @transportMode (if present) must be one of: rail, tram, bus.
      </assert>

    </rule>
  </pattern>
</schema>
