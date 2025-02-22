#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# These test cases are based on log data and rule descriptions used for regression testing,
# potentially derived from or inspired by Wazuh rulesets and public log samples.

import unittest

from internal.logtest import LogtestStatus, send_log


# Converted from sysmon_eid_10.ini
class TestSysmonEid10Rules(unittest.TestCase):

    def test_credential_dump(self) -> None:
        log = r'''
{"win":{"eventdata":{"sourceThreadId":"6716","grantedAccess":"0x1010","targetProcessGUID":"{4dc16835-31bc-6141-0b00-000000006500}","targetProcessId":"596","utcTime":"2021-09-14 20:25:15.480","ruleName":"technique_id=T1003,technique_name=Credential Dumping","sourceProcessId":"6004","sourceImage":"C:\\\\Users\\\\AtomicRed\\\\AppData\\\\Roaming\\\\TransbaseOdbcDriver\\\\smrs.exe","targetImage":"C:\\\\Windows\\\\system32\\\\lsass.exe","sourceProcessGUID":"{4dc16835-052b-6141-bc2f-ea0000000000}","callTrace":"C:\\\\Windows\\\\SYSTEM32\\\\ntdll.dll+9d2e4|C:\\\\Windows\\\\System32\\\\KERNELBASE.dll+2c03e|C:\\\\Users\\\\AtomicRed\\\\AppData\\\\Roaming\\\\TransbaseOdbcDriver\\\\smrs.exe+b11df|C:\\\\Users\\\\AtomicRed\\\\AppData\\\\Roaming\\\\TransbaseOdbcDriver\\\\smrs.exe+b156a|C:\\\\Users\\\\AtomicRed\\\\AppData\\\\Roaming\\\\TransbaseOdbcDriver\\\\smrs.exe+b1135|C:\\\\Users\\\\AtomicRed\\\\AppData\\\\Roaming\\\\TransbaseOdbcDriver\\\\smrs.exe+819e3|C:\\\\Users\\\\AtomicRed\\\\AppData\\\\Roaming\\\\TransbaseOdbcDriver\\\\smrs.exe+81826|C:\\\\Users\\\\AtomicRed\\\\AppData\\\\Roaming\\\\TransbaseOdbcDriver\\\\smrs.exe+815b7|C:\\\\Users\\\\AtomicRed\\\\AppData\\\\Roaming\\\\TransbaseOdbcDriver\\\\smrs.exe+b5444|C:\\\\Windows\\\\System32\\\\KERNEL32.DLL+17034|C:\\\\Windows\\\\SYSTEM32\\\\ntdll.dll+52651"},"system":{"eventID":"10","keywords":"0x8000000000000000","providerGuid":"{5770385f-c22a-43e0-bf4c-06f5698ffbd9}","level":"4","channel":"Microsoft-Windows-Sysmon/Operational","opcode":"0","message":"\"Process accessed:\r\nRuleName: technique_id=T1003,technique_name=Credential Dumping\r\nUtcTime: 2021-09-14 20:25:15.480\r\nSourceProcessGUID: {4dc16835-052b-6141-bc2f-ea0000000000}\r\nSourceProcessId: 6004\r\nSourceThreadId: 6716\r\nSourceImage: C:\\Users\\AtomicRed\\AppData\\Roaming\\TransbaseOdbcDriver\\smrs.exe\r\nTargetProcessGUID: {4dc16835-31bc-6141-0b00-000000006500}\r\nTargetProcessId: 596\r\nTargetImage: C:\\Windows\\system32\\lsass.exe\r\nGrantedAccess: 0x1010\r\nCallTrace: C:\\Windows\\SYSTEM32\\ntdll.dll+9d2e4|C:\\Windows\\System32\\KERNELBASE.dll+2c03e|C:\\Users\\AtomicRed\\AppData\\Roaming\\TransbaseOdbcDriver\\smrs.exe+b11df|C:\\Users\\AtomicRed\\AppData\\Roaming\\TransbaseOdbcDriver\\smrs.exe+b156a|C:\\Users\\AtomicRed\\AppData\\Roaming\\TransbaseOdbcDriver\\smrs.exe+b1135|C:\\Users\\AtomicRed\\AppData\\Roaming\\TransbaseOdbcDriver\\smrs.exe+819e3|C:\\Users\\AtomicRed\\AppData\\Roaming\\TransbaseOdbcDriver\\smrs.exe+81826|C:\\Users\\AtomicRed\\AppData\\Roaming\\TransbaseOdbcDriver\\smrs.exe+815b7|C:\\Users\\AtomicRed\\AppData\\Roaming\\TransbaseOdbcDriver\\smrs.exe+b5444|C:\\Windows\\System32\\KERNEL32.DLL+17034|C:\\Windows\\SYSTEM32\\ntdll.dll+52651\"","version":"3","systemTime":"2021-09-14T20:25:15.4831107Z","eventRecordID":"360656","threadID":"3756","computer":"hrmanager.ExchangeTest.com","task":"10","processID":"2664","severityValue":"INFORMATION","providerName":"Microsoft-Windows-Sysmon"}}}
'''
        response = send_log(log)

        self.assertEqual(response.status, LogtestStatus.RuleMatch)

        self.assertEqual(response.decoder, 'json')
        self.assertEqual(response.rule_id, '92900')
        self.assertEqual(response.rule_level, 12)


    def test_credential_dump_2(self) -> None:
        log = r'''
{"win":{"eventdata":{"sourceThreadId":"7540","grantedAccess":"0x40","targetProcessGUID":"{4dc16835-5620-6157-0c00-000000006d00}","targetProcessId":"688","utcTime":"2021-10-01 15:10:29.169","ruleName":"technique_id=T1036,technique_name=Masquerading","sourceProcessId":"2980","sourceImage":"C:\\\\Users\\\\AtomicRed\\\\AppData\\\\Local\\\\samcat.exe","targetImage":"C:\\\\Windows\\\\system32\\\\lsass.exe","sourceProcessGUID":"{4dc16835-24e4-6157-0c6b-3a0000000000}","callTrace":"C:\\\\Windows\\\\SYSTEM32\\\\ntdll.dll+9d234|C:\\\\Windows\\\\System32\\\\KERNELBASE.dll+2c0fe|C:\\\\Users\\\\AtomicRed\\\\AppData\\\\Local\\\\samcat.exe+8a65|C:\\\\Users\\\\AtomicRed\\\\AppData\\\\Local\\\\samcat.exe+8a12|C:\\\\Users\\\\AtomicRed\\\\AppData\\\\Local\\\\samcat.exe+11e45|C:\\\\Users\\\\AtomicRed\\\\AppData\\\\Local\\\\samcat.exe+a64df|C:\\\\Users\\\\AtomicRed\\\\AppData\\\\Local\\\\samcat.exe+a61d0|C:\\\\Users\\\\AtomicRed\\\\AppData\\\\Local\\\\samcat.exe+8103e|C:\\\\Users\\\\AtomicRed\\\\AppData\\\\Local\\\\samcat.exe+80ffa|C:\\\\Users\\\\AtomicRed\\\\AppData\\\\Local\\\\samcat.exe+b4d70|C:\\\\Windows\\\\System32\\\\KERNEL32.DLL+17034|C:\\\\Windows\\\\SYSTEM32\\\\ntdll.dll+52651"},"system":{"eventID":"10","keywords":"0x8000000000000000","providerGuid":"{5770385f-c22a-43e0-bf4c-06f5698ffbd9}","level":"4","channel":"Microsoft-Windows-Sysmon/Operational","opcode":"0","message":"\"Process accessed:\r\nRuleName: technique_id=T1036,technique_name=Masquerading\r\nUtcTime: 2021-10-01 15:10:29.169\r\nSourceProcessGUID: {4dc16835-24e4-6157-0c6b-3a0000000000}\r\nSourceProcessId: 2980\r\nSourceThreadId: 7540\r\nSourceImage: C:\\Users\\AtomicRed\\AppData\\Local\\samcat.exe\r\nTargetProcessGUID: {4dc16835-5620-6157-0c00-000000006d00}\r\nTargetProcessId: 688\r\nTargetImage: C:\\Windows\\system32\\lsass.exe\r\nGrantedAccess: 0x40\r\nCallTrace: C:\\Windows\\SYSTEM32\\ntdll.dll+9d234|C:\\Windows\\System32\\KERNELBASE.dll+2c0fe|C:\\Users\\AtomicRed\\AppData\\Local\\samcat.exe+8a65|C:\\Users\\AtomicRed\\AppData\\Local\\samcat.exe+8a12|C:\\Users\\AtomicRed\\AppData\\Local\\samcat.exe+11e45|C:\\Users\\AtomicRed\\AppData\\Local\\samcat.exe+a64df|C:\\Users\\AtomicRed\\AppData\\Local\\samcat.exe+a61d0|C:\\Users\\AtomicRed\\AppData\\Local\\samcat.exe+8103e|C:\\Users\\AtomicRed\\AppData\\Local\\samcat.exe+80ffa|C:\\Users\\AtomicRed\\AppData\\Local\\samcat.exe+b4d70|C:\\Windows\\System32\\KERNEL32.DLL+17034|C:\\Windows\\SYSTEM32\\ntdll.dll+52651\"","version":"3","systemTime":"2021-10-01T15:10:29.5682759Z","eventRecordID":"405873","threadID":"3916","computer":"hrmanager.ExchangeTest.com","task":"10","processID":"2440","severityValue":"INFORMATION","providerName":"Microsoft-Windows-Sysmon"}}}
'''
        response = send_log(log)

        self.assertEqual(response.status, LogtestStatus.RuleMatch)

        self.assertEqual(response.decoder, 'json')
        self.assertEqual(response.rule_id, '92900')
        self.assertEqual(response.rule_level, 12)


    def test_explorer_injection(self) -> None:
        log = r'''
{"win":{"eventdata":{"sourceThreadId":"5960","grantedAccess":"0x1410","targetProcessGUID":"{4dc16835-0ceb-615e-5eda-090000000000}","targetProcessId":"5108","utcTime":"2021-10-06 21:13:40.604","ruleName":"technique_id=T1055.001,technique_name=Dynamic-link Library Injection","sourceProcessId":"3420","sourceImage":"C:\\\\Windows\\\\system32\\\\svchost.exe","targetImage":"C:\\\\Windows\\\\Explorer.EXE","sourceProcessGUID":"{4dc16835-0fed-615e-5923-390000000000}","callTrace":"C:\\\\Windows\\\\SYSTEM32\\\\ntdll.dll+9d234|C:\\\\Windows\\\\System32\\\\KERNELBASE.dll+2c0fe|UNKNOWN(000001F3F680C53A)"},"system":{"eventID":"10","keywords":"0x8000000000000000","providerGuid":"{5770385f-c22a-43e0-bf4c-06f5698ffbd9}","level":"4","channel":"Microsoft-Windows-Sysmon/Operational","opcode":"0","message":"\"Process accessed:\r\nRuleName: technique_id=T1055.001,technique_name=Dynamic-link Library Injection\r\nUtcTime: 2021-10-06 21:13:40.604\r\nSourceProcessGUID: {4dc16835-0fed-615e-5923-390000000000}\r\nSourceProcessId: 3420\r\nSourceThreadId: 5960\r\nSourceImage: C:\\Windows\\system32\\svchost.exe\r\nTargetProcessGUID: {4dc16835-0ceb-615e-5eda-090000000000}\r\nTargetProcessId: 5108\r\nTargetImage: C:\\Windows\\Explorer.EXE\r\nGrantedAccess: 0x1410\r\nCallTrace: C:\\Windows\\SYSTEM32\\ntdll.dll+9d234|C:\\Windows\\System32\\KERNELBASE.dll+2c0fe|UNKNOWN(000001F3F680C53A)\"","version":"3","systemTime":"2021-10-06T21:13:40.6074613Z","eventRecordID":"449201","threadID":"3376","computer":"hrmanager.ExchangeTest.com","task":"10","processID":"2480","severityValue":"INFORMATION","providerName":"Microsoft-Windows-Sysmon"}}}
'''
        response = send_log(log)

        self.assertEqual(response.status, LogtestStatus.RuleMatch)

        self.assertEqual(response.decoder, 'json')
        self.assertEqual(response.rule_id, '92910')
        self.assertEqual(response.rule_level, 12)


    def test_windows_rdp_injection(self) -> None:
        log = r'''
{"win":{"eventdata":{"sourceThreadId":"7944","grantedAccess":"0x1410","targetProcessGUID":"{4dc16835-13d3-615e-a46d-620000000000}","targetProcessId":"4620","utcTime":"2021-10-06 21:24:08.535","ruleName":"technique_id=T1055.001,technique_name=Dynamic-link Library Injection","sourceProcessId":"5108","sourceImage":"C:\\\\Windows\\\\Explorer.EXE","targetImage":"C:\\\\Windows\\\\system32\\\\mstsc.exe","sourceProcessGUID":"{4dc16835-0ceb-615e-5eda-090000000000}","callTrace":"C:\\\\Windows\\\\SYSTEM32\\\\ntdll.dll+9d234|C:\\\\Windows\\\\System32\\\\KERNELBASE.dll+2c0fe|UNKNOWN(00000000070AC53A)"},"system":{"eventID":"10","keywords":"0x8000000000000000","providerGuid":"{5770385f-c22a-43e0-bf4c-06f5698ffbd9}","level":"4","channel":"Microsoft-Windows-Sysmon/Operational","opcode":"0","message":"\"Process accessed:\r\nRuleName: technique_id=T1055.001,technique_name=Dynamic-link Library Injection\r\nUtcTime: 2021-10-06 21:24:08.535\r\nSourceProcessGUID: {4dc16835-0ceb-615e-5eda-090000000000}\r\nSourceProcessId: 5108\r\nSourceThreadId: 7944\r\nSourceImage: C:\\Windows\\Explorer.EXE\r\nTargetProcessGUID: {4dc16835-13d3-615e-a46d-620000000000}\r\nTargetProcessId: 4620\r\nTargetImage: C:\\Windows\\system32\\mstsc.exe\r\nGrantedAccess: 0x1410\r\nCallTrace: C:\\Windows\\SYSTEM32\\ntdll.dll+9d234|C:\\Windows\\System32\\KERNELBASE.dll+2c0fe|UNKNOWN(00000000070AC53A)\"","version":"3","systemTime":"2021-10-06T21:24:08.5360585Z","eventRecordID":"449974","threadID":"3376","computer":"hrmanager.ExchangeTest.com","task":"10","processID":"2480","severityValue":"INFORMATION","providerName":"Microsoft-Windows-Sysmon"}}}
'''
        response = send_log(log)

        self.assertEqual(response.status, LogtestStatus.RuleMatch)

        self.assertEqual(response.decoder, 'json')
        self.assertEqual(response.rule_id, '92920')
        self.assertEqual(response.rule_level, 14)

