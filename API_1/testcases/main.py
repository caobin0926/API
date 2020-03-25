import sys
import pytest
sys.path.append('./')
# print()
pytest.main(["-s", "--alluredir", "${WORKSPACE}/report"])