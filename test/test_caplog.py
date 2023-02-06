import logging
LOGGER = logging.getLogger(__name__)

# yet to understand
def test_foo(caplog):
    caplog.set_level(logging.WARNING, logger="logg.baz")
    LOGGER.error('important error')
    assert 1==12