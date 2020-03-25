import sys
import pytest
sys.path.append('./')
# print()
pytest.main(["-s", "--alluredir", "/root/.jenkins/workspace/API/allure-report"])