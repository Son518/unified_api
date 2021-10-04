# Test script to test the applications using the payloads provided in .json files
# For actions and triggers, these .json files contain payloads. And, for APIs, 
# these are considered params (args).
# headers.json files are used for authorization headers

import json
import os
from argparse import ArgumentParser
import logging
import importlib.util 
import pprint
import traceback

# LOAD DEFAULT SETTINGS? TODO: some values/constants may be required, going forward

import sys

unified_path = os.path.dirname(os.path.abspath(__file__))
unified_path = unified_path.replace('\\', '/')  # otherwise, causing problem in Windows
unified_path = unified_path[:unified_path.rfind('/unified')]

sys.path.append(unified_path)
sys.path.append(unified_path + '/unified')
sys.path.append(unified_path + '/unified/modules')
sys.path.append(unified_path + '/unified/modules/main/categories')
# sys.path.append(unified_path + '/unified/modules/main/categories/project_management')

# logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
LOGGER_FORMAT = '%(asctime)s %(message)s'
logging.basicConfig(format=LOGGER_FORMAT)

# TODO: Use cache?
def get_json_from_file(path):
    """Get json object from .json file
    """

    try:
        with open(path) as f:
            return json.load(f)

    except Exception as err:
        # logger.error(err)
        logger.info(f'FILE NOT FOUND - {path}')


def get_entity_alias_json(app_cat_path, activity):
    """Get alias JSON using the path... """
    
    # get entity name - 'project' from 'create_project', 'new_project', 'project'
    mapping_filename = activity.split('_')[-1] + '_mapping.json'

    # derive entity path from class_path
    alias_json_path = os.path.join(app_cat_path, 'entities', mapping_filename)

    return get_json_from_file(alias_json_path)


## THERE ARE TWO variations mapping structure
## THIS MUST BE same version as that of application.py
def unify_payload(input_payload, payload_mapping):
    if not payload_mapping:
        return input_payload

    unified_payload = {}

    for key in input_payload:
        if key in payload_mapping:
            unified_payload[payload_mapping[key]] = input_payload[key]
        else: # copy as-is
            unified_payload[key] = input_payload[key]

    return unified_payload

def get_entity_class(app_cat_path, activity):
    # get entity name - 'project' from 'create_project', 'new_project', 'project'
    entity_name = activity.split('_')[-1]

    try:
        # derive entity path from class_path
        entity_path = os.path.join(app_cat_path, 'entities', entity_name)

        # for the purpose of import, we don't need full path. just as we do in from..import statement
        entity_path = entity_path[entity_path.rfind('categories/') + len('categories/'):]

        # entity module
        entity_mod = importlib.import_module(entity_path.replace('/', '.'))

    except ModuleNotFoundError as err:
        # LOAD <app_name>_<entity> ==> asana_<entity> / stripe_<entity> / ... class
        # print('*(&*(&*()&*()&*()&*()&*()&*() app_class', entity_mod)

        # # derive entity path from class_path
        # entity_path = os.path.join(class_path.rsplit('/', 1)[0], 'entities', 'asana_' + entity_name)

        # # for the purpose of import, we don't need full path. just as we do in from..import statement
        # entity_path = entity_path[entity_path.rfind('categories/') + len('categories/'):]

        # # entity module
        # entity_mod = importlib.import_module(entity_path.replace('/', '.'))
        pass

    # entity class
    return getattr(entity_mod, entity_name.capitalize())

def get_initcap_name(name):
    ''.join([e.capitalize() for e in name.split('_')])

    
def get_testdata_path(category=None):
    """Get test data path, based on location of this script. Change required if this script is moved.
    """
    # path.replace('tests/categories', 'test_data')
    path = os.path.dirname(os.path.abspath(__file__)).replace('/tests', '/test')
    if category:
        path = f"{path}/{category}"

    return path

def show_formatted_result(result):
    for category in result.keys():
        logger.info('----------------------------------------------------------')
        logger.info(f'Category: {category}')
        logger.info('----------------------------------------------------------')
        pp = pprint.PrettyPrinter(indent=2, width=120, stream=sys.stderr)
        pp.pprint(result[category])
        logger.info('----------------------------------------------------------\n')


def save_result(result):
    # import time
    # time.time() returns time including mills in fraction, so int()
    # filename = f"{unified_path}/{int(time.time())}.json"
    if args.filejson:
        filename = f"{args.app[0]}_testsuite_result.json"
    else:
        filename = "test_suite_result.json"

    try:
        with open(filename, "w") as json_file:
            json_file.write(json.dumps(result))

    except Exception as err:
        logger.error(err)


