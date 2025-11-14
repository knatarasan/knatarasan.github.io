from enum import Enum
from time import sleep
from typing import Dict, Any

"""
Robot 

finite ticks = 500
patrol      : 0.001 % / tick    (drop)
fight       : 0.002 % / tick    (drop)
charge speed    : 0.01 % /tick  (added)

"""


class Status(Enum):
    SUCCESS = 1
    FAILURE = 2
    RUNNING = 3


class Node:
    def tick(self, bb) -> Status: ...


class Selector(Node):
    def __init__(self, *children):
        self.children = list(children)
        self.i = 0

    def tick(self, bb):
        while self.i < len(self.children):
            s = self.children[self.i].tick(bb)
            if s == Status.RUNNING:
                return s
            if s == Status.SUCCESS:
                self.i = 0
                return s
            self.i += 1
        self.i = 0
        return Status.FAILURE


class Sequence(Node):
    def __init__(self, *children):
        self.children = list(children)
        self.i = 0

    def tick(self, bb):
        while self.i < len(self.children):
            s = self.children[self.i].tick(bb)
            if s == Status.RUNNING:
                return s
            if s == Status.FAILURE:
                self.i = 0
                return s
            self.i += 1
        self.i = 0
        return Status.SUCCESS


class Condition(Node):
    def __init__(self, fn):
        self.fn = fn

    def tick(self, bb):
        return Status.SUCCESS if self.fn(bb) else Status.FAILURE


class Action(Node):
    def __init__(self, step_fn):
        self.step = step_fn

    def tick(self, bb):
        return self.step(bb)  # returns a Status


# --- Example: minimal demo implementations ---


# CONDITIONS
def low_battery(bb: Dict[str, Any]) -> bool:
    return float(bb.get("battery", 0.0)) <= 0.2 + 1e-9


def enemy_visible(bb: Dict[str, Any]) -> bool:
    return bool(bb.get("enemy_visible", False))


# ACTIONS
def go_charge_step(bb: Dict[str, Any]) -> Status:
    # Simulate moving to charger, then charging until full.
    if not bb.get("at_charger", False):
        bb["at_charger"] = True
        return Status.RUNNING
    # Charge
    battery = float(bb.get("battery", 0.0))
    if battery >= 1.0:
        bb["at_charger"] = False  # leave charger once full
        return Status.SUCCESS
    battery = min(1.0, battery + 0.01)
    bb["battery"] = battery
    return Status.RUNNING


def fight_step(bb: Dict[str, Any]) -> Status:
    # Simulate fighting that completes after two ticks and drains battery.
    if not enemy_visible(bb):
        return Status.FAILURE
    ticks = int(bb.get("fight_ticks", 0)) + 1
    bb["fight_ticks"] = ticks
    # Drain some battery while fighting
    battery = float(bb.get("battery", 1.0))
    battery = max(0.0, battery - 0.002)
    bb["battery"] = battery
    if ticks >= 20:
        bb["enemy_visible"] = False
        bb.pop("fight_ticks", None)
        return Status.SUCCESS
    return Status.RUNNING


def patrol_step(bb: Dict[str, Any]) -> Status:
    # Simulate patrolling which consumes a bit of battery.
    battery = float(bb.get("battery", 1.0))
    bb["battery"] = max(0.0, battery - 0.001)
    # Return SUCCESS so selector re-evaluates higher-priority branches next tick
    return Status.SUCCESS


# BUILD TREE
def build_tree() -> Node:
    return Selector(
        Sequence(Condition(low_battery), Action(go_charge_step)),
        Sequence(Condition(enemy_visible), Action(fight_step)),
        Action(patrol_step),
    )


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Behavior tree demo runner")
    parser.add_argument(
        "--battery", type=float, default=0.4, help="Initial battery level (0-1)"
    )
    parser.add_argument(
        "--enemy-visible",
        dest="enemy_visible",
        action="store_true",
        help="Start with enemy visible",
    )
    parser.add_argument(
        "--no-enemy-visible",
        dest="enemy_visible",
        action="store_false",
        help="Start with no enemy visible",
    )
    parser.set_defaults(enemy_visible=True)
    parser.add_argument("--ticks", type=int, default=500, help="Number of ticks to run")
    parser.add_argument(
        "--dt", type=float, default=0.05, help="Tick duration in seconds"
    )
    args = parser.parse_args()

    # Example blackboard and tick loop for manual runs
    blackboard: Dict[str, Any] = {
        "battery": max(0.0, min(1.0, args.battery)),
        "enemy_visible": bool(args.enemy_visible),
        "at_charger": False,
    }
    dt = args.dt  # seconds
    tree = build_tree()
    # Run a finite demo loop
    for _i in range(args.ticks):
        _status = tree.tick(blackboard)
        # Brief log of status and relevant blackboard keys
        _bb_view = {
            k: blackboard.get(k)
            for k in ("battery", "at_charger", "enemy_visible", "fight_ticks")
        }
        print(f"tick={_i:02d} status={_status.name} bb={_bb_view}")
        sleep(dt)
