import sys
import pytest
sys.path.append('./')
pytest.main(["-s", "--alluredir", "./\\report"])