import pytest
from battery import Battery
from unittest.mock import Mock

todo = pytest.mark.skip(reason='todo: pending spec')

@pytest.fixture
def charged_battery():
    return Battery(100)

@pytest.fixture
def partially_charged_battery():
    b = Battery(100)
    b.mCharge = 70
    return b

def describe_Battery():

    def describe_recharge():
        def it_recharges_to_full():
            b = Battery(100)
            b.mCharge = 0
            b.recharge(100)
            assert b.mCharge == 100

        def it_recharges_and_notifies_monitor():
            mock = Mock() # create mock 
            b = Battery(100, external_monitor=mock)
            b.mCharge = 50 # starting battery charge

            result = b.recharge(30)
            assert result == True
            assert b.mCharge == 80
            mock.notify_recharge.assert_called_once_with(80)

            mock.reset_mock()
            
            result = b.recharge(-20)
            assert result == False
            assert b.mCharge == 80
            mock.notify_recharge.assert_not_called()

    def describe_drain():
        def it_drains_to_zero():
            b = Battery(100)
            b.mCharge = 100
            b.drain(100)
            assert b.mCharge == 0

        def it_drains_and_notifies_monitor():
            mock = Mock()
            b = Battery(100, external_monitor=mock)
            b.mCharge = 100

            #Success case
            result = b.drain(50)
            assert result == True
            assert b.mCharge == 50
            mock.notify_drain.assert_called_once_with(50)

            mock.reset_mock()

            #failure case
            result = b.drain(0)
            assert result == False
            assert b.mCharge == 50
            mock.notify_drain.assert_not_called()
    