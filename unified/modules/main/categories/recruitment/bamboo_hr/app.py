# BambooHrApp - extends App, BambooHrTriggers, BambooHrActions, BambooHrAPI, ..

# from . import module

import json

from recruitment.bamboo_hr.actions import BambooHrActions
from recruitment.bamboo_hr.api import BambooHrApi
from recruitment.bamboo_hr.triggers import BambooHrTriggers

from unified.core.app import App, AuthInfo


class BamboohrApp(App, BambooHrActions, BambooHrApi, BambooHrTriggers):

    def __init__(self):
        super().__init__(
        name = "BambooHr",
        description = "BambooHr brings a modern approach to hiring, with applicant tracking tools that improve every stage of hiring from applications to offer letters.",
        category = "Recruitment",
        logo = "https://logo.500apps.com/bamboo_hr",
        auth_type = "basic",
        auth_info = None
)
