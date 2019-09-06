# cgi_jsont_for_AZ


## Overview

Original design https://www.nict.go.jp/JST/http.html

1. Cloned by Python https://github.com/ipv6labs/cgi_jsont

2. Deployment to Azure App Service


## Environment

- Azure App Service on Linux    https://docs.microsoft.com/ja-jp/azure/app-service/containers/app-service-linux-intro
- Python 3.7    https://docs.python.org/3/whatsnew/3.7.html


## Installation

### Azure App Service

Home -> App Service   Click Add

#### Instance:

select "Code", runtime stack is "Python 3.7", and Operation system is "Linux".

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

DEMO: http://time.ipv6labs.jp/cgi-bin/jst

#### Get NTP time:

http(s)://{application_name}.azurewebsites.net/cgi-bin/ntp

DEMO: http://time.ipv6labs.jp/cgi-bin/ntp

#### Get time for human:

http(s)://{application_name}.azurewebsites.net/cgi-bin/time

DEMO: http://time.ipv6labs.jp/cgi-bin/time

#### Get JSON format:

http(s)://{application_name}.azurewebsites.net/cgi-bin/json

DEMO: http://time.ipv6labs.jp/cgi-bin/json

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
