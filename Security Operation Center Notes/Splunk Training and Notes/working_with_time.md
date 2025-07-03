## Working with Time ##
time is probably one of the most important event data that can be utilized to optimize searches! <br>

in this section:
- learn more on how time works in searches
- learn different functions that work with time in the search query
- learn different commands that revolve around time
- learn how timezones are represented in data

### Searching with Time ###
when data is ingested by the index, it sorts the time the log was receive as _\_time._ <br>
_\_time_ is a part of the default fields in a splunk search, alongside sourcetype, source, and host! <br>
time is sort in EPOCH TIME --> converted into human readable at search time!

__Epoch Time:__ standardized starting point for computer time, with it being January 1st, 1970 at 00:00:00 Coordinated UTC <br>
- ex:        time of this document being typed -->       1751483223

on the right side of the search bar, there is a time selector, which can be used to fine tune what time range you want the search to be executed on. <br>
- relative, real-time, or all time (:skull:)
- real-time searches are incredibly resource intensive on host computer, so keep that in mind!! <br>

__earliest:__, __latest:__ time modifier for time range window. <br>

earliest/latest = [+|-]<timeInt><timeUnit>@<timeUnit>
* -5w@h: 5 weeks ago, rounded to the nearest hour
* +1w1@m: last Monday, rounded to the nearest minute
* -q@mon: last quarter, rounded to the nearest month
- seconds, minutes, days, weeks, months, quatuarly, yearly, subsecond types as well

time ranges specified in the search will have priority over what is set time range in the time range picker <br>

IF SPLUNK CAN NOT FIND a event time, it will default back to the time of when the log was ingested by the index. <br>

### Formatting Time ###
certain functions:
- _now()_ --> returns time a search was started
- _time()_ --> returns the time an event was processed by __eval__ command. 
- _relative\_time(X,Y)_ --> returns epoch timestamp relative to supplied time.
- _strftime_ + _strptime_ --> functions that format time into supplied format.     ( strftime takes epoch to string,      strptime takes string to epoch)
- _span_ --> groups time in supplied time buckets

Format Variables for strftime and strptime: <br>
        __TIME__                        __DAYS__                            __Months+Years__
* %H - 24 hours    00 - 23          %d - dayofmth       01 - 31         %b - abrmon     Jan
* %T - 24 hours    HMS              %w - weekday        0 to 6          %B - mthname    January
* %I - 12 hours    01 - 12          %a - abrwkday       Sun...          %m - mthnum     01 - 12
* %M - minute      00 - 59          %A - weekday        Sunday          %Y - year       2020
* %p              AM or PM          %F - ymd            %Y-%m-%d


### Using Time Commands ###
more time functions!<br>

* _timechart_ --> performs statistical aggregations against time, good with count or sum functions
* _timewrap_ --> works in sync with timechart to have each time section split into their own charts

ex:     timechart <stats-funct>(field) by (field) \[span=<int><timescale>\] \[limit=<int>\] <br>

### Working with Time Zones ###
dealing with time zones can be tricky! <br>
* always verify when using time as a metric that it is what is expected for you endpoint display
to determine your time zone:
1. in _preferences_, set Time Zone to default system timezone.
2. run a search over the last 15 minutes
3. read event timestamps and verify that with your local time. 

![splunk time quiz](images/image-5.png)

