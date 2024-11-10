
import unittest
from fountainai_openapi_parser.utils import resolve_references
import yaml
from pathlib import Path

class TestUtils(unittest.TestCase):
    def setUp(self):
        with open(Path(__file__).parent / "data/external_schema.yaml") as f:
            self.external_ref_yaml = yaml.safe_load(f)

    def test_resolve_external_reference(self):
        resolved_data = resolve_references(self.external_ref_yaml, base_path=Path(__file__).parent / "data")
        self.assertIn("example_field", resolved_data["components"]["schemas"]["ExampleSchema"]["properties"])
    