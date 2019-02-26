Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?
O(1), constant time to append item to storage and constant time to increment size

2. What is the runtime complexity of `dequeue`?
O(n), linear time to delete an item from the list and constant time to decrement size

3. What is the runtime complexity of `len`?
O(1), constant time for value return

## Binary Search Tree

1. What is the runtime complexity of `insert`? 
O(n), n is depth of tree. At worst runs as many times as there are tree nodes (all left or all right, with no balancing).

2. What is the runtime complexity of `contains`?
O(n), n is depth of tree.

3. What is the runtime complexity of `get_max`? 
O(n), n is depth of right branch

## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?
O(1), constant time to assign variables

2. What is the runtime complexity of `ListNode.insert_before`?
O(1), constant time to assign variables

3. What is the runtime complexity of `ListNode.delete`?
O(1), constant time to assign variables

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?
O(1), constant time to assign variables

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
O(1), constant time to assign variables

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
O(1), constant time to assign variables

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
O(1), constant time to assign variables

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?
O(1), constant time to assign variables

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?
O(1), constant time to assign variables

10. What is the runtime complexity of `DoublyLinkedList.delete`?
O(1), constant time to assign variables

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?

    The JS Array.splice method's runtime complexity is O(n), linear time to copy at most n-1 values into new array.