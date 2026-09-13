import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from chayakudi_utils import (
    split_bill,
    is_wrapped_eligible,
    format_member_name,
)


def test_split_bill_divides_evenly():
    assert split_bill(100, ["ana", "raj", "meera"]) == 100 / 3


def test_is_wrapped_eligible_at_exact_threshold():
    assert is_wrapped_eligible(5) is True


def test_format_member_name_uses_last_name():
    assert format_member_name("ana", "lopez") == "Ana Lopez"
