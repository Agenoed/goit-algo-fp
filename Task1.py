class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


def insertion_sort(head):
    if head is None or head.next is None:
        return head

    sorted_list = None
    curr = head
    while curr:
        next_node = curr.next
        sorted_list = sorted_insert(sorted_list, curr)
        curr = next_node
    return sorted_list


def sorted_insert(head, new_node):
    if head is None or new_node.data <= head.data:
        new_node.next = head
        return new_node

    curr = head
    while curr.next and curr.next.data < new_node.data:
        curr = curr.next

    new_node.next = curr.next
    curr.next = new_node
    return head


def merge_sorted_lists(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    if head1.data <= head2.data:
        head = head1
        head.next = merge_sorted_lists(head1.next, head2)
    else:
        head = head2
        head.next = merge_sorted_lists(head1, head2.next)
    return head


# Функція для виведення списку
def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next
    print()


# Створення списків
list1 = Node(5)
list1.next = Node(3)
list1.next.next = Node(1)

list2 = Node(4)
list2.next = Node(2)

# Реверсування списку
list1 = reverse_list(list1)
print("Реверсований список 1:", end=" ")
print_list(list1)

# Сортування списку
list2 = insertion_sort(list2)
print("Відсортований список 2:", end=" ")
print_list(list2)

# Об'єднання списків
merged_list = merge_sorted_lists(list1, list2)
print("Об'єднаний список:", end=" ")
print_list(merged_list)