#!/usr/bin/env python3
#
#
#  IRIS veloquarantineremove Source Code
#  Copyright (C) 2023 - SOCFortress
#  info@socfortress.co
#  Created by SOCFortress - 2023-01-30
#
#  License MIT

module_name = "IrisVeloquarantineremove"
module_description = ""
interface_version = 1.1
module_version = 1.0

pipeline_support = False
pipeline_info = {}


module_configuration = [
    {
        "param_name": "veloquarantineremove_url",
        "param_human_name": "veloquarantineremove URL",
        "param_description": "",
        "default": None,
        "mandatory": True,
        "type": "string"
    },
    {
        "param_name": "veloquarantineremove_key",
        "param_human_name": "veloquarantineremove key",
        "param_description": "veloquarantineremove API key",
        "default": None,
        "mandatory": True,
        "type": "sensitive_string"
    },
    
    {
        "param_name": "veloquarantineremove_manual_hook_enabled",
        "param_human_name": "Manual triggers on IOCs",
        "param_description": "Set to True to offers possibility to manually triggers the module via the UI",
        "default": True,
        "mandatory": True,
        "type": "bool",
        "section": "Triggers"
    },
    {
        "param_name": "veloquarantineremove_on_create_hook_enabled",
        "param_human_name": "Triggers automatically on IOC create",
        "param_description": "Set to True to automatically add a veloquarantineremove insight each time an IOC is created",
        "default": False,
        "mandatory": True,
        "type": "bool",
        "section": "Triggers"
    },
    {
        "param_name": "veloquarantineremove_on_update_hook_enabled",
        "param_human_name": "Triggers automatically on IOC update",
        "param_description": "Set to True to automatically add a veloquarantineremove insight each time an IOC is updated",
        "default": False,
        "mandatory": True,
        "type": "bool",
        "section": "Triggers"
    },
    {
        "param_name": "veloquarantineremove_report_as_attribute",
        "param_human_name": "Add veloquarantineremove report as new IOC attribute",
        "param_description": "Creates a new attribute on the IOC, base on the veloquarantineremove report. Attributes are based "
                             "on the templates of this configuration",
        "default": True,
        "mandatory": True,
        "type": "bool",
        "section": "Insights"
    },# TODO: careful here, remove backslashes from \{\{ results| tojson(indent=4) \}\}
    {
        "param_name": "veloquarantineremove_domain_report_template",
        "param_human_name": "Domain report template",
        "param_description": "Domain report template used to add a new custom attribute to the target IOC",
        "default": "<div class=\"row\">\n    <div class=\"col-12\">\n        <div "
                   "class=\"accordion\">\n            <h3>veloquarantineremove raw results</h3>\n\n           "
                   " <div class=\"card\">\n                <div class=\"card-header "
                   "collapsed\" id=\"drop_r_veloquarantineremove\" data-toggle=\"collapse\" "
                   "data-target=\"#drop_raw_veloquarantineremove\" aria-expanded=\"false\" "
                   "aria-controls=\"drop_raw_veloquarantineremove\" role=\"button\">\n                    <div "
                   "class=\"span-icon\">\n                        <div "
                   "class=\"flaticon-file\"></div>\n                    </div>\n              "
                   "      <div class=\"span-title\">\n                        veloquarantineremove raw "
                   "results\n                    </div>\n                    <div "
                   "class=\"span-mode\"></div>\n                </div>\n                <div "
                   "id=\"drop_raw_veloquarantineremove\" class=\"collapse\" aria-labelledby=\"drop_r_veloquarantineremove\" "
                   "style=\"\">\n                    <div class=\"card-body\">\n              "
                   "          <div id='veloquarantineremove_raw_ace'>\{\{ results| tojson(indent=4) \}\}</div>\n  "
                   "                  </div>\n                </div>\n            </div>\n    "
                   "    </div>\n    </div>\n</div> \n<script>\nvar veloquarantineremove_in_raw = ace.edit("
                   "\"veloquarantineremove_raw_ace\",\n{\n    autoScrollEditorIntoView: true,\n    minLines: "
                   "30,\n});\nveloquarantineremove_in_raw.setReadOnly(true);\nveloquarantineremove_in_raw.setTheme("
                   "\"ace/theme/tomorrow\");\nveloquarantineremove_in_raw.session.setMode("
                   "\"ace/mode/json\");\nveloquarantineremove_in_raw.renderer.setShowGutter("
                   "true);\nveloquarantineremove_in_raw.setOption(\"showLineNumbers\", "
                   "true);\nveloquarantineremove_in_raw.setOption(\"showPrintMargin\", "
                   "false);\nveloquarantineremove_in_raw.setOption(\"displayIndentGuides\", "
                   "true);\nveloquarantineremove_in_raw.setOption(\"maxLines\", "
                   "\"Infinity\");\nveloquarantineremove_in_raw.session.setUseWrapMode("
                   "true);\nveloquarantineremove_in_raw.setOption(\"indentedSoftWrap\", "
                   "true);\nveloquarantineremove_in_raw.renderer.setScrollMargin(8, 5);\n</script> ",
        "mandatory": False,
        "type": "textfield_html",
        "section": "Templates"
    }
    
]