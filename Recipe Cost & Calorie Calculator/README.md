This Python script performs a comprehensive analysis of recipe files, aggregating data from a nutritional database to calculate the total cost and caloric value of a dish.

Key Features:

Nutritional Aggregation: Parses raw recipe data and cross-references it with a food database (foods.txt) to calculate total expenses and energy content.

Dynamic Data Mapping: Automatically identifies ingredients, extracts quantities in grams, and performs unit conversions (Grams to Kilograms) for precision.

Robust Error Handling: Implements try-except blocks to manage OSError during file access and ValueError for inconsistent data types.

Process Termination: Includes a "Method/Procedure" detection logic to stop parsing exactly when the ingredient list ends, preventing data noise.

Technical Implementation:

Optimized Lookups: Utilizes Python Dictionaries for the food database to ensure O(1) time complexity when retrieving cost and calorie data.

String Normalization: Employs .strip() and .split(';') to ensure consistent data parsing, handling whitespace and delimiter variations.

Single-Pass Processing: Calculates totals and tracks ingredient counts within a single file-reading cycle for maximum efficiency.

File Structure:

foods.txt: The reference database containing unit costs and calories per kilogram.

polenta.txt, fusilli.txt :The input file containing the ingredient list and cooking procedure.

recipe.py: The main engine that processes the data and generates the summary report.
