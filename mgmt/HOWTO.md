# Describing how to work in this Repo
This file is a collection of ways we want to do things in this repo to promote the way we work as a team on the realisation guide.

All important elements are in the src folder.

# Preparing to work with it.

## Generate a local copy to work with
* check out the project
* check out the xsd
* build schematrons
* build elements.xml
* build elemnts.md
 
### Setup XSD
We work here to create the next NeTEX realisation guide.

When you clone this project, you will get an empty xsd directory. To complete the xsd download run:
```bash
git submodule init
git submodule update 
```

# Editing 
* Use pycharm to work on the markdown.
* Use XMLSpy to check if the XML/XSD are valid.

## Markdown
- Everything in the src folder
- Folder for resources to include: src/media (we try to avoid resources)
- https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax

### Graphics
Do it as mermaid so that it can be done directly in the markdown.

### General rules
- Comments start with > best do it this way:
<<<<<<< HEAD
  ```md
  > [!CAUTION] 
=======
  ```md 
>>>>>>> upstream/main
  > **TODO** Must be revisited and updated.
  ```
- Things to do are always marked with **TODO** in templates and docs
- We don't use numberings in docs
- Glossary references are used at the top of an element section with a *→ into the annex with a # if possible.
   - Example:`*→ [Glossary definition](A4_annex_glossary.md#timetableframe)*` Result: *→ [Glossary definition](A4_annex_glossary.md#timetableframe)*
- Element names from NeTEx are shown as `code` (except in the headings). Plurals are done like this `ServiceJourney`s.
- A table of contents at the top of each file lists the elements used.
  
### Headings
There is a defined structure to describe elements and frames (examples in [TimetableFrame doc](https://github.com/openTdataCH/netexRealisationGuideSwitzerland/blob/main/docs/09_timetable.md)). There is a structure for frames and one for elements.

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

In the Example portion first the link to the snippet is formed  `[Example snippet](../site/xml-snippets/ServiceJourney.xml)`. There may be several examples with text between them. Also the templates are to be added below each snippet: `[Template](./templates/ServiceJourney.xml)`

### Tables
- Tables as markdown
- through templates when elements are to be described

### Captions
- For the included markdown tables the captions are automatically generated.
- Captions are italic with *italic*
- Captions for tables are before the table (*Table:blabla*), captions for diagrams are below the table (*Figure: blabla*)
### UML diagrams and figures
- we use mermaid: https://mermaid.js.org/intro/syntax-reference.html in githu
- When other things are needed they are to be stored in the docs/media folder
- The sources for drawings are to be stored in docs/media as well

### Links
- When using links between docs, and to other structures we need to add the file and the anchor. E.g. `./10_common.md#CompositeFrame`
- see: https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax

# Review process
- We will always use a PR branch for the reviews.
- Typos and stuff like this can be directly commited to the review branch
- The branch will regularly be merged.
- Issues are to be created for reviews. An issue can deal with one,several or multiple problems.
- For the broader reviews we will provide an example of an issue.