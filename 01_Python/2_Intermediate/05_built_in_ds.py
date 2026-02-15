# DATA STRUCTURE COMPARISON & WHEN TO USE EACH

"""
WHEN TO USE WHICH DATA STRUCTURE:

LIST - Use when you need:
✓ Ordered collection
✓ Allow duplicates
✓ Need to modify (add/remove/change)
✓ Index access
Example: Shopping cart, to-do list, sequence of items

TUPLE - Use when you need:
✓ Ordered collection
✓ Data shouldn't change (immutable)
✓ Faster than lists
✓ Can be dictionary keys
Example: Coordinates (x, y), RGB colors, function return values

DICTIONARY - Use when you need:
✓ Key-value pairs
✓ Fast lookup by key
✓ Descriptive labels for data
Example: User profiles, configuration, word counts, database records

SET - Use when you need:
✓ Unique elements only
✓ Fast membership testing
✓ Mathematical set operations
✓ Remove duplicates
Example: Unique visitors, tags, valid options, duplicate removal
"""


# QUICK REFERENCE CHEAT SHEET

"""
COMMON OPERATIONS COMPARISON:

Operation          │ List            │ Tuple          │ Dict              │ Set
────────────────────┼─────────────────┼────────────────┼───────────────────┼──────────────
Create empty       │ []              │ ()             │ {}                │ set()
Create with data   │ [1, 2, 3]       │ (1, 2, 3)      │ {"a": 1}          │ {1, 2, 3}
Add element        │ .append()       │ ❌             │ dict[key] = val   │ .add()
Remove element     │ .remove()       │ ❌             │ .pop(key)         │ .remove()
Access element     │ list[i]         │ tuple[i]       │ dict[key]         │ ❌
Check membership   │ in              │ in             │ in (keys)         │ in (fast!)
Length             │ len()           │ len()          │ len()             │ len()
Mutable?           │ ✓               │ ❌             │ ✓                 │ ✓
Ordered?           │ ✓               │ ✓              │ ✓ (3.7+)          │ ❌
Duplicates?        │ ✓               │ ✓              │ ❌ (keys)         │ ❌
────────────────────┴─────────────────┴────────────────┴───────────────────┴──────────────

MOST USED METHODS:

Lists:
  .append(x)      - Add element
  .extend(list)   - Add multiple elements
  .remove(x)      - Remove element
  .pop()          - Remove and return last
  .sort()         - Sort in place
  [i]             - Index access
  [start:stop]    - Slicing

Tuples:
  (a, b, c)       - Packing
  a, b, c = tuple - Unpacking
  .count(x)       - Count occurrences
  .index(x)       - Find index

Dictionaries:
  [key]           - Access value
  .get(key)       - Safe access
  .keys()         - Get keys
  .values()       - Get values
  .items()        - Get key-value pairs
  .update(dict)   - Merge dicts

Sets:
  .add(x)         - Add element
  .remove(x)      - Remove element
  | (union)       - Combine sets
  & (intersection)- Common elements
  - (difference)  - Elements in first not second
"""