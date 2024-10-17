# Swiss Sports News Fetcher

This Python script fetches the latest sports news from Switzerland using the News API. Users can retrieve news articles based on specific categories or search terms. The output includes headlines and links to the articles, which are displayed in the console.

## Features

- Fetch top headlines by category (e.g., sports)
- Search news articles based on keywords
- Display available news sources in a specified category

## Prerequisites

- Python 3.x
- `requests` library

## Available Categories

You can use any of the categories supported by the News API. Here are a few examples:

- business
- entertainment
- health
- science
- sports
- technology

## Display Sources by Category

To display news sources in a specific category, you can modify the script to call the `display_sources_by_category` function, passing the desired category as an argument.

## Example Output

```rust
Fetching news for category: sports...

- Headline 1
  Link: https://example.com/article1

- Headline 2
  Link: https://example.com/article2

Successfully retrieved top sports headlines
