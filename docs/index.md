# Python Invest

![Python Invest Logo](./images/logo.png "Python Invest Logo"){ width="300" .center }

Financial data extraction with Python.

The Python Invest package is based on an unofficial data extraction API from the website [Investing.com](https://www.investing.com/). It's a package inspired by the amazing [Investpy](https://github.com/alvarobartt/investpy) library.

!!! warning ""
    This package consumes an unofficial open API and will validate the user's email before providing the data. After that, the user can consume all available services.</b>

Python Invest its a Open Source package and Free to use, respecting the **MIT License**.


## :material-list-status: Requirements

:white_check_mark: Python >= 3.10

## :hammer_and_wrench: Installation

- pip

```
pip install python-invest
```

- poetry

```
poetry add python-invest
```

---

## :chart_with_upwards_trend: Usage Examples

Getting historical **BTC** data:

```{.py3 linenums=1 hl_lines=5}
from python_invest import Invest

inv = Invest('youremail@email.com')

data = inv.crypto.get_historical_data(
        symbol='BTC',
        from_date='2023-01-01',
        to_date='2023-02-01'
    )
```

The API can send a verification link to your email, it's a security measure you won't be charged for anything. If this happens, you will receive an error similar to this:

```{hl_lines="3 5"}
Traceback (most recent call last):
 File "...", line 5, in <module>
    data = inv.crypto.get_historical_data(symbol='BTC', from_date='2023-01-01', to_date='2023-02-01')
    ...
PermissionError: The Scrapper API sent to your email address the verification link. Please verify your email before run the code again.
```

If you get this error: **Just open your email box and click on the verification link.**

The email would be a equal this:

![Verification Email Link](./images/emailValidation.png "Verification Email Link"){ width="700" .center .shadow }

After that, you can run the code:

```{.py3 linenums=5}
data = inv.crypto.get_historical_data(
        symbol='BTC',
        from_date='2023-01-01',
        to_date='2023-02-01'
    )

print(data)
```
```
      Price      Open      High       Low     Vol Change        Date
0  16,674.3  16,618.4  16,766.9  16,551.0  136027   0.34  2023-02-01
1  16,618.4  16,537.5  16,621.9  16,499.7  107837   0.49  2023-01-01
```

The default output is the [Pandas DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html).
