## Visualizations in Splunk ##
me when i want to see my big data

### Formating Commands ###
_fields_ --> include or exclude certain fields, can make big search run a lot faster! (- for exclusion) <br>
_table_ --> will transform data into tabulated format <br>
_dedup_ --> remove duplicate values from search (i like this one :p) <br>
_addtotals_ --> add values of all computed fields specified <br>
_fieldformat_ --> make visual changes without damaging data integrity <br>

### Visualizing Data ###
nice transforming commands include:
- top / rare: display most/least common values of a field 
- stats: can be using for count, min, max, avg ...
- chart: create data chart with fields inputted
    -ex: chart count over _____
- timechart: create chart over a time range
- trendline: computes moving data trends 

_by_ --> can be concated to visualization commands to append additional field values into a command <br>

### Generating Maps ###
pulling geographics == dope <br>

_iplocation:_ lookup and add information that pertain to ip addresses outside of internal network. <br>
_geostats:_ aggregation of geo data into visualized map. <br>
_geom:_ adds field that match KMZ data for visualization. <br>

### Single Value Visualizations ###
can be good for making heavy hitting informatics for visualized data to important non-technical stakeholders. <br>
mess around with visualization tab in splunk for powerpoint like data formating. <br>

### Visual Formatting ###
additional formatting:
- Format: wrap results, show row numbers, data overlay, totals, percentage ... 
- Chart Overlay: allows visualizations to overlayed and mixed together.

