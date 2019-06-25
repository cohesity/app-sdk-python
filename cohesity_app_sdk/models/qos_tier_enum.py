# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

class QosTierEnum(object):

    """Implementation of the 'QosTier' enum.

    Specifies QoS Tier for an app instance. App instances are allocated
    resources such as memory, CPU and IO based on their QoS Tier.

    Attributes:
        KLOW: TODO: type description here.
        KMEDIUM: TODO: type description here.
        KHIGH: TODO: type description here.

    """

    KLOW = 'kLow'

    KMEDIUM = 'kMedium'

    KHIGH = 'kHigh'

