from facmac.controllers.basic_controller import BasicMAC
from facmac.controllers.cqmix_controller import CQMixMAC

REGISTRY = {}
REGISTRY["basic_mac"] = BasicMAC
REGISTRY["cqmix_mac"] = CQMixMAC
