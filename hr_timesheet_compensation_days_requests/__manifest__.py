{
    "name": "hr_timesheet_compensation_days_requests",
    "summary": """ Request compensation days based on timesheet """,
    "license": "AGPL-3",
    "author": "Elabore",
    "website": "https://elabore.coop",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Leaves",
    "version": "12.0.1.2.1",
    # any module necessary for this one to work correctly
    "depends": [
        "base",
        "hr",
        "hr_timesheet",
        "hr_holidays",
    ],
    # always loaded
    "data": [
        "wizard/timesheet_compensation_days_request_view.xml",
        "views/hr_timesheet_views.xml",
    ],
    # only loaded in demonstration mode
    "demo": [],
    "installable": True,
    # Install this module automatically if all dependency have been previously
    # and independently installed.  Used for synergetic or glue modules.
    "auto_install": False,
    "application": False,
}
