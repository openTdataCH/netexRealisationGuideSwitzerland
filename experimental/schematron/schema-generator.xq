xquery version "3.1";

declare namespace xs  = "http://www.w3.org/2001/XMLSchema";
declare namespace sch = "http://purl.oclc.org/dsdl/schematron";

(: EXPath file module for writing the result :)
import module namespace file = "http://expath.org/ns/file";

(: External parameters :)
declare variable $base as xs:string external := "StopPlace.xsd";
declare variable $sch as xs:string external := "Restrictions.sch";
declare variable $out as xs:string external := "StopPlaceRestricted.xsd";

(: Utility: resolve QName token like "netex:Name" using the rule node’s namespaces :)
declare function local:resolve-qname($token as xs:string, $ctx as element()) as xs:QName? {
  try { resolve-QName($token, $ctx) } catch * { () }
};

(: Parse a rule’s context into a sequence of QNames :)
declare function local:parse-context($context as xs:string, $rule as element(sch:rule)) as xs:QName* {
  let $steps := tokenize(normalize-space($context), "/")
  return for $s in $steps return local:resolve-qname($s, $rule)
};

(: Find the global element by name (in the schema’s targetNamespace) :)
declare function local:global-element($xsd as element(xs:schema), $lname as xs:string) as element(xs:element)? {
  $xsd/xs:element[@name = $lname]
};

(: Resolve an xs:element to its complex type (named or anonymous) :)
declare function local:element-type($xsd as element(xs:schema), $el as element(xs:element)) as element(xs:complexType)? {
  let $t := $el/@type
  return
    if ($t)
    then $xsd/xs:complexType[@name = local-name-from-QName(resolve-QName(string($t), $el))]
    else $el/xs:complexType
};

(: Within a complexType, find a direct child element by name (assumes xs:sequence content) :)
declare function local:child-decl($ctype as element(xs:complexType), $lname as xs:string) as element(xs:element)? {
  ($ctype/xs:sequence//xs:element[@name = $lname])[1]
};

(: Traverse a context path (e.g., netex:StopPlace/netex:Extensions) to the complexType of the last step :)
declare function local:context-complex-type($xsd as element(xs:schema), $ctx as xs:QName*) as element(xs:complexType)? {
  if (empty($ctx)) then ()
  else (
    let $first := $ctx[1]
    let $rest  := subsequence($ctx, 2)
    let $rootEl := local:global-element($xsd, local-name-from-QName($first))
    let $rootType := if ($rootEl) then local:element-type($xsd, $rootEl) else ()
    return
      if (empty($rest)) then $rootType
      else (
        fold-left(
          function($acc as element(xs:complexType)?, $step as xs:QName) as element(xs:complexType)? {
            if (empty($acc)) then ()
            else
              let $child := local:child-decl($acc, local-name-from-QName($step))
              return
                if (empty($child)) then ()
                else local:element-type($xsd, $child)
          },
          $rootType,
          $rest
        )
      )
  )
}

(: Classify an assert into an op and extract the child name it mentions.
   Supported patterns:
   - remove:  not(netex:X)  or empty(netex:X)
   - require: exists(netex:X) or netex:X
   - allow:   count(netex:X) <= 1
:)
declare function local:classify-assert($assert as element(sch:assert)) as map(*)? {
  let $test := normalize-space(string($assert/@test))
  let $qname-tokens := analyze-string($test, "([A-Za-z_][\w\-.]*):([A-Za-z_][\w\-.]*)")?match
  let $first-qn     := if (exists($qname-tokens)) then $qname-tokens[1]/string() else ()
  let $child-qname  := if ($first-qn) then local:resolve-qname($first-qn, $assert) else ()
  return
    if (not($child-qname)) then ()
    else if (matches($test, "^(not|empty)\s*\(\s*[A-Za-z_][\w\-.]*:[A-Za-z_][\w\-.]*\s*\)\s*$"))
      then map { "op": "remove",  "child": $child-qname, "assert": $assert }
    else if (matches($test, "^exists\s*\(\s*[A-Za-z_][\w\-.]*:[A-Za-z_][\w\-.]*\s*\)\s*$") or matches($test, "^[A-Za-z_][\w\-.]*:[A-Za-z_][\w\-.]*$"))
      then map { "op": "require", "child": $child-qname, "assert": $assert }
    else if (matches($test, "^count\s*\(\s*[A-Za-z_][\w\-.]*:[A-Za-z_][\w\-.]*\s*\)\s*<=\s*1\s*$"))
      then map { "op": "allow",   "child": $child-qname, "assert": $assert }
    else ()
}

(: Read any diagnostic XML snippets referenced by an assert via @diagnostics.
   If present, return the first xs:element child from referenced diagnostics. :)
declare function local:diagnostic-snippet($sch as document-node(), $assert as element(sch:assert)) as element(xs:element)? {
  let $ids := tokenize(normalize-space(string($assert/@diagnostics)), "\s+")
  let $diags := for $id in $ids return $sch//sch:diagnostic[@id = $id]
  return ($diags/xs:element)[1]
}

(: Apply one operation on the schema :)
declare function local:apply-op($xsd as element(xs:schema),
                                $context as xs:QName*,
                                $op as map(*)) as empty-sequence() {
  let $ctype := local:context-complex-type($xsd, $context)
  let $childLocal := local-name-from-QName($op?child)
  return
    if (empty($ctype)) then ()
    else
      typeswitch($op?op)
        case "remove" return (
          delete nodes $ctype/xs:sequence/xs:element[@name = $childLocal]
        )
        case "require" return (
          for $e in $ctype/xs:sequence/xs:element[@name = $childLocal]
          return
            if (empty($e/@minOccurs) or $e/@minOccurs != "1")
            then replace value of node $e/@minOccurs with "1"
            else ()
        )
        case "allow" return (
          if (exists($ctype/xs:sequence/xs:element[@name = $childLocal]))
          then ()
          else (
            let $snippet := local:diagnostic-snippet(root($xsd), $op?assert)
            let $new :=
              if ($snippet)
              then $snippet
              else element { QName(namespace-uri-from-QName(xs:QName("xs:x")), "element") } {
                     namespace xs { "http://www.w3.org/2001/XMLSchema" },
                     attribute name     { $childLocal },
                     attribute minOccurs { "0" },
                     attribute type     { "xs:string" }
                   }
            return insert node $new as last into ($ctype/xs:sequence)[1]
          )
        )
        default return ()
}

(: Collect operations from Schematron :)
declare function local:collect-ops($schDoc as document-node()) as element()* {
  for $rule in $schDoc//sch:rule
  let $ctxQ := local:parse-context(string($rule/@context), $rule)
  let $ops  := for $a in $rule/sch:assert return local:classify-assert($a)
  for $op in $ops[. instance of map(*)]
  return element op {
    attribute context { string-join(for $q in $ctxQ return local-name-from-QName($q), "/") },
    attribute kind    { $op?op },
    attribute child   { local-name-from-QName($op?child) }
  }
}

(: Main :)
let $xsd  := doc($base)/xs:schema
let $schd := doc($sch)
let $tns  := string($xsd/@targetNamespace)

(: Apply operations :)
let $ops :=
  for $rule in $schd//sch:rule
  let $ctxQ := local:parse-context(string($rule/@context), $rule)
  let $ops  := for $a in $rule/sch:assert return local:classify-assert($a)
  return
    for $op in $ops[. instance of map(*)]
    return local:apply-op($xsd, $ctxQ, $op)

return (
  file:write($out, document { $xsd }, map { "method": "xml", "indent": "yes" }),
  $out
)
