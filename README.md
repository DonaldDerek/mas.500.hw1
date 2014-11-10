##MIT Media Lab MAS.500 - Module III

####Advanced Python track:

* build a module that scrapes (use BeautifulSoup)

* more detailed election [data](http://www.archives.gov/federal-register/electoral-college/2012/popular-vote.html)

* add the ability to export it to CSV and JSON

* comments are for sissies


## Dependencies
```
pip install beautifulsoup4
```

## Test Run
```
python app.py
```

```
Fetching votes from archives.gov...[done]
saved in cvs format under election.cvs...[done]
saved in json format under election.json...[done]
[
    {
        "Democratic": "795696",
        "Green": "3397",
        "Libertarian": "12328",
        "Others": "6992",
        "Republican": "1255925",
        "State": "AL",
        "Total": "2074338"
    },
    {
        "Democratic": "122640",
        "Green": "2917",
        "Libertarian": "7392",
        "Others": "-",
        "Republican": "164676",
        "State": "AK",
        "Total": "297625"
    },
    ...
```

## License

The MIT License (MIT)

Copyright (c) 2014 Donald Derek Haddad

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
