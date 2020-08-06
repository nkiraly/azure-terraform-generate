from collections import OrderedDict as OD

command = "az servicebus topic authorization-rule show --ids %s"

def itemId(details, name):
    try:
        return details[name]["id"]
    except (TypeError, KeyError):
        return None

def build(details):
    return OD([
        # https://www.terraform.io/docs/providers/azurerm/r/servicebus_topic_authorization_rule.html
        # Required
        ("resource_group_name", details["resourceGroup"]),
        ("namespace_name", details["id"].rsplit("/", 5)[1]),
        ("topic_name", details["id"].rsplit("/", 5)[3]),
        ("name", details["name"]),
        # Optional; At least one must be set
        ("listen", ("Listen" in details["rights"])),
        ("manage", ("Manage" in details["rights"])),
        ("send", ("Send" in details["rights"])),
    ])
