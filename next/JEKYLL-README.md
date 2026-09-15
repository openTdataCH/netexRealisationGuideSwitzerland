# Jekyll Documentation

[Jekyll](https://jekyllrb.com) is used in the Github Action [pages.yaml](../.github/pages.yaml) to generate static html pages from generated Markdown (and 
other source documents) in the `site` folder.

See [Jekyll documentation](https://jekyllrb.com/docs/) for more info about Jekyll.

This `jekyll` folder is used as a template for the site. It is copied to the `site` folder during the build.

## Jekyll Adaptions 

The following documents have been adapted according to project needs:
- The Jekyll configuration [_config.yml](_config.yml) 
- The Gemfile
- HTML files (header.html, footer.html, mermaid.html) in the _`includes` folder

### Deployment to Branch Subdirectories

Pages are deployed to a subdirectory according to the branch name, e.g. `main` or `next`. For the hyperlinks to work, 
the `baseurl` variable of the Jekyll configuration is overwritten during build.

E.g., after push to the `next` branch:
- Pages workflow is triggered
- During build, `baseurl` is set `/netexRealisationGuideSwitzerland/next`
- The workflow deploys contents from `site/_site` to the `next` directory of `gh-pages`

### Mermaid

The Java script in `_includes/mermaid.html` is included in `_includes/footer.html`, and consequently, in the footer of 
the generated HTML. 

To use the mermaid Script for a particular page, it must be enabled in the Markdown header:

```markdown
---
mermaid: true
---
```

### Left Sidebar

The left sidebar is realized with the help of a custom layout called `with-sidebar`.
This layout is used by default (as configured in `_config.yml`), so that the left sidebar appears on every page.


#### Sidebar Components

| File                         | Description                                                                                    |
|------------------------------|------------------------------------------------------------------------------------------------|
| `_layouts/with-sidebar.html` | Defines the layout `with-sidebar`. Extends `default` layout. Is used for all pages by default. |
 | `_data/chapters.yml`         | Configuration of chapters to appear in the left sidebar.                                       |
 | `_data/special.yml`          | Configuration of special use cases to appear in the left sidebar.                              |
 | `_data/annexes.yml`          | Configuration of annexes to appear in the left sidebar.                                        |
| `_includes/sidebar.html`     | HTML of the left sidebar.                                                                      | 
| `assets/main.scss`           | CSS extending `minima` theme, with adaptions for the left sidebar.                             | 



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