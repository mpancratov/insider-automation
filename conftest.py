import pytest
import multiprocessing

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    num_processes = config.getoption("--numprocesses")
    if num_processes:
        config.option.numprocesses = int(num_processes) 
    else:
        config.option.numprocesses = multiprocessing.cpu_count()

def pytest_addoption(parser):
    parser.addoption(
        "--numprocesses",
        action="store",
        default=None,
        help="Number of processes to use for parallel test execution"
    )
