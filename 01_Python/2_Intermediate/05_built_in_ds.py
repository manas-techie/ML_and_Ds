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
COMMON OPERATIONS & TIME COMPLEXITY:

Operation          │ List            │ Tuple          │ Dict              │ Set
────────────────────┼─────────────────┼────────────────┼───────────────────┼──────────────────
Create empty       │ []              │ ()             │ {}                │ set()
Create with data   │ [1, 2, 3]       │ (1, 2, 3)      │ {"a": 1}          │ {1, 2, 3}
Add element        │ .append() (O(1))│ ❌             │ d[k]=v (O(1) avg) │ .add() (O(1) avg)
Remove element     │ .remove() (O(n))│ ❌             │ .pop(k) (O(1) avg)│ .remove() (O(1) avg)
Access element     │ list[i] (O(1))  │ tuple[i] (O(1))│ d[k] (O(1) avg)   │ ❌
Check membership   │ in (O(n))       │ in (O(n))      │ in (O(1) avg)     │ in (O(1) avg)
Length             │ len() (O(1))    │ len() (O(1))   │ len() (O(1))      │ len() (O(1))
Mutable?           │ ✓               │ ❌             │ ✓                 │ ✓
Ordered?           │ ✓               │ ✓              │ ✓ (3.7+)          │ ❌
Duplicates?        │ ✓               │ ✓              │ ❌ (keys)         │ ❌
────────────────────┴─────────────────┴────────────────┴───────────────────┴──────────────────

MOST USED METHODS:

Lists:
  .append(x)      - Add element (O(1))
  .extend(list)   - Add multiple elements (O(k))
  .remove(x)      - Remove element (O(n))
  .pop()          - Remove and return last (O(1))
  .sort()         - Sort in place (O(n log n))
  [i]             - Index access (O(1))
  [start:stop]    - Slicing (O(k))

Tuples:
  (a, b, c)       - Packing
  a, b, c = tuple - Unpacking
  .count(x)       - Count occurrences (O(n))
  .index(x)       - Find index (O(n))

Dictionaries:
  [key]           - Access value (O(1) avg)
  .get(key)       - Safe access (O(1) avg)
  .keys()         - Get keys (O(1))
  .values()       - Get values (O(1))
  .items()        - Get key-value pairs (O(1))
  .update(dict)   - Merge dicts (O(k))

Sets:
  .add(x)         - Add element (O(1) avg)
  .remove(x)      - Remove element (O(1) avg)
  | (union)       - Combine sets (O(len(s) + len(t)))
  & (intersection)- Common elements (O(min(len(s), len(t))))
  - (difference)  - Elements in first not second (O(len(s)))
"""