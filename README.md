# cgi_jsont_for_AZ


## Overview

Original design https://www.nict.go.jp/JST/http.html

1. Cloned by Python https://github.com/ipv6labs/cgi_jsont

2. Deployment to Azure App Service


## Environment

- Azure App Service on Linux    https://docs.microsoft.com/ja-jp/azure/app-service/containers/app-service-linux-intro
- Python 3.9    https://docs.python.org/3/whatsnew/3.9.html


## Installation

### Azure App Service

Home -> App Service   Click Add

#### Instance:

select "Code", runtime stack is "Python 3.9", and Operation system is "Linux".

#### Deployment:

Click Deploy Center, set up.

- Sauce: GitHub
- Build: App Service Kudu engine
- Repository: https://github.com/ipv6labs/cgi_jsont_for_AZ
- Branch: "master"

## Usage

Access to http(s)://{application_name}.azurewebsites.net/

#### Get POSIX/UNIX time:

http(s)://{application_name}.azurewebsites.net/cgi-bin/jst

DEMO: https://cgi-jsont.azurewebsites.net/cgi-bin/jst

e.g.)
```
1567995625.038
```

#### Get NTP time:

http(s)://{application_name}.azurewebsites.net/cgi-bin/ntp

DEMO: https://cgi-jsont.azurewebsites.net/cgi-bin/ntp

e.g.)
```
3776984489.287
```

#### Get time for human:

http(s)://{application_name}.azurewebsites.net/cgi-bin/time

DEMO: https://cgi-jsont.azurewebsites.net/cgi-bin/time

e.g.)
```
Mon Sep 09 02:23:07 2019 UTC
```

#### Get JSON format:

http(s)://{application_name}.azurewebsites.net/cgi-bin/json

DEMO: https://cgi-jsont.azurewebsites.net/cgi-bin/json

e.g.)
```
{
  "arch": "x86_64",
  "id": "0807dd80a18d",
  "it": "0.000",
  "leep": "36",
  "next": "1483228800",
  "os": "Linux",
  "st": "1567995866.138",
  "step": "1"
}
```

JSONP is NO Support.


#### Other options:

- Check platform http(s)://{application_name}.azurewebsites.net/platform

- Check Python version http(s)://{application_name}.azurewebsites.net/python_version


## Pull requests

Pull requests receive in "test_branch".

## Scale by Azure

- Plan: P3V2 up to 20 instances
  - Core: 4
  - RAM: 14 GB
  - Storage: 250GB

Command:
~~~
$ ab -n 20000 -c 2000 http://time.ipv6labs.jp/cgi-bin/json
~~~

|instances|    Performance|
:---:|---: 
|        2| 2,600+ req/sec|
|        4| 4,200+ req/sec|
|       10|11,000+ req/sec|

Money is power, Plan: P3V2 about $700 ...
