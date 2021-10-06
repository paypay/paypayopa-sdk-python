class URL(object):
    SANDBOX_BASE_URL = 'https://stg-api.sandbox.paypay.ne.jp'
    PRODUCTION_BASE_URL = 'https://api.paypay.ne.jp'
    PERF_BASE_URL = 'https://perf-api.paypay.ne.jp'
    RESOLVE = 'https://developer.paypay.ne.jp/develop/resolve'
    CODE = "/v2/codes"
    PAYMENT = "/v2/payments"
    ACCOUNT_LINK = "/v1/qr/sessions"
    PENDING_PAYMENT = "/v1/requestOrder"
    USER_AUTH = "/v2/user/authorizations"
    GIVE_CASHBACK = "/v2/cashback"
    REVERSAL_CASHBACK = "/v2/cashback_reversal"
    REFUNDS = "/v2/refunds"
    
