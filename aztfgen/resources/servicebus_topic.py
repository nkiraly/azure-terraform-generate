from collections import OrderedDict as OD

command = "az servicebus topic show --ids %s"

def itemId(details, name):
    try:
        return details[name]["id"]
    except (TypeError, KeyError):
        return None

def build(details):
    return OD([
        # https://www.terraform.io/docs/providers/azurerm/r/servicebus_topic.html
        # Required
        ("resource_group_name", details["resourceGroup"]),
        ("namespace_name", details["id"].rsplit("/", 3)[1]),
        ("name", details["name"]),
        # Optional
        ("default_message_ttl", details["defaultMessageTimeToLive"]),
        ("duplicate_detection_history_time_window", details["duplicateDetectionHistoryTimeWindow"]),
        ("enable_batched_operations", details["enableBatchedOperations"]),
        ("enable_express", details["enableExpress"]),
        ("enable_partitioning", details["enablePartitioning"]),
        ("max_size_in_megabytes", details["maxSizeInMegabytes"]),
        ("requires_duplicate_detection", details["requiresDuplicateDetection"]),
        ("support_ordering", details["supportOrdering"]),
    ])
