import unittest
from qgis.PyQt.QtCore import QVariant, QMetaType

from ORStools.utils.wrapper import create_field_qgis_3_38_plus, create_field_legacy_qgis


class TestUtils(unittest.TestCase):
    def test_create_field_qgis_3_38_plus(self):
        test_cases = [
            ("int_field", QMetaType.Int, 10, 0, "Integer field", None),
            ("double_field", QMetaType.Double, 10, 5, "Double field", QMetaType.Float),
            ("string_field", QMetaType.QString, 50, 0, "String field", None),
        ]

        for name, type_enum, length, precision, comment, subtype_enum in test_cases:
            with self.subTest(name=name, type_enum=type_enum, subtype_enum=subtype_enum):
                field = create_field_qgis_3_38_plus(name, type_enum, length, precision, comment, subtype_enum)
                self.assertEqual(field.name(), name)
                self.assertEqual(field.length(), length)
                self.assertEqual(field.precision(), precision)
                self.assertEqual(field.comment(), comment)
                self.assertEqual(field.type(), type_enum)
                self.assertEqual(field.subType(), subtype_enum or QMetaType.Type.UnknownType)

    def test_create_field_legacy_qgis(self):
        test_cases = [
            ("int_field", QVariant.Int, 10, 0, "Integer field", None),
            ("double_field", QVariant.Double, 10, 5, "Double field", None),
            ("string_field", QVariant.String, 50, 0, "String field", None),
        ]

        for name, type_enum, length, precision, comment, subtype_enum in test_cases:
            with self.subTest(name=name, type_enum=type_enum, subtype_enum=subtype_enum):
                field = create_field_legacy_qgis(name, type_enum, length, precision, comment, subtype_enum)
                self.assertEqual(field.name(), name)
                self.assertEqual(field.length(), length)
                self.assertEqual(field.precision(), precision)
                self.assertEqual(field.comment(), comment)
                self.assertEqual(field.type(), type_enum)
                self.assertEqual(field.subType(), subtype_enum or QVariant.Invalid)
