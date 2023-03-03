# Classes details

## Invest

<p><h4>Invest(email: str)</h4><legend>python_invest.invest.main.Invest</legend></p>

The Invest class is the main class that will be used to interact with all project. Note the email address is **required**.

- **email**: *str*: The email address of the user, if necessary the API will send a verification link to this email address.

- **crypto**: [Crypto](#crypto): The crypto attribute is used to interact with the Crypto class and he's methods, passing the Invest object instance to Crypto class.

## Crypto

<p><h4>Crypto(invest_instance: <a href="#invest"><i>Invest</i></a>)</h4><legend>python_invest.invest.crypto.Crypto</legend></p>

The Crypto class will be used by the Invest class, the methods of the class will be accessed to obtain crypto area data. In *Investing* website is the **crypto products**.

- *method* **get_historical_data** -> <small>dict | pandas.DataFrame</small>

    **symbol**: *str* = None  
    **from_date**: *str* | *datetime.date* = '01/01/2023'  
    **to_date**: *str* | *datetime.date* = '01/02/2023'  
    **name**: *str* = None  
    **time_frame**: *str* = 'Daily'  
    **as_dict**: *bool* = False

**Note**: The date is expected in this format: **m/d/Y**