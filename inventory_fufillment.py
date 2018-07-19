import sys
from models import Inventory

def format_input(request):
    # this will throw a ValueError if there are not enough values
    date, small, medium, large = request.split(',')
    formatted_inputs = []
    for input in request.split(','):
        # this will throw a ValueError if the input cannot be cast
        formatted_inputs.append(int(input))
    return formatted_inputs

event_requests = []
for request in sys.argv[1:]:
    try:
        input = format_input(request)
    except ValueError:
        print ("Invalid input format. Please provide 4 integers in format: date,small,medium,large ie. 5,0,3,2")
        exit(1)
    else:
        event_requests.append(input)

inventory = Inventory()

can_fufill = inventory.can_fufill_all_events(event_requests)
if not can_fufill:
    print("Buy More Tuxedos")
    exit(1)

print("Sufficient Inventory")
