# SMS API DOCs

Kwaug SMS API is to enable users who want to send messages through API, other than platform, to send messages.

[https://sms.kwaug.net](https://sms.kwaug.net/#pricing)
## Installation

No installation requirements needed. Simple as sending request to server

## Production server (Live)
```
https://sms.kwaug.net/
```
Please note that there is no sandbox server availed. For testing, still use the production server. To view 
pricing, please visit the same url link

## API Credentials
To use API, you need primary_sms_api_key, find this under profile, accounts, You will see it there. 

## Usage

### Send SMS Messages

#### Error Response
The response incase of any error is
```json
{
    "error": true,
    "message": "Error message will be here",
    "extra": "this is only for mobile money deposit"
}
```

#### Get REQUEST:

```
https://sms.kwaug.net/api/sendmessage/?username=admin&primary_sms_api_key=eb6dac89-6a65-458f-8470-99b415012463&phone_number=7XXXXXXXXX&message=hello%20there
```
Get (Curl) Request
```bash
curl -X GET "https://sms.kwaug.net/api/sendmessage/?username=admin&primary_sms_api_key=eb6dac89-6a65-458f-8470-99b415012463&phone_number=7XXXXXXXXX&message=hello%20there"
```

#### Post REQUEST

##### Single Receipent

Post (Curl) Request
```bash
curl -X POST "https://sms.kwaug.net/api/postmessage/" \
     -d '{
        "username": "admin",
        "primary_sms_api_key": "eb6dac89-6a65-458f-8470-99b415012463",
        "phone_number": "7XXXXXXXXX",
        "message": "hello there",
        "schedule_time": "2023-08-31 07:05:07.746582" // optional, examples : 2023-08-31 07:05 , 2023-08-31 07:05.99 etc
     }'
```

Post url
```
https://sms.kwaug.net/api/postmessage/
```

Post Data
```json
{
    "username": "username",
    "primary_sms_api_key": "eb6dac89-6a65-458f-8470-99b415012463",
    "phone_number": "7XXXXXXXXX",
    "message": "hello there",
    "schedule_time": "2023-08-31 07:05:07.746582" // optional, examples : 2023-08-31 07:05 , 2023-08-31 07:05.99 etc
}
```

The successful response
```json
{
    "error": false,
    "message": "Message has been sent successfully",
    "total_cost": 40,
    "current_account_balance": 4880
}
```

##### Multiple Receipents

Post (Curl) Request
```bash
curl -X POST "https://sms.kwaug.net/api/postmessagemultiple/" \
     -d '{
        "username": "username",
        "primary_sms_api_key": "eb6dac89-6a65-458f-8470-99b415012463",
        "recipients": ["7XXXXXXXXX", "7XXXXXXXXX"],
        "message": "hello there",
        "schedule_time" : "2023-08-31 07:05:07.746582" // optional, examples : 2023-08-31 07:05 , 2023-08-31 07:05.99 etc
    }'
```

Post url
```
https://sms.kwaug.net/api/postmessagemultiple/
```

Post Data
```json
{
    "username": "username",
    "primary_sms_api_key": "eb6dac89-6a65-458f-8470-99b415012463",
    "recipients": ["7XXXXXXXXX", "7XXXXXXXXX"],
    "message": "hello there",
    "schedule_time" : "2023-08-31 07:05:07.746582" // optional, examples : 2023-08-31 07:05 , 2023-08-31 07:05.99 etc
}
```

Duplicates will be removed, invalid numbers will lead to an error, ensure the numbers are correct

The successful response
```json
{
    "error": false,
    "message": "Message has been sent successfully",
    "total_cost": 40,
    "current_account_balance": 4880
}
```

### DEPOSIT or TOP UP Money on the Account

```
https://sms.kwaug.net/api/topupaccount/
```

POST only
```json
{
    "username": "admin",
    "primary_sms_api_key": "eb6dac89-6a65-458f-8470-99b415012463", 
    "amount": 500,
    "phone_number": "07XXXXXXX"

}
```

The Successful response
```json
{
    "error": false,
    "message": "Successfully Processed, Please Enter your Pin",
    "extra": "Fraud is punishable by law and account deactivation or deletion. No refund made incase."
}
```

The failed response
```json
{
    "error": true,
    "message": "Error message will be here"
}
```
### CHECK Account Balance

```
https://sms.kwaug.net/api/checkbalance/
```

POST only
```json
{
    "username": "admin",
    "primary_sms_api_key": "eb6dac89-6a65-458f-8470-99b415012463"

}
```

The Successful response
```json
{
    "error": false,
    "account_balance": 2350
}
```

The failed response
```json
{
    "error": true,
    "message": "Error message will be here"
}
```

## Contributing

Forks and pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[APACHE](https://www.apache.org/licenses/LICENSE-2.0)
