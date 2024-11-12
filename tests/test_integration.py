import unittest
    from fountainai_openapi_parser.utils import resolve_references
import yaml
    from pathlib import Path


class TestIntegration(unittest.TestCase):
    def setUp(self):
        with open(Path(__file__).parent / "data/openapi.yaml") as f:
            self.openapi_yaml = yaml.safe_load(f)

    def test_external_reference_resolution(self):
        resolved_result = resolve_references(
            self.openapi_yaml, base_path=Path(__file__).parent / "data"
        )
        self.assertIn(
            "example_field",
            resolved_result["components"]["schemas"]["ExampleSchema"][
                "properties"
            ],
        )
