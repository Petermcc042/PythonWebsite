Use XLOOKUP Not VLOOKUP
========================

As many analysts can understand I'm sure, the quest for ever increasing efficiency in a repetitive task is something to strive for. One issue that I continually ran into was formatting the rows/columns of regularly updating data

For example having data organised like below where we have products on the left with order and revenue data.



Summarising this data or pulling this data into another sheet can be complicated and highly prone to breaks in formula if you upset the column or row order. One way to ensure correctness is to use a combination of INDEX(), MATCH(), and SUMIFS().