# Main method called
def test_all(categories=None, apps=None, atypes=None):
    """Test all apps in given categories. If not categories are given, include all categories.

    Args:
        categories (list): List of categories to be tested
        app ([type], optional): List of apps. Defaults to None.
    """
    full_result = {}

    if not categories:
        try:
            category_path = get_testdata_path()
            categories = os.listdir(category_path)
            categories = sorted([e for e in categories if os.path.isdir(f"{category_path}/{e}")])
        except FileNotFoundError as err:
            # category folder not found
            logger.error(err)
            return None

    elif type(categories) is str:
        categories = [categories]

    for category in categories:
        logger.info(f"Testing category - {category}")

        # gather/capture result for this category
        full_result[category] = test_category(category, apps, atypes)

    show_formatted_result(full_result)
    save_result(full_result)

def test_triggers(category, app):
    return test_category(category, app, ['triggers'])


def test_actions(category, app):
    return test_category(category, app, ['actions'])
    
def test_api(category, app):
    return test_category(category, app, ['api'])

def test_app(category, app):
    result_triggers = {
        category: test_triggers(category, app)
    }

    result_actions = {
        category: test_actions(category, app)
    }
     
    result_api = {
        category: test_api(category, app)
    }

    show_formatted_result(result_triggers)
    show_formatted_result(result_actions)
    show_formatted_result(result_api)

def is_fail_payload(payload_path):
    filename = payload_path.rsplit('/', 1)[-1]

    return 'fail_' in filename or '_fail' in filename

def api_payload_check(action_entry, app_wrapper, pid, payload, headers):

    api_entry = action_entry.split('_')[-1]
    logger.debug(f"api_entry {api_entry}")

    # App class has methods for actions, apis, triggers,
    # get API method
    api_method = getattr(app_wrapper, api_entry.lower())
    # id of the entity to be fetched via API
    # *** every app's every action is supposed to ensure 'id' exists in response ***
    api_params = {'id': pid}
    api_data = api_method({'headers': headers}, api_params)

    # verify match
    verified = {k: payload[k] for k in payload if k in api_data and payload[k] == api_data[k]}
    # verified = dict(set(payload.items()) & set(api_data.items()))
    logger.info(f"\n*** Following items are verified exactly:\n {verified}")

    remaining_keys = set(payload) & set(api_data) - set(verified)
    verified2 = {k: payload[k] for k in payload if k in remaining_keys}
    logger.info(f"\n*** Values of following items didn't match:\n {verified2}") 


# result = test_app(category, app)
# return     

