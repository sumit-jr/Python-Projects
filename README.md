# Python-Projects
This repos contains the mini-python projects with it's GUI to make it's visibility better. 

## 1. [Password generator](https://github.com/Sumit-jr/Python-Projects/tree/main/1.%20Password%20Generator)
### Features
* No dependencies.
* Generate a weak,medium & strong password of default length 5-15.
* Generate Non Duplicate Password.

### Configuration

| property   |                          Description                 | Default |
| ---------- |------------------------------------------------------| ------- |
| minlen     |   Minimum length of the password                     | 5 |
| maxlen     |   Maximum length of the password                     | 15 |
| minchars  |   Minimum upper case characters required in strong password | 1 |
| minlchars  |   Minimum lower case characters required in strong password | 1 |
| minnumbers |   Minimum numbers required in strong password               | 1 |
| minschars  |   Minimum special characters in the strong password         | 1 |


### Usuage
Application uses [secrets](https://docs.python.org/3/library/secrets.html) module instead of random module on Python environments above 3.6.

