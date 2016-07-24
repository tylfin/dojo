# Search Trees

## Binary Search Trees (BSTs)
Data structure associated with the binary search algorithm.

### Motivation for BSTs
Basic scheduling problem, call it the `Runway Problem`. Assume that an airport with a single runway.
Constraints:
* Reservation for future landings
* Reserve requests for landings (specifying landing time **T**)
  * Add **T** to the set **R** if no other landings are scheduled within **k**-minutes
* Remove from the set **R** after the plane lands
* All operations should take |**R**| = **n** ~> O(log(n))

Numbers Example:

**k** = 3 minutes

|now=1:00pm|1:03|1:6|1:09|1:12|1:15|future

- Add 1:03
- Add 1:06
- Add 1:07 - fails
- ...

What could we try?

* Unordered array - O(1) insert, O(n) comparison,
* Ordered array - O(n) insert, O(log(n)) comparison
* Sorted list - O(1) insert, O(n) comparison
* Heap - Min/Max heaps - O(n) comparison
* Dictionaries/Hash - same issue as heaps :(

If only we could do fast insertion into an ordered array! BSTs to the rescue!!


### BSTs
* node(x) : key(x)
* Pointers: parent(x), left(x), right(x)
* Invariant: For all nodes, x - if y is in the left sub-tree of x key(y) <= key(x). If y is in the right sub-tree key(y) >= key(x)