def test_category(category, apps=[], atypes=None): # also consider the folders named 'apis' in payloads
    result = {
        'total': {
            'success': 0,
            'failure': 0,
            'notimpl': 0,
        },
    }
    category_path = get_testdata_path(category)  # give test data path for the category

    if not apps:
        try:
            apps = sorted(os.listdir(category_path))
        except FileNotFoundError as err:
            # category folder not found
            logger.error(err)
            return None

    elif type(apps) is str:
        apps = [apps]

    # TODO Shall we change the folder name basecamp_3 to basecamp3 ??
    for app_name in apps:
        # test result for this  app
        result[app_name] = {
            'total': {
                'success': 0,
                'failure': 0,
                'notimpl': 0,
            },
        }

        # DYNAMIC
        code_app_name = ''.join(c for c in app_name if c.isalnum())
        app_class = f'{code_app_name.capitalize()}App'
        # TODO: Remove hardcoded values in path? By means of a CONSTANT?
        app_cat_path = f"{unified_path}/unified/modules/main/categories/{category}"
        app_path = os.path.join(app_cat_path, app_name, 'app.py')
        if not os.path.exists(app_path):
            logger.error(f"ERROR: Application is not found - {app_path}")
            result[app_name]['status'] = 'APPLICATION NOT FOUND'
            continue

        spec = importlib.util.spec_from_file_location(app_class, app_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Get class and create instance 
        app_wrapper = getattr(module, app_class)()  

        # get headers for current app, from test data
        headers = get_json_from_file(f"{category_path}/{app_name}/headers.json")
        logger.debug(f"headers {headers}")

        # for each activity (action, trigger, api,...) type
        if atypes is None:
            atypes=['actions', 'triggers', 'api', 'apis']
            
        for atype in atypes:
            result[app_name][atype] = {
                'total': {
                    'success': 0,
                    'failure': 0,
                    'notimpl': 0,
                },
            }


            logger.debug(f"activity type - {atype}")
            a_path = f"{category_path}/{app_name}/{atype}"

            try:
                a_entries = sorted(os.listdir(a_path))  # sorting improves readabilty of output (logs)
            except FileNotFoundError as err:
                logger.error(err)
                continue
            
            # TEST/DEBUG ONLY a_entries = ['create_project']
            for a_entry in a_entries:
                if args.method and a_entry.lower() not in args.method:
                    continue

                result[app_name][atype][a_entry] = {
                    'success': [],
                    'failure': [],
                }

                logger.debug(f"activity - {a_entry}")
                payload_path = f"{a_path}/{a_entry}"

                try:
                    payload_files = sorted(os.listdir(payload_path))
                except FileNotFoundError as err:
                    logger.error(err)
                    continue

                for payload_file in payload_files:
                    logger.info(f"payload_file - {payload_path}/{payload_file}")
                    payload = get_json_from_file(f"{payload_path}/{payload_file}")

                    try:
                        alias_json = get_entity_alias_json(app_cat_path, a_entry)
                        payload = unify_payload(payload, alias_json)

                        if args.payload:
                            entity_class = get_entity_class(app_cat_path, a_entry)
                            logger.info(f'entity_class: {entity_class}')
                            entity = entity_class(**payload)
                            logger.info(f'entity: {entity}')

                            result[app_name][atype][a_entry]['success'].append(payload_file)
                            result[app_name][atype]['total']['success'] += 1

                        else:
                            logger.info(f"activity: {a_entry}")

                            # action/trigger/api method in the wrapper
                            app_method = getattr(app_wrapper, a_entry.lower())
                            # ALSO CAPTURE STATUS CODE 200?
                            method_resp = app_method({'headers': headers}, payload) # in case of 'api' payload is params

                            logger.info(f"method_resp: {method_resp}")
                            # if an error occurs, control goes to except
                            result[app_name][atype][a_entry]['success'].append(payload_file)
                            result[app_name][atype]['total']['success'] += 1

                            # if json string is returned
                            if type(method_resp) is str:
                                method_resp = json.loads(method_resp)

                            try:
                                # if atype is 'actions', make api call and verify 
                                # for 'deep' testing/verification
                                if atype == 'actions' and method_resp and ('id' in method_resp):
                                    api_payload_check(a_entry, app_wrapper, method_resp['id'], payload, headers)

                            except Exception as err:
                                logger.info(f"ERROR: {err}")
                                # show trace on -verbose
                                if args.verbose:
                                    traceback.print_exc()

                    except NotImplementedError as nierr:
                        result[app_name][atype]['total']['notimpl'] += 1
                        result[app_name][atype][a_entry] = 'NOT-IMPLEMENTED'
                        logger.info(f"ERROR: {nierr}")
                        # show trace on -verbose?
                        if args.verbose:
                            traceback.print_exc()

                    except Exception as err:
                        # if the payload is meant for "failure", count as 'success'
                        if is_fail_payload(payload_file):
                            result[app_name][atype][a_entry]['success'].append(payload_file)
                            result[app_name][atype]['total']['success'] += 1
                        else:
                            result[app_name][atype][a_entry]['failure'].append(payload_file)
                            result[app_name][atype]['total']['failure'] += 1

                        logger.info(f"ERROR: {err}")
                        # show trace on -verbose?
                        if args.verbose:
                            traceback.print_exc()

                    logger.info('------------------------------------\n')

            result[app_name]['total']['success'] += result[app_name][atype]['total']['success']
            result[app_name]['total']['failure'] += result[app_name][atype]['total']['failure']
            result[app_name]['total']['notimpl'] += result[app_name][atype]['total']['notimpl']

        # overall totals
        result['total']['success'] += result[app_name]['total']['success']
        result['total']['failure'] += result[app_name]['total']['failure']
        result['total']['notimpl'] += result[app_name]['total']['notimpl']

    return result
 
if __name__ == '__main__':
    # unified.test - category pm -app asana will test Asana 
    # or test all apps in the pm category if omitted.    

    # -category <categoryname>
    # -app <appname>

    parser = ArgumentParser()
    parser.add_argument("-c", "--category", action="extend", nargs="+",
                        help="Execute tests for the apps in category", metavar="category")

    parser.add_argument("-a", "--app", action="extend", nargs="+",
                        help="Execute tests for given app, all apps tested if omitted", metavar="app")

    parser.add_argument("-t", "--type", action="extend", nargs="+",
                        help="Limit test to given types of activity, out of 'actions', 'triggers', and 'api'/'apis'", metavar="type")

    parser.add_argument("-m", "--method", action="extend", nargs="+",
                        help="Only test given methods", metavar="method")

    parser.add_argument("-p", "--payload", help="Test only payloads against the 'common' entity classes",
                        action="store_true")

    parser.add_argument("-f", "--filejson", help="Use appname in json file, such as <appname>_testsuite_result.json",
                        action="store_true")

    parser.add_argument("-v", "--verbose", help="Increase output verbosity",
                        action="store_true")


    args = parser.parse_args()
    logger.debug(f"""
        category: {args.category}
        app: {args.app}
        type: {args.type}
        type: {args.payload}
        method: {args.method}
        filejson: {args.filejson}
        verbose: {args.verbose}""")
    
    test_all(args.category, args.app, args.type)
