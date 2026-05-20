#!/usr/bin/env python3
import typing 
import random

def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan", "ethan", "fiona", "george", "hannah"]
    actions = ["run", "eat", "sleep", "grab", "move", "climb", "swim", "release", "use"]
    player = random.choice(players)
    action = random.choice(actions)
    while True: 
        yield (player, action)


def consume_event(mylist: list) -> typing.Generator[tuple[str, str], None, None]:
    while (len(mylist) > 0):
        pl_act = random.choice(mylist)
        mylist.remove(pl_act)
        yield pl_act


def main():
    print("=== Game Data Stream Processor ===")
    for i in range(0,1000):
        pl_act = gen_event()
        # print(f"Event {i}: Player {pl_act[0]} did action {pl_act[1]}")
        print(f"Event {i}: Player {(next(pl_act)[0])} did action {(next(pl_act)[1])}")
    events = [next(gen_event()) for _ in range(10)]
    print(f"Built list of 10 events: {events}")
    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")

if __name__ == "__main__":
    main()