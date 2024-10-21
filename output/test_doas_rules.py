    import unittest

    from internal.logtest import LogtestStatus, send_log


    # Converted from doas.ini
    class TestDoasRules(unittest.TestCase):
            def test_failed_command(self) -> None:
            log = '''Apr 13 08:49:20 ix doas: failed command for ddp2: ls'''
            response = send_log(log)

            self.assertEqual(response.status, LogtestStatus.RuleMatch)

            self.assertEqual(response.decoder, 'doas')
            self.assertEqual(response.rule_id, '51554')
            self.assertEqual(response.alert_level, 5)

            def test_command_run_as_root(self) -> None:
            log = '''Mar 22 07:21:58 ix doas: ddp ran command /bin/ksh as root from /data/ddp/projects/git/sysconf/ossec/rules'''
            response = send_log(log)

            self.assertEqual(response.status, LogtestStatus.RuleMatch)

            self.assertEqual(response.decoder, 'doas')
            self.assertEqual(response.rule_id, '51556')
            self.assertEqual(response.alert_level, 2)

            def test_failed_auth(self) -> None:
            log = '''Feb 29 14:58:39 ix doas: failed auth for ddp'''
            response = send_log(log)

            self.assertEqual(response.status, LogtestStatus.RuleMatch)

            self.assertEqual(response.decoder, 'doas')
            self.assertEqual(response.rule_id, '51557')
            self.assertEqual(response.alert_level, 5)

            def test_doas_command_run(self) -> None:
            log = '''Aug 13 15:16:40 ix doas: ddp ran command as ddpnfs: ls'''
            response = send_log(log)

            self.assertEqual(response.status, LogtestStatus.RuleMatch)

            self.assertEqual(response.decoder, 'doas')
            self.assertEqual(response.rule_id, '51555')
            self.assertEqual(response.alert_level, 1)

    