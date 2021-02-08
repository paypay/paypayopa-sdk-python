# Paypay OPA SDK - Python

[![License](https://img.shields.io/:license-apache2.0-red.svg)](https://opensource.org/licenses/Apache-2.0)
[![PyPI Version](https://img.shields.io/pypi/v/paypayopa.svg)](https://pypi.python.org/pypi/paypayopa)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fpaypay%2Fpaypayopa-sdk-python.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Fpaypay%2Fpaypayopa-sdk-python?ref=badge_shield)
[![Build Status](https://travis-ci.org/paypay/paypayopa-sdk-python.svg?branch=master)](https://travis-ci.org/paypay/paypayopa-sdk-python)
[![Coverage Status](https://coveralls.io/repos/github/paypay/paypayopa-sdk-python/badge.svg?branch=feature/testcases)](https://coveralls.io/github/paypay/paypayopa-sdk-python?branch=master)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/paypay/paypayopa-sdk-python.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/paypay/paypayopa-sdk-python/context:python)
[![Black Duck Security Risk](https://copilot.blackducksoftware.com/github/repos/paypay/paypayopa-sdk-python/branches/master/badge-risk.svg)](https://copilot.blackducksoftware.com/github/repos/paypay/paypayopa-sdk-python/branches/master)
[![Maintainability](https://api.codeclimate.com/v1/badges/9165d052bfa9e688ae3f/maintainability)](https://codeclimate.com/github/paypay/paypayopa-sdk-python/maintainability)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=paypay_paypayopa-sdk-python&metric=alert_status)](https://sonarcloud.io/dashboard?id=paypay_paypayopa-sdk-python)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/paypayopa)](https://pypi.python.org/pypi/paypayopa)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a86509528ec944ad9cf86fe2e31a6b27)](https://app.codacy.com/gh/paypay/paypayopa-sdk-python?utm_source=github.com&utm_medium=referral&utm_content=paypay/paypayopa-sdk-python&utm_campaign=Badge_Grade_Settings)
[![BCH compliance](https://bettercodehub.com/edge/badge/paypay/paypayopa-sdk-python?branch=master)](https://bettercodehub.com/)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/4222/badge)](https://bestpractices.coreinfrastructure.org/projects/4222)

So you are a developer and want to start accepting payments using PayPay. PayPay's Payment SDK is the simplest way to achieve the integration. With PayPay's Payment SDK, you can build a custom Payment checkout process to suit your unique business needs and branding guidelines.

# When to use QR Code Payments
QR Code flow is recommended normally in the following scenarios
- Payment to happen on a Tablet
- Payments on Vending Machines
- Payment to happen on a TV Screen
- Printing a QR Code for Bill Payment

## Understanding the Payment Flow
Following diagram defines the flow for Dynamic QR Code.
![](https://www.paypay.ne.jp/opa/doc/v1.0/imgs/dynamicqrcode-sequence.png)

We recommend that the merchant implements a Polling of the Get payment Details API with a 4-5 second interval in order to know the status of the transaction.

## Let's get Started
Once you have understood the payment flow, before we start the integration make sure you have:

- [Registered](https://developer.paypay.ne.jp/) for a PayPay developer/merchant Account
- Get the API key and secret from the Developer Panel.
- Use the sandbox API Keys to test out the integration

### Install pip package
```sh
$ pip install paypayopa
```

## Getting Started
You need to setup your key and secret using the following:

To work in production mode you need to specify your production API_KEY & API_SECRET along with a production_mode True boolean flag
```py
import paypayopa

client = paypayopa.Client(auth=(API_KEY, API_SECRET),
                         production_mode=True)

client.set_assume_merchant("MERCHANT_ID")
```
or


To work in sandbox mode you need to specify your sandbox API_KEY & API_SECRET keys along with a False boolean flag or you could just omit the production_mode flag since it defaults to False if not specified
```py
import paypayopa

client = paypayopa.Client(auth=(API_KEY, API_SECRET),
                         production_mode=False)
```

After setting up the client instance you can get the current PayPay SDK version using the following: 

```py
print(client.get_version())
```

### Create a QR Code
In order to receive payments using this flow, first of all you will need to create a QR Code. Following are the important parameters that you can provide for this method:

| Field  | Required  |Type   | Description  |  
|---|---|---|---|
|merchantPaymentId   |  Yes |string <= 64 characters  |The unique payment transaction id provided by merchant   |
| amount  |Yes   |integer <= 11 characters  |Amount the user has to Pay   |
|codeType   |  Yes |string <= 64 characters  |Please pass the fixed value "ORDER_QR"|
|orderDescription   |No   |string <= 255 characters|Description of the Order, [Click here](https://docs.google.com/presentation/d/1_S4syfMkLDplMVib7ai-L-3oHoIBRmuT6jrCoiANvqQ/edit?usp=sharing) to check how it will show up   |
|isAuthorization   |No   |boolean|By default it will be false, please set true if the amount will be captured later (preauth and capture payment) |

For details of all the request and response parameters , check our [API Documentation guide](https://www.paypay.ne.jp/opa/doc/v1.0/dynamicqrcode#operation/createQRCode)

```py
request = {
    "merchantPaymentId": "cb31bcc0-3b6c-46e0-9002-e5c4bb1e3d5f",
    "codeType": "ORDER_QR",
    "redirectUrl": "http://foobar.com",
    "redirectType":"WEB_LINK",
    "orderDescription":"Example - Mune Cake shop",
    "orderItems": [{
        "name": "Moon cake",
        "category": "pasteries",
        "quantity": 1,
        "productId": "67678",
        "unitPrice": {
            "amount": 1,
            "currency": "JPY"
        }
    }],
    "amount": {
        "amount": 1,
        "currency": "JPY"
    },
}

client.Code.create_qr_code(request)
```

Did you get a **HTTP 201** response, if yes then you are all set for the next step.

<hr>

### Get Payment Details

Now that you have created a Code, the next  step is to implement polling to get Payment Details. We recommend a 4-5 second interval between requests. Following are the important parameters that you can provide for this method:

| Field  | Required  |Type   | Description  |  
|---|---|---|---|
|merchantPaymentId   |  Yes |string <= 64 characters  |The unique payment transaction id provided by merchant   |

### Fetch a particular QR CODE payment details
```py
client.Payment.get_payment_details("<merchantPaymentId>")
```
For details of all the request and response parameters , check our [API Documentation guide](https://www.paypay.ne.jp/opa/doc/jp/v1.0/dynamicqrcode#operation/getPaymentDetails)
On successful payment, the status in the response will change to **COMPLETED**
In case of a Preauth for Payment, the status in the response will change to **AUTHORIZED**

<hr>

### Delete a QRCode
So you want to delete a Code that you have already generated. Following can be possible reasons to use this API:
- User has cancelled the order
- Ensuring race conditions don't come up in the form user has scanned the QR Code and not made the payment and in the meantime the order expires at your end

Following are the important parameters that you can provide for this method:

| Field  | Required  |Type   | Description  |  
|---|---|---|---|
|codeId   |  Yes |string  |This is given as a response in the Create a QR Code method |

```py
client.Code.delete_qr_code("<CodeID>")
```

For details of all the request and response parameters , check our [API Documentation guide](https://www.paypay.ne.jp/opa/doc/jp/v1.0/dynamicqrcode#operation/deleteQRCode)

<hr>

### Cancel a payment
So you want to cancel a Payment. In most cases this should not be needed for payment happening in this flow, however following can be a case when this might be needed.

- Polling for Get Payment Details timeout, and you are uncertain of the status

Note: The Cancel API can be used until 00:14:59 AM the day after the Payment has happened. For 00:15 AM or later, please call the refund API to refund the payment.

Following are the important parameters that you can provide for this method:

| Field  | Required  |Type   | Description  |  
|---|---|---|---|
|merchantPaymentId   |  Yes |string <= 64 characters  |The unique payment transaction id provided by merchant   |


```py
client.Payment.cancel_payment("<merchantPaymentId>")
```

<hr>

### Refund a payment

So the user has decided to return the goods they have purchased and needs to be given a refund. Following are the important parameters that you can provide for this method:

| Field  | Required  |Type   | Description  |  
|---|---|---|---|
|merchantRefundId   |  Yes |string <= 64 characters  |The unique refund transaction id provided by merchant  |
|paymentId   |  Yes |string <= 64 characters  |The payment transaction id provided by PayPay |
|amount   |  Yes |integer <= 11 characters  |The amount to be refunded |
|reason   |  No |integer <= 11 characters  |The reason for refund |

```py
payload = {
    "assumeMerchant": "cb31bcc0-3b6c-46e0-9002-e5c4bb1e3d5f",
    "merchantRefundId": "3b6c-46e0-9002-e5c4bb1e3d5f",
    "paymentId": "456787656",
    "amount": {
        "amount": 1,
        "currency": "JPY"
    },
    "reason": "reason for refund"
}

client.Payment.refund_payment(refund_payment_details)
```

For details of all the request and response parameters , check our [API Documentation guide](https://www.paypay.ne.jp/opa/doc/v1.0/dynamicqrcode#operation/refundPayment). **Please note that currently we only support 1 refund per order.**

<hr>

### Capture a payment authorization

So you are implementing a PreAuth and Capture, and hence want to capture the payment later. In this case, please ensure you have passed *isAuthorization* as *true* in create a code method. Following are the important parameters that you can provide for this method:

| Field  | Required  |Type   | Description  |  
|---|---|---|---|
|merchantPaymentId   |  Yes |string <= 64 characters  |The unique payment transaction id provided by merchant   |
|merchantCaptureId   |  Yes |string <= 64 characters  |The unique capture transaction id provided by merchant  |
| amount  |Yes   |integer <= 11 characters  |Amount to be captured   |
|orderDescription   |Yes   |string <= 255 characters|Description of the Capture for the user|

```py
request_payload = {
    "merchantPaymentId": "merchant_payment_id",
    "amount": {
        "amount": 1,
        "currency": "JPY"
    },
    merchantCapture_id: "31bcc0-3b6c-46e0-9002",
    orderDescription: "Example - Mune Cake shop"
}

client.Payment.capture_payment(request_payload)
```
For details of all the request and response parameters , check our [API Documentation guide](https://www.paypay.ne.jp/opa/doc/v1.0/dynamicqrcode#operation/capturePaymentAuth).

<hr>

### Revert a payment authorization
So the order has cancelled the order while the payment was still Authorized, please use the revert a payment authorization method to refund back to the user. Following are the important parameters that you can provide for this method:

| Field  | Required  |Type   | Description  |  
|---|---|---|---|
|merchantRevertId   |  Yes |string <= 64 characters  |The unique revert transaction id provided by merchant   |
|paymentId   |  Yes |string <= 64 characters  |The payment transaction id provided by PayPay |
|reason   |No   |string <= 255 characters|Reason for reverting the payment authorization|

```py
request_payload = {
    "merchantRevertId": "cb31bcc0-3b6c-46e0-9002-e5c4bb1e3d5f"
    "paymentId": "1585537300"
    "reason":  "reason for refund"
}

client.Payment.revert_payment(request_payload)
```
For List of params refer to the API guide :
https://www.paypay.ne.jp/opa/doc/v1.0/dynamicqrcode#operation/revertAuth

<hr>

### Fetch refund status and details
So you want to confirm the status of the refund, maybe because the request for the refund timed out when you were processing the same. Following are the important parameters that you can provide for this method:

| Field  | Required  |Type   | Description  |  
|---|---|---|---|
|merchantRefundId   |  Yes |string <= 64 characters  |The unique refund transaction id provided by merchant  |


```py
client.Payment.refund_status("<merchantRefundId>")
```
For details of all the request and response parameters , check our [API Documentation guide](https://www.paypay.ne.jp/opa/doc/v1.0/dynamicqrcode#operation/getRefundDetails).

<hr>

# When to use Native Payments
Native Payments is recommended normally in the following scenarios
- If you want provide your customers with the easiest possible checkout
- You have the security in place to ensure our mutual customers money is safe (We have a strict evaluation procedure to enforce the same)

## Integrating Native Integration

### Acquire User Authorization
First of all you need to acquire a user Authorization. Following diagram defines the flow to acquire a user authorization.

![](https://www.paypay.ne.jp/opa/doc/v1.0/imgs/authorization-sequence.png)

In order to acquire an authorization you need to create a JWT Token -

|cliam|	required | type|	description|
|---|---|---|---|
|iss| yes|	string|	the merchant name|
|exp| yes|	number|	The expiration date of the authorization page URL. Set with epoch time stamp (seconds).
|scope| yes|	string|	direct_debit|
|nonce| yes|	string|	will be sent back with response for the client side validation|
|redirectUrl| yes| string|	The callback endpoint provided by client. Must be HTTPS, and its domain should be in the allowed authorization callback domains|
|referenceId| yes|	string|	The id used to identify the user in merchant system. It will be stored in the PayPay db for reconciliation purpose|
|deviceId| no|	string| The user mobile phone device id. If it is provided, we can use it to verify the user and skip the SMS verification, so as to provide more fluent UX|
|phoneNumber| no|	string| The user mobile phone number|

```py
# Helper function to create a JWT Token for requesting user Authorization
client.encode_jwt(API_SECRET,
                redirectUrl = "https://example.com",
                deviceId = "qwertyuiopoiuytre54567",
                phoneNumber = 90999999999 )
```

Once the user has granted authorization, we will return the UserAuthorizationID as a part of the JWT Token in response/ webhook

```py
# Retrieving userAuthorizationId from response JWT
client.decode_jwt(API_SECRET, token)
```

### Unlink a user from the client

| Field  | Required  |Type   | Description  |  
|---|---|---|---|
|userAuthorizationId|yes|string <= 64 characters|The PayPay user reference id returned by the user authorization flow|

```py
# Calling the method to unlink a Payment
response = client.User.unlink_user_athorization('userAuthorizationId')
# Printing if the method call was SUCCESS
print(response.resultInfo.code)
```

Did you get **SUCCESS** in the print statement above, if yes then the API execution has happened correctly.

For details of all the request and response parameters , check our [API Documentation guide](https://www.paypay.ne.jp/opa/doc/v1.0/direct_debit#operation/unlinkUser).

<hr>



### Create a payment
In order to take a payment, you will need to send a request to us with the following parameters:

| Field  | Required  |Type   | Description  |  
|---|---|---|---|
|merchantPaymentId   |  Yes |string <= 64 characters  |The unique payment transaction id provided by merchant   |
|userAuthorizationId   |  Yes |string <= 64 characters  |The PayPay user reference id returned by the user authorization flow |
| amount  |Yes   |integer <= 11 characters  |Amount the user has to Pay   |
|orderDescription   |No   |string <= 255 characters|Description of the Order, [Click here](https://docs.google.com/presentation/d/1_S4syfMkLDplMVib7ai-L-3oHoIBRmuT6jrCoiANvqQ/edit#slide=id.g6feeaf7a3d_1_0) to check how it will show up  |

```py
# Creating the payload to create a Payment, additional parameters can be added basis the API Documentation
request = {
    merchantPaymentId = "my_payment_id",
    userAuthorizationId = "my_user_authorization_id",
    amount = {amount = 1, currency = "JPY"},
    orderDescription = "Mune's Favourite Cake"
}
# Calling the method to create a payment
response = client.Payment.create(request)
# Printing if the method call was SUCCESS, this does not mean the payment was a success
print(response.resultInfo.code)
```

Did you get **SUCCESS** in the print statement above, if yes then the API execution has happened correctly.

For details of all the request and response parameters , check our [API Documentation guide](https://www.paypay.ne.jp/opa/doc/v1.0/direct_debit#operation/createPayment)

<hr>

### Get Payment Details
Now that you have created a payment, in case the payment request timeout, you can call get payment details method to know the payment status. Following are the important parameters that you can provide for this method:

| Field  | Required  |Type   | Description  |  
|---|---|---|---|
|merchantPaymentId   |  Yes |string <= 64 characters  |The unique payment transaction id provided by merchant   |

```py
# Calling the method to get payment details
response = client.Payment.get_payment_details("<merchantPaymentId>")
# Printing if the method call was SUCCESS, this does not mean the payment was a success
print(response.resultInfo.code)
# Printing if the transaction status for the code has COMPLETED/ AUTHORIZED
print(response.data.status)
```

Did you get **SUCCESS** in the print statement above, if yes then the API execution has happen correctly.

On successful payment, the status in response.data.status will be **COMPLETED**
For details of all the request and response parameters , check our [API Documentation guide](https://www.paypay.ne.jp/opa/doc/v1.0/webcashier#operation/getPaymentDetails)

<hr>

### Cancel a payment
So you want to cancel a Payment. In most cases this should not be needed for payment happening in this flow, however following can be a case when this might be needed.
- Initial create payment timeout and you want to cancel the Payment
- Get Payment Details timeout, and you are uncertain of the status

Note: The Cancel API can be used until 00:14:59 AM the day after the Payment has happened. For 00:15 AM or later, please call the refund API to refund the payment.

Following are the important parameters that you can provide for this method:

| Field  | Required  |Type   | Description  |  
|---|---|---|---|
|merchantPaymentId   |  Yes |string <= 64 characters  |The unique payment transaction id provided by merchant   |

```py
# Calling the method to cancel a Payment
response = client.Payment.cancel_payment("<merchantPaymentId>")
# Printing if the method call was SUCCESS
print(response.resultInfo.code)
```

Did you get **SUCCESS** in the print statement above, if yes then the API execution has happend correctly.

For details of all the request and response parameters , check our [API Documentation guide](https://www.paypay.ne.jp/opa/doc/v1.0/direct_debit#operation/cancelPayment)

<hr>

### Refund a payment
So the user has decided to return the goods they have purchased and needs to be giveb a refund. Following are the important parameters that you can provide for this method:

| Field  | Required  |Type   | Description  |  
|---|---|---|---|
|merchantRefundId   |  Yes |string <= 64 characters  |The unique refund transaction id provided by merchant  |
|paymentId   |  Yes |string <= 64 characters  |The payment transaction id provided by PayPay |
|amount   |  Yes |integer <= 11 characters  |The amount to be refunded |
|reason   |  No |integer <= 11 characters  |The reason for refund |

```py
# Creating the payload to refund a Payment, additional parameters can be added basis the API Documentation
request = {
    merchantRefundId = "merchant_refund_id"
    paymentId = "paypay_payment_id
    amount = 1
    reason = "reason for refund"
}
# Calling the method to refund a Payment
response = client.Payment.refund_payment(request)
# Printing if the method call was SUCCESS
print(response.resultInfo.code)
```

Did you get **SUCCESS** in the print statement above, if yes then the API execution has happened correctly.

For details of all the request and response parameters , check our [API Documentation guide](https://www.paypay.ne.jp/opa/doc/v1.0/direct_debit#operation/refundPayment). **Please note that currently we only support 1 refund per order.**

<hr>

### Fetch refund status and details

So you want to confirm the status of the refund, maybe because the request for the refund timed out when you were processing the same. Following are the important parameters that you can provide for this method:

| Field  | Required  |Type   | Description  |  
|---|---|---|---|
|merchantRefundId   |  Yes |string <= 64 characters  |The unique refund transaction id provided by merchant  |

```py
# Calling the method to get Refund Details
response = client.Payment.refund_details("<merchantRefundId>")
# Printing if the method call was SUCCESS
print(response.resultInfo.code)
```
Did you get **SUCCESS** in the print statement above, if yes then the API execution has happen correctly.

For details of all the request and response parameters , check our [API Documentation guide](https://www.paypay.ne.jp/opa/doc/v1.0/direct_debit#operation/getRefundDetails).

<hr>

### Acquire User Authorization

So you want to confirm the status of the refund, maybe because the request for the refund timed out when you were processing the same. Following are the important parameters that you can provide for this method:

| Claim  | Required  |Type   | Description  |  
|---|---|---|---|
| scopes   |  Yes | Array of string	  | Items Enum: 'direct_debit' 'cashback' 'get_balance' 'quick_pay' 'continuous_payments' 'merchant_topup' 'pending_payments' 'user_notification' 'user_topup' 'user_profile' 'preauth_capture_native' 'preauth_capture_transaction' 'push_notification' 'notification_center_ob' 'notification_center_ab' 'notification_center_tl' Scopes of the user authorization |
| nonce | Yes | string | Random generated string |
| redirectType | No | string | Default: 'WEB_LINK' Enum: 'APP_DEEP_LINK' 'WEB_LINK' Parameter to decide whether to redirect to merchant app or merchant web application |
| redirectUrl | Yes | string | The callback endpoint provided by client. For 'WEB_LINK' it must be HTTPS, and its domain should be in the allowed authorization callback domains |
| referenceId | Yes | string | The id used to identify the user in merchant system. It will be stored in the PayPay db for reconsilliation purpose |
| phoneNumber | No | string | The user mobile phone number |
| deviceId | No | string | The user mobile phone device id. If it is provided, we can use it to verify the user and skip the SMS verification, so as to provide more fluent UX |
| userAgent | No | string | The User agent of the web browser. When redirectType is 'WEB_LINK' this parameter is provided, on mobile devices PayPay tries to open the browser that the merchant website is using. |

```py
payload = {
  "scopes": [
    "direct_debit"
  ],
  "nonce": "rtyuhghj7989",
  "redirectType": "WEB_LINK",
  "redirectUrl": "www.example.com",
  "referenceId": "uioiugf789",
  "phoneNumber": "90999999999",
  "deviceId": "qwertyuiopoiuytre54567",
  "userAgent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}

client.Account.create_qr_session(payload)
```

Once the user has granted authorization, we will return the UserAuthorizationID as a part of the JWT Token in response/ webhook


```py
# Retrieving userAuthorizationId from response JWT
client.decode_jwt(API_SECRET, token)
```

Did you get **SUCCESS** in the print statement above, if yes then the API execution has happen correctly.

For details of all the request and response parameters , check our [API Documentation guide](https://www.paypay.ne.jp/opa/doc/v1.0/preauth_capture#operation/createAuth).

<hr>

### Create a Payment Authorization

In order to create a payment authorization, you will need to send a request to us with the following parameters:

| Claim  | Required  |Type   | Description  |  
|---|---|---|---|
| merchantPaymentId | Yes | string <= 64 characters	 | The unique payment transaction id provided by merchant |
| userAuthorizationId | Yes | string <= 64 characters	 | The PayPay user reference id returned by the user authorization flow |
| amount | Yes | integer <= 11 characters	 | Amount the user has to Pay |
| requestedAt | Yes | integer | Epoch timestamp in seconds |
| orderDescription | Yes | string <= 255 characters	| Description of the Capture for the user |

```py
# Creating the payload for a payment authorization request, additional parameters can be added basis the API Documentation
request_payload = {
    "merchantPaymentId": "merchant_payment_id",
    "userAuthorizationId": "user_authorization_id",
    "amount": {
      "amount": 26.00,
      "currency": "JPY"
    },
    "requestedAt": 5353454354,
    "orderReceiptNumber": "435435435",
    "orderDescription": "Mune's Favourite Cake",
  }

# Calling the method to create a payment authorization
client.Preauth.pre_authorize_create(request_payload)
```

<hr>

### Creating a Continuous Payment authorization

In order to acquire an authorization you need to create a JWT Token -

| Claim  | Required  |Type   | Description  |  
|---|---|---|---|
| scopes | Yes | Array of string	| Items Enum: 'direct_debit' 'cashback' 'get_balance' 'quick_pay' 'continuous_payments' 'merchant_topup' 'pending_payments' 'user_notification' 'user_topup' 'user_profile' 'preauth_capture_native' 'preauth_capture_transaction' 'push_notification' 'notification_center_ob' 'notification_center_ab' 'notification_center_tl' Scopes of the user authorization |
| nonce | Yes | string | Random generated string |
| redirectType | No | string | Default: 'WEB_LINK' Enum: 'APP_DEEP_LINK' 'WEB_LINK' Parameter to decide whether to redirect to merchant app or merchant web application |
| redirectUrl | Yes | string | The callback endpoint provided by client. For 'WEB_LINK' it must be HTTPS, and its domain should be in the allowed authorization callback domains |
| referenceId | Yes | string | The id used to identify the user in merchant system. It will be stored in the PayPay db for reconsilliation purpose |
| phoneNumber | No | string | The user mobile phone number |
| deviceId | No | string | The user mobile phone device id. If it is provided, we can use it to verify the user and skip the SMS verification, so as to provide more fluent UX |
| userAgent | No | string | The User agent of the web browser. When redirectType is 'WEB_LINK' this parameter is provided, on mobile devices PayPay tries to open the browser that the merchant website is using. |

```py
# Creating the payload for a payment authorization request, additional parameters can be added basis the API Documentation
request_payload = {
    "merchantPaymentId": "merchant_payment_id",
    "userAuthorizationId": "my_user_authorization_id",
    "orderDescription":"Mune's Favourite Cake",
    "amount": {
          "amount": 1,
          "currency": "JPY"
          }
    }

# Calling the method to create a continuous payment authorization
client.Payment.create_continuous_payment(request_payload)

# Printing if the method call was SUCCESS, this does not mean the payment was a success
print(response.resultInfo.code)
```

<hr>

### Creating a Pending Payment authorization

In order to acquire an authorization you need to create a JWT Token -

| Claim  | Required  |Type   | Description  |  
|---|---|---|---|
| merchantPaymentId | Yes | string <= 64 characters	 | The unique payment transaction id provided by merchant |
| userAuthorizationId | Yes | string <= 64 characters	 | The PayPay user reference id returned by the user authorization flow |
| amount | Yes | integer <= 11 characters	 | Amount the user has to Pay |
| requestedAt | Yes | integer | Epoch timestamp in seconds |
| orderDescription | Yes | string <= 255 characters	| Description of the Capture for the user |

```py
# Creating the payload for a payment authorization request, additional parameters can be added basis the API Documentation
request_payload = {
  "merchantPaymentId": "merchant_payment_id",
  "userAuthorizationId": "my_user_authorization_id",
  "amount": {
    "amount": 1,
    "currency": "JPY"
  },
  "requestedAt": 01918189,
  "expiryDate": null,
  "storeId": "001",
  "terminalId": "0042",
  "orderReceiptNumber": "0878",
  "orderDescription":"Example - Mune Cake shop",
    "orderItems": [{
        "name": "Moon cake",
        "category": "pasteries",
        "quantity": 1,
        "productId": "67678",
        "unitPrice": {
            "amount": 1,
            "currency": "JPY"
        }
    }],
  "metadata": {}
}

# Calling the method to create a continuous payment authorization
client.Pending.create_pending_payment(request_payload)

# Printing if the method call was SUCCESS, this does not mean the payment was a success
print(response.resultInfo.code)
```

Did you get **SUCCESS** in the print statement above, if yes then the API execution has happen correctly.

On successful payment, the status in response.data.status will be **COMPLETED**
For details of all the request and response parameters , check our [API Documentation guide](https://www.paypay.ne.jp/opa/doc/v1.0/pending_payments#operation/createPayment)

<hr>

### Get Pending Payment Details
Now that you have created a pending payment, in case the payment request timeout, you can call get payment details method to know the payment status. Following are the important parameters that you can provide for this method:

| Field  | Required  |Type   | Description  |  
|---|---|---|---|
|merchantPaymentId   |  Yes |string <= 64 characters  |The unique payment transaction id provided by merchant   |

```py
# Calling the method to get payment details
response = client.Pending.get_payment_details("<merchantPaymentId>")
# Printing if the method call was SUCCESS, this does not mean the payment was a success
print(response.resultInfo.code)
# Printing if the transaction status for the code has COMPLETED/ AUTHORIZED
print(response.data.status)
```

Did you get **SUCCESS** in the print statement above, if yes then the API execution has happen correctly.

On successful payment, the status in response.data.status will be **COMPLETED**
For details of all the request and response parameters , check our [API Documentation guide](https://www.paypay.ne.jp/opa/doc/v1.0/pending_payments#operation/getPaymentDetails)

<hr>

### Cancel Pending Payment Details

| Field  | Required  |Type   | Description  |  
|---|---|---|---|
|merchantPaymentId   |  Yes |string <= 64 characters  |The unique payment transaction id provided by merchant   |

```py
# Calling the method to cancel pending payment
response = client.Pending.cancel_payment("<merchantPaymentId>")
# Printing if the method call was SUCCESS, this does not mean the payment was a success
print(response.resultInfo.code)
# Printing if the transaction status for the code has COMPLETED/ AUTHORIZED
print(response.data.status)
```

Did you get **SUCCESS** in the print statement above, if yes then the API execution has happen correctly.

On successful payment, the status in response.data.status will be **COMPLETED**
For details of all the request and response parameters , check our [API Documentation guide](https://www.paypay.ne.jp/opa/doc/v1.0/pending_payments#operation/cancelPendingOrder)

<hr>

### Refund a Pending Payment
So the user has decided to return the goods they have purchased and needs to be given a refund. Following are the important parameters that you can provide for this method:

| Field  | Required  |Type   | Description  |  
|---|---|---|---|
|merchantRefundId   |  Yes |string <= 64 characters  |The unique refund transaction id provided by merchant  |
|paymentId   |  Yes |string <= 64 characters  |The payment transaction id provided by PayPay |
|amount   |  Yes |integer <= 11 characters  |The amount to be refunded |
|reason   |  No |integer <= 11 characters  |The reason for refund |

```py
payload = {
    "assumeMerchant": "cb31bcc0-3b6c-46e0-9002-e5c4bb1e3d5f",
    "merchantRefundId": "3b6c-46e0-9002-e5c4bb1e3d5f",
    "paymentId": "456787656",
    "amount": {
        "amount": 1,
        "currency": "JPY"
    },
    "reason": "reason for refund"
}

client.Pending.refund_payment(refund_payment_details)
```

On successful payment, the status in response.data.status will be **COMPLETED**
For details of all the request and response parameters , check our [API Documentation guide](https://www.paypay.ne.jp/opa/doc/v1.0/pending_payments#operation/refundPayment)

<hr>

### Cashback

Paypay Cashback API can give users some balance.
If you use Cashback API, you should authorize paypay user to use **create_qr_session** sdk.

#### Give Cashback 

| Field  | Required  |Type   | Description  |  
|---|---|---|---|
|merchantCashbackId   |  Yes |string <= 64 characters  |The unique cashback transaction id provided by merchant  |
|userAuthorizationId   |  Yes |string <= 64 characters  |The paypay user reference id provided by PayPay |
|amount   |  Yes |integer <= 11 characters  |The amount to cashback |
|currency   |  Yes |string |"JPY" |
|requestedAt   |  Yes |integer |Epoch timestamp in seconds |
|orderDescription   |  No |string <= 255 characters |Description of the order |
|walletType   |  No |string  |Wallet type |
|expiryDate   |  No |date  |The date on which the Cashback Expires |
|metadata   |  No |string  |Extra information the merchant want to add |

```python
payload = {
    "merchantCashbackId": "ab31bcc0-3b6c-46e0-9002-e5c4bb1e3d5f",
    "userAuthorizationId": "3b6c-a7c9-9002-e5c4bb1e3d5f",
    "amount": {
        "amount": 100,
        "currency": "JPY"
    },
    "requestedAt": 1609749559,
    "orderDescription": "order description",
    "walletType": "PREPAID",
    "expiryDate": None,
    "metadata": ""
}
client.Cashback.give_cashback(payload)
```
#### Check Cashback Details 

| Field  | Required  |Type   | Description  |  
|---|---|---|---|
|merchantCashbackId   |  Yes |string <= 64 characters  |The unique cashback transaction id provided by merchant  |

```python  
merchant_cashback_id = "ab31bcc0-3b6c-46e0-9002-e5c4bb1e3d5f"
client.Cashback.check_give_cashback(merchant_cashback_id)
```

#### Reverse Cashback

| Field  | Required  |Type   | Description  |  
|---|---|---|---|
|merchantCashbackReversalId   |  Yes |string <= 64 characters  |The unique reversal cashback transaction id provided by merchant  |
|merchantCashbackId   |  Yes |string <= 64 characters  |The unique cashback transaction id provided by merchant  |
|amount   |  Yes |integer <= 11 characters  |The amount to cashback |
|currency   |  Yes |string |"JPY" |
|reason   |  No |string <= 255 characters |Reason for reversing the cashback |
|metadata   |  No |string  |Extra information the merchant want to add |

```python
payload = {
    "merchantCashbackReversalId": "e031bcc0-3b6c-9a7d-9002-e5c4cc1e3d5f",
    "merchantCashbackId": "ab31bcc0-3b6c-46e0-9002-e5c4bb1e3d5f",
    "amount": {
        "amount": 100,
        "currency": "JPY"
    },
    "requestedAt": 1609749559,
    "reason": "reversal reason",
    "metadata": {}
}
client.Cashback.reverse_cashback(payload)
```

#### Check Cashback Reversal Details

| Field  | Required  |Type   | Description  |  
|---|---|---|---|
|merchantCashbackReversalId   |  Yes |string <= 64 characters  |The unique reversal cashback transaction id provided by merchant  |
|merchantCashbackId   |  Yes |string <= 64 characters  |The unique cashback transaction id provided by merchant  |

```python
merchant_cashback_reversal_id = "e031bcc0-3b6c-9a7d-9002-e5c4cc1e3d5f"
merchant_cashback_id = "ab31bcc0-3b6c-46e0-9002-e5c4bb1e3d5f"
client.Cashback.check_reversal_cashback(merchant_cashback_reversal_id, merchant_cashback_id)
```


### Get refund details of a Pending payment

So the user has decided to return the goods they have purchased and needs to be given a refund. Following are the important parameters that you can provide for this method:

| Field  | Required  |Type   | Description  |  
|---|---|---|---|
|merchantPaymentId   |  Yes |string <= 64 characters  |The unique payment transaction id provided by merchant   |

```py
# Calling the method to cancel pending payment
response = client.Pending.refund_details("<merchantPaymentId>")
# Printing if the method call was SUCCESS, this does not mean the payment was a success
print(response.resultInfo.code)
# Printing if the transaction status for the code has COMPLETED/ AUTHORIZED
print(response.data.status)
```

Did you get **SUCCESS** in the print statement above, if yes then the API execution has happen correctly.

On successful payment, the status in response.data.status will be **COMPLETED**
For details of all the request and response parameters , check our [API Documentation guide](https://www.paypay.ne.jp/opa/doc/v1.0/pending_payments#operation/getRefundDetails)



### Error Handling
PayPay uses HTTP response status codes and error code to indicate the success or failure of the requests. With this information, you can decide what error handling strategy to use. In general, PayPay returns the following http status codes.

#### HTTP 2xx
**200**
Everything works as expected.

**201**
The requested resource(e.g. dynamic QR code) was created.

**202**
Means the request is received, and will be processed sometime later.

#### HTTP 4xx
**400**
This status code indicates an error because the information provided in request is not able to be processed. The following OPA error code may be returned.

- INVALID_PARAMS
The information provided by the request contains invalid data. E.g. unsupported currency.

- UNACCEPTABLE_OP
The requested operation is not able to be processed due to the current condition. E.g. the transaction limit exceeded.

- NO_SUFFICIENT_FUND
There is no sufficient fund for the transaction.

**401**
This status code indicates an authorization error. The following OPA error code may be returned.

- UNAUTHORIZED
No valid api key and secret provided.

- OP_OUT_OF_SCOPE
The operation is not permitted.

**404**
This status code indicates that the requested resource is not existing in the system.

**429**
This status code indicates that the client sent too many requests in a specific period of time, and hit the rate limits. You should slow down the request sending or contact us to rise your limit.

#### HTTP 5xx
**500**

This status code indicates that something went wrong on the PayPay side. A few OPA error code could be returned.

- TRANSACTION_FAILED
This code means the transaction is failed on the PayPay side. You can create new transactions for the same purpose with reasonable backoff time.

- INTERNAL_SERVER_ERROR
This code means that something goes wrong, but we don't know exactly if the transaction has happened or not. It should be treated as unknown payment status.

**502,503,504**
Treated as unknown payment status.

#### Timeout
The recommended timeout setting is specified in each API. The most important one is for the payment creation api, where the read timeout should not be less than 30 seconds. When timeout happens, it should be treated as unknown payment status.

#### Handle unknown payment status
There are two ways to react with this situation:
- Use the query api to query the transaction status. If the original transaction was failed or not found in PayPay, you can start a new transaction for the same purpose.
- Or, you can cancel the transaction, if the cancel api is provided. After the cancellation is accepted, you can start a new transaction for the same purpose.


### Response code list
**Common response code**

| Status  | CodeId  |Code   | Message  |  
|---|---|---|---|
|200|	08100001|	SUCCESS|	Success|
|202|	08100001|	REQUEST_ACCEPTED|	Request accepted|
|400|	08100006|	INVALID_REQUEST_PARAMS|	Invalid request params|
|401|	08100023|	OP_OUT_OF_SCOPE|	The operation is not permitted|
|400|	08100024|	MISSING_REQUEST_PARAMS|	|
|401|	08100016|	UNAUTHORIZED|	Unauthorized request|
|404|	08100007|	OPA_CLIENT_NOT_FOUND|	OPA Client not found|
|429|	08100998|	RATE_LIMIT|	Too many requests|
|500|	08100026|	SERVICE_ERROR|	|
|500|	08101000|	INTERNAL_SERVER_ERROR|	Something went wrong on PayPay service side|
|503|	08100999|	MAINTENANCE_MODE|	Sorry, we are down for scheduled maintenance|

**Create a QRCode**

|Status	|CodeId	|Code	|Message|
|---|---|---|---|
|400|	01652073|	DUPLICATE_DYNAMIC_QR_REQUEST|	Duplicate Dynamic QR request error|
|400|	00400060|	PRE_AUTH_CAPTURE_UNSUPPORTED_MERCHANT|	Merchant do not support| Pre-Auth-Capture
|400|	00400061|	PRE_AUTH_CAPTURE_INVALID_EXPIRY_DATE|	Provided Expiry Date is above the allowed limit of Max allowed expiry days|
|400|	01650000|	DYNAMIC_QR_BAD_REQUEST|	Dynamic QR bad request error|

**Get payment details**

|Status	|CodeId	|Code	|Message|
|---|---|---|---|
|400|	01652075|	DYNAMIC_QR_PAYMENT_NOT_FOUND|	Dynamic QR payment not found|
|400|	01650000|	DYNAMIC_QR_BAD_REQUEST|	Dynamic QR bad request error|

**Delete a QRCode**

|Status	|CodeId	|Code	|Message|
|---|---|---|---|
|400	|01652074	|DYNAMIC_QR_ALREADY_PAID|	Dynamic QR already paid|
|400	|01650000	|DYNAMIC_QR_BAD_REQUEST|	Dynamic QR bad request error|
|404	|01652072	|DYNAMIC_QR_NOT_FOUND|	Dynamic qr code not found|

**Cancel a Payment**

|Status	|CodeId	|Code	|Message|
|---|---|---|---|
|400	|00200044	|ORDER_NOT_REVERSIBLE|	Order cannot be reversed|
|500	|00200034	|INTERNAL_SERVER_ERROR|	Request timed out|

**Refund a payment**

|Status	|CodeId	|Code	|Message|
|---|---|---|---|
|400	|00200004	|INVALID_PARAMS	|Invalid parameters received|
|400	|00200013	|UNACCEPTABLE_OP	|Order cannot be refunded|
|400	|00200014	|UNACCEPTABLE_OP	|Multiple refund not allowed|
|400	|00200015	|INVALID_PARAMS	|Invalid refund amount|
|400	|01103027	|CANCELED_USER	|Canceled user|
|404	|00200001	|RESOURCE_NOT_FOUND	|Order not found|
|500	|00200002	|TRANSACTION_FAILED	|Transaction failed|
|500	|00200003	|TRANSACTION_FAILED	|Transaction failed|
|500	|00800017	|TRANSACTION_FAILED	|Balance exceeded|
|500	|00200034	|INTERNAL_SERVER_ERROR	|Request timed out|

**Fetch refund status and details**

|Status	|CodeId	|Code	|Message|
|---|---|---|---|
|404	|00200018|	NO_SUCH_REFUND_ORDER	|Refund not found|
|500	|00200034|	INTERNAL_SERVER_ERROR	|Request timed out|

**Capture a payment authorization**

|Status	|CodeId	|Code	|Message|
|---|---|---|---|
|202	|08300103	|USER_CONFIRMATION_REQUIRED	|User confirmation required as requested amount is above allowed limit|
|400	|00400035	|UNACCEPTABLE_OP	|Total transaction limit exceeds merchant limit|
|400	|00200039	|ALREADY_CAPTURED	|Cannot capture already captured acquiring order|
|400	|01103027	|CANCELED_USER	|Canceled user|
|400	|00400062	|HIGHER_CAPTURE_NOT_PERMITTED	|Merchant not allowed to capture higher amount|
|400	|00200043	|ORDER_EXPIRED	|Order cannot be captured or updated as it has already expired|
|400	|00200035	|ORDER_NOT_CAPTURABLE	|Order is not capturable|
|400	|00200038	|REAUTHORIZATION_IN_PROGRESS	|Order is being reauthorized|
|400	|00400064	|TOO_CLOSE_TO_EXPIRY	|Order cannot be reauthorized as request is too close to expiry time|

**Revert a payment authorization**

|Status	|CodeId	|Code	|Message|
|---|---|---|---|
|400	|00200042|ORDER_NOT_CANCELABLE	|Order is not cancelable|


## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fpaypay%2Fpaypayopa-sdk-python.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Fpaypay%2Fpaypayopa-sdk-python?ref=badge_large)
