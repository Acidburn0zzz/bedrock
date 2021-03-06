# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from pages.home import HomePage


@pytest.mark.skip_if_internet_explorer(reason='https://ci.us-west.moz.works/job/bedrock_integration_tests_runner/11169/')
@pytest.mark.nondestructive
def test_navigation(base_url, selenium):
    page = HomePage(selenium, base_url).open()
    internet_health_page = page.navigation.open_internet_health()
    assert internet_health_page.seed_url in selenium.current_url

    page.open()
    technology_page = page.navigation.open_technology()
    assert technology_page.seed_url in selenium.current_url


@pytest.mark.skip_if_internet_explorer(reason='https://ci.us-west.moz.works/job/bedrock_integration_tests_runner/11169/')
@pytest.mark.smoke
@pytest.mark.nondestructive
@pytest.mark.viewport('mobile')
def test_mobile_navigation(base_url, selenium):
    page = HomePage(selenium, base_url).open()
    page.navigation.show()
    internet_health_page = page.navigation.open_internet_health()
    assert internet_health_page.seed_url in selenium.current_url

    page.open().navigation.show()
    technology_page = page.navigation.open_technology()
    assert technology_page.seed_url in selenium.current_url
