# -*- coding:utf-8 -*-
from . import module

import os.path
import inspect
from main import swagger

from flask import request, jsonify

from default_settings import logger,DB_CONFIG
from lib import util

# Imports for the apps supported.
# TODO: we should look for a way to load them differently.
#       This list can grow HUGEly as we target to add 1000+ apps.

from project_management.asana.app import AsanaApp
from project_management.teamwork.app import TeamworkApp
from project_management.podio.app import PodioApp
from project_management.wrike.app import WrikeApp
from project_management.trello.app import TrelloApp
from project_management.basecamp3.app import Basecamp3App
from project_management.mondaydotcom.app import MondaydotcomApp
from project_management.jira_software_cloud.app import JirasoftwarecloudApp
from project_management.clickup.app import ClickupApp
from project_management.projectsly.app import ProjectslyApp
from project_management.pivotal_tracker.app import PivotaltrackerApp
from project_management.redbooth.app import RedboothApp
from project_management.paymo.app import PaymoApp
from project_management.runrunit.app import RunrunitApp



from crm.redtailcrm.app import RedtailcrmApp
from crm.agilecrm.app import AgilecrmApp
from crm.onepagecrm.app import OnepagecrmApp
from crm.microsoftdynamics365crm.app import Microsoftdynamics365crmApp
from crm.hubspotcrm.app import HubspotcrmApp
from crm.pipedrive.app import PipedriveApp
from crm.copper_crm.app import CoppercrmApp
from crm.zoho_crm.app import ZohocrmApp
from crm.capsule_crm.app import CapsulecrmApp
from crm.zendesk_sell.app import ZendesksellApp
from crm.freshworks.app import FreshworksApp
from crm.salesforce.app import SalesforceApp
from crm.salesmate.app import SalesmateApp
from crm.insightly.app import InsightlyApp
from crm.pipelinedeals.app import PipelinedealsApp
from crm.nocrm_io.app import NocrmioApp
from crm.nimble.app import NimbleApp


from documents.google_docs.app import GoogledocsApp

from drip_emails.convertkit.app import ConvertkitApp

from email_newsletters.aweber.app import AweberApp
from email_newsletters.sendinblue.app import SendinblueApp
from email_newsletters.mailchimp.app import MailchimpApp
from email_newsletters.campaign_monitor.app import CampaignmonitorApp
from email_newsletters.mailerlite.app import MailerliteApp
from email_newsletters.mailjet.app import MailjetApp

from payment_processing.stripe.app import StripeApp
from payment_processing.square.app import SquareApp

from emails.microsoft_office_365_email.app import Microsoftoffice365emailApp
from emails.gmail.app import GmailApp

from marketing_automation.ontraport.app import OntraportApp
from marketing_automation.getresponse.app import GetresponseApp
from marketing_automation.active_campaign.app import ActivecampaignApp
from marketing_automation.keap_max_classic.app import KeapmaxclassicApp
from marketing_automation.hubspot.app import HubspotApp

from forms_surveys.typeform.app import TypeformApp
from forms_surveys.jotform.app import JotformApp
from forms_surveys.wufoo.app import WufooApp
from forms_surveys.surveymonkey.app import SurveymonkeyApp

from file_management_storage.dropbox.app import DropboxApp
from file_management_storage.google_drive.app import GoogledriveApp
from file_management_storage.onedrive.app import OnedriveApp

from spreadsheets.smartsheet.app import SmartsheetApp
from spreadsheets.google_sheets.app import GooglesheetsApp

from customer_support.zendesk.app import ZendeskApp
from customer_support.freshdesk.app import FreshdeskApp
from customer_support.jira_service_desk.app import JiraservicedeskApp
from customer_support.intercom.app import IntercomApp
from customer_support.livechat.app import LivechatApp
from customer_support.drift.app import DriftApp
from customer_support.help_scout.app import HelpscoutApp
from customer_support.zoho_desk.app import ZohodeskApp

from phone_sms.twilio.app import TwilioApp
from phone_sms.plivo.app import PlivoApp
from phone_sms.clicksend_sms.app import ClicksendsmsApp

from teamchat.chatwork.app import ChatworkApp
from teamchat.slack.app import SlackApp


from accounting_invoicing.zoho_books.app import ZohobooksApp
from accounting_invoicing.xero.app import XeroApp
from accounting_invoicing.freshbooks.app import FreshbooksApp
from accounting_invoicing.quickbooks_online.app import QuickbooksonlineApp
from accounting_invoicing.wave.app import WaveApp


from scheduling_bookings.schedule_once.app import ScheduleonceApp
from scheduling_bookings.google_calendar.app import GooglecalendarApp

from contacts_management.google_contacts.app import GooglecontactsApp
from contacts_management.microsoft_office_365_contacts.app import Microsoftoffice365contactsApp

from transactional_email.postmark.app import PostmarkApp


from infinity.todoist.app import TodoistApp

from task_management.toodledo.app import ToodledoApp

from server_monitoring.freshservice.app import FreshserviceApp

from social_media.instagram_for_business.app import InstagramforbusinessApp
from social_media.facebook_pages.app import FacebookpagesApp
from social_media.linkedin.app import LinkedinApp
from social_media.medium.app import MediumApp
from social_media.twitter.app import TwitterApp
from social_media.pinterest.app import PinterestApp

from email_marketing.mailsend.app import MailsendApp


from ecommerce.shopify.app import ShopifyApp
from ecommerce.shipstation.app import ShipstationApp

