## Using Fields ##

### What is the Field / Files Sidebar ###
field sidebar shows all of the fields that are shown in a user search. <br>

_selected fields_ --> most important fields <br>
_interesting fields_ --> fields that show up in at least 20% of events that were captured in the search <br>

clicking on field with show related data, such as captured values, count, and percentage of occurances in that field. <br>
adding a field to the selected selection will make sure the field is shown in the results of the search, and will persist until it is deselected. <br>

### Fields in Search Queries ###
REMINDER, best practice is to filter commands AS much as possible before attempt to perform some type of evaluation / data visualization. 
in search queries, field names ARE case sensitive, so keep that in mind (makes sense though) <br>
operations can be able to fields, like    !=,=      which can be applied to fields with numerical/string values <br>
clicking on a field can add it to the search, and can be paired with wildcard operators. :p

IN operator --> will capture all values in the range provided for the operation. <br>

__fields__ command can be piped to filter out for events with/out the chosen field.      for inclusion(+)     for negation(-) <br>
__rename__ command can be used to rename fields in a search. <br>


### Fields in Search Results ###
some fields are extracted at index, but some are also extracted at search time. why and what does that mean??
when splunk ingested data, it will automatically "harvest" fields for the logs of data that it is receiving, like...
- host
- source and sourcetype
- _time
- _raw

at search time, splunk with then additional pull more fields for the data that is extracted from the search. <br>

_temporary fields_ --> using commands like __eval__, results of certain commands can create/override fields. <br>
__erex__ command can be used to retrieve additional fields temporary, only for the search it is within. <br>
- requires sampling data, can be used as a baseline at first to understand a general regex query that might work for matching all events
__rex__ command can be used instead of erex, but instead you are now provide the regular expression for matching. <br>
- better for fine tuning, prefered solution


__Field Extractor:__
- allows for additional fields to be extracted that splunk was not able to automatically check.
- this tool can use regular expression in aiding in that addtional capture!

if you have a bunch of similar data fields --> --> use a field alias to condense them down to one field! <br>

![alt text](images/image-4.png)
link to splunk documentation, review!<br>
http://docs.splunk.com       regexr is a good source for practice regex commands!