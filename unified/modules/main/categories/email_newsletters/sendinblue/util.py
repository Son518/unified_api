import sib_api_v3_sdk


def sendinblue_configuration(headers):

    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = headers['api_key']
    return configuration