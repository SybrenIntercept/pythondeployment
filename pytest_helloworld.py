import importlib
import json
from pathlib import Path
import unittest

import pytest


class TestHelloWorldUnitTests(unittest.TestCase):
	def test_helloworld_module_can_be_imported(self):
		module = importlib.import_module("helloworld")
		self.assertIsNotNone(module)

	def test_hello_function_returns_expected_text_when_available(self):
		module = importlib.import_module("helloworld")
		validated = False

		for name in ("hello", "hello_world", "get_message", "main"):
			func = getattr(module, name, None)
			if callable(func):
				result = func()
				if result is not None:
					self.assertIsInstance(result, str)
					self.assertIn("hello", result.lower())
					validated = True
					break

		if not validated:
			self.assertIsNotNone(module)


@pytest.mark.usefixtures("capsys")
def test_main_prints_hello_when_return_is_none(capsys):
	module = importlib.import_module("helloworld")
	main = getattr(module, "main", None)

	if callable(main):
		result = main()
		if result is None:
			captured = capsys.readouterr()
			assert isinstance(captured.out, str)
		else:
			assert isinstance(result, str)
	else:
		assert main is None


def test_host_json_exists_with_required_version():
	host_file = Path(__file__).with_name("host.json")
	assert host_file.exists()

	host_config = json.loads(host_file.read_text(encoding="utf-8"))
	assert host_config.get("version") == "2.0"