from time_tracking.harvest.app import HarvestApp
from time_tracking.clockify.app import ClockifyApp
from time_tracking.toggl.app import TogglApp

from notes.onenote.app import OnenoteApp

from task_management.microsoft_to_do.app import MicrosofttodoApp
from task_management.googletasks.app import GoogletasksApp
from task_management.ticktick.app import TicktickApp
from task_management.any_do.app import AnydoApp

from recruitment.bamboo_hr.app import BamboohrApp

from website_builders.webflow.app import WebflowApp


from video_conferencing.clickmeeting.app import ClickmeetingApp
from recruitment.zoho_recruit.app import ZohorecruitApp
from video_conferencing.livestorm.app import LivestormApp

from dev_tools.github.app import GithubApp

from lib.util import applet_token
from lib.auth import proj_auth
from lib.db import DB
import json
db_insta = DB(DB_CONFIG)

@module.route('/<app>/<activity>', methods=['POST', 'GET', 'PUT', 'DELETE'])
# @proj_auth.login_required
def do_app_action(app, activity, headers = None, payload = None):
    """
    Perform an activity (action, api, trigger, ), for an app
    """

    # TODO: if we can identify if an activity is an action, api or trigger,
    #       we can restrict user to use APPROPRIATE HTTP method
    # ALTERNATIVELY, I think, we can just pass on the http-method to the method called?

    activity = activity.replace("-", "_").lower()
    if app.lower() == 'monday.com':
        app = 'mondaydotcom'

    # we are calling this method for widgets. in request we dont get any headers
    # for widgets we dont get app related headers directly through request. we need to fetch it from db
    if headers is None:
        headers = {**request.headers}

    # calls to Application's sdk requires headers with _ (underscore).
    headers = {k.replace("-", "_").lower(): v for k, v in headers.items()}

    context = {
        'headers': headers
    }

    if request.method == 'GET':
        payload = {**request.args}

        # Add headers to payload. Payload is params for API calls.
        # This is required for compatibility with plugins, which sends
        # the params in headers.
        # NOT SURE, if the 'headers which are not required in params'
        #           will cause any problem. Worked fine with BaseCamp3
        payload.update(headers)
    else:
        # TODO: check with request.content_type that input payload is in application/json type
        # payload = request.get_json() or {**request.args}
        payload = request.get_json() or {**request.form} or {**request.data} or {**request.args}

    app_class = get_app_class(app)
    alias_json = get_entity_alias_json(activity, app_class)
    payload = util.unify_payload(payload, alias_json)


    # instantiate the class and get the method
    method = getattr(app_class(), activity.lower())
    try:
        resp = method(context, payload)

    except NotImplementedError as nie:
        resp = {'error': nie}  # status code?

    ## TODO: We used json.dumps in the methods of the application wrappers
    ##       as it jsonify was causing context issues when running test_suite.
    ##       A good alternative is to use jsonify here. But, changing here implies
    ##       removing json.dumps in all the applications merged.
    ##
    ## return jsonify(resp)
    return resp



def get_app_class(app_name):
    """
    Get the imported App class (from globals) and return it
    """
    # TODO add checks to verify app, or anything related
    # and throw exception, if needed
    # print(globals())

    # get imported module from global objects. strip special chars.
    code_app_name = ''.join(c for c in app_name if c.isalnum())
    app_class = globals()[f'{code_app_name.capitalize()}App']

    return app_class


def get_entity_alias_json(activity, app_class):
    """Get alias JSON using the path derived from the app_class inspection and name of json derived from activity"""
    # get path of the file in which the class is defined
    class_path = inspect.getfile(app_class)

    # get entity name - 'project' from 'create_project', 'new_project', 'project'
    entity_name = activity.split('_')[-1] + '_mapping.json'

    # derive entity path from class_path
    alias_json_path = os.path.join(class_path.rsplit('/', 2)[0], 'entities', entity_name)

    return util.get_json_from_file(alias_json_path)


@module.route("/swagger/generate", methods=["GET"])
@module.route("/swagger/generate/<swagger_category>", methods=["GET"])
def get_swagger(swagger_category=None):
    response = swagger.generate_swagger(swagger_category)
    return response

@module.route("/swagger/yaml")
@module.route("/swagger/yaml/<category>")
def swagger_get_yml(category=None):
    return swagger.swagger_doc(category)


@module.route("/unified2/<int:widget_id>/<widget_name>", methods=['GET', 'POST'])
@ applet_token.login_required
def get_widget_data(widget_id, widget_name):
    """
    Get data for given widget. Get associated app_name from
    widgets_v2.external_users and use it to get widget data via unified.

    widget_id: id of the user registerd for widgets
    widget_name: name of widget for which data has to be fetched

    return: JSON object with data from external app
    """

    project_id = applet_token.current_user()['project_id']
    if project_id is None:
        return {'error': 'Invalid Project ID.'}

    results_json = db_insta.get_select_user_where_condition(
        'widgets_v2', 'external_users', request.args.get('fields', None),
        f'project_id={project_id} AND id={widget_id}', applet_token)

    if not results_json:
        return {'error': 'No data found for given widget ID'}

    headers_json = json.loads(results_json[0]['auth_json'])
    # To Update Refresh Token for the apps which are providing refresh token every time
    headers_json['widget_id'] = str(widget_id)
    post_data = None
    if request.method == 'GET':
        payload = {**request.args}
        headers_json.update(payload)

    app_name = results_json[0]['app_name']
    response = do_app_action(app_name, widget_name.lower(), headers_json, post_data)

    return response
