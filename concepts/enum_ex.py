import enum

class MyState(enum.Enum):
    stateA=1
    stateB=2
    stateC=4
    stateD=3
    stateM=54


state = MyState.stateM

print state

if state == MyState.stateM:
    state = MyState.stateB
else:
    state = MyState.stateC


print state
