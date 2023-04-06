from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import SUPER_JUMP, JUMP_TYPE

class Super_jump(PowerUp):

    def __init__(self):
        self.image = SUPER_JUMP
        self.type = JUMP_TYPE
        super().__init__(self.image, self.type)
