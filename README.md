# cgi_jsont_for_AZ


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
-- Branch: "master" is stable
-- Branch: "test_branch" is unstable
