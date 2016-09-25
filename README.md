alex (anyone's learning experience )


Spiders for crawling course information from University of Mayaguez.


## Execution

To view the list of spiders use the `list` command.

    $ scrapy list

    uprm.edu



To crawl the uprm.edu site use the `uprm.edu` spider. To output in *csv* format do the following.

* *-o* output filename
* *-t* output format

    $ scrapy crawl uprm.edu -t csv -o data/uprm.edu.csv
