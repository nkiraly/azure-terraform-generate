from collections import OrderedDict as OD

command = "az servicebus topic subscription show --ids %s"

def itemId(details, name):
    try:
        return details[name]["id"]
    except (TypeError, KeyError):
        return None

def build(details):
    return OD([
        # https://www.terraform.io/docs/providers/azurerm/r/servicebus_subscription.html
        # Required
        ("resource_group_name", details["resourceGroup"]),
        ("namespace_name", details["id"].rsplit("/", 5)[1]),
        ("topic_name", details["id"].rsplit("/", 5)[3]),
        ("name", details["name"]),
        ("max_delivery_count", details["maxDeliveryCount"]),
        # Optional
        ("auto_delete_on_idle", details["autoDeleteOnIdle"]),
        ("dead_lettering_on_message_expiration", details["deadLetteringOnMessageExpiration"]),
        ("default_message_ttl", details["defaultMessageTimeToLive"]),
        ("enable_batched_operations", details["enableBatchedOperations"]),
        ("lock_duration", details["lockDuration"]),
        ("requires_session", details["requiresSession"]),
        ("forward_to", details["forwardTo"]),
        ("forward_dead_lettered_messages_to", details["forwardDeadLetteredMessagesTo"]),
        ("status", details["status"]),
    ])
