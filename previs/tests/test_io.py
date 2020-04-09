import json
from pathlib import Path

import pytest
from previs import load_survey, save_survey, survey

TEST_DIR = Path(__file__).parent
TEST_DATA_DIR = TEST_DIR / "data"
small_survey_file = TEST_DATA_DIR / "small_survey.json"


@pytest.mark.parametrize(
    "filepath",
    [small_survey_file, small_survey_file.with_suffix(
        ""), str(small_survey_file)],
)
def test_load_survey(filepath):
    s = load_survey(filepath)
    assert isinstance(s, dict)


@pytest.mark.timeout(120)
def test_reproduce_survey():
    s1 = load_survey(small_survey_file)
    stars = list(s1.keys())

    s2 = survey(stars)
    assert isinstance(s2, dict)
    assert len(s1) == len(s2)
    for star in s1:
        assert star in s2
        assert set(list(s1[star].keys())) == set(list(s2[star].keys()))


def test_overwrite(tmpdir):
    s = load_survey(small_survey_file)

    target_file = Path(tmpdir.join("already_there.json"))
    target_file.touch()

    with pytest.raises(FileExistsError):
        save_survey(s, target_file)

    save_survey(s, target_file, overwrite=True)


@pytest.mark.parametrize("filepath", ["s0", "s1.json"])
def test_save_survey(tmpdir, filepath):
    s = load_survey(small_survey_file)
    target_path = Path(tmpdir.join(filepath))
    savepath = save_survey(s, target_path)

    assert savepath.is_file()

    # json validation
    with open(savepath, mode="rt") as ofile:
        json.load(ofile)