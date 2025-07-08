## Search Under the Hood ##
search is THE main tool of splunk, so its good to understand it more in depth. <br>

how searches are ingested by the index, how to make optimal searches ... 

### Using the Search Job Inspector ###
_Search Job Inspector:_ helpful tool to view the overall stats of a search, how it was processed, and what splunk spent its time on. <br>
- Execution Cost
- Search Job Properties
- duration, component, invocations, input and output count

any expired searches will not have this option for evaluation... <br>
for any search, splunk creates an optimized version of your search and runs that in order to improve performance! (cool!) <br>

### Splunk Commenting ###
\`\`\` comment style in splunk! \`\`\`
` also used for code section in md lol `

### Splunk Architecture ### 
Scheluded Searches are something that you REALLY want to optimize!! <br>

search head <--><--> (index/indexes):
- _index:_ logical grouping of data   <-- stored in buckets
- _buckets:_ storage mediums, think cloud arch, in which they have different levels, hot, warm, cold, and frozen (ready for data decommissioning)
- buckets work in a paging like system, two main files, one of which storages the raw logs and are split into small chunks/pages around 128k, and then a time indexer that stores the key of what time frame represents what page.
- each bucket holds a bloom filter that helps splunk understand if the bucket contains data relevent to its search (bloom is created by hashing)

### Streaming vs. Non-Streaming Commands ###
__Transforming Commands:__ operate on an entire result set of data. <br>
_Streaming Commands:_
- __Centralized:__ execute on the search to each event return in result. (transaction, streamstacks.. )
- __Distributable:__ can execute while events are still coming through, better processing time! (eval, rename, fields, regex.. )

distributable commands should come before any centralized or transforming commands for better performance. this is because if the dis happenings after the transformer that sends all the data to the search index, it has to reparse through it. If the distributable command came first, its load could be split by the indexers, and then the transforming command can be done after in one shot. <br>

### Breakers and Segmentation ###
Major Breakers:
- Any whitespace
- carriage characters /r /c
- brackets, exclaims ...

Minor Breakers:
- forward slash
- colon
- punctation
- hypen
- dollar sign 

dude the way this works is like ONE huge fat CS280 parser lololol. <br>
_lispy_ expressions = tokenized search <br>

__TERM()__ --> will wrap inner term to be one term, bypassing minor and major spaces like . or spaces.
think about an ip address!    196.168.2.1 --> normally would be split by minor breaker, causing the search to also look for those numbers seperated as well, making it less optimized. <br>
term does not work with aliases 😬

wildcards at a beginning of a string will NOT work!<br>
wildcards in the middle of a string == VERY TAXING <br>

### Commands and Functions for Troubleshooting and Field Summary ###
_makeresults:_ make temporary events in a field, must be the first command after a search <br>
_fieldsummary:_ calculate a summary of specificed fields for visualization and calculations <br>

getter functions exist in splunk!

typeof(), isnull() istype() ... <br>

![search_under Splunk Quiz](images/image-9.png)