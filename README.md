# PyNewsAggregator

[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)

## 🔍 Overview

**PyNewsAggregator** is a Python-based news aggregation system that:

- Scrapes the latest news articles from across the internet based on user interests.
- Processes and filters news by keyword or category.
- Sends **scheduled emails** with the latest articles to users’ respective email addresses.

The goal of this project is to help users stay up to date with relevant news without manually browsing multiple websites. :contentReference[oaicite:1]{index=1}

---

## Features

**Custom News Scraping**  
Pulls latest news articles from multiple sources.

**User Preferences**  
Users can define interests or keywords for personalized news feeds.

**Automated Scheduling**  
Automatically sends email updates at scheduled times.

**Email Notifications**  
Aggregated news summaries delivered directly via email.

**Modular & Extensible**  
Easy to extend with new sources or delivery mechanisms.

---

## Tech Stack

- **Python 3.8+**
- Web scraping: Selenium WebDriver
- Email automation: Standard Python mail libraries  
- NLP/Keyword processing for interest matching
