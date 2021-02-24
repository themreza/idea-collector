# Idea Collector
An idea collector that automatically scrapes websites to find new app ideas and uses 
machine learning to summarize and classify them.

![](assets/idea-collector-128.png)

**Development Status**: Initial planning.

## Features

- [ ] Generates a short summary of each idea
- [ ] Classifies ideas by keywords
- [ ] Search collected ideas by text, keywords, and sources
- [ ] Automatic alerts via webhook (e.g. Slack) for new ideas with filter match
- [ ] Ignores non-English scraped content
- [ ] Detect and remove duplicate ideas
- [ ] Scrape HTML pages or use source APIs
- [ ] New sources can be added using a template or programmatically
- [ ] GraphQL API
- [ ] Web app

## Built-in Sources

- Twitter
  - Search queries:
    - [ ] `"make an app that"`
    - [ ] `"is there an app"`
    - [ ] `"I want an app"`
  - Hashtags:
    - [ ] `#appidea`
- Product Hunt
  - [ ] Post descriptions and keywords
- Reddit
  - Search queries:
    - [ ] `"make an app that"`
  - Subreddits:
    - [ ] `/r/AppIdeas`
    - [ ] `/r/SomebodyMakeThis`
    - [ ] `/r/Startup_Ideas`

## About the author

This project was created and is maintained by [Mohammad Tomaraei](https://tomaraei.com).

[![Mohammad Tomaraei](https://raw.githubusercontent.com/themreza/themreza/master/logo-mini.png)](https://tomaraei.com)