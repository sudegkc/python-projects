Project: Artistic Gymnastics Score Manager

This Python program manages and processes athletic performance scores from a gymnastics competition, implementing specific sports-scoring rules to determine winners and rankings.

Key Features:

Outlier Removal Logic: Automatically identifies and discards the highest and lowest scores for each athlete, calculating the final result based on the remaining three scores.

Gender-Specific Filtering: Identifies the female winner by comparing valid scores across all participants.

National Ranking System: Aggregates and ranks the top 3 countries by summing the total scores of all their athletes (both male and female).

Technical Implementation:

File Parsing: Processes unstructured text data with variable line lengths and space-separated fields.

Data Processing: Uses sorting and list slicing to handle the "discard high/low" rule efficiently.

Global Aggregation: Utilizes dictionaries to track and update cumulative scores for multiple nations simultaneously.
