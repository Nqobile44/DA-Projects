# Optimizing E-commerce Engagement (SQL Project)

## Storyline Overview

This project analyzes e-commerce customer behavior using a relational SQL database I designed from scratch. The aim is to uncover valuable insights that help improve customer retention, satisfaction, and revenue.

- **Customer Segmentation:** Understand who the most valuable and satisfied customers are.

- **Behavior Analysis:** Explore how factors like discounts, membership tiers, and cities affect purchasing behavior.

- **Satisfaction Trends:** Investigate what drives satisfaction—and what causes customers to leave.

- **Data Modeling:** Normalized raw data into five clean, interrelated tables for efficient querying and meaningful insights.

---

## Demo

[Add a screenshot or GIF of your app working here if applicable.]

---

## Technologies Used

- **SQL (MySQL):** Core querying language used to explore and extract insights.

- **CSV Tools:** Initial raw data format before importing to SQL.

---

## Database Structure

The raw dataset was cleaned and restructured into the following five normalized tables:

- **main_table:** Core table holding customer demographics and engagement metrics.

- **subscription:** Tracks membership type and total spending.

- **engagement:** Stores behavioral metrics like average rating and discount usage.

- **satisfaction:** Maps satisfaction level by ID.

- **city:** Contains city names and their unique IDs.

---

## Key Questions Answered

Each query was written with a short business-driven comment explaining its purpose.

- Who are the top 5 spenders, and what membership tiers do they belong to?

- Which membership tier has the highest average satisfaction?

- What city has the highest rate of unsatisfied customers?

- Does applying a discount influence the number of items purchased?

- Is there a link between satisfaction level and time since last purchase?

- What’s the profile of a high-value, satisfied customer?

---

## What I Learned

- How to normalize messy CSV data into a relational schema.

- Creating foreign keys to model clean relationships between data.

- Writing business-driven SQL queries with purpose and clarity.

- Telling a data story that’s insightful, not just technical.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/rain-alert-notifications-system.git
