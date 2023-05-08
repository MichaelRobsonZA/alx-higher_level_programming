/**
 * check_cycle - checks if a linked list has a cycle in it
 * @list: pointer to head of list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
    listint_t *tortoise, *hare;

    if (list == NULL || list->next == NULL)
        return (0);

    tortoise = list;
    hare = list->next;
    while (hare != NULL && hare->next != NULL)
    {
        if (hare == tortoise)
            return (1);
        tortoise = tortoise->next;
        hare = hare->next->next;
    }

    return (0);
}

