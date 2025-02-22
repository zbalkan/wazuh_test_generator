#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# These test cases are based on log data and rule descriptions used for regression testing,
# potentially derived from or inspired by Wazuh rulesets and public log samples.

import unittest

from internal.logtest import LogtestStatus, send_log


# Converted from win_security.ini
class TestWinSecurityRules(unittest.TestCase):

    def test_user_account_enabled_or_created(self) -> None:
        log = r'''
{ "win": { "eventdata": { "subjectLogonId": "0x1f6f29", "targetUserName": "toby", "subjectUserSid": "S-1-5-21-3002370232-1004552484-2337450515-1103", "subjectDomainName": "XRISBARNEY", "targetDomainName": "APT29W1", "targetSid": "S-1-5-21-184966080-802066075-2268707989-1002", "subjectUserName": "itadmin" }, "system": { "eventID": "4722", "keywords": "0x8020000000000000", "providerGuid": "{54849625-5478-4994-a5ba-3e3b0328c30d}", "level": "0", "channel": "Security", "opcode": "0", "message": "\"A user account was enabled.\r\n\r\nSubject:\r\n\tSecurity ID:\t\tS-1-5-21-3002370232-1004552484-2337450515-1103\r\n\tAccount Name:\t\titadmin\r\n\tAccount Domain:\t\tXRISBARNEY\r\n\tLogon ID:\t\t0x1F6F29\r\n\r\nTarget Account:\r\n\tSecurity ID:\t\tS-1-5-21-184966080-802066075-2268707989-1002\r\n\tAccount Name:\t\ttoby\r\n\tAccount Domain:\t\tAPT29W1\"", "version": "0", "systemTime": "2021-11-08T18:09:47.4367951Z", "eventRecordID": "15217", "threadID": "2256", "computer": "apt29w1.xrisbarney.local", "task": "13824", "processID": "620", "severityValue": "AUDIT_SUCCESS", "providerName": "Microsoft-Windows-Security-Auditing" } } }
'''
        response = send_log(log)

        self.assertEqual(response.status, LogtestStatus.RuleMatch)

        self.assertEqual(response.decoder, 'json')
        self.assertEqual(response.rule_id, '60109')
        self.assertEqual(response.rule_level, 8)


    def test_user_account_changed(self) -> None:
        log = r'''
{ "win": { "eventdata": { "subjectLogonId": "0x1f6f29", "scriptPath": "%%1793", "passwordLastSet": "11/8/2021 10:09:47 AM", "homeDirectory": "%%1793", "subjectDomainName": "XRISBARNEY", "displayName": "%%1793", "accountExpires": "%%1794", "homePath": "%%1793", "samAccountName": "toby", "targetUserName": "toby", "subjectUserSid": "S-1-5-21-3002370232-1004552484-2337450515-1103", "primaryGroupId": "513", "logonHours": "%%1797", "targetDomainName": "APT29W1", "profilePath": "%%1793", "userWorkstations": "%%1793", "oldUacValue": "0x15", "newUacValue": "0x10", "targetSid": "S-1-5-21-184966080-802066075-2268707989-1002", "userAccountControl": "    %%2048    %%2050", "subjectUserName": "itadmin" }, "system": { "eventID": "4738", "keywords": "0x8020000000000000", "providerGuid": "{54849625-5478-4994-a5ba-3e3b0328c30d}", "level": "0", "channel": "Security", "opcode": "0", "message": "\"A user account was changed.\r\n\r\nSubject:\r\n\tSecurity ID:\t\tS-1-5-21-3002370232-1004552484-2337450515-1103\r\n\tAccount Name:\t\titadmin\r\n\tAccount Domain:\t\tXRISBARNEY\r\n\tLogon ID:\t\t0x1F6F29\r\n\r\nTarget Account:\r\n\tSecurity ID:\t\tS-1-5-21-184966080-802066075-2268707989-1002\r\n\tAccount Name:\t\ttoby\r\n\tAccount Domain:\t\tAPT29W1\r\n\r\nChanged Attributes:\r\n\tSAM Account Name:\ttoby\r\n\tDisplay Name:\t\t<value not set>\r\n\tUser Principal Name:\t-\r\n\tHome Directory:\t\t<value not set>\r\n\tHome Drive:\t\t<value not set>\r\n\tScript Path:\t\t<value not set>\r\n\tProfile Path:\t\t<value not set>\r\n\tUser Workstations:\t<value not set>\r\n\tPassword Last Set:\t11/8/2021 10:09:47 AM\r\n\tAccount Expires:\t\t<never>\r\n\tPrimary Group ID:\t513\r\n\tAllowedToDelegateTo:\t-\r\n\tOld UAC Value:\t\t0x15\r\n\tNew UAC Value:\t\t0x10\r\n\tUser Account Control:\t\r\n\t\tAccount Enabled\r\n\t\t'Password Not Required' - Disabled\r\n\tUser Parameters:\t-\r\n\tSID History:\t\t-\r\n\tLogon Hours:\t\tAll\r\n\r\nAdditional Information:\r\n\tPrivileges:\t\t-\"", "version": "0", "systemTime": "2021-11-08T18:09:47.4369635Z", "eventRecordID": "15218", "threadID": "2256", "computer": "apt29w1.xrisbarney.local", "task": "13824", "processID": "620", "severityValue": "AUDIT_SUCCESS", "providerName": "Microsoft-Windows-Security-Auditing" } } }
'''
        response = send_log(log)

        self.assertEqual(response.status, LogtestStatus.RuleMatch)

        self.assertEqual(response.decoder, 'json')
        self.assertEqual(response.rule_id, '60110')
        self.assertEqual(response.rule_level, 8)


    def test_windows_audit_policy_changed(self) -> None:
        log = r'''
{ "win": { "eventdata": { "subjectLogonId": "0x3e7", "subjectUserSid": "S-1-5-18", "subjectDomainName": "XRISBARNEY", "auditPolicyChanges": "Failure added", "subcategoryId": "%%14339", "auditPolicyChangesId": "%%8451", "category": "Account Logon", "subcategory": "Kerberos Authentication Service", "categoryId": "%%8280", "subjectUserName": "HOTELDC$", "subcategoryGuid": "{0cce9242-69ae-11d9-bed3-505054503030}" }, "system": { "eventID": "4719", "keywords": "0x8020000000000000", "providerGuid": "{54849625-5478-4994-a5ba-3e3b0328c30d}", "level": "0", "channel": "Security", "opcode": "0", "message": "\"System audit policy was changed.\r\n\r\nSubject:\r\n\tSecurity ID:\t\tS-1-5-18\r\n\tAccount Name:\t\tHOTELDC$\r\n\tAccount Domain:\t\tXRISBARNEY\r\n\tLogon ID:\t\t0x3E7\r\n\r\nAudit Policy Change:\r\n\tCategory:\t\tAccount Logon\r\n\tSubcategory:\t\tKerberos Authentication Service\r\n\tSubcategory GUID:\t{0cce9242-69ae-11d9-bed3-505054503030}\r\n\tChanges:\t\tFailure added\"", "version": "0", "systemTime": "2021-11-11T17:40:12.383182200Z", "eventRecordID": "144520", "threadID": "608", "computer": "hoteldc.xrisbarney.local", "task": "13568", "processID": "560", "severityValue": "AUDIT_SUCCESS", "providerName": "Microsoft-Windows-Security-Auditing" } } }
'''
        response = send_log(log)

        self.assertEqual(response.status, LogtestStatus.RuleMatch)

        self.assertEqual(response.decoder, 'json')
        self.assertEqual(response.rule_id, '60112')
        self.assertEqual(response.rule_level, 8)


    def test_domain_users_group_changed(self) -> None:
        log = r'''
{ "win": { "eventdata": { "subjectLogonId": "0x1f6f29", "targetUserName": "None", "memberSid": "S-1-5-21-184966080-802066075-2268707989-1002", "subjectUserSid": "S-1-5-21-3002370232-1004552484-2337450515-1103", "subjectDomainName": "XRISBARNEY", "targetDomainName": "APT29W1", "targetSid": "S-1-5-21-184966080-802066075-2268707989-513", "subjectUserName": "itadmin" }, "system": { "eventID": "4728", "keywords": "0x8020000000000000", "providerGuid": "{54849625-5478-4994-a5ba-3e3b0328c30d}", "level": "0", "channel": "Security", "opcode": "0", "message": "\"A member was added to a security-enabled global group.\r\n\r\nSubject:\r\n\tSecurity ID:\t\tS-1-5-21-3002370232-1004552484-2337450515-1103\r\n\tAccount Name:\t\titadmin\r\n\tAccount Domain:\t\tXRISBARNEY\r\n\tLogon ID:\t\t0x1F6F29\r\n\r\nMember:\r\n\tSecurity ID:\t\tS-1-5-21-184966080-802066075-2268707989-1002\r\n\tAccount Name:\t\t-\r\n\r\nGroup:\r\n\tSecurity ID:\t\tS-1-5-21-184966080-802066075-2268707989-513\r\n\tGroup Name:\t\tNone\r\n\tGroup Domain:\t\tAPT29W1\r\n\r\nAdditional Information:\r\n\tPrivileges:\t\t-\"", "version": "0", "systemTime": "2021-11-08T18:09:47.3872627Z", "eventRecordID": "15215", "threadID": "2256", "computer": "apt29w1.xrisbarney.local", "task": "13826", "processID": "620", "severityValue": "AUDIT_SUCCESS", "providerName": "Microsoft-Windows-Security-Auditing" } } }
'''
        response = send_log(log)

        self.assertEqual(response.status, LogtestStatus.RuleMatch)

        self.assertEqual(response.decoder, 'json')
        self.assertEqual(response.rule_id, '60160')
        self.assertEqual(response.rule_level, 5)


    def test_a_new_external_device_was_recognized_by_the_system(self) -> None:
        log = r'''
{ "win": { "eventdata": { "subjectLogonId": "0x3e7", "compatibleIds": "    USB\\\\Class_06&amp;SubClass_01&amp;Prot_01    USB\\\\Class_06&amp;SubClass_01    USB\\\\Class_06", "classId": "{eec5ad98-8080-425f-922a-dabf3de3f69a}", "subjectUserSid": "S-1-5-18", "deviceDescription": "Apple iPhone", "vendorIds": "    USB\\\\VID_05AC&amp;PID_12A8&amp;REV_1003&amp;MI_00    USB\\\\VID_05AC&amp;PID_12A8&amp;MI_00", "subjectDomainName": "WORKGROUP", "locationInformation": "    0000.0014.0000.001.000.000.000.000.000", "className": "WPD", "deviceId": "USB\\\\VID_05AC&amp;PID_12A8&amp;MI_00\\\\6&amp;161d18cc&amp;0&amp;0000", "subjectUserName": "CYBERWARRIOR$" }, "system": { "eventID": "6416", "keywords": "0x8020000000000000", "providerGuid": "{54849625-5478-4994-a5ba-3e3b0328c30d}", "level": "0", "channel": "Security", "opcode": "0", "message": "\"A new external device was recognized by the system.\r\n\r\nSubject:\r\n\tSecurity ID:\t\tS-1-5-18\r\n\tAccount Name:\t\tCYBERWARRIOR$\r\n\tAccount Domain:\t\tWORKGROUP\r\n\tLogon ID:\t\t0x3E7\r\n\r\nDevice ID:\tUSB\\VID_05AC&PID_12A8&MI_00\\6&161d18cc&0&0000\r\n\r\nDevice Name:\tApple iPhone\r\n\r\nClass ID:\t\t{eec5ad98-8080-425f-922a-dabf3de3f69a}\r\n\r\nClass Name:\tWPD\r\n\r\nVendor IDs:\t\r\n\t\tUSB\\VID_05AC&PID_12A8&REV_1003&MI_00\r\n\t\tUSB\\VID_05AC&PID_12A8&MI_00\r\n\t\t\r\n\t\t\r\n\r\nCompatible IDs:\t\r\n\t\tUSB\\Class_06&SubClass_01&Prot_01\r\n\t\tUSB\\Class_06&SubClass_01\r\n\t\tUSB\\Class_06\r\n\t\t\r\n\t\t\r\n\r\nLocation Information:\t\r\n\t\t0000.0014.0000.001.000.000.000.000.000\r\n\t\t\"", "version": "1", "systemTime": "2021-11-11T16:25:05.2558280Z", "eventRecordID": "27135", "threadID": "23840", "computer": "cyberwarrior", "task": "13316", "processID": "4", "severityValue": "AUDIT_SUCCESS", "providerName": "Microsoft-Windows-Security-Auditing" } } }
'''
        response = send_log(log)

        self.assertEqual(response.status, LogtestStatus.RuleMatch)

        self.assertEqual(response.decoder, 'json')
        self.assertEqual(response.rule_id, '60227')
        self.assertEqual(response.rule_level, 8)


    def test_a_scheduled_task_was_created(self) -> None:
        log = r'''
{ "win": { "eventdata": { "subjectLogonId": "0x6a874", "subjectUserSid": "S-1-5-21-3002370232-1004552484-2337450515-500", "taskContent": "&lt", "subjectDomainName": "XRISBARNEY", "taskName": "\\\\sdfg", "subjectUserName": "Administrator" }, "system": { "eventID": "4698", "keywords": "0x8020000000000000", "providerGuid": "{54849625-5478-4994-a5ba-3e3b0328c30d}", "level": "0", "channel": "Security", "opcode": "0", "message": "\"A scheduled task was created.", "version": "0", "systemTime": "2021-11-12T11:40:29.919882400Z", "eventRecordID": "144538", "threadID": "1892", "computer": "hoteldc.xrisbarney.local", "task": "12804", "processID": "560", "severityValue": "AUDIT_SUCCESS", "providerName": "Microsoft-Windows-Security-Auditing" } } }
'''
        response = send_log(log)

        self.assertEqual(response.status, LogtestStatus.RuleMatch)

        self.assertEqual(response.decoder, 'json')
        self.assertEqual(response.rule_id, '60228')
        self.assertEqual(response.rule_level, 4)


    def test_a_directory_service_object_was_modified(self) -> None:
        log = r'''
{ "win": { "eventdata": { "subjectLogonId": "0x6a874", "dSName": "xrisbarney.local", "attributeValue": "accounting accounting", "subjectDomainName": "XRISBARNEY", "objectClass": "user", "opCorrelationID": "{199ff79b-1b43-4bdc-a742-67c94ef4eaba}", "objectDN": "CN=accounting accounting2,CN=Users,DC=xrisbarney,DC=local", "attributeSyntaxOID": "2.5.5.12", "subjectUserSid": "S-1-5-21-3002370232-1004552484-2337450515-500", "dSType": "%%14676", "attributeLDAPDisplayName": "name", "objectGUID": "{3f7a4d00-7651-4e57-acc7-5ef76585351e}", "operationType": "%%14674", "subjectUserName": "Administrator" }, "system": { "eventID": "5136", "keywords": "0x8020000000000000", "providerGuid": "{54849625-5478-4994-a5ba-3e3b0328c30d}", "level": "0", "channel": "Security", "opcode": "0", "message": "\"A directory service object was modified.\r\n\t\r\nSubject:\r\n\tSecurity ID:\t\tS-1-5-21-3002370232-1004552484-2337450515-500\r\n\tAccount Name:\t\tAdministrator\r\n\tAccount Domain:\t\tXRISBARNEY\r\n\tLogon ID:\t\t0x6A874\r\n\r\nDirectory Service:\r\n\tName:\txrisbarney.local\r\n\tType:\tActive Directory Domain Services\r\n\t\r\nObject:\r\n\tDN:\tCN=accounting accounting2,CN=Users,DC=xrisbarney,DC=local\r\n\tGUID:\t{3f7a4d00-7651-4e57-acc7-5ef76585351e}\r\n\tClass:\tuser\r\n\t\r\nAttribute:\r\n\tLDAP Display Name:\tname\r\n\tSyntax (OID):\t2.5.5.12\r\n\tValue:\taccounting accounting\r\n\t\r\nOperation:\r\n\tType:\tValue Added\r\n\tCorrelation ID:\t{199ff79b-1b43-4bdc-a742-67c94ef4eaba}\r\n\tApplication Correlation ID:\t-\"", "version": "0", "systemTime": "2021-11-12T11:53:46.800716700Z", "eventRecordID": "144592", "threadID": "660", "computer": "hoteldc.xrisbarney.local", "task": "14081", "processID": "560", "severityValue": "AUDIT_SUCCESS", "providerName": "Microsoft-Windows-Security-Auditing" } } }
'''
        response = send_log(log)

        self.assertEqual(response.status, LogtestStatus.RuleMatch)

        self.assertEqual(response.decoder, 'json')
        self.assertEqual(response.rule_id, '60229')
        self.assertEqual(response.rule_level, 4)


    def test_a_directory_service_object_was_created(self) -> None:
        log = r'''
{ "win": { "eventdata": { "subjectLogonId": "0x6a874", "dSName": "xrisbarney.local", "subjectUserSid": "S-1-5-21-3002370232-1004552484-2337450515-500", "subjectDomainName": "XRISBARNEY", "dSType": "%%14676", "objectGUID": "{1a7bf7a4-3d57-4674-b1a1-3b0f5456e014}", "objectClass": "user", "opCorrelationID": "{fd9b26af-5d82-4cd3-a55a-5abb54d9f538}", "objectDN": "cn=test,CN=Users,DC=xrisbarney,DC=local", "subjectUserName": "Administrator" }, "system": { "eventID": "5137", "keywords": "0x8020000000000000", "providerGuid": "{54849625-5478-4994-a5ba-3e3b0328c30d}", "level": "0", "channel": "Security", "opcode": "0", "message": "\"A directory service object was created.\r\n\t\r\nSubject:\r\n\tSecurity ID:\t\tS-1-5-21-3002370232-1004552484-2337450515-500\r\n\tAccount Name:\t\tAdministrator\r\n\tAccount Domain:\t\tXRISBARNEY\r\n\tLogon ID:\t\t0x6A874\r\n\t\r\nDirectory Service:\r\n\tName:\txrisbarney.local\r\n\tType:\tActive Directory Domain Services\r\n\t\r\nObject:\r\n\tDN:\tcn=test,CN=Users,DC=xrisbarney,DC=local\r\n\tGUID:\t{1a7bf7a4-3d57-4674-b1a1-3b0f5456e014}\r\n\tClass:\tuser\r\n\t\r\nOperation:\r\n\tCorrelation ID:\t{fd9b26af-5d82-4cd3-a55a-5abb54d9f538}\r\n\tApplication Correlation ID:\t-\"", "version": "0", "systemTime": "2021-11-12T12:06:07.200487500Z", "eventRecordID": "144612", "threadID": "660", "computer": "hoteldc.xrisbarney.local", "task": "14081", "processID": "560", "severityValue": "AUDIT_SUCCESS", "providerName": "Microsoft-Windows-Security-Auditing" } } }
'''
        response = send_log(log)

        self.assertEqual(response.status, LogtestStatus.RuleMatch)

        self.assertEqual(response.decoder, 'json')
        self.assertEqual(response.rule_id, '60230')
        self.assertEqual(response.rule_level, 4)


    def test_a_directory_service_object_was_deleted(self) -> None:
        log = r'''
{ "win": { "eventdata": { "subjectLogonId": "0x6a874", "dSName": "xrisbarney.local", "treeDelete": "%%14679", "subjectUserSid": "S-1-5-21-3002370232-1004552484-2337450515-500", "subjectDomainName": "XRISBARNEY", "dSType": "%%14676", "objectGUID": "{3f7a4d00-7651-4e57-acc7-5ef76585351e}", "objectClass": "user", "opCorrelationID": "{c235ef0e-0d48-4381-b6a0-114c69fc3324}", "objectDN": "CN=accounting accounting,CN=Users,DC=xrisbarney,DC=local", "subjectUserName": "Administrator" }, "system": { "eventID": "5141", "keywords": "0x8020000000000000", "providerGuid": "{54849625-5478-4994-a5ba-3e3b0328c30d}", "level": "0", "channel": "Security", "opcode": "0", "message": "\"A directory service object was deleted.\r\n\t\r\nSubject:\r\n\tSecurity ID:\t\tS-1-5-21-3002370232-1004552484-2337450515-500\r\n\tAccount Name:\t\tAdministrator\r\n\tAccount Domain:\t\tXRISBARNEY\r\n\tLogon ID:\t\t0x6A874\r\n\t\r\nDirectory Service:\r\n\tName:\txrisbarney.local\r\n\tType:\tActive Directory Domain Services\r\n\t\r\nObject:\r\n\tDN:\tCN=accounting accounting,CN=Users,DC=xrisbarney,DC=local\r\n\tGUID:\t{3f7a4d00-7651-4e57-acc7-5ef76585351e}\r\n\tClass:\tuser\r\n\t\r\nOperation:\r\n\tTree Delete:\tNo\r\n\tCorrelation ID:\t{c235ef0e-0d48-4381-b6a0-114c69fc3324}\r\n\tApplication Correlation ID:\t-\"", "version": "0", "systemTime": "2021-11-12T12:03:37.060332200Z", "eventRecordID": "144611", "threadID": "660", "computer": "hoteldc.xrisbarney.local", "task": "14081", "processID": "560", "severityValue": "AUDIT_SUCCESS", "providerName": "Microsoft-Windows-Security-Auditing" } } }
'''
        response = send_log(log)

        self.assertEqual(response.status, LogtestStatus.RuleMatch)

        self.assertEqual(response.decoder, 'json')
        self.assertEqual(response.rule_id, '60231')
        self.assertEqual(response.rule_level, 4)

