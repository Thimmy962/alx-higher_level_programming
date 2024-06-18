#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if linked list is circular
 * @list: pointer to list
 * Return: 0 if cycle is absent else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}
	fast = list->next;
	slow = list;
	while (fast != NULL && fast->next != NULL)
	{
		if (slow == fast)
		{
			return (1);
		}
		slow = slow->next;
		fast = fast->next->next;
	}

	return (0);
}
