import copy

SLIM = 'slim'
REG = 'regular'

class Inventory():
    def __init__(self):
        self.inventory = {
            'slim': {'small': 5, 'medium': 5, 'large': 5},
            'regular': {'small': 5, 'medium': 5, 'large': 5}
        }

    def can_fufill_all_events(self, events):
        event_array = self.format_events(events)
        for event in event_array:
            can_fufill = self.can_fufill_event(event)
            if not can_fufill:
                return False
        return True

    def can_fufill_event(self, event):
        new_inventory = copy.deepcopy(self.inventory)
        can_fufill = True
        # first try slim
        for inven in new_inventory[SLIM]:
            new_inventory[SLIM][inven] -= getattr(event, inven)
            if new_inventory[SLIM][inven] < 1:
                can_fufill = False
                break;
        if not can_fufill:
            # now try regular
            for inven in new_inventory[REG]:
                new_inventory[REG][inven] -= getattr(event, inven)
                if new_inventory[REG][inven] < 1:
                    can_fufill = False
                    break;
        return can_fufill

    def format_events(self, events):
        event_array = []
        for e in events:
            new_event = Event(*e)
            event_array.append(new_event)
            # create a return event that will refill inventory
            event_array.append(new_event.get_return_event())
        event_array.sort(key=lambda x: x.date)
        return event_array


class Event():
    def __init__(self, date, small, med, large):
        self.date = date
        self.small = small
        self.medium = med
        self.large = large

    def get_return_event(self):
        return Event(self.date+3, -1 * self.small, -1 * self.medium, -1 * self.large)
