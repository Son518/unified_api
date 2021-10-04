**Here are some details of this application structure**

# Directory Structure:

```
core/ - contains Base classes 
    app.py - Base class for the applications that are going to be implemented
    actions.py
    triggers.py
    api.py
    
modules/ - most of the application's code
    lib/
    health-check/ - provides a service for Unified2's status
    main/
        application.py - provides services to consume the Unified2's Actions, API, etc. which internally creates instance of the application's wrapper and call the method.
        categories/
            <category1>/  - directory for categories such project_management, crm, etc.
                entities/ - common entities for this category
                <app1>/ - directory for app sdk wrapper, such as Asana (YOU'LL ADD HERE)
                    entities/ - entities specific to this app
                    app.py    - This is the main script for this app. This is derived from Base class App in core directory and the Actions, Triggers, API here.
                    actions.py - class containing methods for actions 
                    triggers.py - class containing methods for triggers
                    api.py - class containing methods for API 

                <app2>/
                <app3>/
                ...
            <category2>/
            <category3>/
            ...

test/ - testsuite and test payload data in .json files
    test_suite.py
    <category1> - directory for each of the catgories such project_management, crm, etc.
        <app1>/ - directory with application name 
            actions/
                <action1>/
                    1.json - test payload 1 for action1
                    2.json - test payload 2 for action1
                    ...
                <action2>/
                <action3>/
                ...
            triggers/
                <trigger1>/
                    1.json - test payload 1 for trigger1
                    2.json - test payload 2 for trigger1
                    ...
                <trigger2>/
                <trigger3>/
                ...
            api/  (to be added)
        <app2>/
        <app3>/
        ...
    <category2>
    <category3>
    ...
}
```
**When you add a new application (wrapper):** 
- Add app.py, actions.py, triggers.py and api.py to `categories/<category>/<app>/` directory, including app-specific entities to `entities/` directory. And test the code

- Payload data will be provided as .json files in `test/<category>/<app>` - actions, triggers, and api directories, as discribed.

- Headers for authentication will be provided as .json in `test/<category>/<app>/headers.json`

- Test functionality using the test_suite.py using the command line. 
	`python unified/test/test_suite.py -c <category> -a <app>`

