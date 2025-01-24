#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# These test cases are based on log data and rule descriptions used for regression testing,
# potentially derived from or inspired by Wazuh rulesets and public log samples.

import unittest

from internal.logtest import LogtestStatus, send_log


# Converted from amazon_sec_lake.ini
class TestAmazonSecLakeRules(unittest.TestCase):

    def test_amazon_security_lake_cloudtrail_failed_api_operation_with_error_from_srcip_by_user(self) -> None:
        log = r'''
{"metadata": {"product": {"version": "1.08", "name": "CloudTrail", "feature": {"name": "Management, Data, and Insights"}, "vendor_name": "AWS"}, "profiles": ["cloud"], "version": "0.26.1"}, "time": 1680609784000, "cloud": {"region": "us-east-1", "provider": "AWS"}, "api": {"response": {"error": "AccessDenied", "message": "User: arn:aws:iam::567970947422:user/joseluis.lopez is not authorized to perform: iam:GetServiceLinkedRoleDeletionStatus on resource: arn:aws:iam::567970947422:role/aws-service-role/eks-nodegroup.amazonaws.com/AWSServiceRoleForAmazonEKSNodegroup because no identity-based policy allows the iam:GetServiceLinkedRoleDeletionStatus action"}, "operation": "GetServiceLinkedRoleDeletionStatus", "request": {"uid": "c843b04d-e7b4-4b0c-bd69-b2ebad898d52"}, "version": null, "service": {"name": "iam.amazonaws.com"}}, "ref_event_uid": "cbd70933-0003-42cd-9688-4af05b13fde0", "src_endpoint": {"uid": null, "ip": "62.117.187.171", "domain": null}, "resources": null, "identity": {"user": {"type": "IAMUser", "name": "joseluis.lopez", "uid": "AIDAYIPNU4FPDJPJKPTHV", "uuid": "arn:aws:iam::567970947422:user/joseluis.lopez", "account_uid": "567970947422", "credential_uid": "ASIAYIPNU4FPHJDVLMD6"}, "session": {"created_time": 1680601962000, "mfa": true, "issuer": null}, "invoked_by": null, "idp": {"name": null}}, "http_request": {"user_agent": "aws-internal/3 aws-sdk-java/1.12.414 Linux/5.10.165-126.735.amzn2int.x86_64 OpenJDK_64-Bit_Server_VM/25.362-b10 java/1.8.0_362 vendor/Oracle_Corporation cfg/retry-mode/standard"}, "class_name": "Cloud API", "class_uid": 5001, "category_name": "Cloud Activity", "category_uid": 5, "severity_id": 0, "severity": "Unknown", "activity_name": "Operational", "activity_id": 3, "type_uid": 500103, "type_name": "Cloud API: Operational", "unmapped": [["eventCategory", "Management"], ["recipientAccountId", "567970947422"], ["readOnly", "true"], ["eventType", "AwsApiCall"], ["managementEvent", "true"]]}
'''
        response = send_log(log)

        self.assertEqual(response.status, LogtestStatus.RuleMatch)

        self.assertEqual(response.decoder, 'json')
        self.assertEqual(response.rule_id, '99020')
        self.assertEqual(response.rule_level, 3)


    def test_amazon_security_lake_cloudtrail_successful_api_operation_by_user_from_srcip(self) -> None:
        log = r'''
{"metadata": {"product": {"version": "1.08", "name": "CloudTrail", "feature": {"name": "Management, Data, and Insights"}, "vendor_name": "AWS"}, "profiles": ["cloud"], "version": "0.26.1"}, "time": 1680290782000, "cloud": {"region": "us-east-1", "provider": "AWS"}, "api": {"response": {"error": null, "message": null}, "operation": "CreateRole", "request": {"uid": "50ce3d1c-ad17-466f-8724-62c6ed1b61d3"}, "version": null, "service": {"name": "monitoring.amazonaws.com"}}, "ref_event_uid": "7a73c797-75ca-4355-a703-cb88a5259805", "src_endpoint": {"uid": null, "ip": "186.127.25.250", "domain": null}, "resources": null, "identity": {"user": {"type": "IAMUser", "name": "javier.medeot", "uid": "AIDAYIPNU4FPI6FVZ4SEC", "uuid": "arn:aws:iam::567970947422:user/javier.medeot", "account_uid": "567970947422", "credential_uid": "ASIAYIPNU4FPPUVMVKXH"}, "session": {"created_time": 1680265937000, "mfa": true, "issuer": null}, "invoked_by": null, "idp": {"name": null}}, "http_request": {"user_agent": "AWS Internal"}, "class_name": "Cloud API", "class_uid": 5001, "category_name": "Cloud Activity", "category_uid": 5, "severity_id": 0, "severity": "Unknown", "activity_name": "Operational", "activity_id": 3, "type_uid": 500103, "type_name": "Cloud API: Operational", "unmapped": [["eventCategory", "Management"], ["sessionCredentialFromConsole", "true"], ["requestParameters", "{\"maxRecords\":100}"], ["recipientAccountId", "567970947422"], ["readOnly", "true"], ["eventType", "AwsApiCall"], ["managementEvent", "true"]]} {"metadata": {"product": {"version": "1.08", "name": "CloudTrail", "feature": {"name": "Management, Data, and Insights"}, "vendor_name": "AWS"}, "profiles": ["cloud"], "version": "0.26.1"}, "time": 1680290783000, "cloud": {"region": "us-east-1", "provider": "AWS"}, "api": {"response": {"error": null, "message": null}, "operation": "DescribeInstanceStatus", "request": {"uid": "5df43e93-4a05-497b-bef6-cc30105e028d"}, "version": null, "service": {"name": "ec2.amazonaws.com"}}, "ref_event_uid": "f751b1d8-8923-4975-9c95-c93a36485e15", "src_endpoint": {"uid": null, "ip": "186.127.25.250", "domain": null}, "resources": null, "identity": {"user": {"type": "IAMUser", "name": "javier.medeot", "uid": "AIDAYIPNU4FPI6FVZ4SEC", "uuid": "arn:aws:iam::567970947422:user/javier.medeot", "account_uid": "567970947422", "credential_uid": "ASIAYIPNU4FPPUVMVKXH"}, "session": {"created_time": 1680265937000, "mfa": true, "issuer": null}, "invoked_by": null, "idp": {"name": null}}, "http_request": {"user_agent": "AWS Internal"}, "class_name": "Cloud API", "class_uid": 5001, "category_name": "Cloud Activity", "category_uid": 5, "severity_id": 0, "severity": "Unknown", "activity_name": "Operational", "activity_id": 3, "type_uid": 500103, "type_name": "Cloud API: Operational", "unmapped": [["eventCategory", "Management"], ["sessionCredentialFromConsole", "true"], ["requestParameters", "{\"instancesSet\":{\"items\":[{\"instanceId\":\"i-08f69652bddf329c6\"},{\"instanceId\":\"i-0ade6659862bbc885\"},{\"instanceId\":\"i-0710bad5b508b7466\"},{\"instanceId\":\"i-0d9e76e5b1c5e9074\"},{\"instanceId\":\"i-0a7d0c7b4474826c1\"},{\"instanceId\":\"i-082b4362d842263ad\"}]},\"filterSet\":{},\"includeAllInstances\":false}"], ["recipientAccountId", "567970947422"], ["readOnly", "true"], ["eventType", "AwsApiCall"], ["managementEvent", "true"]]} {"metadata": {"product": {"version": "1.08", "name": "CloudTrail", "feature": {"name": "Management, Data, and Insights"}, "vendor_name": "AWS"}, "profiles": ["cloud"], "version": "0.26.1"}, "time": 1680290785000, "cloud": {"region": "us-east-1", "provider": "AWS"}, "api": {"response": {"error": null, "message": null}, "operation": "DescribeInstances", "request": {"uid": "59128c45-403a-436e-88ed-894c1fbd252c"}, "version": null, "service": {"name": "ec2.amazonaws.com"}}, "ref_event_uid": "6e397d33-caf9-4d41-875e-fc05b72ebe9b", "src_endpoint": {"uid": null, "ip": "186.127.25.250", "domain": null}, "resources": null, "identity": {"user": {"type": "IAMUser", "name": "javier.medeot", "uid": "AIDAYIPNU4FPI6FVZ4SEC", "uuid": "arn:aws:iam::567970947422:user/javier.medeot", "account_uid": "567970947422", "credential_uid": "ASIAYIPNU4FPPUVMVKXH"}, "session": {"created_time": 1680265937000, "mfa": true, "issuer": null}, "invoked_by": null, "idp": {"name": null}}, "http_request": {"user_agent": "AWS Internal"}, "class_name": "Cloud API", "class_uid": 5001, "category_name": "Cloud Activity", "category_uid": 5, "severity_id": 0, "severity": "Unknown", "activity_name": "Operational", "activity_id": 3, "type_uid": 500103, "type_name": "Cloud API: Operational", "unmapped": [["eventCategory", "Management"], ["sessionCredentialFromConsole", "true"], ["requestParameters", "{\"maxResults\":100,\"instancesSet\":{},\"filterSet\":{}}"], ["recipientAccountId", "567970947422"], ["readOnly", "true"], ["eventType", "AwsApiCall"], ["managementEvent", "true"]]}
'''
        response = send_log(log)

        self.assertEqual(response.status, LogtestStatus.RuleMatch)

        self.assertEqual(response.decoder, 'json')
        self.assertEqual(response.rule_id, '99022')
        self.assertEqual(response.rule_level, 3)


    def test_amazon_security_lake_cloudtrail_successful_api_operation(self) -> None:
        log = r'''
{"metadata": {"product": {"version": "1.08", "name": "CloudTrail", "feature": {"name": "Management, Data, and Insights"}, "vendor_name": "AWS"}, "profiles": ["cloud"], "version": "0.26.1"}, "time": 1680275892000, "cloud": {"region": "us-east-1", "provider": "AWS"}, "api": {"response": {"error": null, "message": null}, "operation": "PutObject", "request": {"uid": "NMC8MTA3E1793RVC"}, "version": null, "service": {"name": "s3.amazonaws.com"}}, "ref_event_uid": "c463c54b-3432-4db8-81de-dbca7fda12a7", "src_endpoint": {"uid": "vpce-06f1b2645e5d578c4", "ip": null, "domain": "securitylake.amazonaws.com"}, "resources": [{"uid": "arn:aws:s3:::aws-security-data-lake-us-east-1-fx1db6hfupnadeixhhsfnnqgwxvmdp/aws/ROUTE53/region=us-east-1/accountId=567970947422/eventHour=2023033115/70c39c1f6750aa35e4e563d2fa7306ce.gz.parquet", "account_uid": null, "type": "AWS::S3::Object"}, {"uid": "arn:aws:s3:::aws-security-data-lake-us-east-1-fx1db6hfupnadeixhhsfnnqgwxvmdp", "account_uid": "567970947422", "type": "AWS::S3::Bucket"}], "identity": {"user": {"type": "AWSService", "name": null, "uid": null, "uuid": null, "account_uid": null, "credential_uid": null}, "session": {"created_time": null, "mfa": null, "issuer": null}, "invoked_by": "securitylake.amazonaws.com", "idp": {"name": null}}, "http_request": {"user_agent": "securitylake.amazonaws.com"}, "class_name": "Cloud API", "class_uid": 5001, "category_name": "Cloud Activity", "category_uid": 5, "severity_id": 0, "severity": "Unknown", "activity_name": "Operational", "activity_id": 3, "type_uid": 500103, "type_name": "Cloud API: Operational", "unmapped": [["eventCategory", "Data"], ["sharedEventID", "1f2779c6-9386-4b6b-8239-99065d1b05f6"], ["responseElements", "{\"x-amz-server-side-encryption\":\"AES256\"}"], ["requestParameters", "{\"bucketName\":\"aws-security-data-lake-us-east-1-fx1db6hfupnadeixhhsfnnqgwxvmdp\",\"Host\":\"aws-security-data-lake-us-east-1-fx1db6hfupnadeixhhsfnnqgwxvmdp.s3.amazonaws.com\",\"x-amz-acl\":\"bucket-owner-full-control\",\"key\":\"aws/ROUTE53/region=us-east-1/accountId=567970947422/eventHour=2023033115/70c39c1f6750aa35e4e563d2fa7306ce.gz.parquet\"}"], ["recipientAccountId", "567970947422"], ["readOnly", "false"], ["eventType", "AwsApiCall"], ["managementEvent", "false"], ["additionalEventData", "{\"SignatureVersion\":\"SigV4\",\"CipherSuite\":\"ECDHE-RSA-AES128-GCM-SHA256\",\"bytesTransferredIn\":12294,\"SSEApplied\":\"Default_SSE_S3\",\"AuthenticationMethod\":\"AuthHeader\",\"x-amz-id-2\":\"RDc4/4Xa4qms34j/fZAnkJVxLs77jUq2/Uy3oUH6cnoW6oOz7N/PjWdDaEqL3nqoFSEv4YLyWs8=\",\"bytesTransferredOut\":0}"]]}
'''
        response = send_log(log)

        self.assertEqual(response.status, LogtestStatus.RuleMatch)

        self.assertEqual(response.decoder, 'json')
        self.assertEqual(response.rule_id, '99023')
        self.assertEqual(response.rule_level, 3)


    def test_amazon_security_lake_cloudtrail_successful_api_operation_from_srcip(self) -> None:
        log = r'''
{"metadata": {"product": {"version": "1.08", "name": "CloudTrail", "feature": {"name": "Management, Data, and Insights"}, "vendor_name": "AWS"}, "profiles": ["cloud"], "version": "0.26.1"}, "time": 1680375508000, "cloud": {"region": "us-east-1", "provider": "AWS"}, "api": {"response": {"error": null, "message": null}, "operation": "GetObject", "request": {"uid": "EETZJHE0KH99BBQP"}, "version": null, "service": {"name": "s3.amazonaws.com"}}, "ref_event_uid": "9f64a211-6bca-46c7-8038-74b58ed4250a", "src_endpoint": {"uid": null, "ip": "152.171.212.190", "domain": null}, "resources": [{"uid": "arn:aws:s3:::aws-security-data-lake-us-east-1-fx1db6hfupnadeixhhsfnnqgwxvmdp/aws/ROUTE53/region=us-east-1/accountId=567970947422/eventHour=2023040118/0ec39f175e03649046975a26cc4a4faf.gz.parquet", "account_uid": null, "type": "AWS::S3::Object"}, {"uid": "arn:aws:s3:::aws-security-data-lake-us-east-1-fx1db6hfupnadeixhhsfnnqgwxvmdp", "account_uid": "567970947422", "type": "AWS::S3::Bucket"}], "identity": {"user": {"type": "AssumedRole", "name": null, "uid": "AROAYIPNU4FPKWRVMKFS2:WazuhLogParsing", "uuid": "arn:aws:sts::567970947422:assumed-role/AmazonSecurityLake-4820c06e-9d69-4417-b75b-7cd2f002c3f1/WazuhLogParsing", "account_uid": "567970947422", "credential_uid": "ASIAYIPNU4FPHJLUAB5V"}, "session": {"created_time": 1680375505000, "mfa": false, "issuer": "arn:aws:iam::567970947422:role/AmazonSecurityLake-4820c06e-9d69-4417-b75b-7cd2f002c3f1"}, "invoked_by": null, "idp": {"name": null}}, "http_request": {"user_agent": "[Boto3/1.17.85 Python/3.9.16 Linux/6.2.0-76060200-generic Botocore/1.20.85]"}, "class_name": "Cloud API", "class_uid": 5001, "category_name": "Cloud Activity", "category_uid": 5, "severity_id": 0, "severity": "Unknown", "activity_name": "Operational", "activity_id": 3, "type_uid": 500103, "type_name": "Cloud API: Operational", "unmapped": [["eventCategory", "Data"], ["userIdentity_sessionContext_sessionIssuer_accountId", "567970947422"], ["requestParameters", "{\"bucketName\":\"aws-security-data-lake-us-east-1-fx1db6hfupnadeixhhsfnnqgwxvmdp\",\"Host\":\"aws-security-data-lake-us-east-1-fx1db6hfupnadeixhhsfnnqgwxvmdp.s3.amazonaws.com\",\"key\":\"aws/ROUTE53/region=us-east-1/accountId=567970947422/eventHour=2023040118/0ec39f175e03649046975a26cc4a4faf.gz.parquet\"}"], ["readOnly", "true"], ["eventType", "AwsApiCall"], ["userIdentity_sessionContext_sessionIssuer_userName", "AmazonSecurityLake-4820c06e-9d69-4417-b75b-7cd2f002c3f1"], ["additionalEventData", "{\"SignatureVersion\":\"SigV4\",\"CipherSuite\":\"ECDHE-RSA-AES128-GCM-SHA256\",\"bytesTransferredIn\":0,\"AuthenticationMethod\":\"AuthHeader\",\"x-amz-id-2\":\"uSALiYQ8bnDNNwUjmo0DwPy48gHeUWIoWQYvMvJJu3lKBbwgdf7m2BowwMDpozuU3+4vCZ4Jh2TJ8hkBJ76+jg==\",\"bytesTransferredOut\":12415}"], ["userIdentity_sessionContext_sessionIssuer_type", "Role"], ["tlsDetails", "{\"tlsVersion\":\"TLSv1.2\",\"cipherSuite\":\"ECDHE-RSA-AES128-GCM-SHA256\",\"clientProvidedHostHeader\":\"aws-security-data-lake-us-east-1-fx1db6hfupnadeixhhsfnnqgwxvmdp.s3.amazonaws.com\"}"], ["recipientAccountId", "567970947422"], ["userIdentity_sessionContext_sessionIssuer_principalId", "AROAYIPNU4FPKWRVMKFS2"], ["managementEvent", "false"], ["userIdentity_sessionContext_sessionIssuer_arn", "arn:aws:iam::567970947422:role/AmazonSecurityLake-4820c06e-9d69-4417-b75b-7cd2f002c3f1"]]}
'''
        response = send_log(log)

        self.assertEqual(response.status, LogtestStatus.RuleMatch)

        self.assertEqual(response.decoder, 'json')
        self.assertEqual(response.rule_id, '99024')
        self.assertEqual(response.rule_level, 3)


    def test_amazon_security_lake_cloudtrail_successful_api_operation_by_user(self) -> None:
        log = r'''
{"metadata": {"product": {"version": "1.08", "name": "CloudTrail", "feature": {"name": "Management, Data, and Insights"}, "vendor_name": "AWS"}, "profiles": ["cloud"], "version": "0.26.1"}, "time": 1680609823000, "cloud": {"region": "us-east-1", "provider": "AWS"}, "api": {"response": {"error": null, "message": null}, "operation": "DescribeEventAggregates", "request": {"uid": "6caab450-4600-4125-83b9-613aa773b2a2"}, "version": null, "service": {"name": "health.amazonaws.com"}}, "ref_event_uid": "6af6a63a-8bb3-428d-a1f4-fd29f9e83299", "src_endpoint": {"uid": null, "ip": null, "domain": "AWS Internal"}, "resources": null, "identity": {"user": {"type": "IAMUser", "name": "facundo.dalmau", "uid": "AIDAYIPNU4FPNQVGPI26X", "uuid": "arn:aws:iam::567970947422:user/facundo.dalmau", "account_uid": "567970947422", "credential_uid": "ASIAYIPNU4FPBWJ76265"}, "session": {"created_time": 1680609815000, "mfa": true, "issuer": null}, "invoked_by": "AWS Internal", "idp": {"name": null}}, "http_request": {"user_agent": "AWS Internal"}, "class_name": "Cloud API", "class_uid": 5001, "category_name": "Cloud Activity", "category_uid": 5, "severity_id": 0, "severity": "Unknown", "activity_name": "Operational", "activity_id": 3, "type_uid": 500103, "type_name": "Cloud API: Operational", "unmapped": [["eventCategory", "Management"], ["sessionCredentialFromConsole", "true"], ["requestParameters", "{\"filter\":{\"startTimes\":[{\"from\":\"Mar 28, 2023, 12:03:43 PM\"}],\"eventStatusCodes\":[\"open\",\"upcoming\"]},\"aggregateField\":\"eventTypeCategory\"}"], ["recipientAccountId", "567970947422"], ["readOnly", "true"], ["eventType", "AwsApiCall"], ["managementEvent", "true"]]}
'''
        response = send_log(log)

        self.assertEqual(response.status, LogtestStatus.RuleMatch)

        self.assertEqual(response.decoder, 'json')
        self.assertEqual(response.rule_id, '99025')
        self.assertEqual(response.rule_level, 3)


    def test_credentials_access_attempt_to_retrieve_ec2_credentials(self) -> None:
        log = r'''
{"metadata": {"product": {"version": "1.08", "name": "CloudTrail", "feature": {"name": "Management, Data, and Insights"}, "vendor_name": "AWS"}, "profiles": ["cloud"], "version": "0.26.1"}, "time": 1680290782000, "cloud": {"region": "us-east-1", "provider": "AWS"}, "api": {"response": {"error": null, "message": null}, "operation": "GetPasswordData", "request": {"uid": "50ce3d1c-ad17-466f-8724-62c6ed1b61d3"}, "version": null, "service": {"name": "monitoring.amazonaws.com"}}, "ref_event_uid": "7a73c797-75ca-4355-a703-cb88a5259805", "src_endpoint": {"uid": null, "ip": "186.127.25.250", "domain": null}, "resources": null, "identity": {"user": {"type": "IAMUser", "name": "javier.medeot", "uid": "AIDAYIPNU4FPI6FVZ4SEC", "uuid": "arn:aws:iam::567970947422:user/javier.medeot", "account_uid": "567970947422", "credential_uid": "ASIAYIPNU4FPPUVMVKXH"}, "session": {"created_time": 1680265937000, "mfa": true, "issuer": null}, "invoked_by": null, "idp": {"name": null}}, "http_request": {"user_agent": "AWS Internal"}, "class_name": "Cloud API", "class_uid": 5001, "category_name": "Cloud Activity", "category_uid": 5, "severity_id": 0, "severity": "Unknown", "activity_name": "Operational", "activity_id": 3, "type_uid": 500103, "type_name": "Cloud API: Operational", "unmapped": [["eventCategory", "Management"], ["sessionCredentialFromConsole", "true"], ["requestParameters", "{\"maxRecords\":100}"], ["recipientAccountId", "567970947422"], ["readOnly", "true"], ["eventType", "AwsApiCall"], ["managementEvent", "true"]]} {"metadata": {"product": {"version": "1.08", "name": "CloudTrail", "feature": {"name": "Management, Data, and Insights"}, "vendor_name": "AWS"}, "profiles": ["cloud"], "version": "0.26.1"}, "time": 1680290783000, "cloud": {"region": "us-east-1", "provider": "AWS"}, "api": {"response": {"error": null, "message": null}, "operation": "DescribeInstanceStatus", "request": {"uid": "5df43e93-4a05-497b-bef6-cc30105e028d"}, "version": null, "service": {"name": "ec2.amazonaws.com"}}, "ref_event_uid": "f751b1d8-8923-4975-9c95-c93a36485e15", "src_endpoint": {"uid": null, "ip": "186.127.25.250", "domain": null}, "resources": null, "identity": {"user": {"type": "IAMUser", "name": "javier.medeot", "uid": "AIDAYIPNU4FPI6FVZ4SEC", "uuid": "arn:aws:iam::567970947422:user/javier.medeot", "account_uid": "567970947422", "credential_uid": "ASIAYIPNU4FPPUVMVKXH"}, "session": {"created_time": 1680265937000, "mfa": true, "issuer": null}, "invoked_by": null, "idp": {"name": null}}, "http_request": {"user_agent": "AWS Internal"}, "class_name": "Cloud API", "class_uid": 5001, "category_name": "Cloud Activity", "category_uid": 5, "severity_id": 0, "severity": "Unknown", "activity_name": "Operational", "activity_id": 3, "type_uid": 500103, "type_name": "Cloud API: Operational", "unmapped": [["eventCategory", "Management"], ["sessionCredentialFromConsole", "true"], ["requestParameters", "{\"instancesSet\":{\"items\":[{\"instanceId\":\"i-08f69652bddf329c6\"},{\"instanceId\":\"i-0ade6659862bbc885\"},{\"instanceId\":\"i-0710bad5b508b7466\"},{\"instanceId\":\"i-0d9e76e5b1c5e9074\"},{\"instanceId\":\"i-0a7d0c7b4474826c1\"},{\"instanceId\":\"i-082b4362d842263ad\"}]},\"filterSet\":{},\"includeAllInstances\":false}"], ["recipientAccountId", "567970947422"], ["readOnly", "true"], ["eventType", "AwsApiCall"], ["managementEvent", "true"]]} {"metadata": {"product": {"version": "1.08", "name": "CloudTrail", "feature": {"name": "Management, Data, and Insights"}, "vendor_name": "AWS"}, "profiles": ["cloud"], "version": "0.26.1"}, "time": 1680290785000, "cloud": {"region": "us-east-1", "provider": "AWS"}, "api": {"response": {"error": null, "message": null}, "operation": "DescribeInstances", "request": {"uid": "59128c45-403a-436e-88ed-894c1fbd252c"}, "version": null, "service": {"name": "ec2.amazonaws.com"}}, "ref_event_uid": "6e397d33-caf9-4d41-875e-fc05b72ebe9b", "src_endpoint": {"uid": null, "ip": "186.127.25.250", "domain": null}, "resources": null, "identity": {"user": {"type": "IAMUser", "name": "javier.medeot", "uid": "AIDAYIPNU4FPI6FVZ4SEC", "uuid": "arn:aws:iam::567970947422:user/javier.medeot", "account_uid": "567970947422", "credential_uid": "ASIAYIPNU4FPPUVMVKXH"}, "session": {"created_time": 1680265937000, "mfa": true, "issuer": null}, "invoked_by": null, "idp": {"name": null}}, "http_request": {"user_agent": "AWS Internal"}, "class_name": "Cloud API", "class_uid": 5001, "category_name": "Cloud Activity", "category_uid": 5, "severity_id": 0, "severity": "Unknown", "activity_name": "Operational", "activity_id": 3, "type_uid": 500103, "type_name": "Cloud API: Operational", "unmapped": [["eventCategory", "Management"], ["sessionCredentialFromConsole", "true"], ["requestParameters", "{\"maxResults\":100,\"instancesSet\":{},\"filterSet\":{}}"], ["recipientAccountId", "567970947422"], ["readOnly", "true"], ["eventType", "AwsApiCall"], ["managementEvent", "true"]]}
'''
        response = send_log(log)

        self.assertEqual(response.status, LogtestStatus.RuleMatch)

        self.assertEqual(response.decoder, 'json')
        self.assertEqual(response.rule_id, '99026')
        self.assertEqual(response.rule_level, 5)


    def test_security_group_with_inbound_rules_allowing_unknown_cidrip_on_port_unknown_port_detected(self) -> None:
        log = r'''
{"metadata": {"product": {"version": "1.08", "name": "CloudTrail", "feature": {"name": "Management, Data, and Insights"}, "vendor_name": "AWS"}, "profiles": ["cloud"], "version": "0.26.1"}, "time": 1680290782000, "cloud": {"region": "us-east-1", "provider": "AWS"}, "api": {"response": {"error": null, "message": null}, "operation": "AuthorizeSecurityGroupIngress", "request": {"uid": "50ce3d1c-ad17-466f-8724-62c6ed1b61d3"}, "version": null, "service": {"name": "monitoring.amazonaws.com"}}, "ref_event_uid": "7a73c797-75ca-4355-a703-cb88a5259805", "src_endpoint": {"uid": null, "ip": "186.127.25.250", "domain": null}, "resources": null, "identity": {"user": {"type": "IAMUser", "name": "javier.medeot", "uid": "AIDAYIPNU4FPI6FVZ4SEC", "uuid": "arn:aws:iam::567970947422:user/javier.medeot", "account_uid": "567970947422", "credential_uid": "ASIAYIPNU4FPPUVMVKXH"}, "session": {"created_time": 1680265937000, "mfa": true, "issuer": null}, "invoked_by": null, "idp": {"name": null}}, "http_request": {"user_agent": "AWS Internal"}, "class_name": "Cloud API", "class_uid": 5001, "category_name": "Cloud Activity", "category_uid": 5, "severity_id": 0, "severity": "Unknown", "activity_name": "Operational", "activity_id": 3, "type_uid": 500103, "type_name": "Cloud API: Operational", "unmapped": [["eventCategory", "Management"], ["sessionCredentialFromConsole", "true"], ["requestParameters", "{\"maxRecords\":100}"], ["recipientAccountId", "567970947422"], ["readOnly", "true"], ["eventType", "AwsApiCall"], ["managementEvent", "true"]]} {"metadata": {"product": {"version": "1.08", "name": "CloudTrail", "feature": {"name": "Management, Data, and Insights"}, "vendor_name": "AWS"}, "profiles": ["cloud"], "version": "0.26.1"}, "time": 1680290783000, "cloud": {"region": "us-east-1", "provider": "AWS"}, "api": {"response": {"error": null, "message": null}, "operation": "DescribeInstanceStatus", "request": {"uid": "5df43e93-4a05-497b-bef6-cc30105e028d"}, "version": null, "service": {"name": "ec2.amazonaws.com"}}, "ref_event_uid": "f751b1d8-8923-4975-9c95-c93a36485e15", "src_endpoint": {"uid": null, "ip": "186.127.25.250", "domain": null}, "resources": null, "identity": {"user": {"type": "IAMUser", "name": "javier.medeot", "uid": "AIDAYIPNU4FPI6FVZ4SEC", "uuid": "arn:aws:iam::567970947422:user/javier.medeot", "account_uid": "567970947422", "credential_uid": "ASIAYIPNU4FPPUVMVKXH"}, "session": {"created_time": 1680265937000, "mfa": true, "issuer": null}, "invoked_by": null, "idp": {"name": null}}, "http_request": {"user_agent": "AWS Internal"}, "class_name": "Cloud API", "class_uid": 5001, "category_name": "Cloud Activity", "category_uid": 5, "severity_id": 0, "severity": "Unknown", "activity_name": "Operational", "activity_id": 3, "type_uid": 500103, "type_name": "Cloud API: Operational", "unmapped": [["eventCategory", "Management"], ["sessionCredentialFromConsole", "true"], ["requestParameters", "{\"instancesSet\":{\"items\":[{\"instanceId\":\"i-08f69652bddf329c6\"},{\"instanceId\":\"i-0ade6659862bbc885\"},{\"instanceId\":\"i-0710bad5b508b7466\"},{\"instanceId\":\"i-0d9e76e5b1c5e9074\"},{\"instanceId\":\"i-0a7d0c7b4474826c1\"},{\"instanceId\":\"i-082b4362d842263ad\"}]},\"filterSet\":{},\"includeAllInstances\":false}"], ["recipientAccountId", "567970947422"], ["readOnly", "true"], ["eventType", "AwsApiCall"], ["managementEvent", "true"]]} {"metadata": {"product": {"version": "1.08", "name": "CloudTrail", "feature": {"name": "Management, Data, and Insights"}, "vendor_name": "AWS"}, "profiles": ["cloud"], "version": "0.26.1"}, "time": 1680290785000, "cloud": {"region": "us-east-1", "provider": "AWS"}, "api": {"response": {"error": null, "message": null}, "operation": "DescribeInstances", "request": {"uid": "59128c45-403a-436e-88ed-894c1fbd252c"}, "version": null, "service": {"name": "ec2.amazonaws.com"}}, "ref_event_uid": "6e397d33-caf9-4d41-875e-fc05b72ebe9b", "src_endpoint": {"uid": null, "ip": "186.127.25.250", "domain": null}, "resources": null, "identity": {"user": {"type": "IAMUser", "name": "javier.medeot", "uid": "AIDAYIPNU4FPI6FVZ4SEC", "uuid": "arn:aws:iam::567970947422:user/javier.medeot", "account_uid": "567970947422", "credential_uid": "ASIAYIPNU4FPPUVMVKXH"}, "session": {"created_time": 1680265937000, "mfa": true, "issuer": null}, "invoked_by": null, "idp": {"name": null}}, "http_request": {"user_agent": "AWS Internal"}, "class_name": "Cloud API", "class_uid": 5001, "category_name": "Cloud Activity", "category_uid": 5, "severity_id": 0, "severity": "Unknown", "activity_name": "Operational", "activity_id": 3, "type_uid": 500103, "type_name": "Cloud API: Operational", "unmapped": [["eventCategory", "Management"], ["sessionCredentialFromConsole", "true"], ["requestParameters", "{\"maxResults\":100,\"instancesSet\":{},\"filterSet\":{}}"], ["recipientAccountId", "567970947422"], ["readOnly", "true"], ["eventType", "AwsApiCall"], ["managementEvent", "true"]]}
'''
        response = send_log(log)

        self.assertEqual(response.status, LogtestStatus.RuleMatch)

        self.assertEqual(response.decoder, 'json')
        self.assertEqual(response.rule_id, '99028')
        self.assertEqual(response.rule_level, 12)


    def test_possible_iam_role_backdooring_iam_role_granted_from_an_external_account(self) -> None:
        log = r'''
{"metadata": {"product": {"version": "1.08", "name": "CloudTrail", "feature": {"name": "Management, Data, and Insights"}, "vendor_name": "AWS"}, "profiles": ["cloud"], "version": "0.26.1"}, "time": 1680276859000, "cloud": {"region": "us-east-1", "provider": "AWS"}, "api": {"response": {"error": null, "message": null}, "operation": "CreateRole", "request": {"uid": "d882cba8-da5a-4914-a6db-83a3def09858"}, "version": null, "service": {"name": "iam.amazonaws.com"}}, "ref_event_uid": "5c8e297b-8341-4b6a-b5f8-2ce76282290e", "src_endpoint": {"uid": null, "ip": null, "domain": "securitylake.amazonaws.com"}, "resources": null, "identity": {"user": {"type": "IAMUser", "name": "nicolas.stefi", "uid": "AIDAYIPNU4FPPVP5OOEJ3", "uuid": "arn:aws:iam::567970947422:user/nicolas.stefi", "account_uid": "567970947422", "credential_uid": "ASIAYIPNU4FPBPXFFKDC"}, "session": {"created_time": 1680269774000, "mfa": true, "issuer": null}, "invoked_by": "securitylake.amazonaws.com", "idp": {"name": null}}, "http_request": {"user_agent": "securitylake.amazonaws.com"}, "class_name": "Cloud API", "class_uid": 5001, "category_name": "Cloud Activity", "category_uid": 5, "severity_id": 0, "severity": "Unknown", "activity_name": "Operational", "activity_id": 3, "type_uid": 500103, "type_name": "Cloud API: Operational", "unmapped": [["eventCategory", "Management"], ["sessionCredentialFromConsole", "true"], ["responseElements", "{\"role\":{\"assumeRolePolicyDocument\":\"%7B%22Version%22%3A%222012-10-17%22%2C%22Statement%22%3A%5B%7B%22Sid%22%3A%221%22%2C%22Effect%22%3A%22Allow%22%2C%22Principal%22%3A%7B%22AWS%22%3A%22567970947422%22%7D%2C%22Action%22%3A%5B%22sts%3AAssumeRole%22%5D%2C%22Condition%22%3A%7B%22StringEquals%22%3A%7B%22sts%3AExternalId%22%3A%5B%22TEST%22%5D%7D%7D%7D%5D%7D\",\"roleName\":\"AmazonSecurityLake-4820c06e-9d69-4417-b75b-7cd2f002c3f1\",\"roleId\":\"AROAYIPNU4FPKWRVMKFS2\",\"permissionsBoundary\":{\"permissionsBoundaryArn\":\"arn:aws:iam::aws:policy/AmazonSecurityLakePermissionsBoundary\",\"permissionsBoundaryType\":\"Policy\"},\"arn\":\"arn:aws:iam::567970947422:role/AmazonSecurityLake-4820c06e-9d69-4417-b75b-7cd2f002c3f1\",\"createDate\":\"Mar 31, 2023 3:34:19 PM\",\"path\":\"/\"}}"], ["requestParameters", "{\"assumeRolePolicyDocument\":\"{\\\"Version\\\":\\\"2012-10-17\\\",\\\"Statement\\\":[{\\\"Sid\\\":\\\"1\\\",\\\"Effect\\\":\\\"Allow\\\",\\\"Principal\\\":{\\\"AWS\\\":\\\"567970947422\\\"},\\\"Action\\\":[\\\"sts:AssumeRole\\\"],\\\"Condition\\\":{\\\"StringEquals\\\":{\\\"sts:ExternalId\\\":[\\\"TEST\\\"]}}}]}\",\"description\":\"Created a new role for subscriber to assume.\",\"roleName\":\"AmazonSecurityLake-4820c06e-9d69-4417-b75b-7cd2f002c3f1\",\"permissionsBoundary\":\"arn:aws:iam::aws:policy/AmazonSecurityLakePermissionsBoundary\"}"], ["recipientAccountId", "567970947422"], ["readOnly", "false"], ["eventType", "AwsApiCall"], ["managementEvent", "true"]]}
'''
        response = send_log(log)

        self.assertEqual(response.status, LogtestStatus.RuleMatch)

        self.assertEqual(response.decoder, 'json')
        self.assertEqual(response.rule_id, '99029')
        self.assertEqual(response.rule_level, 12)


    def test_possible_disruption_of_cloudtrail_logging_management_events_logging_disabled_with_an_event_selector(self) -> None:
        log = r'''
{"metadata": {"product": {"version": "1.08", "name": "CloudTrail", "feature": {"name": "Management, Data, and Insights"}, "vendor_name": "AWS"}, "profiles": ["cloud"], "version": "0.26.1"}, "time": 1680290782000, "cloud": {"region": "us-east-1", "provider": "AWS"}, "api": {"response": {"error": null, "message": null}, "operation": "PutEventSelectors", "request": {"uid": "50ce3d1c-ad17-466f-8724-62c6ed1b61d3"}, "version": null, "service": {"name": "monitoring.amazonaws.com"}}, "ref_event_uid": "7a73c797-75ca-4355-a703-cb88a5259805", "src_endpoint": {"uid": null, "ip": "186.127.25.250", "domain": null}, "resources": null, "identity": {"user": {"type": "IAMUser", "name": "javier.medeot", "uid": "AIDAYIPNU4FPI6FVZ4SEC", "uuid": "arn:aws:iam::567970947422:user/javier.medeot", "account_uid": "567970947422", "credential_uid": "ASIAYIPNU4FPPUVMVKXH"}, "session": {"created_time": 1680265937000, "mfa": true, "issuer": null}, "invoked_by": null, "idp": {"name": null}}, "http_request": {"user_agent": "AWS Internal"}, "class_name": "Cloud API", "class_uid": 5001, "category_name": "Cloud Activity", "category_uid": 5, "severity_id": 0, "severity": "Unknown", "activity_name": "Operational", "activity_id": 3, "type_uid": 500103, "type_name": "Cloud API: Operational", "unmapped": [["eventCategory", "Management"], ["sessionCredentialFromConsole", "true"], ["requestParameters", "{\"maxRecords\":100}"], ["recipientAccountId", "567970947422"], ["readOnly", "true"], ["eventType", "AwsApiCall"], ["managementEvent", "true"]]} {"metadata": {"product": {"version": "1.08", "name": "CloudTrail", "feature": {"name": "Management, Data, and Insights"}, "vendor_name": "AWS"}, "profiles": ["cloud"], "version": "0.26.1"}, "time": 1680290783000, "cloud": {"region": "us-east-1", "provider": "AWS"}, "api": {"response": {"error": null, "message": null}, "operation": "DescribeInstanceStatus", "request": {"uid": "5df43e93-4a05-497b-bef6-cc30105e028d"}, "version": null, "service": {"name": "ec2.amazonaws.com"}}, "ref_event_uid": "f751b1d8-8923-4975-9c95-c93a36485e15", "src_endpoint": {"uid": null, "ip": "186.127.25.250", "domain": null}, "resources": null, "identity": {"user": {"type": "IAMUser", "name": "javier.medeot", "uid": "AIDAYIPNU4FPI6FVZ4SEC", "uuid": "arn:aws:iam::567970947422:user/javier.medeot", "account_uid": "567970947422", "credential_uid": "ASIAYIPNU4FPPUVMVKXH"}, "session": {"created_time": 1680265937000, "mfa": true, "issuer": null}, "invoked_by": null, "idp": {"name": null}}, "http_request": {"user_agent": "AWS Internal"}, "class_name": "Cloud API", "class_uid": 5001, "category_name": "Cloud Activity", "category_uid": 5, "severity_id": 0, "severity": "Unknown", "activity_name": "Operational", "activity_id": 3, "type_uid": 500103, "type_name": "Cloud API: Operational", "unmapped": [["eventCategory", "Management"], ["sessionCredentialFromConsole", "true"], ["requestParameters", "{\"instancesSet\":{\"items\":[{\"instanceId\":\"i-08f69652bddf329c6\"},{\"instanceId\":\"i-0ade6659862bbc885\"},{\"instanceId\":\"i-0710bad5b508b7466\"},{\"instanceId\":\"i-0d9e76e5b1c5e9074\"},{\"instanceId\":\"i-0a7d0c7b4474826c1\"},{\"instanceId\":\"i-082b4362d842263ad\"}]},\"filterSet\":{},\"includeAllInstances\":false}"], ["recipientAccountId", "567970947422"], ["readOnly", "true"], ["eventType", "AwsApiCall"], ["managementEvent", "true"]]} {"metadata": {"product": {"version": "1.08", "name": "CloudTrail", "feature": {"name": "Management, Data, and Insights"}, "vendor_name": "AWS"}, "profiles": ["cloud"], "version": "0.26.1"}, "time": 1680290785000, "cloud": {"region": "us-east-1", "provider": "AWS"}, "api": {"response": {"error": null, "message": null}, "operation": "DescribeInstances", "request": {"uid": "59128c45-403a-436e-88ed-894c1fbd252c"}, "version": null, "service": {"name": "ec2.amazonaws.com"}}, "ref_event_uid": "6e397d33-caf9-4d41-875e-fc05b72ebe9b", "src_endpoint": {"uid": null, "ip": "186.127.25.250", "domain": null}, "resources": null, "identity": {"user": {"type": "IAMUser", "name": "javier.medeot", "uid": "AIDAYIPNU4FPI6FVZ4SEC", "uuid": "arn:aws:iam::567970947422:user/javier.medeot", "account_uid": "567970947422", "credential_uid": "ASIAYIPNU4FPPUVMVKXH"}, "session": {"created_time": 1680265937000, "mfa": true, "issuer": null}, "invoked_by": null, "idp": {"name": null}}, "http_request": {"user_agent": "AWS Internal"}, "class_name": "Cloud API", "class_uid": 5001, "category_name": "Cloud Activity", "category_uid": 5, "severity_id": 0, "severity": "Unknown", "activity_name": "Operational", "activity_id": 3, "type_uid": 500103, "type_name": "Cloud API: Operational", "unmapped": [["eventCategory", "Management"], ["sessionCredentialFromConsole", "true"], ["requestParameters", "{\"maxResults\":100,\"instancesSet\":{},\"filterSet\":{}}"], ["recipientAccountId", "567970947422"], ["readOnly", "true"], ["eventType", "AwsApiCall"], ["managementEvent", "true"]]}
'''
        response = send_log(log)

        self.assertEqual(response.status, LogtestStatus.RuleMatch)

        self.assertEqual(response.decoder, 'json')
        self.assertEqual(response.rule_id, '99030')
        self.assertEqual(response.rule_level, 12)


    def test_amazon_security_lake_vpc_ssh_connection_established_dst(self) -> None:
        log = r'''
{"metadata": {"product": {"version": "5", "name": "Amazon VPC", "feature": {"name": "Flowlogs"}, "vendor_name": "AWS"}, "profiles": ["cloud"], "version": "0.39.0"}, "cloud": {"account_uid": "567970947422", "region": "us-east-1", "zone": "use1-az4", "provider": "AWS"}, "src_endpoint": {"port": 44250, "svc_name": "-", "ip": "131.100.164.234", "intermediate_ips": null, "interface_uid": null, "vpc_uid": null, "instance_uid": null, "subnet_uid": null}, "dst_endpoint": {"port": 22, "svc_name": "-", "ip": "172.31.17.20", "intermediate_ips": null, "interface_uid": "eni-047062ec08692c9dc", "vpc_uid": "vpc-f825c385", "instance_uid": "i-0d9e76e5b1c5e9074", "subnet_uid": "subnet-4023460d"}, "connection_info": {"protocol_num": 6, "tcp_flags": 3, "protocol_ver": "IPv4", "direction": "ingress", "boundary_id": 0, "boundary": "Unknown", "direction_id": 1}, "traffic": {"packets": 13, "bytes": 1776}, "time": 1680282685000, "start_time": 1680282685000, "end_time": 1680282744000, "severity_id": -1, "severity": "Other", "class_name": "Network Activity", "class_uid": 4001, "category_name": "Network Activity", "category_uid": 4, "activity_name": "Established", "activity_id": 1, "type_uid": 400101, "type_name": "Network Activity: Established", "unmapped": [["log_status", "OK"], ["sublocation_id", "-"], ["sublocation_type", "-"]]}
'''
        response = send_log(log)

        self.assertEqual(response.status, LogtestStatus.RuleMatch)

        self.assertEqual(response.decoder, 'json')
        self.assertEqual(response.rule_id, '99051')
        self.assertEqual(response.rule_level, 3)


    def test_amazon_security_lake_vpc_ssh_connection_established_src(self) -> None:
        log = r'''
{"metadata": {"product": {"version": "5", "name": "Amazon VPC", "feature": {"name": "Flowlogs"}, "vendor_name": "AWS"}, "profiles": ["cloud"], "version": "0.39.0"}, "cloud": {"account_uid": "567970947422", "region": "us-east-1", "zone": "use1-az4", "provider": "AWS"}, "src_endpoint": {"port": 22, "svc_name": "-", "ip": "172.31.17.20", "intermediate_ips": null, "interface_uid": "eni-047062ec08692c9dc", "vpc_uid": "vpc-f825c385", "instance_uid": "i-0d9e76e5b1c5e9074", "subnet_uid": "subnet-4023460d"}, "dst_endpoint": {"port": 44360, "svc_name": "-", "ip": "131.100.164.234", "intermediate_ips": null, "interface_uid": null, "vpc_uid": null, "instance_uid": null, "subnet_uid": null}, "connection_info": {"protocol_num": 6, "tcp_flags": 19, "protocol_ver": "IPv4", "direction": "egress", "boundary_id": 5, "boundary": "Internet/VPC Gateway", "direction_id": 2}, "traffic": {"packets": 11, "bytes": 2297}, "time": 1680282685000, "start_time": 1680282685000, "end_time": 1680282744000, "severity_id": -1, "severity": "Other", "class_name": "Network Activity", "class_uid": 4001, "category_name": "Network Activity", "category_uid": 4, "activity_name": "Established", "activity_id": 1, "type_uid": 400101, "type_name": "Network Activity: Established", "unmapped": [["log_status", "OK"], ["sublocation_id", "-"], ["sublocation_type", "-"]]}
'''
        response = send_log(log)

        self.assertEqual(response.status, LogtestStatus.RuleMatch)

        self.assertEqual(response.decoder, 'json')
        self.assertEqual(response.rule_id, '99052')
        self.assertEqual(response.rule_level, 3)


    def test_amazon_security_lake_vpc_rdp_connection_established_dst(self) -> None:
        log = r'''
{"metadata": {"product": {"version": "5", "name": "Amazon VPC", "feature": {"name": "Flowlogs"}, "vendor_name": "AWS"}, "profiles": ["cloud"], "version": "0.39.0"}, "cloud": {"account_uid": "567970947422", "region": "us-east-1", "zone": "use1-az2", "provider": "AWS"}, "src_endpoint": {"port": 59001, "svc_name": "-", "ip": "192.3.136.82", "intermediate_ips": null, "interface_uid": null, "vpc_uid": null, "instance_uid": null, "subnet_uid": null}, "dst_endpoint": {"port": 3389, "svc_name": "-", "ip": "172.31.94.2", "intermediate_ips": null, "interface_uid": "eni-03a9d41902b1a1035", "vpc_uid": "vpc-f825c385", "instance_uid": "i-08f69652bddf329c6", "subnet_uid": "subnet-cfa777ee"}, "connection_info": {"protocol_num": 6, "tcp_flags": 2, "protocol_ver": "IPv4", "direction": "ingress", "boundary_id": 0, "boundary": "Unknown", "direction_id": 1}, "traffic": {"packets": 1, "bytes": 40}, "time": 1680280702000, "start_time": 1680280702000, "end_time": 1680280730000, "severity_id": -1, "severity": "Other", "class_name": "Network Activity", "class_uid": 4001, "category_name": "Network Activity", "category_uid": 4, "activity_name": "Established", "activity_id": 1, "type_uid": 400101, "type_name": "Network Activity: Established", "unmapped": [["log_status", "OK"], ["sublocation_id", "-"], ["sublocation_type", "-"]]}
'''
        response = send_log(log)

        self.assertEqual(response.status, LogtestStatus.RuleMatch)

        self.assertEqual(response.decoder, 'json')
        self.assertEqual(response.rule_id, '99053')
        self.assertEqual(response.rule_level, 3)


    def test_amazon_security_lake_vpc_rdp_connection_established_src(self) -> None:
        log = r'''
{"metadata": {"product": {"version": "5", "name": "Amazon VPC", "feature": {"name": "Flowlogs"}, "vendor_name": "AWS"}, "profiles": ["cloud"], "version": "0.39.0"}, "cloud": {"account_uid": "567970947422", "region": "us-east-1", "zone": "use1-az2", "provider": "AWS"}, "src_endpoint": {"port": 3389, "svc_name": "-", "ip": "172.31.94.2", "intermediate_ips": null, "interface_uid": "eni-03a9d41902b1a1035", "vpc_uid": "vpc-f825c385", "instance_uid": "i-08f69652bddf329c6", "subnet_uid": "subnet-cfa777ee"}, "dst_endpoint": {"port": 59001, "svc_name": "-", "ip": "192.3.136.82", "intermediate_ips": null, "interface_uid": null, "vpc_uid": null, "instance_uid": null, "subnet_uid": null}, "connection_info": {"protocol_num": 6, "tcp_flags": 4, "protocol_ver": "IPv4", "direction": "egress", "boundary_id": 11, "boundary": "Internet Gateway", "direction_id": 2}, "traffic": {"packets": 1, "bytes": 40}, "time": 1680280702000, "start_time": 1680280702000, "end_time": 1680280730000, "severity_id": -1, "severity": "Other", "class_name": "Network Activity", "class_uid": 4001, "category_name": "Network Activity", "category_uid": 4, "activity_name": "Established", "activity_id": 1, "type_uid": 400101, "type_name": "Network Activity: Established", "unmapped": [["log_status", "OK"], ["sublocation_id", "-"], ["sublocation_type", "-"]]}
'''
        response = send_log(log)

        self.assertEqual(response.status, LogtestStatus.RuleMatch)

        self.assertEqual(response.decoder, 'json')
        self.assertEqual(response.rule_id, '99054')
        self.assertEqual(response.rule_level, 3)


    def test_amazon_security_lake_vpc_smb_connection_established_dst(self) -> None:
        log = r'''
{"metadata": {"product": {"version": "5", "name": "Amazon VPC", "feature": {"name": "Flowlogs"}, "vendor_name": "AWS"}, "profiles": ["cloud"], "version": "0.39.0"}, "cloud": {"account_uid": "567970947422", "region": "us-east-1", "zone": "use1-az4", "provider": "AWS"}, "src_endpoint": {"port": 443, "svc_name": "-", "ip": "216.239.36.21", "intermediate_ips": null, "interface_uid": null, "vpc_uid": null, "instance_uid": null, "subnet_uid": null}, "dst_endpoint": {"port": 54454, "svc_name": "-", "ip": "172.31.17.20", "intermediate_ips": null, "interface_uid": "eni-047062ec08692c9dc", "vpc_uid": "vpc-f825c385", "instance_uid": "i-0d9e76e5b1c5e9074", "subnet_uid": "subnet-4023460d"}, "connection_info": {"protocol_num": 6, "tcp_flags": 19, "protocol_ver": "IPv4", "direction": "ingress", "boundary_id": 0, "boundary": "Unknown", "direction_id": 1}, "traffic": {"packets": 12, "bytes": 5945}, "time": 1680275123000, "start_time": 1680275123000, "end_time": 1680275181000, "severity_id": -1, "severity": "Other", "class_name": "Network Activity", "class_uid": 4001, "category_name": "Network Activity", "category_uid": 4, "activity_name": "Established", "activity_id": 1, "type_uid": 400101, "type_name": "Network Activity: Established", "unmapped": [["log_status", "OK"], ["sublocation_id", "-"], ["sublocation_type", "-"]]}
'''
        response = send_log(log)

        self.assertEqual(response.status, LogtestStatus.RuleMatch)

        self.assertEqual(response.decoder, 'json')
        self.assertEqual(response.rule_id, '99055')
        self.assertEqual(response.rule_level, 3)


    def test_amazon_security_lake_vpc_smb_connection_established_src(self) -> None:
        log = r'''
{"metadata": {"product": {"version": "5", "name": "Amazon VPC", "feature": {"name": "Flowlogs"}, "vendor_name": "AWS"}, "profiles": ["cloud"], "version": "0.39.0"}, "cloud": {"account_uid": "567970947422", "region": "us-east-1", "zone": "use1-az4", "provider": "AWS"}, "src_endpoint": {"port": 54454, "svc_name": "-", "ip": "172.31.17.20", "intermediate_ips": null, "interface_uid": "eni-047062ec08692c9dc", "vpc_uid": "vpc-f825c385", "instance_uid": "i-0d9e76e5b1c5e9074", "subnet_uid": "subnet-4023460d"}, "dst_endpoint": {"port": 443, "svc_name": "-", "ip": "216.239.36.21", "intermediate_ips": null, "interface_uid": null, "vpc_uid": null, "instance_uid": null, "subnet_uid": null}, "connection_info": {"protocol_num": 6, "tcp_flags": 3, "protocol_ver": "IPv4", "direction": "egress", "boundary_id": 5, "boundary": "Internet/VPC Gateway", "direction_id": 2}, "traffic": {"packets": 14, "bytes": 6050}, "time": 1680275123000, "start_time": 1680275123000, "end_time": 1680275181000, "severity_id": -1, "severity": "Other", "class_name": "Network Activity", "class_uid": 4001, "category_name": "Network Activity", "category_uid": 4, "activity_name": "Established", "activity_id": 1, "type_uid": 400101, "type_name": "Network Activity: Established", "unmapped": [["log_status", "OK"], ["sublocation_id", "-"], ["sublocation_type", "-"]]}
'''
        response = send_log(log)

        self.assertEqual(response.status, LogtestStatus.RuleMatch)

        self.assertEqual(response.decoder, 'json')
        self.assertEqual(response.rule_id, '99056')
        self.assertEqual(response.rule_level, 3)


    def test_amazon_security_lake_vpc_dce_rpc_connection_established_dst(self) -> None:
        log = r'''
{"metadata": {"product": {"version": "5", "name": "Amazon VPC", "feature": {"name": "Flowlogs"}, "vendor_name": "AWS"}, "profiles": ["cloud"], "version": "0.39.0"}, "cloud": {"account_uid": "567970947422", "region": "us-east-1", "zone": "use1-az4", "provider": "AWS"}, "src_endpoint": {"port": 123, "svc_name": "-", "ip": "44.190.40.123", "intermediate_ips": null, "interface_uid": null, "vpc_uid": null, "instance_uid": null, "subnet_uid": null}, "dst_endpoint": {"port": 41354, "svc_name": "-", "ip": "172.31.17.20", "intermediate_ips": null, "interface_uid": "eni-047062ec08692c9dc", "vpc_uid": "vpc-f825c385", "instance_uid": "i-0d9e76e5b1c5e9074", "subnet_uid": "subnet-4023460d"}, "connection_info": {"protocol_num": 17, "tcp_flags": 0, "protocol_ver": "IPv4", "direction": "ingress", "boundary_id": 0, "boundary": "Unknown", "direction_id": 1}, "traffic": {"packets": 1, "bytes": 76}, "time": 1680290069000, "start_time": 1680290069000, "end_time": 1680290127000, "severity_id": -1, "severity": "Other", "class_name": "Network Activity", "class_uid": 4001, "category_name": "Network Activity", "category_uid": 4, "activity_name": "Established", "activity_id": 1, "type_uid": 400101, "type_name": "Network Activity: Established", "unmapped": [["log_status", "OK"], ["sublocation_id", "-"], ["sublocation_type", "-"]]}
'''
        response = send_log(log)

        self.assertEqual(response.status, LogtestStatus.RuleMatch)

        self.assertEqual(response.decoder, 'json')
        self.assertEqual(response.rule_id, '99057')
        self.assertEqual(response.rule_level, 3)


    def test_amazon_security_lake_vpc_dce_rpc_connection_established_src(self) -> None:
        log = r'''
{"metadata": {"product": {"version": "5", "name": "Amazon VPC", "feature": {"name": "Flowlogs"}, "vendor_name": "AWS"}, "profiles": ["cloud"], "version": "0.39.0"}, "cloud": {"account_uid": "567970947422", "region": "us-east-1", "zone": "use1-az4", "provider": "AWS"}, "src_endpoint": {"port": 41354, "svc_name": "-", "ip": "172.31.17.20", "intermediate_ips": null, "interface_uid": "eni-047062ec08692c9dc", "vpc_uid": "vpc-f825c385", "instance_uid": "i-0d9e76e5b1c5e9074", "subnet_uid": "subnet-4023460d"}, "dst_endpoint": {"port": 123, "svc_name": "-", "ip": "44.190.40.123", "intermediate_ips": null, "interface_uid": null, "vpc_uid": null, "instance_uid": null, "subnet_uid": null}, "connection_info": {"protocol_num": 17, "tcp_flags": 0, "protocol_ver": "IPv4", "direction": "egress", "boundary_id": 5, "boundary": "Internet/VPC Gateway", "direction_id": 2}, "traffic": {"packets": 1, "bytes": 76}, "time": 1680290069000, "start_time": 1680290069000, "end_time": 1680290127000, "severity_id": -1, "severity": "Other", "class_name": "Network Activity", "class_uid": 4001, "category_name": "Network Activity", "category_uid": 4, "activity_name": "Established", "activity_id": 1, "type_uid": 400101, "type_name": "Network Activity: Established", "unmapped": [["log_status", "OK"], ["sublocation_id", "-"], ["sublocation_type", "-"]]}
'''
        response = send_log(log)

        self.assertEqual(response.status, LogtestStatus.RuleMatch)

        self.assertEqual(response.decoder, 'json')
        self.assertEqual(response.rule_id, '99058')
        self.assertEqual(response.rule_level, 3)


    def test_amazon_security_lake_route_53_succsessful_dns_request_query_type_hostname_from_srcip(self) -> None:
        log = r'''
{"metadata": {"product": {"version": "1.100000", "name": "Route 53", "feature": {"name": "Resolver Query Logs"}, "vendor_name": "AWS"}, "profiles": ["cloud"], "version": "0.26.1"}, "cloud": {"account_uid": "567970947422", "region": "us-east-1", "provider": "AWS"}, "src_endpoint": {"vpc_uid": "vpc-f825c385", "ip": "172.31.6.147", "port": 35646, "instance_uid": "i-0ade6659862bbc885"}, "time": 1680601347000, "query": {"hostname": "s3-r-w.dualstack.us-east-1.amazonaws.com.", "type": "AAAA", "class": "IN"}, "rcode": "NOERROR", "answers": [{"type": "AAAA", "rdata": "2600:1fa0:80b4:db08:34d9:6f20::", "class": "IN"}, {"type": "AAAA", "rdata": "2600:1fa0:81ef:9d31:34d8:d68a::", "class": "IN"}, {"type": "AAAA", "rdata": "2600:1fa0:811b:a2e1:34d8:3e1a::", "class": "IN"}, {"type": "AAAA", "rdata": "2600:1fa0:816f:9968:34d9:7122::", "class": "IN"}, {"type": "AAAA", "rdata": "2600:1fa0:81eb:a321:34d8:de0a::", "class": "IN"}, {"type": "AAAA", "rdata": "2600:1fa0:8095:39c1:34d8:fa58::", "class": "IN"}, {"type": "AAAA", "rdata": "2600:1fa0:8038:4a81:34d9:53b8::", "class": "IN"}, {"type": "AAAA", "rdata": "2600:1fa0:81ab:9269:34d8:29fa::", "class": "IN"}], "connection_info": {"protocol_name": "UDP", "direction": "Unknown", "direction_id": 0}, "dst_endpoint": {"instance_uid": null, "interface_uid": null}, "severity_id": -1, "severity": "Other", "class_name": "DNS Activity", "class_uid": 4003, "category_name": "Network Activity", "category_uid": 4, "rcode_id": 0, "activity_id": 1, "activity_name": "Resolved", "type_name": "DNS Activity: Resolved", "type_uid": 400301, "unmapped": null}
'''
        response = send_log(log)

        self.assertEqual(response.status, LogtestStatus.RuleMatch)

        self.assertEqual(response.decoder, 'json')
        self.assertEqual(response.rule_id, '99080')
        self.assertEqual(response.rule_level, 3)


    def test_amazon_security_lake_route_53_failed_dns_request_for_a_non_existent_domain_query_type_hostname_from_srcip(self) -> None:
        log = r'''
{"metadata": {"product": {"version": "1.100000", "name": "Route 53", "feature": {"name": "Resolver Query Logs"}, "vendor_name": "AWS"}, "profiles": ["cloud"], "version": "0.26.1"}, "cloud": {"account_uid": "567970947422", "region": "us-east-1", "provider": "AWS"}, "src_endpoint": {"vpc_uid": "vpc-f825c385", "ip": "172.31.26.42", "port": 35540, "instance_uid": "i-0710bad5b508b7466"}, "time": 1680552621000, "query": {"hostname": "94-153-212-78.ip.kyivstar.net.ec2.internal.", "type": "A", "class": "IN"}, "rcode": "NXDOMAIN", "answers": [], "connection_info": {"protocol_name": "UDP", "direction": "Unknown", "direction_id": 0}, "dst_endpoint": {"instance_uid": null, "interface_uid": null}, "severity_id": -1, "severity": "Other", "class_name": "DNS Activity", "class_uid": 4003, "category_name": "Network Activity", "category_uid": 4, "rcode_id": 3, "activity_id": 2, "activity_name": "Unresolved", "type_name": "DNS Activity: Unresolved", "type_uid": 400302, "unmapped": null}
'''
        response = send_log(log)

        self.assertEqual(response.status, LogtestStatus.RuleMatch)

        self.assertEqual(response.decoder, 'json')
        self.assertEqual(response.rule_id, '99081')
        self.assertEqual(response.rule_level, 3)


    def test_amazon_security_lake_route_53_failed_dns_request_query_type_hostname_from_srcip(self) -> None:
        log = r'''
{"metadata": {"product": {"version": "1.100000", "name": "Route 53", "feature": {"name": "Resolver Query Logs"}, "vendor_name": "AWS"}, "profiles": ["cloud"], "version": "0.26.1"}, "cloud": {"account_uid": "567970947422", "region": "us-east-1", "provider": "AWS"}, "src_endpoint": {"vpc_uid": "vpc-f825c385", "ip": "172.31.26.42", "port": 37822, "instance_uid": "i-0710bad5b508b7466"}, "time": 1680552600000, "query": {"hostname": "229.65.70.202.in-addr.arpa.", "type": "PTR", "class": "IN"}, "rcode": "", "answers": [], "connection_info": {"protocol_name": "UDP", "direction": "Unknown", "direction_id": 0}, "dst_endpoint": {"instance_uid": null, "interface_uid": null}, "severity_id": -1, "severity": "Other", "class_name": "DNS Activity", "class_uid": 4003, "category_name": "Network Activity", "category_uid": 4, "rcode_id": -1, "activity_id": -1, "activity_name": "Unknown", "type_name": "DNS Activity: Unknown", "type_uid": 400300, "unmapped": null}
'''
        response = send_log(log)

        self.assertEqual(response.status, LogtestStatus.RuleMatch)

        self.assertEqual(response.decoder, 'json')
        self.assertEqual(response.rule_id, '99082')
        self.assertEqual(response.rule_level, 3)

