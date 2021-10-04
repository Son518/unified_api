from hubspot import HubSpot

def hubspot_client(headers):

    api_client = HubSpot(api_key=headers["api_key"])
    return api_client