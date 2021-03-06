##############################################################################
# Copyright (c) 2016 Huawei Technologies Co.,Ltd and others.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
##############################################################################
from __future__ import absolute_import
import unittest
import mock
import uuid

from yardstick.cmd.commands.env import EnvCommand


class EnvCommandTestCase(unittest.TestCase):

    @mock.patch('yardstick.cmd.commands.env.EnvCommand._start_async_task')
    @mock.patch('yardstick.cmd.commands.env.EnvCommand._check_status')
    def test_do_influxdb(self, check_status_mock, start_async_task_mock):
        env = EnvCommand()
        env.do_influxdb({})
        start_async_task_mock.assert_called_once()
        check_status_mock.assert_called_once()

    @mock.patch('yardstick.cmd.commands.env.EnvCommand._start_async_task')
    @mock.patch('yardstick.cmd.commands.env.EnvCommand._check_status')
    def test_do_grafana(self, check_status_mock, start_async_task_mock):
        env = EnvCommand()
        env.do_grafana({})
        start_async_task_mock.assert_called_once()
        check_status_mock.assert_called_once()

    @mock.patch('yardstick.cmd.commands.env.EnvCommand._start_async_task')
    @mock.patch('yardstick.cmd.commands.env.EnvCommand._check_status')
    def test_do_prepare(self, check_status_mock, start_async_task_mock):
        env = EnvCommand()
        env.do_prepare({})
        start_async_task_mock.assert_called_once()
        check_status_mock.assert_called_once()

    @mock.patch('yardstick.cmd.commands.env.HttpClient.post')
    def test_start_async_task(self, post_mock):
        data = {'action': 'create_grafana'}
        EnvCommand()._start_async_task(data)
        post_mock.assert_called_once()

    @mock.patch('yardstick.cmd.commands.env.HttpClient.get')
    @mock.patch('yardstick.cmd.commands.env.EnvCommand._print_status')
    def test_check_status(self, print_mock, get_mock):
        # pylint: disable=unused-argument
        # NOTE(ralonsoh): the pylint exception must be removed. The mocked
        # command call must be tested.
        task_id = str(uuid.uuid4())
        get_mock.return_value = {'status': 2, 'result': 'error'}
        status = EnvCommand()._check_status(task_id, 'hello world')
        self.assertEqual(status, 2)

    def test_print_status(self):
        try:
            EnvCommand()._print_status('hello', 'word')
        except Exception as e:  # pylint: disable=broad-except
            # NOTE(ralonsoh): try to reduce the scope of this exception.
            self.assertIsInstance(e, IndexError)
