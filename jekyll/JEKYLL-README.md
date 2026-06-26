# Jekyll Documentation

[Jekyll](https://jekyllrb.com) is used in the Github Action [pages.yaml](../.github/pages.yaml) to generate static html pages from generated Markdown (and 
other source documents) in the `site` folder.

See [Jekyll documentation](https://jekyllrb.com/docs/) for more info about Jekyll.

This `jekyll` folder is used as a template for the site. It is copied to the `site` folder during the build.

## Jekyll Adaptions 

The following documents 
- See [_config.yml](_config.yml) for the basic Jekyll configuration.
- The Gemfile
- files in _`includes` folder

### Mermaid

The Java script in _includes/mermaid.html is included in _includes/footer.html, and consequently in the footer of 
the generated html, if mermaid is enabled in the Markdown header:

```markdown
---
mermaid: true
---
```

## How to locally build pages with Jekyll

### Prerequisites

- [Setup the build](../tools/README.md#how-to-setup-and-run-the-build)
- [Install bundle and jekyll](https://jekyllrb.com/docs/installation/)

### Build the pages

```bash
uv run python -m build
cd site
bundle exec jekyll build
```

You can also do `bundle exec jekyll serve` to run a server.