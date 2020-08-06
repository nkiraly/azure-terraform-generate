from collections import OrderedDict as OD

command = "az servicebus topic subscription rule show --ids %s"

def itemId(details, name):
    try:
        return details[name]["id"]
    except (TypeError, KeyError):
        return None

def build(details):
    ro = OD([
        # https://www.terraform.io/docs/providers/azurerm/r/servicebus_subscription_rule.html
        # Required
        ("resource_group_name", details["resourceGroup"]),
        ("namespace_name", details["id"].rsplit("/", 7)[1]),
        ("topic_name", details["id"].rsplit("/", 7)[3]),
        ("subscription_name", details["id"].rsplit("/", 7)[5]),
        ("name", details["name"]),
        ("filter_type", details["filterType"]),
        ("action", details["action"]),
    ])

    # Optional; Required for matching filter type
    if details["filterType"] == "SqlFilter":
        ro["sql_filter"] = details["sqlFilter"]["sqlExpression"]
    elif details["filterType"] == "CorrelationFilter":
        ro["correlation_filter"] = OD([
          ("content_type", details["correlationFilter"]["contentType"])
          ("correlation_id", details["correlationFilter"]["correlationId"])
          ("label", details["correlationFilter"]["label"])
          ("message_id", details["correlationFilter"]["messageId"])
          ("reply_to", details["correlationFilter"]["replyTo"])
          ("reply_to_session_id", details["correlationFilter"]["replyToSessionId"])
          ("session_id", details["correlationFilter"]["sessionId"])
          ("to", details["correlationFilter"]["to"])
        ])    

    return ro
