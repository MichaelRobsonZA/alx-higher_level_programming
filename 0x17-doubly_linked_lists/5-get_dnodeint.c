#include "lists.h"

/**
 * get_dnodeint_at_index - returns the nth node of a doubly linked list
 * @head: pointer to head of list
 * @index: index of node to return
 *
 * Return: address of nth node, or NULL if failed
 */
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
    unsigned int count = 0;

    while (head != NULL)
    {
        if (count == index)
            return (head);
        count++;
        head = head->next;
    }

    return (NULL);
}

