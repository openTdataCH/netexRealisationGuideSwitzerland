# Describing how to work in this Repo
This file is a collection of ways we want to do things in this repo to promote the way we work as a team on the realisation guide.

## Generate a local copy to work with
* check out the project
* check out the xsd
* build schematrons
* build elements.xml
* build elemnts.md
 
### Setup XSD
We work here to create the next NeTEX realisation guide.

When you clone this project, you will get an empty xsd directory. To complete the xsd download run:
```
git submodule init
git submodule update 
```

## Markdown
- Everything in the docs folder
- Folder von inclusion stuff: docs/media
- https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax

### General rules
- Comments start with > best do it this way:
  ```
  > [!CAUTION] 
  > **TODO** Must be revisited and updated.
  ```
- Things to do are always marked with **TODO** in templates and docs
- We don' use numberings in docs
- Glossary references are used at the top with a *→ into the annex with a # if possible.  **TODO* André pls add an example here.
- Elements from NeTEx are shown as code (except in the headings). Plurals are done like this `ServiceJourney`s.

  
### Headings
The TimetableFrame doc shows the structure. There is one for Frames and one for elements.

 Frames
- Purpose
- Contained Elements
- Table
- Example
- Frame Relationships

 Elements:
 - Purpose
 - Table
 - Example
 - Usage Notes (when necessary)

In the Table heading first it is the link to the element/frame md which will be copied into it by the generator. The link is formed this way `[Swiss profile NeTEx definition](../generated/markdown-examples/ServiceJourney.md)`. The Link to the future xcore Snippet is formed this ways `*→ [General NeTEx definition ](../generated/xcore/ServiceJourney.html)*`

In the Example portion first the link to the snippet is formed  `[Example snippet](../generated/xml-snippets/ServiceJourney.xml)`. There may be several examples with text between them. Also the templates are to be added below each snippet: `[Template](../templates/ServiceJourney.xml)`

### Tables
- Tables as markdown
- through templates when elements are to be described

### XSD tables
> **TODO** will be done by Urs

### UML diagrams and figures
- we use mermaid: https://mermaid.js.org/intro/syntax-reference.html in githu
- When other things are needed they are to be stored in the docs/media folder
- The sources for drawings are to be stored in docs/media as well
> **TODO** expand on how to do diagrams

 #### Usage of drawio
- We try to use mermaid, where possible.
- https://www.drawio.com/blog/embed-diagrams-github-markdown
- 
#### Internal diagram
usage of mermaid instead of plantuml
> **TODO** expand on how to do diagrams


### Links
- When using links between docs, and to other structures we need to add the file and the anchor. E.g. `./10_common.md#CompositeFrame`
- see: https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax



