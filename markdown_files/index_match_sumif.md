# Use INDEX MATCH and SUMIF for Better Excel Efficiency

While Excel offers many powerful functions, INDEX MATCH and SUMIF stand out as essential tools for users seeking flexibility and precision. These functions not only expand upon traditional capabilities like VLOOKUP but also provide greater control for advanced operations, such as dynamic lookups and conditional sums. Here’s why you should use them and how they work.

Note: while I refer to Excel a lot this works perfectly in Google Sheets as well

## Why Use INDEX MATCH Instead of VLOOKUP?
VLOOKUP is one of Excel’s most recognized functions, but it has several limitations that can be addressed by using INDEX MATCH. Combining the INDEX and MATCH functions creates a powerful, flexible alternative to VLOOKUP.

### INDEX and MATCH Overview
INDEX returns the value of a cell within a specified range based on its row and column positions:

```
=INDEX(array, row_num, [col_num])
```

MATCH locates the position of a specific value within a range:

```
=MATCH(lookup_value, lookup_array, [match_type])
```

When combined, these functions allow for dynamic lookups across any direction — vertical or horizontal.

### Example: INDEX MATCH vs. VLOOKUP
Below is a table with columns Product ID, Product Name, and Price. 


<table style="border-collapse: collapse; width: 100%; font-family: Arial, sans-serif;">
  <thead>
    <tr style="background-color: #f5f5f5; border: 1px solid #ccc;">
      <th style="border: 1px solid #ccc; padding: 8px;">A</th>
      <th style="border: 1px solid #ccc; padding: 8px;">B</th>
      <th style="border: 1px solid #ccc; padding: 8px;">C</th>
      <th style="border: 1px solid #ccc; padding: 8px;">D</th>
    </tr>
  </thead>
  <tbody>
    <tr  style="background-color: #86b2d3;">
      <td style="border: 1px solid #ccc; padding: 8px;">Product ID</td>
      <td style="border: 1px solid #ccc; padding: 8px;">Product Name</td>
      <td style="border: 1px solid #ccc; padding: 8px;">Class Name</td>
      <td style="border: 1px solid #ccc; padding: 8px;">Price</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;">UI2547</td>
      <td style="border: 1px solid #ccc; padding: 8px;">Trousers</td>
      <td style="border: 1px solid #ccc; padding: 8px;">Trouser/Shorts</td>
      <td style="border: 1px solid #ccc; padding: 8px;">£12</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;">UI2083</td>
      <td style="border: 1px solid #ccc; padding: 8px;">Shorts</td>
      <td style="border: 1px solid #ccc; padding: 8px;">Trouser/Shorts</td>
      <td style="border: 1px solid #ccc; padding: 8px;">£10</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;">UI4920</td>
      <td style="border: 1px solid #ccc; padding: 8px;">T-Shirt</td>
      <td style="border: 1px solid #ccc; padding: 8px;">Tops</td>
      <td style="border: 1px solid #ccc; padding: 8px;">£8</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;">UI2093</td>
      <td style="border: 1px solid #ccc; padding: 8px;">Boxers</td>
      <td style="border: 1px solid #ccc; padding: 8px;">Underwear</td>
      <td style="border: 1px solid #ccc; padding: 8px;">£5</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;">UI9946</td>
      <td style="border: 1px solid #ccc; padding: 8px;">Jumpers</td>
      <td style="border: 1px solid #ccc; padding: 8px;">Tops</td>
      <td style="border: 1px solid #ccc; padding: 8px;">£50</td>
    </tr>
  </tbody>
</table>

Suppose you want to retrieve the price for a given product ID.

Using VLOOKUP:

```
=VLOOKUP("UI2547", A:D, 4, FALSE) -> returns: £12
```

Using INDEX MATCH:


```
=INDEX(D:D, MATCH("UI2547", A:A, 0), 1) -> returns: £12
```

Advantages of INDEX MATCH:

* Two-directional Lookups: Unlike VLOOKUP, which can only search left-to-right, INDEX MATCH can look up values in any direction.
* Resilience to Changes: (This one is huge) Since INDEX MATCH uses relative column references, it doesn’t break if columns are added or removed in the table.
* Efficiency for Large Data: INDEX MATCH calculates smaller ranges, improving performance on larger datasets. This argument is similar to switching from VLOOKUP to XLOOKUP. VLOOKUP requires loading all the columns you pass in to return a value. The example above requires A:C to be passed to VLOOKUP while the index function only requires 2 columns. This will not be noticable at this scale but as your sheet progresses it will.

Why Use SUMIF?
When working with conditional aggregations, SUMIF is a simple and efficient solution. It allows you to sum values based on a single condition, making it a faster alternative to writing complex formulas or filtering data manually.

SUMIF Syntax and Usage
The basic syntax for SUMIF is:

```
=SUMIF(range, criteria, [sum_range])
```

range: The range of cells to evaluate against the condition.
criteria: The condition to apply (e.g., ">=100", "Trousers").
sum_range (optional): The range of cells to sum. If omitted, Excel sums the cells in the range parameter.
Example: SUMIF in Action
Consider a table of sales data with columns Salesperson, Region, and Sales. Suppose you want to calculate the total sales in the North region.

Formula:

```
=SUMIF(B:B, "North", C:C)
```

Explanation:

B
is the column containing regions.
"North" is the criterion for the calculation.
C
is the column of sales values to sum.
This quickly returns the total sales for the North region.



<style>
  table {
    width: 100%;
    border-collapse: collapse;
  }
  th, td {
    border: 1px solid #ccc;
    padding: 8px;
    text-align: center;
  }
  th {
    background-color: #f5f5f5;
  }
  code {
  background-color: #f9f9f9;
  padding: 2px 4px;
  border: 1px solid #ddd;
  border-radius: 3px;
  font-family: monospace;
}
</style>

## Advanced Usage of INDEX MATCH and SUMIF Together
For even more complex scenarios, you can combine INDEX MATCH and SUMIF. For example, suppose you need to sum all sales for a specific region and product. Using these two functions together allows you to dynamically calculate results based on multiple conditions.

### Example: Using INDEX MATCH and SUMIF Together

Below is a sample dataset representing **Sales Data** for a company. The goal is to:

1. Use `INDEX MATCH` to find the **Sales** column.
2. Use `SUMIF` to calculate the total sales for a specific **Region**.

The reason this is an issue in the first place is because when you paste this data in regularly, you only need to sum this column and specific elements in it based on region. When you download it from *our almighty Apple gods*, they change the column or row order every time. 

<table style="border-collapse: collapse; width: 100%; font-family: Arial, sans-serif;">
  <thead>
    <tr style="background-color: #f5f5f5; border: 1px solid #ccc;">
      <th style="border: 1px solid #ccc; padding: 8px;">Salesperson</th>
      <th style="border: 1px solid #ccc; padding: 8px;">Region</th>
      <th style="border: 1px solid #ccc; padding: 8px;">Sales</th>
      <th style="border: 1px solid #ccc; padding: 8px;">Sales Target</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;">Alice</td>
      <td style="border: 1px solid #ccc; padding: 8px;">North</td>
      <td style="border: 1px solid #ccc; padding: 8px;">$12,000</td>
      <td style="border: 1px solid #ccc; padding: 8px;">$15,000</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;">Bob</td>
      <td style="border: 1px solid #ccc; padding: 8px;">East</td>
      <td style="border: 1px solid #ccc; padding: 8px;">$8,000</td>
      <td style="border: 1px solid #ccc; padding: 8px;">$10,000</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;">Charlie</td>
      <td style="border: 1px solid #ccc; padding: 8px;">North</td>
      <td style="border: 1px solid #ccc; padding: 8px;">$18,000</td>
      <td style="border: 1px solid #ccc; padding: 8px;">$20,000</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;">Diana</td>
      <td style="border: 1px solid #ccc; padding: 8px;">South</td>
      <td style="border: 1px solid #ccc; padding: 8px;">$10,000</td>
      <td style="border: 1px solid #ccc; padding: 8px;">$12,000</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;">Eve</td>
      <td style="border: 1px solid #ccc; padding: 8px;">East</td>
      <td style="border: 1px solid #ccc; padding: 8px;">$5,000</td>
      <td style="border: 1px solid #ccc; padding: 8px;">$8,000</td>
    </tr>
  </tbody>
</table>


#### Task 1: Find Sales Column for a Specific Salesperson (`INDEX MATCH`)
To find the Sales column from the data with this formula:

```
=INDEX(A:D, ,MATCH("Sales", 1:1, 0))
```
By leaving the middle parameter blank, this now returns the entire column of sales data.
It works like this:

* Look at the range A:D
* Return all rows (due to blank parameter)
* return the column where we find the word Sales

#### Task 2: Sum the sales column for a specific region (`SUMIF INDEX MATCH`)
We can combine the formula above and SUMIF to dynamically find the correct columns and sum the correct values. Here is the formula below:

```
=SUMIF(INDEX(A:D, ,MATCH("Region", 1:1, 0)),"North", INDEX(A:D, ,MATCH("Sales", 1:1, 0)))
```
The formula above finds the Region column and the Sales column in the data regardless of where they are positioned. Then using sumif it sums for regions where the value equals "North"

## Why These Functions Matter
If you are looking for more flexible sheets where you are regularly pasting data or data is being piped in having dynamic lookups can be a lifesaver. INDEX MATCH provides flexibility for complex lookups, avoiding the limitations of older functions like VLOOKUP. SUMIF streamlines conditional summing, eliminating the need for manual filtering or convoluted formulas.

These tools are indispensable for anyone looking to boost their Excel efficiency and precision. By mastering these functions, you’ll not only handle large datasets more effectively but also future-proof your spreadsheets against common pitfalls like broken references or slow calculations.